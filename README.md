# DevTrack – Issue Tracking API

## How to Run the Project

### Step 1: Clone the Repository

Download or clone the repository to your local machine.

### Step 2: Create a Virtual Environment

```powershell
py -m venv .venv
```

### Step 3: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 5: Run the Development Server

```powershell
py manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### 1. Reporters

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/reporters/` | Get all reporters |
| GET | `/api/reporters/?id=1` | Get a reporter by ID |
| POST | `/api/reporters/` | Create a new reporter |

#### Create Reporter – Request Body

```json
{
  "name": "Name",
  "email": "test@email.com",
  "team": "backend"
}
```

**Valid team values:** `backend`, `frontend`, `devops`

### 2. Issues

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/issues/` | Get all issues |
| GET | `/api/issues/?status=open` | Get issues by status |
| GET | `/api/issues/?id=1` | Get an issue by ID |
| POST | `/api/issues/` | Create a new issue |

#### Create Issue – Request Body

```json
{
  "title": "Title",
  "description": "Description",
  "status": "open",
  "priority": "medium",
  "reporter_id": 1
}
```

**Valid status values:** `open`, `in_progress`, `resolved`, `closed`

**Valid priority values:** `low`, `medium`, `high`, `critical`

---

## Postman Testing Evidence

Add screenshots of your API tests below to demonstrate the endpoints and their responses.
