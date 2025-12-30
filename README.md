# Todo API

A robust RESTful API for managing todo items, built with FastAPI and PostgreSQL. This project demonstrates full CRUD (Create, Read, Update, Delete) functionality using SQLAlchemy for ORM and Pydantic for data validation.

## Features

- **Create Todo**: Add new tasks with a title, optional description, and completion status.
- **Read Todos**: Retrieve a list of all tasks with pagination support, or fetch a specific task by ID.
- **Update Todo**: Modify existing tasks (partial updates supported).
- **Delete Todo**: Remove tasks from the database.
- **Database Integration**: Persists data using PostgreSQL.

## Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todoapi
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory and add your database connection string:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

5. **Initialize the Database**
   Run the initialization script to create the necessary tables:
   ```bash
   python init_db.py
   ```

6. **Run the Application**
   Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## Author

Raji Olatubosun Joshua
