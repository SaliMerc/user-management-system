User Management System - Django REST Framework

Project Purpose

This project is a robust user management system built with Django and Django REST Framework. It provides a secure API backend for handling user accounts with full CRUD functionality, including user creation, deletion, password changes, and profile updates.

Tech Stack

- Backend Framework: Django 4.x
- API Framework: Django REST Framework (DRF)
- Database: SQLite
- Authentication: Token Authentication (JWT)
- Validation: Django model validators + DRF serializers
- Testing: Postman collection

Features Implemented

1. User Creation: Secure user registration endpoint
2. User Deletion: Account removal functionality
3. Password Management: Secure password change endpoint
4. Profile Updates: Modify user details
5. Data Validation: Comprehensive input validation

Setup Instructions

Prerequisites

- Python 3.9+
- pip (Python package manager)
- Virtualenv (recommended)

Installation

1. Clone the repository:
   ```bash
   git clone (https://github.com/SaliMerc/user-management-system/)
   cd UserManagement
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   Linux: source venv/bin/activate
   On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

Running the Development Server
```bash
python manage.py runserver
```
The API will be available at `http://localhost:8000/api/`

Postman Collection

The repository includes a Postman collection (`https://salinemercy.postman.co/workspace/Saline-Mercy' 's-Workspace~7d90ad68-1f65-4df4-8a66-051acda73610/collection/44878844-360eed90-9448-43d6-927c-6652947211ca?action=share&creator=44878844&active-environment=44878844-53432727-a9e3-49c3-83d5-22bf63b190a0`) with pre-configured requests for all API endpoints. 


API ENDPOINTS   
1. Admin Login

   Endpoint: /api/login/  
   Method: POST  
   Request Body:    
      ```json
      {
       "username": "string",
       "password": "string"
      }
   ```
   Response:  
      ```json
      {
       "message": "string",
       "access": "string",
       "refresh": "string"
      }
      ```

2. Getting a list of all users in the system  

   Endpoint: /api/get-users/  
   Method: GET  
   Headers:  
   Authorization: Bearer <access_token>  
   Content-Type: application/json  
   Response:  
      ```json
      [
       {
           "id": "integer",
           "username": "string",
           "password": "string",
           "email": "string",
           "first_name": "string",
           "last_name": "string",
           "display_name": "string",
           "phone_number": "integer",
           "city": "string",
           "country": "string",
           "profile_picture": ""image/...."
       }
      ]
      ```
3. Creating a new user

   Endpoint: /api/create-user/  
   Method: POST  
   Headers:  
   Authorization: Bearer <access_token>  
   Content-Type: form-data  
   
   Request Body:  
      ```json
      {
        "id": "integer",
        "password": "string",
        "username": "string",
        "password": "string",
        "email": "string",
        "first_name": "string",
        "last_name": "string",
        "display_name": "string",
        "phone_number": "integer",
        "city": "string",
        "country": "string",
        "profile_picture": "image/...."
      }
      ```
   Response:  
      ```json
       {
           "username": "string",
           "email": "string",
           "first_name": "string",
           "last_name": "string",
           "display_name": "string",
           "phone_number": "integer",
           "city": "string",
           "country": "string"
       }
      ```

4. Updating User Details  

Endpoint: /api/update-user-details/<int:id>/  
Method: PATCH  
Headers:  
Authorization: Bearer <access_token>  
Content-Type: application/json  
   Request Body:  
   ```json
   {
     "password": "string",
     "username": "string",
     "password": "string",
     "email": "string",
     "first_name": "string",
     "last_name": "string",
     "display_name": "string",
     "phone_number": "integer",
     "city": "string",
     "country": "string"
   }
   ```
   Response:  
   ```json
    {
        "username": "string",
        "password": "string",
        "email": "string",
        "first_name": "string",
        "last_name": "string",
        "display_name": "string",
        "phone_number": "integer",
        "city": "string",
        "country": "string"
    }
   ```
6. Changing User Passwords  

Endpoint: /api/change-password/<int: id>/  
Method: POST  
Headers:  
Authorization: Bearer <access_token>  
Content-Type: application/json  
   Request body:  
   ```json
    {
        "old_password": "string",
        "new_password": "string",
        "confirm_password": "string",
    }
   ```
   Response:  
   ```json
    {
        "Success": [
        "Password changed successfully."
    ]
    }
   ```
7. Deleting users from the system  

Endpoint: /api/user/delete/<int: id>/  
Method: DELETE  
Headers:  
Authorization: Bearer <access_token>  
Content-Type: application/json  
   Response:  
   ```json
    {
    "Deletion": "User deleted successfully"
   }
   ```
