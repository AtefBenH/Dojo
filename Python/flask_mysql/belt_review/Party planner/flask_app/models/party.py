from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Party:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.location = data['location']
        self.date = data['date']
        self.all_ages = data['all_ages']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! VALIDATIONS
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])<2:
            is_valid = False
            flash("Title must be at least 2")
        if len(data['location'])<2:
            is_valid = False
            flash("Location must be at least 2")
        if len(data['description'])<6:
            is_valid = False
            flash("Description greater than 6")
        if data['date'] == "":
            is_valid = False
            flash("Date is required")
        return is_valid

    # - CREATE
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO parties (user_id,title, location, description, all_ages, date)
            VALUES (%(user_id)s,%(title)s,%(location)s,%(description)s, %(all_ages)s, %(date)s);
        """

        return connectToMySQL(DATABASE).query_db(query,data)
    
    # - GET ALL
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM parties 
            JOIN users 
            ON parties.user_id = users.id;
            """
        results = connectToMySQL(DATABASE).query_db(query)
        parties = []
        for row in results:
            party = cls(row)
            party.creator = f"{row['first_name']} {row['last_name']}"
            parties.append(party)
        return parties
    
    # - GET ALL parties for One User
    @classmethod
    def get_parties_by_user(cls,data):
        query = """
            SELECT * FROM parties WHERE user_id = %(user_id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        parties = []
        for row in results:
            party = cls(row)
            parties.append(party)
        return parties

    # - GET ONE BY ID
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM parties WHERE id = %(id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE parties SET 
            title = %(title)s, location = %(location)s, date = %(date)s, all_ages = %(all_ages)s, description = %(description)s 
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM parties WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)