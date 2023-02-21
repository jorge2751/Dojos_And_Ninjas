from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, first_name, last_name, age, dojo, created_at=None, updated_at=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dojo = dojo
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        data = {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age, 'dojo_id': self.dojo.id}
        self.id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return self


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for row in results:
            dojo = Dojo.get_one(row['dojo_id'])
            ninja = cls(row['first_name'], row['last_name'], row['age'], dojo, row['created_at'], row['updated_at'])
            ninja.id = row['id']
            ninjas.append(ninja)
        return ninjas