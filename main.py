import random
#Arms - Biceps, Triceps, Shoulders
#Legs - Hamstrings, Quadriceps, Calves, Glutes
#Push - Chest, Shoulders, Triceps
#Pull - Back and Biceps
#Push - Chest and Back
def getArms():
  bicep_exercises = ["Seated Hammer Curl", "Bicep Curls", "EZ Bar Curl", "Preacher Curls", "Hammer Curl", "Chin Ups", "Dumbell Incline Bicep Curls"]
  tricep_exercises = ["Dips", "Rope Pushdowns", "Skullcrushers", "Overhead Dumbell Extensions"]
  shoulder_exercises = ["Seated Shoulder Press", "Arnold Press", "Front Press", "Lateral Raises", "Shoulder Shrugs", "Overhead Shoulder Press"]
  random_b = random.randint(0, 5)
  random_t = random.randint(0, 3)
  random_s = random.randint(0, 5)
  return(bicep_exercises[random_b] + ", "+ tricep_exercises[random_t] + ", " + shoulder_exercises[random_s]) 


print("What type of split would you like to follow today:\n1. Arms (Biceps, Triceps, Shoulders)\n2.Legs (Hamstrings, Quadriceps, Calves, Glutes)\n3. Push Variation 1 (Chest, Shoulders, Triceps)\n4. Pull (Back and Biceps)\n5. Push Variation 2(Chest and Back)")
#1 - Arms, 2 - Legs, 3 - Push 1, 4 - Pull, 5 - Push 2
split = input()
print("Would you like to focus on a specific muscle in this group?")
response = input("Y/N: ")
if response == "Y":
  specific = True
  print("What kind of muscle would you like to focus on?")
  response2 = input()
else:
  specific = False

if int(split) == 1:
  print(getArms())

