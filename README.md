# CodeCraftHub

CodeCraftHub is a beginner-friendly REST API for tracking courses that developers want to learn.

The application is built with:

* Python

* Flask

* JSON file storage

* REST API principles

No database, authentication, or user management is required. Course information is stored in a local file named `courses.json`.

## Project Overview

CodeCraftHub allows you to create and manage learning courses.

Each course contains:

* An automatically generated ID

* A course name

* A description

* A target completion date

* A learning status

* An automatically generated creation timestamp

The API supports all basic CRUD operations:

| CRUD operation | HTTP method | Purpose | 
 | ----- | ----- | ----- | 
| Create | `POST` | Add a new course | 
| Read | `GET` | View courses | 
| Update | `PUT` | Change course details | 
| Delete | `DELETE` | Remove a course | 

This project is designed to help beginners learn:

* What REST APIs are

* How HTTP methods work

* How to send JSON data

* How Flask handles routes

* How to read and write JSON files

* How API status codes communicate results

## Features

* Create new courses

* View all courses

* View one course by ID

* Get course statistics

* Update course details

* Delete courses

* Automatically generate course IDs

* Automatically generate creation timestamps

* Store course data in `courses.json`

* Automatically create `courses.json` if it does not exist

* Validate required fields

* Validate target dates

* Validate course statuses

* Return JSON responses

* Return helpful error messages

* Handle missing courses

* Handle file read and write errors

* No database required

* No authentication required

## Requirements

Before installing the project, make sure you have:

* Python 3.9 or newer

* `pip`, Python's package installer

* A terminal or command prompt

* `curl` for testing the API

You can check whether Python is installed:

```
python --version

```

On some systems, use:

```
python3 --version

```

Check whether `pip` is installed:

```
pip --version

```

Or:

```
pip3 --version

```

## Project Structure

A simple CodeCraftHub project may look like this:

```
codecrafthub/
├── app.py
├── courses.json
├── requirements.txt
└── README.md

```

### `app.py`

This is the main Flask application. It contains:

* Flask configuration

* API routes

* Course validation

* JSON file reading

* JSON file writing

* Error handling

### `courses.json`

This file stores all course data. The file is created automatically when the application starts if it does not already exist.

An empty `courses.json` file contains:

```
[]

```

After adding courses, it may look like:

```
[
  {
    "id": 1,
    "name": "Flask REST API Fundamentals",
    "description": "Learn how to build REST APIs with Python and Flask.",
    "target_date": "2026-12-31",
    "status": "Not Started",
    "created_at": "2026-09-30T12:00:00+00:00"
  }
]

```

### `requirements.txt`

This file lists the Python packages required by the project.

Example:

```
Flask

```

### `README.md`

This file contains project documentation and instructions.

## Installation

Follow these steps to install CodeCraftHub.

### Step 1: Create a project directory

Create a directory for the project:

```
mkdir codecrafthub
cd codecrafthub

```

### Step 2: Create a virtual environment

A virtual environment keeps this project's packages separate from other Python projects.

On macOS or Linux:

```
python3 -m venv venv

```

On Windows:

```
python -m venv venv

```

### Step 3: Activate the virtual environment

On macOS or Linux:

```
source venv/bin/activate

```

On Windows Command Prompt:

```
venv\Scripts\activate

```

On Windows PowerShell:

```
venv\Scripts\Activate.ps1

```

After activation, your terminal may show `(venv)` at the beginning of the command prompt.

### Step 4: Install Flask

If you have a `requirements.txt` file:

```
pip install -r requirements.txt

```

Alternatively, install Flask directly:

```
pip install Flask

```

### Step 5: Verify Flask installation

```
pip show Flask

```

You should see information about the installed Flask package.

## Running the Application

Make sure your virtual environment is activated.

Start the application with:

```
python app.py

```

On some macOS or Linux systems, use:

```
python3 app.py

```

