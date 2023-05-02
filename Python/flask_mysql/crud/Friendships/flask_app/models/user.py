from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friends = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL('friendships').query_db(query, data)
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL('friendships').query_db(query)
    
    @classmethod
    def get_all_friendships(cls):
        query = "SELECT concat(users.first_name, ' ', users.last_name) AS user, group_concat(users1.first_name, ' ', users1.last_name SEPARATOR ', ') AS friend FROM users JOIN friendships ON friendships.user_id = users.id JOIN users AS users1 ON friendships.friend_id = users1.id Group By users.id;"
        return connectToMySQL('friendships').query_db(query)
    
    @classmethod
    def get_user_with_friends(cls, data):
        query = "SELECT * FROM users LEFT JOIN friendships ON friendships.user_id = users.id LEFT JOIN users AS users1 ON friendships.friend_id = users1.id WHERE users.id = %(id)s;"
        results = connectToMySQL('friendships').query_db(query , data)
        # print('~~'*20, results, '~~'*20)
        user = cls(results[0])
        for row_from_db in results:
            friend_data = {
                "id" : row_from_db["users1.id"],
                "first_name" : row_from_db["users1.first_name"],
                "last_name" : row_from_db["users1.last_name"],
                "created_at" : row_from_db["users1.created_at"],
                "updated_at" : row_from_db["users1.updated_at"]
            }
            user.friends.append(cls(friend_data))
        return user
    
    @classmethod
    def add_friendship(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
        return connectToMySQL('friendships').query_db(query , data)