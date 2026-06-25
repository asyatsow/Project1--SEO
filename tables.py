from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()


class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(db.Integer, primary_key=True)
    username = database.Column(db.String(80), unique=True, nullable=False)
    email = database.Column(db.String(120), unique=True, nullable=False)



    def __repr__(self):
        return f'<User {self.username}>'


