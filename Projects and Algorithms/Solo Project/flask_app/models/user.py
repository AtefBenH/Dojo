from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import book
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.warning = data['warning']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_books = []
    
    # =====================Validations=====================
    #? PASSWORD MUST HAVE AT LEAST ONE UPPERCASE AND ONE NUMBER
    
    @staticmethod
    def verify_password(str):
        upper_in = False
        number_in = False
        
        for char in str:
            if char.isupper():
                upper_in = True
            if char.isdigit():
                number_in = True
        
        if upper_in and number_in:
            return True
        else:
            return False

    # @staticmethod
    # def validate(data):
    #     is_valid = True
    #     if len(data['first_name'])<2:
    #         is_valid = False
    #         flash("First Name must contain at least 2 characters","register")
    #     if len(data['last_name'])<2:
    #         is_valid = False
    #         flash("Last Name must contain at least 2 characters","register")
    #     if not EMAIL_REGEX.match(data['email']): 
    #         is_valid = False
    #         flash("Email not valid","register")
    #     elif User.get_by_email({'email':data['email']}):
    #         is_valid = False
    #         flash("Email Already Exists","register")
    #     if len(data['password']) <8:
    #         is_valid = False
    #         flash("Password Must Have More Than 8 Characters", "register")
    #     elif not User.verify_password(data['password']) :
    #         is_valid = False
    #         flash("Password Must Contain At Least A Number And An Uppercase Character", "register")
    #     elif data['password']!= data['confirm_password']:
    #         is_valid = False
    #         flash("Password and Confirmation Doesn't Match", "register")
    #     return is_valid

    # =======================Queries=======================

    # - CREATE
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # - GET ONE BY EMAIL
    @classmethod
    def get_by_email(cls,data):
        query = """
            SELECT * FROM users WHERE email = %(email)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])

    # - GET ONE BY ID
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM users WHERE id = %(id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    #UPDATE WARNINGS FOR HACKERS
    @classmethod
    def add_warning(cls, data):
        query = "UPDATE users SET warning = warning + 1 WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def get_user_with_fav(cls, data):
        query = "SELECT * FROM users LEFT JOIN fav_books ON fav_books.user_id = users.id LEFT JOIN books ON fav_books.book_id = books.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query , data)
        # print('~~'*20, results, '~~'*20)
        user = cls(results[0])
        for row_from_db in results:
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            user.fav_books.append(book.Book(book_data))
        return user
    
    #Add user's Favorite Book to fav_books table
    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO fav_books (book_id, user_id) VALUES (%(book_id)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #Get the users that didn't like a specefic book
    @classmethod
    def unfav_users(cls,data):
        query = "SELECT * FROM users WHERE users.id NOT IN ( SELECT user_id FROM fav_books WHERE book_id = %(id)s );"
        unfav_users = []
        results = connectToMySQL(DATABASE).query_db(query,data)
        for res in results:
            unfav_users.append(cls(res))
        return unfav_users