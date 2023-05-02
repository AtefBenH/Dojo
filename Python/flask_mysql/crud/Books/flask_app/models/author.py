from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
class Author:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_books = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        return connectToMySQL('books_schema').query_db(query)
    
    @classmethod
    def get_author_with_fav(cls, data):
        query = "SELECT * FROM authors LEFT JOIN fav_books ON fav_books.author_id = authors.id LEFT JOIN books ON fav_books.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query , data)
        # print('~~'*20, results, '~~'*20)
        author = cls(results[0])
        for row_from_db in results:
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            author.fav_books.append(book.Book(book_data))
        return author
    
    #Add author's Favorite Book to fav_books table
    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO fav_books (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);"
        return connectToMySQL('books_schema').query_db(query, data)
    
    #Get the authors that didn't like a specefic book
    @classmethod
    def unfav_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM fav_books WHERE book_id = %(id)s );"
        unfav_authors = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for res in results:
            unfav_authors.append(cls(res))
        return unfav_authors