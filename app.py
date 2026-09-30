"""
CodeCraftHub - Simple Flask REST API

This application manages learning courses using a JSON file instead of a database.

Available endpoints:

POST   /api/courses       Create a course
GET    /api/courses       Get all courses
GET    /api/courses/<id>  Get one course
PUT    /api/courses/<id>  Update a course
DELETE /api/courses/<id>  Delete a course
"""

from datetime import date, datetime, timezone
import json
from pathlib import Path

from flask import Flask, jsonify, request


# Create the Flask application
app = Flask(__name__)


# Store courses.json in the same directory as this app.py file
COURSES_FILE = Path(__file__).parent / "courses.json"


# The only status values accepted by the API
VALID_STATUSES = {
    "Not Started",
    "In Progress",
    "Completed",
}


def create_courses_file_if_missing():
    """
    Create courses.json automatically if it does not exist.

    The file starts with an empty JSON list because courses will be
    stored as a list of objects.
    """
    try:
        if not COURSES_FILE.exists():
            COURSES_FILE.write_text("[]", encoding="utf-8")
    except OSError as error:
        raise RuntimeError(
            f"Unable to create courses.json: {error}"
        ) from error


def read_courses():
    """
    Read and return all courses from courses.json.

    Returns:
        list: A list of course dictionaries.

    Raises:
        RuntimeError: If the file cannot be read or contains invalid JSON.
    """
    try:
        create_courses_file_if_missing()

        with COURSES_FILE.open("r", encoding="utf-8") as file:
            courses = json.load(file)

        # Make sure the JSON file contains a list
        if not isinstance(courses, list):
            raise RuntimeError(
                "courses.json must contain a JSON list."
            )

        return courses

    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"courses.json contains invalid JSON: {error}"
        ) from error

    except OSError as error:
        raise RuntimeError(
            f"Unable to read courses.json: {error}"
        ) from error


def write_courses(courses):
    """
    Write the provided course list to courses.json.

    Args:
        courses (list): The courses to save.

    Raises:
        RuntimeError: If the file cannot be written.
    """
    try:
        with COURSES_FILE.open("w", encoding="utf-8") as file:
            json.dump(courses, file, indent=4)

    except OSError as error:
        raise RuntimeError(
            f"Unable to write to courses.json: {error}"
        ) from error


def get_next_course_id(courses):
    """
    Generate the next course ID.

    IDs start at 1. The next ID is one greater than the current
    highest ID. If there are no courses, the first ID is 1.
    """
    if not courses:
        return 1

    existing_ids = [
        course.get("id", 0)
        for course in courses
        if isinstance(course.get("id"), int)
    ]

    if not existing_ids:
        return 1

    return max(existing_ids) + 1


def validate_course_data(data, require_all_fields=True):
    """
    Validate course data sent by the client.

    Args:
        data (dict): JSON request data.
        require_all_fields (bool): Whether all course fields are required.
            This is True when creating a course and False when updating one.

    Returns:
        str or None: An error message, or None if the data is valid.
    """
    if not isinstance(data, dict):
        return "Request body must be a JSON object."

    required_fields = [
        "name",
        "description",
        "target_date",
        "status",
    ]

    if require_all_fields:
        missing_fields = [
            field for field in required_fields
            if field not in data
        ]

        if missing_fields:
            return (
                "Missing required field(s): "
                + ", ".join(missing_fields)
            )

    # For updates, validate only fields that were provided.
    fields_to_validate = (
        required_fields if require_all_fields
        else [field for field in required_fields if field in data]
    )

    if "name" in fields_to_validate:
        if not isinstance(data.get("name"), str):
            return "name must be a string."

        if not data["name"].strip():
            return "name is required and cannot be empty."

    if "description" in fields_to_validate:
        if not isinstance(data.get("description"), str):
            return "description must be a string."

        if not data["description"].strip():
            return "description is required and cannot be empty."

    if "target_date" in fields_to_validate:
        target_date = data.get("target_date")

        if not isinstance(target_date, str):
            return "target_date must be a string in YYYY-MM-DD format."

        # Check the exact YYYY-MM-DD format and ensure it is a real date.
        try:
            if len(target_date) != 10:
                raise ValueError

            if target_date[4] != "-" or target_date[7] != "-":
                raise ValueError

            date.fromisoformat(target_date)

        except ValueError:
            return "target_date must use the YYYY-MM-DD format."

    if "status" in fields_to_validate:
        if data.get("status") not in VALID_STATUSES:
            return (
                "Invalid status. Status must be one of: "
                '"Not Started", "In Progress", or "Completed".'
            )

    return None


