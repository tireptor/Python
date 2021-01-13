from flask import Flask 
from flask_restful import Api, Resource, reqparse,abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:fitelec@localhost/librarycatalog'
app.debug = True
db = SQLAlchemy(app)

class books(db.Model):
    __tablename__ = "books"
    bookTitle = db.Column(db.String(100), primary_key=True)
    bookText = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer(),nullable = False,default=0)

    def __init__(self,bookTitle, bookText,likes):
        self.bookTitle = bookTitle
        self.bookText = bookText
        self.likes = likes

class author(db.Model):
    __tablename__ = "auteur"
    authorName = db.Column(db.String(100), primary_key=True)
    authorAge = db.Column(db.Integer(),nullable = False,default=0)
    authorGenre = db.Column(db.String(10), nullable = False)

    def __init__(self,authorName, authorAge,authorGenre):
        self.authorName = authorName
        self.authorAge = authorAge
        self.authorGenre = authorGenre

#db.create_all() #For first run

@app.route('/test',methods=['GET'])
def test():
    return {
        'test': 'test'
    }