
from api import get_coordinates, create_activities
from database import create_database,add_activity,like_activity,create_user

create_database()
user_name = input("Enter Username: ")
user_id =  create_user(user_name)
location = input("Where are you heading?: ")
budget = int(input("What is your budget: "))
coordinates = get_coordinates(location)
if coordinates is None:
    print("Location not found, please try again")
else:
    address,lat,long = coordinates

activities = create_activities(lat,long,budget)
activity_ids = []#used for database functions to get queries


for activity in activities:
    #add_activity(placeholder to add activity to database)
    activity_id = add_activity(activity["name"],activity["location"],activity["cost"])
    activity_ids.append(activity_id)

print("\nHere are the activities we reccommend!: \n")

#print the activties to the screen
for i, activity in enumerate(activities,start=1):
    print(f"{i}. {activity["name"]}")
    print(f" Location: {activity["location"]}")
    print(f" Cost:  ${activity["cost"]}")
    print()


# #liking activities functionality
# choices = input("Enter the the activty numbers you would want to like (e.g. 1,3,5)")
# choices = choices.split(",")
# for choice in choices:
#     idx = int(choice.strip())
#     if 0 <= idx <= len(activity_ids):
#         curr_activity_id = activity_ids[idx]
#         #placeholder record in database
#         like_activity(user_id,curr_activity_id)
#     else:
#         print(f"Activity {choice.strip()} does not exist.")

# print("Added to your liked activities!!")







    





    