from dotenv import load_dotenv
from flask import Flask
from connectors.mysql_connector import engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from models.product import Product
from sqlalchemy import select

from flask_login import LoginManager
from models.user import User
import os

# Load Controller Files
from controllers.product import product_routes
from controllers.user_login import user_routes
from controllers.user_register import user_routes

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

app.register_blueprint(product_routes)
app.register_blueprint(user_routes)

# Product Route
@app.route("/")
def hello_world():
    
    # Fetch all Products
    product_query = select(Product)
    
    connection = engine.connect()
    Session = sessionmaker(connection)
    with Session() as session:
        result = session.execute(product_query)
        for row in result.scalars():
            print(f'ID: {row.id}, Name: {row.name}')

    return "<p>Insert Success</p>"