You should see output similar to:

```
- Using course data file: /path/to/codecrafthub/courses.json
Running on http://127.0.0.1:5000

```

The API is now available at: `http://127.0.0.1:5000`

Keep the terminal running while testing the API. To stop the application, press `Ctrl+C`.

## API Concepts for Beginners

An API allows one program to communicate with another program. CodeCraftHub provides URLs called endpoints. Each endpoint performs an action on courses.

For example:
`GET http://127.0.0.1:5000/api/courses`

The parts of this request are:

* `GET` — the HTTP method

* `http://127.0.0.1:5000` — the server address

* `/api/courses` — the API endpoint

### Common HTTP methods

* **`POST`**: Used to create new data.

* **`GET`**: Used to retrieve data.

* **`PUT`**: Used to update existing data.

* **`DELETE`**: Used to remove data.

### Common HTTP status codes

| Status code | Meaning | 
 | ----- | ----- | 
| `200 OK` | The request succeeded | 
| `201 Created` | A new resource was created | 
| `400 Bad Request` | The request contains invalid data | 
| `404 Not Found` | The requested course or endpoint does not exist | 
| `405 Method Not Allowed` | The HTTP method is not supported | 
| `500 Internal Server Error` | The server encountered an unexpected problem | 

## API Documentation

The base API URL is: `http://127.0.0.1:5000`

### Course Data Format

Each course has the following fields:

| Field | Type | Required | Description | 
 | ----- | ----- | ----- | ----- | 
| `id` | Integer | Automatically generated | Unique course ID | 
| `name` | String | Yes | Course name | 
| `description` | String | Yes | Course description | 
| `target_date` | String | Yes | Date in `YYYY-MM-DD` format | 
| `status` | String | Yes | Course progress status | 
| `created_at` | String | Automatically generated | Creation timestamp | 

Allowed status values are:

* `Not Started`

* `In Progress`

* `Completed`

Example course:

```
{
  "id": 1,
  "name": "Flask REST API Fundamentals",
  "description": "Learn how to build REST APIs with Python and Flask.",
  "target_date": "2026-12-31",
  "status": "Not Started",
  "created_at": "2026-09-30T12:00:00+00:00"
}

```

*Note: The actual `created_at` value will be generated by the application.*

### Endpoints

#### 1. Create a Course

`POST /api/courses`

Creates a new course.

**Request:**

```
curl -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Flask REST API Fundamentals",
    "description": "Learn how to build REST APIs with Python and Flask.",
    "target_date": "2026-12-31",
    "status": "Not Started"
  }'

```

**Successful response:**

* **Status:** `201 Created`

* **Response:**

  ```
  {
    "id": 1,
    "name": "Flask REST API Fundamentals",
    "description": "Learn how to build REST APIs with Python and Flask.",
    "target_date": "2026-12-31",
    "status": "Not Started",
    "created_at": "2026-09-30T12:00:00+00:00"
  }
  
  ```

*The `id` and `created_at` fields are generated automatically.*

#### 2. Get All Courses

`GET /api/courses`

Returns all courses.

**Request:**

```
curl -X GET http://127.0.0.1:5000/api/courses

```

**Successful response:**

* **Status:** `200 OK`

* **Response:**

  ```
  [
    {
      "id": 1,
      "name": "Flask REST API Fundamentals",
      "description": "Learn how to build REST APIs with Python and Flask.",
      "target_date": "2026-12-31",
      "status": "Not Started",
      "created_at": "2026-09-30T12:00:00+00:00"
    }
  ]
  
  ```

If no courses have been added, the response is `[]`.

#### 3. Get One Course

`GET /api/courses/<id>`

Returns one course by its ID.

**Request:**

```
curl -X GET http://127.0.0.1:5000/api/courses/1

```

**Successful response:**

* **Status:** `200 OK`

