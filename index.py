from dotenv import load_dotenv
from flask import Flask
from connectors.mysql_connector import engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from models.book import Book
from sqlalchemy import select

from flask_login import LoginManager
from models.user import User
import os

# Load Controller Files
from controllers.book import book_routes
from controllers.user_login import user_routes_login
from controllers.user_register import user_routes_register

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)

# untuk cek data cookie
# u/ mengetahui siapa yg login
@login_manager.user_loader
def load_user(user_id):
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    return session.query(User).get(int(user_id))

app.register_blueprint(book_routes)
app.register_blueprint(user_routes_register)
app.register_blueprint(user_routes_login)

# Book Route
@app.route("/")
def hello_world():
    
    # Fetch all Books
    book_query = select(Book)
    
    connection = engine.connect()
    Session = sessionmaker(connection)
    with Session() as session:
        result = session.execute(book_query)
        for row in result.scalars():
            print(f'ID: {row.id}, Name: {row.name}')

    return "<p>Insert Success</p>"