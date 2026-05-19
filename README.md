# 🚗 Vehicle AI Platform

A production-oriented backend engineering project built using FastAPI, Pydantic, SQLite, SQLAlchemy , Docker, Pytest (Testing Workflows), AWS Cloud, and AI system architecture.

This project was developed step-by-step from absolute zero to showcase how modern backend systems are architected, validated, persisted, scaled, deployed, and evolved into cloud-native AI-enabled applications.

---

# 🎯 Project Vision

Vehicle AI Platform is designed as a scalable backend system for managing and analyzing vehicle incidents.

The project demonstrates:

- Backend API engineering (FastAPI)
- Layered architecture
- Database persistence (Sqlite3 db)
- RESTful API design
- Pydantic domain modelling
- API Contracts
- Serialization and Deserialization
- Validation 
- SQL & relational database concepts
- Async & concurrency fundamentals
- Production reliability concepts
- Docker containerization
- Testing workflows
- AWS deployment architecture
- AI integration pipelines

---

# 🏗️ System Architecture

```text
Client Applications
        ↓
FastAPI HTTP Layer
        ↓
Pydantic Validation Layer
        ↓
Service Layer (Business Logic) + (AI Workflows/Layer)
        ↓
Database Access Layer
        ↓
SQLite / SQL Database
        ↓
Persistent Storage
```

---

# 📂 Project Structure

```text
Vehicle-AI-Platform/
│
├── main.py
│
├── Models/
│   └── VehicleIncidentModel.py
│
├── Services/
│   └── Incidents.py
│
├── DatabaseLayer/
│   └── db.py
│
├── Tests/
│   └── test_incidents.py
│
├── Dockerfile
├── requirements.txt
├── README.md
│
└── Vehicle_Incidents.db
```

---

# ⚡ Core Features

## ✅ REST API CRUD Operations

- Create Incident
- Get All Incidents
- Get Incident By ID
- Update Incident
- Delete Incident

---

## ✅ Persistent Database Storage

The application uses SQLite as a relational database engine.

Features:

- Persistent storage
- Auto-generated primary keys
- SQL CRUD operations
- Database initialization
- Relational schema design
- Transaction commits
- Database migration concepts

---

## ✅ Layered Backend Architecture

The project follows separation of concerns:

| Layer | Responsibility |
|---|---|
| API Layer | HTTP communication |
| Service Layer | Business logic & workflows |
| Database Layer | Persistence & SQL execution |
| Database Engine | Data storage & consistency |

---

## ✅ Vehicle Incident Analysis

The service layer analyzes vehicle incident descriptions and categorizes incidents into:

- Engine
- Brake
- Battery
- General

along with:

- Severity levels
- Suggested actions
- Maintenance recommendations

---

# 🧠 Concepts Implemented & Learned

# 1️⃣ Backend Engineering Fundamentals

- Backend architecture
- Client-server model
- Layered architecture
- Separation of concerns
- CRUD operations
- REST API design
- HTTP request lifecycle
- API contracts
- Service orchestration

---

# 2️⃣ FastAPI Concepts

- FastAPI routing
- Path parameters
- Query parameters
- Request body handling
- Response models
- Automatic OpenAPI generation
- Swagger documentation
- ASGI architecture
- Request validation
- Response validation

---

# 3️⃣ Pydantic Concepts

- BaseModel
- Request models
- Response models
- Data validation
- Serialization
- Deserialization
- JSON encoding/decoding
- Type safety
- API schema generation

---

# 4️⃣ JSON Concepts

## JSON Object

```json
{
  "vehicle": "Audi",
  "issue": "Engine overheating"
}
```

## JSON Array

```json
[
  {
    "id": 1
  },
  {
    "id": 2
  }
]
```

### Python Mapping

| JSON | Python |
|---|---|
| Object | dict |
| Array | list |
| String | str |
| Number | int / float |
| Boolean | bool |
| Null | None |

---

# 5️⃣ Database Engineering Concepts

## Relational Databases

- Tables
- Rows
- Columns
- Primary keys
- Database schema
- Persistent storage
- SQL operations

---

## SQLite Concepts

- Embedded database engine
- Database initialization
- Persistent `.db` file
- SQL execution
- Auto-generated IDs
- Transactions
- Commits
- Cursors
- Database connections

---

## SQL Concepts

### CREATE TABLE

