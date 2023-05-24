from flask_app import app
from flask import render_template, redirect, request, session, jsonify
from flask_app.models.user import User
from flask_app.models.book import Book
from flask_app.models.like import Like

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        all_books = Book.get_all()
        posted_books_id = Book.get_books_by_user({'id' : session['user_id']})
        logged_user = User.get_by_id({'id' : session['user_id']})
        liked_books_id = Like.get_books_id_for_user({'id' : session['user_id']})
        user_likes = Like.count_for_user({'user_id' : session['user_id']})
        return render_template('dashboard.html', user = logged_user, all_books = all_books, liked_books_id = liked_books_id, user_likes=user_likes, posted_books_id=posted_books_id)
    return redirect('/')

@app.route('/books/create', methods=['POST'])
def create_book():
    errors = Book.validate(request.form)
    if len(errors)==0:
        book_id = Book.save({**request.form, 'user_id':session['user_id']})
        Like.save({'user_id':session['user_id'], 'book_id':book_id})
        return jsonify({'errors' : []})
    return jsonify({'errors' : errors})

@app.route('/books/<int:book_id>/edit')
def edit_book(book_id):
    if 'user_id' in session:
        book = Book.get_by_id({'id' : book_id})
        if book:
            if Book.user_id == session['user_id'] :
                return render_template('edit_book.html', book = book)
            else :
                hacker = User.get_by_id({'id' : session['user_id']})
                if hacker.warning<1 : #TRUE MEANS IT'S HIS FIRST TIME
                    User.add_warning({'id' : session['user_id']}) #ADD A WARNING
                    ip_address = request.remote_addr
                    return render_template('hackAttempt.html', hacker=hacker, book_id = book_id, ip_address=ip_address)
                #LOGOUT THE HACKER
                return redirect('/logout')
        else :
            return render_template('404.html')
    return redirect('/')