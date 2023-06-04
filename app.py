import input_handler
import random as ran

user_health = 100
computer_health = 100

attack_computer = ran.randint(0,100)
if(attack_computer < 50):
    print("punch")
else:
    print("kick")


defence_computer = ran.randint(0,100)
if(defence_computer < 50):
    print("high")
else:
    print("low")

user_punches = "input_attack" 
if("user_punches and computer blocks low"):
    print("computer_health = -10")


user_kicks = "input_attack"
if("user_kicks and computer blocks high"):
    print("computer_health = -10")


computer_punches = "input_attack"
if("computer_punches and user blocks low"):
    print("user_health = -10")


computer_punches2 = "input_attack"
if("computer_punches2 and user blocks low"):
    print("user_health = -10")  


computer_health = 0
if(computer_health == 0):
    print("user wins and game over")
else:
    print("Great you win!")


user_health = 0
if(user_health == 0):
    print("computer wins and game over")
else:
    print("Great you win!")