def get_json_request_body():
    """
    Safely get the JSON body from a request.

    Returns:
        tuple: (data, error_message)
    """
    if not request.is_json:
        return None, "Request Content-Type must be application/json."

    data = request.get_json(silent=True)

    if data is None:
        return None, "Request body must contain valid JSON."

    return data, None


@app.route("/api/courses", methods=["POST"])
def create_course():
    """
    Create a new course.

    Required fields:
    - name
    - description
    - target_date
    - status
    """
    data, error = get_json_request_body()

    if error:
        return jsonify({"error": error}), 400

    validation_error = validate_course_data(
        data,
        require_all_fields=True
    )

    if validation_error:
        return jsonify({"error": validation_error}), 400

    try:
        courses = read_courses()

        new_course = {
            "id": get_next_course_id(courses),
            "name": data["name"].strip(),
            "description": data["description"].strip(),
            "target_date": data["target_date"],
            "status": data["status"],
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        courses.append(new_course)
        write_courses(courses)

        return jsonify(new_course), 201

    except RuntimeError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses", methods=["GET"])
def get_all_courses():
    """Return all courses."""
    try:
        courses = read_courses()
        return jsonify(courses), 200

    except RuntimeError as error:
        return jsonify({"error": str(error)}), 500

@app.route("/api/courses/stats", methods=["GET"])
def get_course_stats():
    """
    Return statistics about all courses.

    The response includes:
    - Total number of courses
    - Number of courses in each status
    """
    try:
        courses = read_courses()

        # Start every status at zero so missing statuses are still included.
        status_counts = {
            "Not Started": 0,
            "In Progress": 0,
            "Completed": 0,
        }

        # Count each course based on its status.
        for course in courses:
            status = course.get("status")

            if status in status_counts:
                status_counts[status] += 1

        response = {
            "total_courses": len(courses),
            "courses_by_status": status_counts,
        }

        return jsonify(response), 200

    except RuntimeError as error:
        return jsonify({"error": str(error)}), 500

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    """Return one course using its ID."""
    try:
        courses = read_courses()

        course = next(
            (
                course for course in courses
                if course.get("id") == course_id
            ),
            None,
        )

        if course is None:
            return jsonify({"error": "Course not found."}), 404

        return jsonify(course), 200

    except RuntimeError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    """
    Update a course.

    The request may contain one or more editable fields:
    - name
    - description
    - target_date
    - status

    The ID and created_at values cannot be changed.
    """
    data, error = get_json_request_body()

    if error:
        return jsonify({"error": error}), 400

    # PUT updates any details provided while preserving omitted fields.
    validation_error = validate_course_data(
        data,
        require_all_fields=False
    )

    if validation_error:
        return jsonify({"error": validation_error}), 400

    editable_fields = {
        "name",
        "description",
        "target_date",
        "status",
    }

    unknown_fields = set(data.keys()) - editable_fields

    if unknown_fields:
        return jsonify({
            "error": (
                "Unknown field(s): "
                + ", ".join(sorted(unknown_fields))
            )
        }), 400

    if not data:
        return jsonify({
            "error": "At least one course field is required for an update."
        }), 400

    try:
        courses = read_courses()

        course = next(
            (
                course for course in courses
                if course.get("id") == course_id
            ),
            None,
        )

        if course is None:
            return jsonify({"error": "Course not found."}), 404

        # Update only the fields included in the request.
        for field in editable_fields:
            if field in data:
                value = data[field]

                if field in {"name", "description"}:
                    value = value.strip()

                course[field] = value

        write_courses(courses)

        return jsonify(course), 200

    except RuntimeError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    """Delete a course using its ID."""
    try:
        courses = read_courses()

        course = next(
            (
                course for course in courses
                if course.get("id") == course_id
            ),
            None,
        )

        if course is None:
            return jsonify({"error": "Course not found."}), 404

        courses.remove(course)
        write_courses(courses)

        return jsonify({
            "message": "Course deleted successfully.",
            "course": course,
        }), 200

    except RuntimeError as error:
        return jsonify({"error": str(error)}), 500


@app.errorhandler(404)
def handle_404(error):
    """Return JSON instead of Flask's default HTML 404 response."""
    return jsonify({"error": "Endpoint not found."}), 404


@app.errorhandler(405)
def handle_405(error):
    """Return JSON when an HTTP method is not supported."""
    return jsonify({"error": "HTTP method not allowed."}), 405


if __name__ == "__main__":
    # This also creates courses.json before the server starts.
    try:
        create_courses_file_if_missing()
        print(f"Using course data file: {COURSES_FILE}")
    except RuntimeError as error:
        print(f"Startup error: {error}")
        raise SystemExit(1)

    # Debug mode is useful while learning.
    # Set debug=False for production use.
    app.run(debug=True)