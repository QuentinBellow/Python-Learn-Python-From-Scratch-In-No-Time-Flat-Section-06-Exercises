available_exits = ["east", "north east", "south"]

print("Please select a direction from the following list {} \n".format(available_exits))

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = raw_input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
    else:
        if chosen_exit not in available_exits:
            print("sorry, please try again.")

print("\n")
print("aren't you glad you got out of there!")