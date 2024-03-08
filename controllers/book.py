from flask import Blueprint, render_template, request
from connectors.mysql_connector import Session, engine
from sqlalchemy.orm import sessionmaker
from models.book import Book
from models.review import Review
from sqlalchemy import select, or_

from flask_login import current_user, login_required

book_routes = Blueprint('book_routes',__name__)

@book_routes.route("/book", methods=['GET'])
@login_required
def book_home():
    response_data = dict()

    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    try:
        book_query = select(Book)

        if request.args.get('query') != None:
            search_query = request.args.get('query')
            book_query = book_query.where(or_(Book.title.like(f"%{search_query}%"), Book.description.like(f"%{search_query}%")))

        books = session.execute(book_query)
        books = books.scalars()
        response_data['books'] = books
        
    except Exception as e:
        print(e)
        return "Error Processing Data"

    response_data['name'] = current_user.name
    return render_template("books/book_home.html", response_data = response_data)

@book_routes.route("/book/<id>", methods=['GET'])
def book_detail(id):
    response_data = dict()

    session = Session()

    try:
        book = session.query(Book).filter((Book.id==id)).first()
        if (book == None):
            return "Data not found"
        response_data['book'] = book
    except Exception as e:
        print(e)
        return "Error Processing Data"

    return render_template("books/book_detail.html", response_data = response_data)

@book_routes.route("/book", methods=['POST'])
# agar yg bisa akses /product hanya yg sdh login butuh @login_required
@login_required
def book_insert():
    
    new_book = Book(
        title=request.form['title'],
        price=request.form['price'],
        description=request.form['description']
    )

    session = Session()
    session.begin()
    try:
        session.add(new_book)
        session.commit()
    except Exception as e:
        session.rollback()
        return { "message": "Fail to insert data"}

    return { "message": "Success insert data"}

@book_routes.route("/book/<id>", methods=['DELETE'])
def book_delete(id):

    session = Session()
    session.begin()

    try:
        book = session.query(Book).filter(Book.id==id).first()
        session.delete(book)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return { "message": "Fail to delete data"}
    
    return { "message": "Success delete data"}

@book_routes.route("/book/<id>", methods=['PUT'])
def book_update(id):

    session = Session()
    session.begin()

    try:
        book = session.query(Book).filter(Book.id==id).first()

        book.title = request.form['title']
        book.price = request.form['price']
        book.description = request.form['description']

        session.commit()
    except Exception as e:
        session.rollback()
        return { "message": "Fail to Update data"}
    
    return { "message": "Success updating data"}