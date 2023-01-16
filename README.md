# nats-listener

This application is a simple web service that allows for easy integration with a NATS messaging service. 
It sets up a web server on port 5000 and defines several routes for interacting with the messaging service and a Postgres database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- A running NATS messaging service
- A running Postgres database

### Installing

1. Clone the repository
'''
    $ git clone git@github.com:LizAsraf/nats-publisher.git
'''

2. Create a virtual environment and activate it
'''
    $ python3 -m venv env
    $ source env/bin/activate
'''

3. Install the dependencies
'''
    $ pip install -r requirements.txt
'''

4. Set the following environment variables:
- `POSTGRES_USER`: the username for the Postgres database
- `POSTGRES_PASSWORD`: the password for the Postgres database
- `DATABASE_HOST`: the hostname or IP address of the Postgres database
- `PORT`: the port number of the Postgres database
- `POSTGRES_DB`: the name of the Postgres database

5. Run the application
'''
    $ python sender_app.py
'''

## Usage

Once the application is running, you can access the following routes:
- `/`: Returns a simple "Hello Aiohttp!" message
- `/hit`: Publishes a message to the "request" subject and returns the message data
- `/count`: Queries the Postgres database for the number of rows in the "messages" table and returns that count as a JSON response

## Built With

* [panini](https://pypi.org/project/panini/) - A library for easy integration with NATS messaging services
* [aiohttp](https://docs.aiohttp.org/en/stable/) - Asynchronous HTTP client/server framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - A SQL toolkit and ORM

## Authors

* **Liz Asraf** - *Initial work* - [Your Github](https://github.com/LizAsraf/)