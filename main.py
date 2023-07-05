from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)


#Первая таб, white fields


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow) #time right now

    def __repr__(self):             #помогает отброжать способ отображения класов в консоли
        return f"<users{self.id}>" #ввывод клласа в формате users and id of user


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):             #помогает отброжать способ отображения класов в консоли
        return f"<users{self.id}>"



if __name__ == "__main__":
    app.run(debug=True)