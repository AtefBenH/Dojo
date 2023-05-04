from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email():
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate(email):
        is_valid = True
        if len(email['email']) <1:
            flash("Empty Email Address.")
            is_valid = False
        elif not EMAIL_REGEX.match(email['email']): 
            flash("Invalid Email Address!")
            is_valid = False
        elif Email.get_by_email({'email' : email['email']}):
            flash("Email Already Exists!")
            is_valid = False
        return is_valid

    @classmethod
    def add(cls, data):
        query = "INSERT INTO emails (email) Values (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM emails WHERE email = (%(email)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE FROM emails WHERE id = (%(id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)