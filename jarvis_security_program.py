known_users = ["Sirius","Jack","John","Dan","Walter","Fred","Georgie","Harry"] 

while True:
    print("Hi! My name is Jarvis")
    name = input("What is your name?: ").strip().capitalize() # strip: Remove spaces at the beginning and at the end of the string | capitalize: converts the first character of a string to capital (uppercase) letter.
    
    if name in known_users:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower() # The lower() method returns the lowercased string from the given string.
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
                    
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the sytem (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you arround!")