* **Response:**

  ```
  {
    "id": 1,
    "name": "Flask REST API Fundamentals",
    "description": "Learn how to build REST APIs with Python and Flask.",
    "target_date": "2026-12-31",
    "status": "Not Started",
    "created_at": "2026-09-30T12:00:00+00:00"
  }
  
  ```

*Replace `1` with the ID of the course you want to retrieve.*

**Course not found:**

* **Request:** `curl -X GET http://127.0.0.1:5000/api/courses/999`

* **Status:** `404 Not Found`

* **Response:**

  ```
  {
    "error": "Course not found."
  }
  
  ```

#### 4. Get Course Statistics

`GET /api/courses/stats`

Returns the total number of courses and the number of courses in each status category.

**Request:**

```
curl -X GET http://127.0.0.1:5000/api/courses/stats

```

**Successful response:**

* **Status:** `200 OK`

* **Example response:**

  ```
  {
    "total_courses": 4,
    "courses_by_status": {
      "Not Started": 2,
      "In Progress": 1,
      "Completed": 1
    }
  }
  
  ```

**Response fields:**

| Field | Description | 
 | ----- | ----- | 
| `total_courses` | Total number of courses | 
| `courses_by_status.Not Started` | Number of courses that have not started | 
| `courses_by_status.In Progress` | Number of courses currently in progress | 
| `courses_by_status.Completed` | Number of completed courses | 

**Empty course list response:**

If no courses have been created, the API returns:

```
{
  "total_courses": 0,
  "courses_by_status": {
    "Not Started": 0,
    "In Progress": 0,
    "Completed": 0
  }
}

```

**Example error response:**

If the application cannot read `courses.json`, the API returns:

* **Status:** `500 Internal Server Error`

* **Response:**

  ```
  {
    "error": "Unable to read courses.json: <error details>"
  }
  
  ```

#### 5. Update a Course

`PUT /api/courses/<id>`

Updates one or more details of an existing course.

The following fields can be updated:

* `name`

* `description`

* `target_date`

* `status`

The following fields **cannot** be updated:

* `id`

* `created_at`

**Update all editable fields:**

```
curl -X PUT http://127.0.0.1:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Advanced Flask REST APIs",
    "description": "Build production-style REST APIs using Flask.",
    "target_date": "2027-01-15",
    "status": "In Progress"
  }'

```

**Successful response:**

* **Status:** `200 OK`

* **Response:**

  ```
  {
    "id": 1,
    "name": "Advanced Flask REST APIs",
    "description": "Build production-style REST APIs using Flask.",
    "target_date": "2027-01-15",
    "status": "In Progress",
    "created_at": "2026-09-30T12:00:00+00:00"
  }
  
  ```

**Update one field:**

You can update only the status:

```
curl -X PUT http://127.0.0.1:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Completed"
  }'

```

The other course fields remain unchanged.

#### 6. Delete a Course

`DELETE /api/courses/<id>`

Deletes a course by its ID.

**Request:**

```
curl -X DELETE http://127.0.0.1:5000/api/courses/1

```

**Successful response:**

* **Status:** `200 OK`

* **Response:**

  ```
  {
    "message": "Course deleted successfully.",
    "course": {
      "id": 1,
      "name": "Flask REST API Fundamentals",
      "description": "Learn how to build REST APIs with Python and Flask.",
      "target_date": "2026-12-31",
      "status": "Not Started",
      "created_at": "2026-09-30T12:00:00+00:00"
    }
  }
  
  ```

## Error Responses

### Missing required fields

A new course requires: `name`, `description`, `target_date`, `status`.

* **Request:**

  ```
  curl -X POST http://127.0.0.1:5000/api/courses \
    -H "Content-Type: application/json" \
    -d '{
      "name": "Incomplete Course"
    }'
  
  ```

* **Status:** `400 Bad Request`

* **Response:**

  ```
  {
    "error": "Missing required field(s): description, target_date, status"
  }
  
  ```

