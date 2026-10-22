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

<img width="1107" height="960" alt="Screenshot 2026-10-22 123246" src="https://github.com/user-attachments/assets/74fca279-4b8b-4dc6-b3e7-fe24fe50de8e" />
<img width="1117" height="783" alt="Screenshot 2026-10-22 123303" src="https://github.com/user-attachments/assets/691634de-10e6-4cf6-8dcb-28706c75df42" />
<img width="1100" height="780" alt="Screenshot 2026-10-22 123319" src="https://github.com/user-attachments/assets/c721e55f-4365-452f-a365-1ed27003bd10" />
<img width="1082" height="757" alt="Screenshot 2026-10-22 125721" src="https://github.com/user-attachments/assets/0c663fbd-39bd-44c6-a0b1-2a0844451a50" />
<img width="1185" height="772" alt="Screenshot 2026-10-22 125745" src="https://github.com/user-attachments/assets/261ef379-3c77-47b6-83b0-ab133ee8e913" />
<img width="1092" height="803" alt="Screenshot 2026-10-22 125802" src="https://github.com/user-attachments/assets/327f5b4d-6e7f-4db5-895f-51ad8e1bf5f4" />
<img width="1095" height="891" alt="Screenshot 2026-10-22 125819" src="https://github.com/user-attachments/assets/5ae7cca2-47a8-471a-82fe-3358dba9b155" />
<img width="1051" height="940" alt="Screenshot 2026-10-22 125900" src="https://github.com/user-attachments/assets/d67c4093-1ccf-4abf-8c9f-2fcb91f5246c" />
<img width="1095" height="835" alt="Screenshot 2026-10-22 130816" src="https://github.com/user-attachments/assets/91dc7951-eb16-4d07-a236-9f8e1eb82c60" />
<img width="1097" height="827" alt="Screenshot 2026-10-22 130827" src="https://github.com/user-attachments/assets/d3a952f2-3f0f-44c4-a4ae-102d7f8097a1" />
<img width="1077" height="847" alt="Screenshot 2026-10-22 131119" src="https://github.com/user-attachments/assets/803d55ca-f500-4fa8-9cd4-a2c69ef0bd14" />
<img width="1101" height="797" alt="Screenshot 2026-10-22 131139" src="https://github.com/user-attachments/assets/c330131c-2926-4188-812e-df886d203c55" />
<img width="1062" height="731" alt="Screenshot 2026-10-22 131216" src="https://github.com/user-attachments/assets/71de73d1-6ef8-439a-b5a7-b06b16c631c1" />
<img width="1078" height="777" alt="Screenshot 2026-10-22 131234" src="https://github.com/user-attachments/assets/831b3b05-8101-4e72-8d25-62ef75bc3338" />
