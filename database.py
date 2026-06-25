import sqlalchemy as db


#activities table for database
def create_database():
    engine = db.create_engine('sqlite:///explorer_hub.db')
    #Activities table
    with engine.connect() as connection:
        connection.execute(db.text("""CREATE TABLE IF NOT EXISTS activities(
            activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            activity_name TEXT NOT NULL,
            location TEXT NOT NULL,
            cost INTEGER
        )"""))
    
    #Liked Activities Table
    with engine.connect() as connection:
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

    



    