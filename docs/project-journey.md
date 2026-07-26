# AI Knowledge Assistant - Project Journey

## Project Overview

The AI Knowledge Assistant is a full-stack application that allows users to upload documents and interact with their knowledge through AI-powered search and question answering.

The project follows production-level software engineering practices used in large technology companies.

Technologies:

- Backend: FastAPI (Python)
- Frontend: React
- Database: PostgreSQL
- ORM: SQLAlchemy
- Database Migration: Alembic
- AI Pipeline: Embeddings, Vector Search, Ollama
- Storage: S3 (planned)

---

# Phase 1: Project Initialization

## Why?

Before writing application code, we created a clean project structure.

Large applications separate responsibilities instead of putting everything in one place.

## Initial Structure

```text
ai-knowledge-assistant/

├── backend/
├── frontend/
├── docs/
├── tests/
└── README.md

Purpose
backend/

Contains the FastAPI backend application.

frontend/

Contains the React frontend application.

docs/

Contains project documentation and engineering decisions.

tests/

Contains automated tests.

Phase 2: Backend Setup
FastAPI
Why?

FastAPI was selected because:

High performance
Modern Python framework
Async support
Automatic API documentation
Good integration with AI ecosystem
Phase 3: Configuration Management

Created environment-based configuration.

Example
APP_NAME=AI Knowledge Assistant
DB_HOST=localhost
DB_PORT=5432
DB_NAME=Ai_Knowledge_Assistant
DB_USER=postgres
DB_PASSWORD=*****
OLLAMA_URL=http://localhost:11434
Why?

Sensitive information should not be hardcoded.

Flow
.env
 |
 v
Application Settings
 |
 v
FastAPI Application
Library Added
pydantic-settings

Purpose:

Reads and validates environment variables.

Phase 4: Database Layer
PostgreSQL
Why?

PostgreSQL was chosen because:

Production ready
Reliable relational database
Open source
Widely used in companies
SQLAlchemy
Why?

SQLAlchemy is an ORM.

Instead of writing SQL directly:

SELECT * FROM users;

We work with Python objects:

User()
Flow
Python Object
      |
      v
SQLAlchemy
      |
      v
PostgreSQL
Database Structure

Created:

app/

└── database/

    ├── base.py
    └── session.py
base.py

Contains the SQLAlchemy base class.

All database models inherit from this base.

session.py

Creates database sessions used by the application.

Phase 5: Database Migration System
Alembic
Why?

Database structures change over time.

Example:

Before:
users

id
email
After:
users

id
email
password_hash

Alembic tracks and applies these changes.

Migration Workflow
SQLAlchemy Model Change

        |
        v

Alembic Detects Difference

        |
        v

Migration File

        |
        v

Database Updated
Commands
Create migration:
alembic revision --autogenerate -m "message"
Apply migration:
alembic upgrade head
Phase 6: User Model

Created:

app/models/user.py
Purpose

Represents the users table in PostgreSQL.

Current structure:
users

id
email
password_hash
Phase 7: Schemas Layer

Created:

app/schemas/user.py
Why?

Models and schemas have different responsibilities.

Models:
Database structure
Schemas:
API input/output validation
Example
User sends:
{
    "email": "user@test.com",
    "password": "mypassword"
}
Database stores:
{
    "email": "user@test.com",
    "password_hash": "encrypted_value"
}
UserCreate

Used when creating a new user.

Contains:

email
password
UserResponse

Used when returning user information.

Contains:

id
email

Password is never returned.

Phase 8: Security Layer

Created:

app/core/security.py
Library Added
pip install passlib[bcrypt]
Why?

Passwords should never be stored as plain text.

Bad:
password = mypassword
Good:
mypassword

      |
      v

bcrypt hashing

      |
      v

$2b$12$.....

Database stores only the hash.

Functions
hash_password()

verify_password()
Purpose:
Create secure password hashes
Verify user passwords during login
Phase 9: API Architecture
Production structure:
app/

└── api/

    └── v1/

        ├── router.py

        └── routes/

            └── auth.py
Why API Versioning?

Future versions should not break existing users.

Example:

/api/v1/users

/api/v2/users

Both versions can exist.

API Flow
Client

GET /api/v1/auth/test

        |

        v

main.py

        |

        v

api/v1/router.py

        |

        v

routes/auth.py

        |

        v

Response
Test Endpoint

Created:

GET /api/v1/auth/test
Response:
{
    "message": "Auth router is working"
}
Confirmed:
FastAPI works
Router structure works
API versioning works
Routes are connected correctly
Current Project Status

Completed:

✅ Project structure
✅ FastAPI setup
✅ Environment configuration
✅ PostgreSQL connection
✅ SQLAlchemy setup
✅ Alembic migrations
✅ User database model
✅ User schemas
✅ Password hashing system
✅ Versioned API architecture

Next Steps
Create database dependency injection
Build user registration endpoint
Create service layer
Implement JWT authentication
Build login functionality
Connect frontend
Build document upload system
Add AI processing pipeline



































touch docs/project-journey.md