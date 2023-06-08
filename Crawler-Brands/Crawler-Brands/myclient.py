from pymongo import MongoClient
import json
from alive_progress import alive_bar; 
import time

class Brand:
    
    def __init__(self, name):
        self.name = name

class MyDB:
    def __init__(self) -> None:
        self.conn = self.connect()

    def connect(self):
        return MongoClient('mongodb+srv://arianepaulabarros:senha123@cluster0.n0vuy8b.mongodb.net/')['db']
    
    def addBrands (self, brand):
        if not self.conn.client:
            print('não conectou')
            self.conn = self.connect()
        self.conn['brands'].insert_one(brand)

file = open('marcas.json','r')
data = json.load(file)
db = MyDB()
with alive_bar(len(data)) as bar:
    for i in data:
        db.addBrands(i)
        time.sleep(.001)
        bar()