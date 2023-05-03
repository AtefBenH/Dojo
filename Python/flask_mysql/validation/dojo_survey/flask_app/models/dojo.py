from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request, redirect
class Dojo :
    def __init__(self, data):
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_dojo(dojo):
        print('#'*30, dojo['location'], '#'*30)
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("You must choose a Location.")
        if len(dojo['language']) < 1:
            flash("You must choose a Language.")
            is_valid = False
        if len(dojo['comment']) < 10:
            flash("Comment must be at least 10 characters.")
            is_valid = False
        return is_valid
    
    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)
    
    @classmethod
    def get_dojo_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)