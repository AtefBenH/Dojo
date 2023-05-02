from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author_fav = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL('books_schema').query_db(query)
    
    @classmethod
    def get_book_with_fav(cls, data):
        query = "SELECT * FROM books LEFT JOIN fav_books ON fav_books.book_id = books.id LEFT JOIN authors ON fav_books.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query , data)

        book = cls(results[0])
        for row_from_db in results:

            author_data = {
                "id" : row_from_db["authors.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            book.author_fav.append(author.Author(author_data))
        return book
    
    #Add author to the list that favored the Book
    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO fav_books (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);"
        return connectToMySQL('books_schema').query_db(query, data)
    
    #Get the unfavorite books for that specific author
    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM fav_books WHERE author_id = %(id)s );"
        results = connectToMySQL('books_schema').query_db(query,data)
        unfav_books = []
        for row in results:
            unfav_books.append(cls(row))
        return unfav_books
