Blogapp
Using Flask to build blog that .

Integration with mongo DB.

Extension:
MONGODB: mongo DB for the users and the posts that are posted in the blog.

Testing: E2E test using curl for all the features in the blog.

Installation
Install with pip:

$ pip install -r requirements.txt
Flask Application Structure
.
├── microblog
│   ├── app
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── templates
│   │   │   ├── base.html
│   │   │   ├── delete_edit.html
│   │   │   ├── index.html
│   │   │   ├── login.html
│   │   │   └── posts.html


Run Flask
flask run
In flask, Default port is 5000






This application is a Flask web application that connects to a Postgres database and a NATS messaging server. 
The application sets up the Flask application, connects to the Postgres database and NATS server.
The routes for the application and handles incoming requests:

The root endpoint '/' and the '/count' both are a simple GET endpoint that establishes a session with the Postgres database using SQLAlchemy's ORM,
the application queries the message table and retrieve the count of the rows in the table. 
The '/hit' endpoint accepts POST method used to send message to a NATS server. 
Prometheus metrics have been integrated on the '/metrics' route
you can also check the logs for the application using python logger.

The application using environment variables to configure the connection to the Postgres database and NATS server,
also there are default values if the variables are not set.
