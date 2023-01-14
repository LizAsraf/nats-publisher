from panini import app as panini_app
from aiohttp import web
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

app = panini_app.App(
        service_name='sender_app',
        host='nats_messanger',
        port=4222,
)
app.setup_web_server(port=5000)
# @app.timer_task(interval=2)  
# async def publish():
#     for _ in range(10):
#         await app.publish(subject="some.publish.subject", message={'some':'message'})

# Create a connection string
db_user = os.getenv('POSTGRES_USER', default='root')
db_password = os.getenv('POSTGRES_PASSWORD', default='example')
db_url = os.getenv('DATABASE_HOST', default='db')
db_port = int(os.getenv('PORT', default='5432'))
db_name = os.getenv('POSTGRES_DB', default='messages')
connection = "postgresql://{}:{}@{}:{}/{}".format(db_user,db_password, db_url,db_port, db_name)

# Connect to Postgres
engine = create_engine(connection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# ORM Model
Base = declarative_base()

class Message(Base):
    __tablename__ = db_name

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    data = Column(String)
Base.metadata.create_all(bind=engine)
@app.http.get("/")
async def index(request):
    return web.Response(text='Hello Aiohttp!')

@app.task()
async def publish_periodically1():
    message = {"data":"request1234567890-onetime"}
    response = await app.publish(subject="request",message=message)
    print(response)

@app.http.post("/hit")
async def publish_periodically(self):
    message = {"data":"request1234567890-bypost"}
    data = message["data"]
    response = await app.publish(subject="request",message=message)
    print(response)
    return web.Response(text=data)

@app.http.get("/count")
def counter(self):
    # Establish a session
    # session = SessionLocal()
    session.begin()
    print("session  begin success")    
    try:
        print("entered to try")
        count = session.query(Message).count()
        print(f"The number of messages detected and is {count}") 
        return web.json_response({"count": count})
    except NoResultFound:
        # Handle no result error
        # logging.error("No messages found")
        print("entered to exept NoResultFound") 
        return web.json_response({"message": "No messages found"}), 404 
    except Exception as e:
        # Handle other errors
        # logging.error(str(e))
        print("entered to exept general") 
        return web.json_response({"message": "An error occurred"}), 500 
    finally:
        print("entered to finally")                
    #     logging.info("Number of messages retrieved from the database")
        session.commit()
        session.close()
        print("session closed")     

if __name__ == "__main__":
    app.start()