```sql
CREATE TABLE incidents (
    id INTEGER PRIMARY KEY,
    vehicle TEXT,
    issue TEXT,
    category TEXT,
    status TEXT,
    action TEXT
)
```

### INSERT

```sql
INSERT INTO incidents (...)
VALUES (...)
```

### SELECT

```sql
SELECT * FROM incidents
```

### UPDATE

```sql
UPDATE incidents SET ...
```

### DELETE

```sql
DELETE FROM incidents WHERE id=?
```

---

# 6️⃣ Database Architecture Concepts

## Database Layer Responsibilities

- SQL query execution
- Persistence management
- Database interaction
- Connection management
- Transaction handling

---

## Transactions & Locks

### Transactions

Ensure operations either:

- Fully succeed
- OR fully rollback

### Locks

Prevent unsafe concurrent modifications.

---

# 7️⃣ Concurrency & Async Concepts

## Synchronous Execution

```text
Request
   ↓
Thread waits during I/O
```

---

## Asynchronous Execution

```text
Request pauses during waiting
        ↓
Server handles other requests meanwhile
```

---

## Concepts Learned

- Blocking vs non-blocking operations
- Threadpool
- Event loop
- Async architecture
- Concurrency
- Request lifecycle
- Waiting vs computation
- Database consistency
- Race conditions

---

# 8️⃣ Error Handling & Reliability

## HTTP Status Codes

| Status | Meaning |
|---|---|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 404 | Resource Not Found |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## Error Handling Principles

- Graceful failures
- Structured API responses
- Layer-specific responsibilities
- Infrastructure vs business errors
- Controlled exception propagation

---

# 9️⃣ Testing Concepts

The project architecture is designed to support production-grade testing using pytest.

## Testing Features

- Unit testing
- API testing
- Service layer testing
- Database testing
- Mocking dependencies
- Automated regression testing
- CI/CD-ready testing workflows

## Tools

- pytest
- FastAPI TestClient
- Mocking libraries

---

# 🔟 Docker & Containerization

The backend will be containerized using Docker.

## Concepts

- Docker images
- Containers
- Environment isolation
- Dependency packaging
- Portable deployments
- Production runtime consistency

## Components

- Dockerfile
- docker-compose
- Multi-container architecture
- Environment variables

---
# ☁️ AWS Cloud Engineering 

The project is designed to evolve into a cloud-native backend system.

##  AWS Concepts

- EC2 deployment
- RDS databases
- S3 object storage
- IAM permissions
- Cloud networking
- Infrastructure as Code
- Monitoring & logging
- Auto scaling

## Infrastructure as Code

Planned using:

- AWS CDK
- Cloud-native deployment workflows

---

# 🤖 AI Layer & Future Expansion

The system is designed to evolve into an AI-powered automotive platform.

## Planned AI Features

- AI incident classification
- Predictive maintenance
- Vehicle telemetry analysis
- ML inference pipelines
- RAG-based maintenance assistant
- Cloud AI integration
- Real-time analytics
- AI recommendation engine

---

# 🚀 Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd Vehicle-AI-Platform
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

---

# ▶️ Run Application

```bash
uvicorn main:app --reload
```

---

# 📖 Swagger Documentation

Once server starts:

```text
http://127.0.0.1:8000/docs
```

Interactive API documentation is automatically generated.

---

# 📌 API Endpoints

## Home Route

```http
GET /
```

---

## Get All Incidents

```http
GET /incidents
```

---

## Get Incident By ID

```http
GET /incident/{id}
```

---

## Create Incident

```http
POST /incident
```

### Request Body

```json
{
  "vehicle": "Audi A6",
  "issue": "Engine overheating"
}
```

---

## Update Incident

```http
PUT /incident/{id}
```

---

## Delete Incident

```http
DELETE /incident/{id}
```

---

# 🔒 Security & Reliability Goals

Planned production goals include:

- Authentication & authorization
- JWT tokens
- API rate limiting
- Structured logging
- Monitoring & observability
- Secure secret management
- Production-grade error handling
- Cloud deployment security

---

# 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- Backend engineering
- REST APIs
- FastAPI
- Pydantic
- SQLite
- SQL
- Layered architecture
- Persistence
- Serialization
- Concurrency concepts
- Async principles
- Database transactions
- Reliability engineering
- Cloud-native architecture concepts

---

# 👨‍💻 Developer

Nikhil Chakravarthy

---

# 📜 License

This project was built for backend engineering learning, cloud engineering preparation, AI systems exploration, and production architecture understanding.

