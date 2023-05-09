from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Like:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.show_id = data['show_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CREATE A LIKE
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO likes (user_id, show_id)
            VALUES (%(user_id)s, %(show_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #! GET ALL THE SHOWS ID'S LIKED BY ONE USER
    @classmethod
    def get_shows_id_for_user(cls, data):
        liked_shows_id = []
        query = """SELECT shows.id FROM shows 
        JOIN likes 
        ON shows.id = likes.show_id
        JOIN users
        ON likes.user_id = users.id
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        for row in results:
            liked_shows_id.append(row['id'])
        return liked_shows_id
    
    #DELETE A LIKE SINCE SHOW DELETED
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM likes WHERE show_id = %(show_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    #DELETE A LIKE
    @classmethod
    def unlike(cls, data):
        query = "DELETE FROM likes WHERE user_id = %(user_id)s AND show_id = %(show_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #COUNT OF LIKES FOR ONE SHOW
    @classmethod
    def count_for_show(cls, data):
        query = "SELECT count(*) AS likes FROM likes WHERE show_id = %(show_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    #COUNT OF LIKES FOR ONE USER
    @classmethod
    def count_for_user(cls, data):
        query = "SELECT count(*) AS likes FROM likes WHERE user_id = %(user_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    
