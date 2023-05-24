from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.author = data['author']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_fav = []
    
    @staticmethod
    def validate(data):
        errorMessages = []
        if len(data['title'])<1:
            errorMessages.append("Book Must Have a Title")

        if len(data['author'])<2:
            errorMessages.append("Author must contain at least 2 characters")
        
        if len(data['description'])<5:
            errorMessages.append("Description must contain at least 5 characters")
        return errorMessages

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (user_id, title, author, description) VALUES (%(user_id)s, %(title)s, %(author)s, %(description)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM books JOIN users ON books.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for row in results:
            book = cls(row)
            book.creator = f"{row['first_name']} {row['last_name']}"
            books.append(book)
        return books
    
    # - GET ONE BY ID
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM books WHERE id = %(id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def get_books_by_user(cls, data):
        query = """
            SELECT books.id FROM books JOIN users ON books.user_id = users.id WHERE users.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        posted_books_id = []
        for row in results:
            posted_books_id.append(row['id'])
        return posted_books_id

    @classmethod
    def get_book_with_fav(cls, data):
        query = "SELECT * FROM books LEFT JOIN likes ON likes.book_id = books.id LEFT JOIN users ON likes.user_id = users.id WHERE books.id = %(id)s;"
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
        query = "INSERT INTO likes (book_id, user_id) VALUES (%(book_id)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #Get the unfavorite books for that specific user
    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM likes WHERE user_id = %(id)s );"
        results = connectToMySQL(DATABASE).query_db(query,data)
        unfav_books = []
        for row in results:
            unfav_books.append(cls(row))
        return unfav_books