### Invalid status

* **Request:**

  ```
  curl -X POST http://127.0.0.1:5000/api/courses \
    -H "Content-Type: application/json" \
    -d '{
      "name": "Example Course",
      "description": "An example course.",
      "target_date": "2026-12-31",
      "status": "Pending"
    }'
  
  ```

* **Status:** `400 Bad Request`

* **Response:**

  ```
  {
    "error": "Invalid status. Status must be one of: \"Not Started\", \"In Progress\", or \"Completed\"."
  }
  
  ```

### Invalid target date

Dates must use the format: `YYYY-MM-DD`.

* **Request:**

  ```
  curl -X POST http://127.0.0.1:5000/api/courses \
    -H "Content-Type: application/json" \
    -d '{
      "name": "Example Course",
      "description": "An example course.",
      "target_date": "31-12-2026",
      "status": "Not Started"
    }'
  
  ```

* **Status:** `400 Bad Request`

* **Response:**

  ```
  {
    "error": "target_date must use the YYYY-MM-DD format."
  }
  
  ```

### Course not found

* **Request:** `curl -X DELETE http://127.0.0.1:5000/api/courses/999`

* **Status:** `404 Not Found`

* **Response:**

  ```
  {
    "error": "Course not found."
  }
  
  ```

### Invalid JSON

* **Request:**

  ```
  curl -X POST http://127.0.0.1:5000/api/courses \
    -H "Content-Type: application/json" \
    -d '{"name": "Invalid JSON"'
  
  ```

* **Status:** `400 Bad Request`

* **Response:**

  ```
  {
    "error": "Request body must contain valid JSON."
  }
  
  ```

## Testing the API

### Test with `curl`

`curl` is a command-line tool for sending HTTP requests. Make sure the Flask application is running (`python app.py`), open another terminal window, and run the API commands.

**Recommended testing order:**

1. Create a course

2. Get all courses

3. Get the created course

4. Get course statistics

5. Update the course

6. Get the updated course

7. Delete the course

8. Try to get the deleted course

**Example Walkthrough:**

Create a course:

```
curl -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn the fundamentals of Python.",
    "target_date": "2026-11-30",
    "status": "Not Started"
  }'

```

Get all courses:

```
curl http://127.0.0.1:5000/api/courses

```

Get course by ID (assuming ID `1`):

```
curl http://127.0.0.1:5000/api/courses/1

```

Get course statistics:

```
curl http://127.0.0.1:5000/api/courses/stats

```

Update it:

```
curl -X PUT http://127.0.0.1:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }'

```

Delete it:

```
curl -X DELETE http://127.0.0.1:5000/api/courses/1

```

### Test with a Web Browser

A browser can send simple `GET` requests. Open this URL in your browser:

* All courses: `http://127.0.0.1:5000/api/courses`

* Specific course: `http://127.0.0.1:5000/api/courses/1`

* Course stats: `http://127.0.0.1:5000/api/courses/stats`

*Browsers are not convenient for testing `POST`, `PUT`, and `DELETE` requests. For those requests, use `curl`, Postman, Insomnia, or an API testing extension.*

### Test with Postman or Insomnia

For a `POST` (create) request:

1. Create a new request.

2. Choose the `POST` method.

3. Enter `http://127.0.0.1:5000/api/courses`.

4. Select a **JSON** request body.

5. Add:

   ```
   {
     "name": "Postman Testing",
     "description": "Practice testing a Flask REST API.",
     "target_date": "2026-12-31",
     "status": "Not Started"
   }
   
   ```

6. Send the request. The response should have a `201 Created` status.

## File Storage

CodeCraftHub does not use a database. Instead, all data is stored in `courses.json`.

The application loads courses from this file when it receives a request and writes the updated list back when modified.

**Reading data in Python:**

```
with open("courses.json", "r", encoding="utf-8") as file:
    courses = json.load(file)

```

