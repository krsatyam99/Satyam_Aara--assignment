# Satyam_Aara--assignment
Django Rest Framework Project
Introduction
This is a Django Rest Framework project that uses Simple JWT for authentication and Django's built-in User model for user management.

Installation
To install the required packages, run the following command:

Copy code
pip install -r requirements.txt
Authentication
This project uses Simple JWT for authentication. 
Copy code
/auth/token/
with the following payload:

json
Copy code
{
    "username": "<username>",
    "password": "<password>"
}
This will return an access token, which can be used to make authenticated requests to other endpoints.

API Endpoints
The following API endpoints are available:

Postman Collection
A Postman collection is available for testing the API endpoints. You can import the collection by clicking the following link:

Postman Collection Link

API Flow Diagrams
The following API flow diagrams illustrate the steps involved in making requests to the various endpoints:

API Flow Diagrams Image

Video Link
A video demonstration of the project is available at the following link:

Video Link
