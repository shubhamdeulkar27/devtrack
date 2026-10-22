#How to Run Project
# Step 1 : Download Repository
# Step 2 : create virtual environment - py -m venv .venv
# Step 3 : Activate virtual enviroment - .\venv\Scripts\Activate.ps1
# Step 4 : download the dependancies by running - pip install -r .\requirements.txt
# Step 5 : run server by - py manage.py runserver

#Endpoints
Get All Reporters : Get http://127.0.0.1:8000/api/reporters/
Get Reporter By ID : Get http://127.0.0.1:8000/api/reporters?id=1
Create Reporter : Post http://127.0.0.1:8000/api/reporters/
Request : 
{
    "name": "Name",
    "email": "test@email.com",
    "team": "team"
}

Get All Issues : Get http://127.0.0.1:8000/api/issues
Get Issues By Status : Get http://127.0.0.1:8000/api/issues/?status=open
Get Issue By Id : Get http://127.0.0.1:8000/api/issues/?id=1
Create Issue : Post http://127.0.0.1:8000/api/issues/
Request : 
{
    "title": "Title",
    "description": "Description",
    "status": "status",
    "priority": "priority",
    "reporter_id": "1"
}

Postman Testing Evidance