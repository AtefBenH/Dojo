from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.user import User
from flask import flash

class Show :
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# =====================Validations=====================
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])<3:
            is_valid = False
            flash("Title must be at least 3 characters","show")
        if len(data['network'])<2:
            is_valid = False
            flash("Network must be at least 3 characters","show")
        if len(data['description'])<3:
            is_valid = False
            flash("Description must be at least 3 characters","show")
        if data['release_date'] == "":
            is_valid = False
            flash("Release Date is required","show")
        return is_valid
    
    #!=================================QUERIES===================================

    # - CREATE
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO shows (user_id, title, network, release_date, description)
            VALUES (%(user_id)s,%(title)s,%(network)s,%(release_date)s, %(description)s);
        """

        return connectToMySQL(DATABASE).query_db(query,data)
    
    # - GET ALL
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM shows 
            JOIN users 
            ON shows.user_id = users.id;
            """
        results = connectToMySQL(DATABASE).query_db(query)
        shows = []
        for row in results:
            show = cls(row)
            shows.append(show)
        return shows
    
    #GET ALL ORDER BY
    @classmethod
    def get_all_by(cls, data):
        query = """
            SELECT * FROM shows 
            JOIN users 
            ON shows.user_id = users.id 
            ORDER BY {order};
            """
        results = connectToMySQL(DATABASE).query_db(query.format(order=data['order']))
        shows = []
        for row in results:
            show = cls(row)
            shows.append(show)
        return shows
    
    # - GET ALL shows for One User
    @classmethod
    def get_shows_by_user(cls,data):
        query = """
            SELECT * FROM shows WHERE user_id = %(user_id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        shows = []
        for row in results:
            show = cls(row)
            shows.append(show)
        return shows

    # - GET ONE BY ID
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM shows WHERE id = %(id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE shows SET 
            title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s 
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
        