from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @staticmethod
    def validate(user):
        is_valid = True
        #First Name Validation
        if len(user['first_name']) <2:
            flash("First Name Must Be At Least 2 Characters.")
            is_valid = False
        elif not user['first_name'].isalpha():
            flash("First Name Must Be Only Letters.")
            is_valid = False
        #Last Name Validation
        if len(user['last_name']) <2:
            flash("Last Name Must Be At Least 2 Characters.")
            is_valid = False
        elif not user['last_name'].isalpha():
            flash("Last Name Must Be Only Letters.")
        #Email Validation
        if len(user['email']) <1:
            flash("Empty Email Address.")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid Email Address!")
            is_valid = False
        elif User.get_by_email({'email' : user['email']}):
            flash("Email Already Exists!")
            is_valid = False
        #Password Validation
        if len(user['password']) <8:
            is_valid = False
            flash("Password Must Have More Than 8 Characters")
        elif user['password']!= user['confirm_password']:
            is_valid = False
            flash("Password and Confirmation Doesn't Match")
        return is_valid


    @classmethod
    def add(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password) Values 
        (%(first_name)s), (%(last_name)s), (%(email)s), (%(password)s);"""
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = (%(email)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
