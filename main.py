
from api import get_coordinates, create_activities
from database import create_database,add_activity,like_activity,create_user

create_database()
user_name = input("Enter Username: ")
user_id =  create_user(user_name)
location = input("Where are you heading?: ")
budget = int(input("What is your budget: "))
coordinates = get_coordinates(location)     #lat,long coordinates for gemini api

if coordinates is None:
    print("Location not found, please try again")
else:
    address,lat,long = coordinates

activities = create_activities(lat,long,budget)     #gemini api call to store new activities in database
activity_ids = []   #Stores ids of the activties to be used for liked_activties table

#add each generated activity to database if not present already and store id
for activity in activities:
    activity_id = add_activity(activity["name"],activity["location"],activity["cost"])
    activity_ids.append(activity_id)


print("\nHere are the activities we reccommend!: \n")

#print the activties to the screen
for i, activity in enumerate(activities,start=1):
    print(f"{i}. {activity["name"]}")
    print(f" Location: {activity["location"]}")
    print(f" Cost:  ${activity["cost"]}")
    print()


#User enters comma seperated sequence of numbers.
#Parsed to be the activties the user likes and stored in the database.
choices = input("Like the activities you find interesting! (e.g. 1,3,5), Enter 0 if no activity")
if choices == 0:
    print("You liked no activties")
else:
    choices = choices.split(",")
    for choice in choices:
        idx = int(choice.strip()) - 1       #since the ids start at 1.
        if 0 <= idx <= len(activity_ids):
            curr_activity_id = activity_ids[idx]
            like_activity(user_id,curr_activity_id)
        else:
            print(f"Activity {choice.strip()} does not exist.")

print("Added to your liked activities!!")






