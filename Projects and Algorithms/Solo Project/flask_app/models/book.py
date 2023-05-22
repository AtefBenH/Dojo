from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_fav = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def get_book_with_fav(cls, data):
        query = "SELECT * FROM books LEFT JOIN fav_books ON fav_books.book_id = books.id LEFT JOIN users ON fav_books.user_id = users.id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query , data)

        book = cls(results[0])
        for row_from_db in results:

            user_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["users.created_at"],
                "updated_at" : row_from_db["users.updated_at"]
            }
            book.user_fav.append(user.User(user_data))
        return book
    
    #Add user to the list that favored the Book
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO fav_books (book_id, user_id) VALUES (%(book_id)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #Get the unfavorite books for that specific user
    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM fav_books WHERE user_id = %(id)s );"
        results = connectToMySQL(DATABASE).query_db(query,data)
        unfav_books = []
        for row in results:
            unfav_books.append(cls(row))
        return unfav_books
