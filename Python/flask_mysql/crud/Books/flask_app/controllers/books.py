from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books/new')
def new_book():
    return render_template('new_book.html', books = Book.get_all_books())

@app.route('/books/create', methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect ('/books/new')

@app.route('/books/<int:book_id>')
def show_book_fav(book_id):
    data = {'id': book_id}
    book = Book.get_book_with_fav(data)
    unfav_authors = Author.unfav_authors(data)
    return render_template("book_show.html", book = book, authors = unfav_authors)

@app.route('/books/<int:book_id>/add_author_fav', methods=['POST'])
def add_favorite_book(book_id):
    data = {
        'book_id': book_id,
        'author_id': request.form['author_id']
    }
    Book.add_author(data)
    return redirect(f'/books/{book_id}')
