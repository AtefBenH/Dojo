from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User :
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # =====================Validations=====================
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

    @staticmethod
    def validate(data):
        errorMessages = []
        if len(data['first_name'])<2:
            errorMessages.append("First Name must contain at least 2 characters")

        if len(data['last_name'])<2:
            errorMessages.append("Last Name must contain at least 2 characters")
            
        if not EMAIL_REGEX.match(data['email']): 
            errorMessages.append("Email not valid")
        elif User.get_by_email({'email':data['email']}):
            errorMessages.append("Email Already Exists")

        if len(data['password']) <8:
            errorMessages.append("Password Must Have More Than 8 Characters")
        elif not User.verify_password(data['password']) :
            errorMessages.append("Password Must Contain At Least A Number And An Uppercase Character")
        elif data['password']!= data['confirm_password']:
            errorMessages.append("Password and Confirmation Doesn't Match")
        return errorMessages

    # =======================Queries=======================

    # - CREATE
    @classmethod
    def create(cls, data):
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

