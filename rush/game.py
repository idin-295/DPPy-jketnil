import os
import time

npcs = {
    "old_man": {
        "name": "Old Man",
        "role": "Dorm Owner",
        "room": 0,
        "dialogue": (
            "Oh! Hello there, young man. Are you the new tenant?\n"
            "Could you do an old man a favor?\n"
            "I've forgotten where I put something important.\n"
            "It's a small brass key. I think I left it somewhere "
            "in this dorm.\n"
            "Could you look around and find it for me?\n"
            "Oh, and if you find my notebook, bring that back too!\n"
            "Now... what was I looking for again?"
        ),
        "quest": {
            "name": "The Missing Brass Key",
            "target_item": "brass_key",
            "optional_item": "old_notebook",
            "completed": False
        }
    }
}

print(npcs["old_man"]["name"])
print(npcs["old_man"]["dialogue"])



def main():
    while True :
        os.system("cls" if os.name == "nt" else "clear")
        print("\......MAIN......./")
        print("1.room1")
        print("2.room2")
        print("3.room3")
        print("4.room4")
        print("5. EXIT")
        func() 
        func2()

def func():
    choice = int(input("chose 1-5 :"))
    match choice:
        case 1:
            while True :
                os.system("cls" if os.name == "nt" else "clear")        
                print("you go to room number 1 and enter the room.")
                print("1. wardrome")
                print("2. table,chair")
                print("4. storage box")
                print("5. bed")
                print("5. EXIT",)
                choice = int(input("chose 1-5 :"))
                match choice:
                        case 1:
                            print("in wardrome not have anything it's emty ")
                            time.sleep(5)
                        case 2 :
                            print("on table doesn't have anything and on chair too")
                            time.sleep(3)
                        case 3 :
                            print("you walk to be do you want to sleep for save ")
                        case 4 :
                            print("you walk to storage box you open it,It have spyder web and some dusk")
                            time.sleep(3)
                        case 5 :
                            print("exit to main hall")
                            time.sleep(3)
                            break
def func2() :
    choice = int(input("chose 1-5 :" ))
    match choice:
        case 2:
            print("2. you go to room number 2 and enter the room")
            while True :
                os.system("cls" if os.name == "nt" else "clear")        
                print("you go to room number 1 and enter the room.")
                print("1. beoken wardrome")
                print("2. rusty table leg with damp wood tabletop and a chair that missing 1 leg")
                print("4. storage box with broken box lid")
                print("5. bed with a torn be sheet")
                print("5. EXIT",)
                choice = int(input("chose 1-5 :"))
                match choice:
                        case 1:
                            print("in wardrome is broken anything it's emty ")
                            time.sleep(5)
                        case 2 :
                            print("on table doesn't have anything and on chair too")
                            time.sleep(3)
                        case 3 :
                            print("you walk to be do you want to sleep for save ")
                        case 4 :
                            print("you walk to storage box you open it,It have spyder web and some dusk")
                            time.sleep(3)
                        case 5 :
                            print("exit to main hall")
                            time.sleep(3)
                            break 
        case 3:
            print("3. you go to room number 3 but you can't open the door the door is lock")
        case 4:
            print("4. you go to room number 4")            
        case 5:
            print("you go to EXIT door and go out off building,GOODBYE")
            exit()
        case _:
            print("ERROR,pls select 1-5")

main()

# while True :
#     print("\......MAIN......./")
#     print("1.")
#     print("2.")
#     print("3.")
#     print("4.")
#     print("5. EXIT")

#     choice = input("chose 1-5 :")

#     if choice =="1":
#         print("you enter 1")
#         print("1.wardrome")
#         print("2.table")
#         print("3.Storage box")
#         print("4.bed")
#         choice2 = input("chose what to do in 1 :")
#         if choice2 == "1":
#             print("you chose 1 will you open wardrome ")
#             print("1.yes")
#             print("2.no")
#     elif choice =="2":
#         print("you enter 2")
#     elif choice == "3" :
#         print("you enter 3")
#     elif choice == "4" :
#         print("you enter 4")
#     elif choice == "5" :
#         print("you enter exit,goodbye")
#         break
#     else :
#         print("ERROR ,PLESE CHOSE 1-5")
