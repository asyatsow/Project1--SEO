import unittest
import sqlalchemy as db
# importing our functions from database.py
from database import create_database, create_user, add_activity, engine


class TestDatabase(unittest.TestCase):


    def test_create_new_user(self):
        # make sure database exists first
        create_database()
       
        # testing if a brand new user gets added and gets a real id
        new_id = create_user("Traveler123")
       
        # the id should not be empty and should be a number bigger than 0
        self.assertIsNotNone(new_id)
        self.assertTrue(new_id > 0)


    def test_no_duplicate_users(self):
        create_database()
       
        # if we try to add the exact same person twice it should give back the same id
        first_id = create_user("SoloExplorer")
        second_id = create_user("SoloExplorer")
       
        # making sure it didnt make a duplicate row and just matched the original id
        self.assertEqual(first_id, second_id)


    def test_add_new_activity(self):
        create_database()
       
        # lets check if adding a unique activity saves properly to the db
        act_id = add_activity("Golden Gate Bridge", "San Francisco, CA", 0)
       
        # should save fine and give us a valid id number
        self.assertIsNotNone(act_id)
        self.assertTrue(act_id > 0)


    def test_no_duplicate_activities(self):
        create_database()
       
        # checking that adding the same exact activity twice doesnt duplicate it
        id_one = add_activity("Museum of Art", "San Diego, CA", 15)
        id_two = add_activity("Museum of Art", "San Diego, CA", 15)
       
        # both ids should be identical cuz it should just return the existing one
        self.assertEqual(id_one, id_two)


if __name__ == '__main__':
    unittest.main()