**Saving data in Python:**

```
with open("courses.json", "w", encoding="utf-8") as file:
    json.dump(courses, file, indent=4)

```

*This approach is useful for learning and small projects. For a larger production application, a database would be more reliable, especially when many users or requests access the application at the same time.*

## Troubleshooting

### Problem: `python` command is not recognized

You may see: `'python' is not recognized as an internal or external command`.

Try:

```
python3 --version

```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/). On Windows, select the option to **Add Python to PATH** during installation.

### Problem: Flask is not installed

You may see: `ModuleNotFoundError: No module named 'flask'`.

Install Flask:

```
pip install Flask

```

Or with `requirements.txt`:

```
pip install -r requirements.txt

```

*Make sure your virtual environment is activated before installing packages.*

### Problem: Virtual environment is not activated

Activate it using:

* **macOS/Linux:** `source venv/bin/activate`

* **Windows CMD:** `venv\Scripts\activate`

* **Windows PowerShell:** `venv\Scripts\Activate.ps1`

### Problem: Port 5000 is already in use

Solutions:

1. Stop the other application using port `5000`.

2. Close another running Flask process.

3. Run CodeCraftHub on another port by updating `app.py`:

   ```
   app.run(debug=True, port=5001)
   
   ```

   Then use `http://127.0.0.1:5001` for requests.

### Problem: Connection refused

Make sure the server is running (`python app.py`) and that you are using the correct address (`http://127.0.0.1:5000`).

### Problem: `courses.json` does not exist

If it does not automatically create:

1. Check directory permissions.

2. Ensure you are running `app.py` from the correct directory.

3. Manually create `courses.json` with the following content:

   ```
   []
   
   ```

### Problem: Invalid JSON in `courses.json`

Check for:

* Missing or extra commas

* Missing quotation marks or brackets

* Incorrect JSON syntax

### Problem: `400 Bad Request`

Check that:

* Request header contains `Content-Type: application/json`.

* Request body contains valid JSON.

* All required fields are present and valid (`target_date` is `YYYY-MM-DD`, `status` is valid).

### Problem: `404 Course not found`

First, list all courses using `GET /api/courses` to confirm the course ID exists.

### Problem: Changes are not visible

1. Confirm the request returned a success status code.

2. Inspect `courses.json` directly.

3. Call `GET http://127.0.0.1:5000/api/courses` again.

### Problem: PowerShell handles `curl` differently

In Windows PowerShell, `curl` may alias to `Invoke-WebRequest`. Use:

```
curl.exe http://127.0.0.1:5000/api/courses

```

Or PowerShell's built-in command:

```
Invoke-RestMethod http://127.0.0.1:5000/api/courses

```

## Important Notes

* **IDs:** Start at `1`. New courses receive an ID based on the highest existing ID plus one (e.g., 1, 2, 3...).

* **Timestamps:** `created_at` is generated automatically in ISO 8601 format (e.g., `2026-09-30T12:00:00+00:00`).

* **Data Persistence:** Data stays in `courses.json` across restarts. Back up the file and avoid editing it manually while the app is running.

* **Debug Mode:** `app.run(debug=True)` provides helpful error messages during development. Do not use debug mode in public production deployments.

## Learning Exercises

1. Add three different courses with different statuses.

2. Retrieve all courses, then retrieve one course by ID.

3. Call `/api/courses/stats` to verify status counts match your added courses.

4. Update a course from `Not Started` to `In Progress`, then mark it as `Completed`.

5. Test validation: try sending an invalid status, missing name, or invalid date.

6. Delete a course and inspect `courses.json` and `/api/courses/stats` to see updated counts.

## Future Improvements

* Add a web-based frontend

* Add filtering by status

* Add searching by course name

* Add sorting by target date

* Add automated tests with `pytest`

* Add a database such as SQLite

* Add user authentication

* Add pagination, course categories, progress percentages, and learning notes