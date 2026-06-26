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
        )"""))
        connection.commit()




#if user exist already just return id
def create_user(username):
    with engine.connect() as connection:
        check = connection.execute(
            db.text("""SELECT user_id FROM users WHERE user_name = :username"""),
            {"username": username}
            ).fetchone()
        #user exist already
        if check:
            return check[0]
        
        result = connection.execute(
            db.text("""INSERT INTO users (user_name) VALUES (:username)"""),
            {"username": username}
        )
        connection.commit()
        return result.lastrowid




#we dont want to add duplicate records
def add_activity(name,location,cost):
    with engine.connect() as connection:
        check = connection.execute(
            db.text("""SELECT activity_id
                    FROM activities
                    WHERE activity_name = :name
                    AND location = :location AND cost = :cost"""),
            {"name": name,
             "location": location,
             "cost": cost
             }
            ).fetchone()
        
        #Record already exist
        if check:
            return check[0]
        
        result = connection.execute(
            db.text("""INSERT INTO activities (activity_name, location, cost) VALUES (:activity_name, :location, :cost)"""),
            {"activity_name": name,
             "location": location,
             "cost": cost
             }
            )
        connection.commit()
        return result.lastrowid




#store the (user_idmactivity_id) pair in the database. Indicates user_id likes activity number activity_id
def like_activity(user_id,activity_id):
    if user_id <= 0 or activity_id <= 0: return     #malformed inputs check
    #no duplicate pairs
    with engine.connect() as connection:
        check = connection.execute(
            db.text("""SELECT user_id, activity_id
            FROM liked_activities
            WHERE user_id = :user_id AND activity_id = :activity_id """),
            {"user_id": user_id, "activity_id": activity_id}
            ).fetchone()
        #if pair already exist just exit function
        if check:
            return
            
        
        result = connection.execute(
            db.text("""INSERT INTO liked_activities (user_id,activity_id)
        VALUES (:user_id,:activity_id)"""),
        {"user_id": user_id, "activity_id": activity_id})
        connection.commit()














    