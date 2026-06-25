import sqlalchemy as db

engine = db.create_engine('sqlite:///explorer_hub.db')
#activities table for database
def create_database():
    #Activities table(activity_id,activity_name,location,cost)
    with engine.connect() as connection:
        connection.execute(db.text("""CREATE TABLE IF NOT EXISTS activities(
            activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            activity_name TEXT NOT NULL,
            location TEXT NOT NULL,
            cost INTEGER
        )"""))
        
        #User info table(user_id,user_name)
        connection.execute(db.text("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL UNIQUE
        )"""))

        #Liked Activities Table(user_id,activity_id)
        connection.execute(db.text("""CREATE TABLE IF NOT EXISTS liked_activities(
            user_id INTEGER,
            activity_id INTEGER,
            PRIMARY KEY (user_id,activity_id)
        )
    """))
        connection.commit()



def add_activity(name,location,cost):

    pass




def like_activity(user_id,activity_id):
    pass



#if user exist already just return id
def create_user(username):
    with engine.connect() as connection:
        result = connection.execute(
            db.text("""SELECT user_id FROM users WHERE user_name = :username"""),
            {"username": username}
            ).fetchone()
        #user exist already
        if result:
            return result[0]
        
        result = connection.execute(
            db.text("""INSERT INTO users (user_name) VALUES (:username)"""),
            {"username": username}
        )
        connection.commit()
        return result.lastrowid





    