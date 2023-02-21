from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:

    DB = "dojos_and_ninjas_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        if 'id' in data:
            return cls.update(data)
        else:
            query = """
                INSERT INTO dojos (name)
                VALUES (%(name)s);
            """
            return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': dojo_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    def get_ninjas(self):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        data = {'id': self.id}
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        ninjas = []
        for row in results:
            ninja = Ninja(row['first_name'], row['last_name'], row['age'], self, row['created_at'], row['updated_at'])
            ninja.id = row['id']
            ninjas.append(ninja)
        return ninjas