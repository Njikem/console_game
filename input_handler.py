# function for user attack input
def get_user_attack():    

     input_attack = input("Choose your attack(1 for punch or 2 for kick):")
     if(input_attack == "1 for punch" or input_attack == "2 for kick"):
          return("input_attack")
     else:
          return("attack is invalide")
     
user_attack_input = get_user_attack() 
 
 
 #function for defence input

def get_user_defence():

     input_defence = input("Choose your defence(1 for high or 2 for low):")
     if(input_defence == "1 for high" or input_defence == "2 for low"):
          return("input_defence")
     else:
          return("defence is invalid")

user_defence_input = get_user_defence()

      







