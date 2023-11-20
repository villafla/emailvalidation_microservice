How to...

A) REQUEST data: 
- HTTP POST request: Client should send HTTP POST request to the /validate-email endpoint.
- Client includes JSON data in the request body, JSON data should contain an email field with the email address to be validated.
- Example call can be found in request.py

B) RECEIVING data:
- In the validate_email route handler, MS uses the request.get_json() method to receive and parse the JSON data sent by the client.
- Extracts the email field from the received JSON data.

C) UML:


<img width="816" alt="Screenshot 2023-11-20 at 12 19 44 AM" src="https://github.com/villafla/emailvalidation_microservice/assets/132638899/e5699aec-73c4-4c0e-b5a5-c0b8123b5d6f">
