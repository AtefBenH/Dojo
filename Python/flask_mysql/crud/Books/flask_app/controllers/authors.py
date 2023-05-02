from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def add_show_authors():
    return render_template('authors.html', authors = Author.get_all_authors())

@app.route('/authors/create', methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect ('/authors')

@app.route('/authors/<int:author_id>')
def show_author_fav(author_id):
    data = {'id': author_id}
    author = Author.get_author_with_fav(data)
    unfav_books = Book.unfavorited_books(data)
    return render_template("author_show.html", author = author, books = unfav_books)

@app.route('/authors/<int:author_id>/add_book_fav', methods=['POST'])
def add_favorate_author(author_id):
    data = {
        'author_id': author_id,
        'book_id': request.form['book_id']
    }
    Author.add_book(data)
    return redirect(f'/authors/{author_id}')