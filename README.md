# Event Planner

Event Planner is a web application built with **FastAPI** for managing and organizing events. 
It uses **MongoDB** as the database and implements secure authentication with **OAuth2** and **JWT**. 
The application is tested with **Pytest**, and code coverage is tracked using **Coverage**. 
Configuration is simplified with **python-dotenv**.

---

## Features
- Create, update, and manage events.
- User authentication and authorization with OAuth2 and JWT.
- Scalable and efficient backend built with FastAPI.
- MongoDB integration for fast and flexible data storage.
- Comprehensive testing suite using Pytest and Coverage.

---

## Technologies Used
- **FastAPI**: High-performance Python web framework.
- **MongoDB**: NoSQL database for storing application data.
- **Pytest**: Testing framework for ensuring application reliability.
- **Coverage**: Tool for measuring test coverage.
- **OAuth2 & JWT**: Secure authentication and token-based authorization.
- **python-dotenv**: Simplifies the management of environment variables.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/event-planner.git
   cd event-planner
   
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
   ```pip install -r requirements.txt```

4. Create a .env file in the project root and configure the following environment variables:
   DATABASE_URL=mongodb://localhost:27017
   DATABASE_NAME=your_database_name
   SECRET_KEY=your_secret_key

5. Run the application:
   ```uvicorn main:app --reload```

6. Access the API documentation at:
    - Swagger UI: http://127.0.0.1:8000/docs
    - ReDoc: http://127.0.0.1:8000/redoc

---

## Running Tests  
To run the tests, use the following command:
  `pytest`  
To measure test coverage:
   `coverage run -m pytest`  
   `coverage report`  
For a detailed HTML report:
   `coverage html`




