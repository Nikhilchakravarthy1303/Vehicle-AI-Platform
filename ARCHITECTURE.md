# Vehicle AI Platform Architecture

```mermaid
flowchart TD
    Client["Client / Swagger UI / API Consumer"]

    subgraph API["FastAPI HTTP Layer"]
        Routes["API Routes in main.py"]
        Auth["JWT Auth Dependency"]
        Validation["Pydantic Request / Response Models"]
        Exceptions["Custom Exception Handlers"]
    end

    subgraph Services["Service Layer"]
        IncidentService["Incident Service"]
        UserService["User Service"]
        SearchService["Semantic Search Service"]
    end

    subgraph AI["AI Intelligence Workflows"]
        LLMWorkflow["Incident AI Classification Workflow"]
        RetrievalWorkflow["Incident Retrieval Workflow"]
        OpenRouter["OpenRouter / OpenAI-compatible LLM"]
    end

    subgraph Persistence["Persistence Layer"]
        DBLayer["SQLite Database Layer"]
        SQLite["Vehicle_Incidents.db"]
        ChromaClient["Chroma Client"]
        ChromaDB["Persistent Chroma Vector DB"]
    end

    subgraph Security["Security"]
        PasswordHashing["bcrypt Password Hashing"]
        JWT["JWT Token Creation / Verification"]
    end

    subgraph Runtime["Runtime / Operations"]
        Docker["Docker / docker-compose"]
        Env["Environment Config"]
        Logging["File Logging"]
    end

    Client --> Routes
    Routes --> Auth
    Routes --> Validation
    Auth --> JWT
    Routes --> IncidentService
    Routes --> UserService
    Routes --> SearchService
    Routes --> Exceptions

    UserService --> PasswordHashing
    UserService --> JWT
    UserService --> DBLayer

    IncidentService --> LLMWorkflow
    LLMWorkflow --> OpenRouter
    LLMWorkflow --> DBLayer
    LLMWorkflow --> ChromaClient

    SearchService --> RetrievalWorkflow
    RetrievalWorkflow --> ChromaClient

    DBLayer --> SQLite
    ChromaClient --> ChromaDB

    Exceptions --> Logging
    Docker --> Routes
    Env --> Routes
    Env --> DBLayer
    Env --> LLMWorkflow
    Env --> JWT
```

## Request Flow

```mermaid
sequenceDiagram
    participant Client
    participant FastAPI as FastAPI Routes
    participant Auth as JWT Auth
    participant Service as Service Layer
    participant AI as AI Workflow
    participant LLM as OpenRouter LLM
    participant DB as SQLite DB
    participant Vector as Chroma DB

    Client->>FastAPI: Send API request
    FastAPI->>Auth: Validate bearer token
    Auth-->>FastAPI: Current user
    FastAPI->>Service: Call business logic

    alt Create incident
        Service->>AI: Analyze vehicle issue
        AI->>LLM: Request JSON classification
        LLM-->>AI: Summary, category, severity, action
        AI->>DB: Save incident record
        AI->>Vector: Store searchable incident document
        AI-->>Service: Return AI result
    else Semantic search
        Service->>Vector: Query similar incidents
        Vector-->>Service: Matching incident documents
    else User login
        Service->>DB: Fetch user by username
        Service-->>FastAPI: Return JWT token
    end

    Service-->>FastAPI: Return response
    FastAPI-->>Client: JSON response
```

## Main Components

- `main.py`: FastAPI application, route registration, authentication dependency usage.
- `Models/`: Pydantic API contracts for incidents and users.
- `Services/`: Business logic for incidents, users, login, and semantic search.
- `AIIntelligenceWorkflows/`: LLM-based incident classification and Chroma retrieval logic.
- `DatabaseLayer/`: SQLite persistence for incidents and users.
- `VectorDB/`: Chroma persistent vector database integration.
- `AuthHandler/`: Password hashing and JWT token handling.
- `ExceptionHandlers/`: API-level exception mapping and structured error responses.
- `Core/Logging.py`: Application file logging.
- `Dockerfile` and `docker-compose.yml`: Containerized runtime setup.
