from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, redirect
import math
from datetime import datetime

class Message:
    def __init__(self, data):
        self.id = data['messages.id']
        self.sender_id = data['sender_id']
        self.sender_name = data['first_name']
        self.receiver_id = data['receiver_id']
        self.receiver_name = data['u2.first_name']
        self.message = data['message']
        self.created_at = data['messages.created_at']
        self.updated_at = data['messages.updated_at']
    
    #VALIDATE MESSAGE
    @staticmethod
    def validate(str):
        is_valid = True
        if len(str) < 5 :
            flash('Message Should Contain 5 Characters At Least', "message")
            is_valid = False
        return is_valid
    
    #TIME DIFFERENCE
    def time_difference(self):
        now = datetime.now()
        diff = now - self.created_at
        if diff.days > 0:
            return f"{diff.days} Days Ago"
        elif (math.floor(diff.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(diff.total_seconds() / 60)/60)} Hours Ago"
        elif diff.total_seconds() >= 60:
            return f"{math.floor(diff.total_seconds() / 60)} Minutes Ago"
        else:
            return f"{math.floor(diff.total_seconds())} Seconds Ago"

    #CREATE MESSAGE
    @classmethod
    def create(cls, data):
        query = """INSERT INTO messages 
        (sender_id, receiver_id, message) 
        VALUES (%(sender_id)s, %(receiver_id)s, %(message)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #GET ALL MESSAGES FOR A SENDER
    @classmethod
    def get_messages_by_sender(cls, data):
        all_messages = []
        query = """
            SELECT * FROM users as u1 
            JOIN messages 
            ON sender_id = u1.id 
            JOIN users as u2 
            ON receiver_id = u2.id 
            WHERE u1.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        # print('-'*30, results, "-"*30)
        for row in results :
            # print('#'*30, row, "#"*30)
            # print('-'*30, cls(row), "-"*30)
            all_messages.append(cls(row))
        return all_messages
    
    @classmethod
    def get_messages_for_receiver(cls, data):
        all_messages =[]
        query = """
            SELECT * FROM users as u1 
            JOIN messages 
            ON sender_id = u1.id 
            JOIN users as u2 
            ON receiver_id = u2.id 
            WHERE u2.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        for row in results :
            all_messages.append(cls(row))
        return all_messages
    
    @classmethod
    def delete(cls, data):
        query ="DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)