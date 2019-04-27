
import pymongo

client = pymongo.MongoClient()
db = client.projeto

class User:

    def __init__(self, name, email, age, roles = []):
        self.name = name
        self.email = email
        self.age = age
        self.roles = roles

    def add_role(self, role):
        self.roles.append(role)

    def exists(self):
        u = db.users.find_one({ 'email': self.email })
        if not u:
            return False
        return True
    
    def save(self):
        db.users.insert({
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'roles': self.roles
        })