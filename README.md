# Todo API

A secure RESTful API for managing todo items with JWT authentication, built with FastAPI and PostgreSQL. This project demonstrates full CRUD (Create, Read, Update, Delete) functionality with user authentication using SQLAlchemy for ORM, Pydantic for data validation, and bcrypt for password hashing.

## Features

### Authentication

- **User Registration**: Create accounts with username, email, and securely hashed passwords using bcrypt.
- **User Login**: Authenticate with credentials and receive a JWT access token.
- **Protected Routes**: All todo endpoints require a valid JWT token in the Authorization header.
- **Token-Based Security**: Stateless authentication using JSON Web Tokens with configurable expiration.

### Todo Management

- **Create Todo**: Add new tasks with a title, optional description, and completion status (linked to authenticated user).
- **Read Todos**: Retrieve a list of all tasks with pagination support, or fetch a specific task by ID.
- **Update Todo**: Modify existing tasks (partial updates supported).
- **Delete Todo**: Remove tasks from the database.
- **User-Scoped Data**: Each todo is associated with the user who created it via user_id.

### Infrastructure

- **Database Integration**: Persists data using PostgreSQL with Docker containerization.
- **CORS Support**: Configured for frontend integration from multiple origins.

## Tech Stack

- **Language**: Python 3.12
- **Framework**: FastAPI
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Authentication**: JWT (python-jose), bcrypt (passlib)
- **Server**: Uvicorn
- **Containerization**: Docker, Docker Compose

## Setup and Installation

### Prerequisites

- Python 3.12+
- Docker and Docker Compose
- PostgreSQL (or use the provided Docker configuration)

### Steps

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd todoapi
   ```

2. **Start the PostgreSQL database**

   ```bash
   docker-compose up -d
   ```

   This creates a PostgreSQL container with the database `tododb` on port `5432`.

3. **Create a virtual environment**

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Environment Configuration**
   Create a `.env` file in the root directory with the following variables:

   ```
   # Database
   DATABASE_URL=postgresql://todouser:todopassword@localhost:5432/tododb

   # JWT Configuration
   JWT_SECRET_KEY=your-secret-key-here
   JWT_ALGORITHM=HS256
   JWT_EXPIRATION_MINUTES=30
   ```

   **Important**: Replace `your-secret-key-here` with a strong, random secret key for production.

6. **Initialize the Database**
   Run the initialization script to create the necessary tables:

   ```bash
   python init_db.py
   ```

7. **Run the Application**
   Start the development server:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## API Reference for Frontend Developers

### Base URL

- **Local (Docker)**: `http://localhost:8001`
- **Local (Python)**: `http://localhost:8000`
- **Production (AWS)**: `http://<YOUR_EC2_PUBLIC_IP>:8001`

### Interactive Documentation

FastAPI provides automatic interactive documentation (Swagger UI). This is the best place to test endpoints and see exact request/response schemas.

- **URL**: `/docs` (e.g., `http://localhost:8001/docs`)

### OpenAPI Specification

You can generate client libraries (e.g., for TypeScript/React) using the OpenAPI JSON spec.

- **URL**: `/openapi.json`

### Endpoints Summary

#### Authentication Endpoints

| Method | Endpoint         | Description                | Request Body / Params                                                     |
| :----- | :--------------- | :------------------------- | :------------------------------------------------------------------------ |
| `POST` | `/auth/register` | Register a new user        | JSON: `{ "username": "string", "email": "string", "password": "string" }` |
| `POST` | `/auth/login`    | Authenticate and get token | Form: `username`, `password` (OAuth2 password flow)                       |

**Login Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Todo Endpoints (Protected)

All todo endpoints require authentication. Include the JWT token in the Authorization header:

```
Authorization: Bearer <access_token>
```

| Method   | Endpoint      | Description         | Request Body / Params                                                        |
| :------- | :------------ | :------------------ | :--------------------------------------------------------------------------- |
| `GET`    | `/`           | Health check        | None                                                                         |
| `GET`    | `/todos/`     | List all todos      | Query: `skip` (default 0), `limit` (default 100)                             |
| `POST`   | `/todos/`     | Create a todo       | JSON: `{ "title": "string", "description": "string", "completed": boolean }` |
| `GET`    | `/todos/{id}` | Get a specific todo | Path: `id` (int)                                                             |
| `PUT`    | `/todos/{id}` | Update a todo       | Path: `id` (int). JSON: Partial todo object                                  |
| `DELETE` | `/todos/{id}` | Delete a todo       | Path: `id` (int)                                                             |

### CORS Configuration

The API allows requests from `http://localhost:3000`, `http://localhost:5173`, and `http://localhost:8080`. To add more origins, update `app/main.py`.

## Project Structure

```
todoapi/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application entry point
│   ├── database.py       # Database connection and session management
│   ├── models.py         # SQLAlchemy ORM models (User, Todo)
│   ├── schemas.py        # Pydantic validation schemas
│   ├── crud.py           # Database CRUD operations
│   ├── auth.py           # JWT and password utilities
│   └── routers/
│       ├── __init__.py
│       ├── auth.py       # Authentication endpoints
│       └── todos.py      # Todo endpoints
├── init_db.py            # Database initialization script
├── docker-compose.yml    # PostgreSQL container configuration
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in version control)
└── README.md
```

## Author

Raji Olatubosun Joshua
