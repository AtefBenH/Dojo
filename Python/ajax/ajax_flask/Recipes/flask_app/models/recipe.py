from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Recipe :
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.made_on = data['made_on']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #VALIDATION
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])<3:
            is_valid = False
            flash("The recipe Name must contain at least 3 characters","recipe")
        if len(data['description'])<3:
            is_valid = False
            flash("Description must contain at least 3 characters","recipe")
        if len(data['instructions'])<3:
            is_valid = False
            flash("Instructions must contain at least 3 characters","recipe")
        if data['made_on'] == "":
            is_valid = False
            flash("You must contain pick a date","recipe")
        return is_valid
    
    #CREATE A RECIPE
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO recipes (user_id, name, description, instructions, made_on, under_30)
                VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s, %(made_on)s, %(under_30)s);
            """
        return connectToMySQL(DATABASE).query_db(query,data)

    #GET ALL RECIPES
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for row in results:
            recipe = cls(row)
            all_recipes.append(recipe)
        return all_recipes
    
    #GET ONE BY ID
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1 :
            return False
        return cls(results[0])
    
    #UPDATE RECIPE
    @classmethod
    def update(cls, data):
        query = """
            UPDATE recipes SET 
            name = %(name)s, description = %(description)s, instructions = %(instructions)s, made_on = %(made_on)s, under_30 = %(under_30)s 
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #GET ONE USER'S RECIPES
    @classmethod
    def get_by_user(cls,data):
        query = """
            SELECT * FROM recipes WHERE user_id = %(user_id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipes.append(recipe)
        return recipes
    

