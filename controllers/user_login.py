from flask import Blueprint, render_template, request, redirect
from connectors.mysql_connector import engine

from models.user import User
from sqlalchemy import select, or_
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, logout_user

user_routes = Blueprint('user_routes',__name__)

@user_routes.route("/login", methods=['GET'])
def user_login():
    return render_template("users/login.html")

@user_routes.route("/login", methods=['POST'])
def do_user_login():
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    try:
        user = session.query(User).filter(User.email==request.form['email']).first()

        if user == None:
            return {"message": "email tidak terdaftar"}
        
        # check password 
        if not user.check_password(request.form['password']):
            return {"message": "password salah"}
        
        # u/ menyimpan data user yg berhasil login ke session 
        # lalu dibuatkan session id yg akan dikembalikan ke browser dan disimpan dalam cookie 
        login_user(user, remember = False)
        return redirect('/product')

    except Exception as e:
        return {"message": "login gagal"}
    
@user_routes.route("/logout", methods=['GET'])
def do_user_logout():
    logout_user()
    return redirect('/login')