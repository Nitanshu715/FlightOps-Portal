def sign_up():
    usrnm = input("Enter the username:")
    pswd = input("Enter the password:")
    role = input("Enter your role ->(admin/user):")
    with open("users.txt", "a") as file:   #opens the text file users.txt
        file.write(f"{usrnm},{pswd},{role}\n")    # adds all the 3 elements username, password, role to the file
    print("Congratulations!!!!, Your sign up is successful :)")
    log_choice = input("Do you want to log in now? (y/n): ")  #ask if the user or admin wants to log in immediately or no
    if log_choice.lower() == "y":
        login()
    elif log_choice.lower() == "n":
        pass                         #pass for this time only terminates this choice if no is being entered 
    else:
        print("Invalid input")

def login():
    usrnm = input("Enter your username:")
    pswd = input("Enter your password:")
    with open("users.txt", "r") as file:
        for i in file:                           #iterates through every element of the file with the variable i
            packer = i.strip().split(',')        # packer being a variable stores the elements of the file as a list
            if len(packer) == 3:                 # strip() deletes any additional backspace from the input and split writes it with commas 
                stored_usrnm, stored_pswd, role = packer   #all three elements stored in the variable packer 
                if usrnm == stored_usrnm and pswd == stored_pswd:
                    print("Login successful")
                    return role.strip().lower()
                else:
                    print("Invalid username or password. Please try again.")
                    return None

def admin_menu():
    print("Admin Menu:")   #only admin can access this section
    while True:
        print("1. Update Ticket Price")      
        print("2. Delete Flight")
        print("3. Reschedule Flight")
        print("4. Delete Location")
        print("5. Exit Admin Menu")
        choice = input("Enter your choice from above (1/2/3/4/5): ")
        if choice == "1":
            updtticketprice()
        elif choice == "2":
            dltflights()
        elif choice == "3":
            rescheduleflight()
        elif choice == "4":
            dltlocation()
        elif choice == "5":
            print("Exiting The Admin Menu....")
            break
        else:
            print("That's an invalid choice, please try again :)")

def updtticketprice():
    flightname = input("Enter the name of flight:")
    newprice = input("Enter the new ticket price (add $ in front):")
    file_path = "C:/Users/nitan/OneDrive/Desktop/python/project/flights.txt"
    with open(file_path, "r") as file:       #text file imported using file path method and is then opened in a read mode
        lines = file.readlines()
    with open(file_path, "w") as file:          
        for i in lines:
            if flightname in i:
                flightinfo = i.strip().split(',')  #as the file is opened in the write mode it can change the data within the file now
                flightinfo[-1] = newprice  #with this we can first take out the price from the list, change it and then put it back in the file 
                i = ",".join(flightinfo) + "\n" 
            file.write(i)
    print("The ticket price has now been updated successfully :)")

def dltflights():
    flightname = input("Enter the flight name to be deleted:")
    file_path = "C:/Users/nitan/OneDrive/Desktop/python/project/flights.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for i in lines:
            if flightname not in i:
                file.write(i)
    print("Entered Flight has now been deleted successfully :)")

def rescheduleflight():
    flightname = input("Enter the flight name to reschedule:")
    newtime = input("Enter the new departure time of the flight:")
    file_path = "C:/Users/nitan/OneDrive/Desktop/python/project/flights.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for i in lines:                 #similar to as update price, here the flight time is being changed 
            if flightname in i:
                flightinfo = i.strip().split(',')
                flightinfo[1] = newtime
                i = ",".join(flightinfo) + "\n"
            file.write(i)
    print("The entered flight has now been rescheduled successfully :)")

def dltlocation():
    location = input("Enter the location to be deleted:")
    file_path = "C:/Users/nitan/OneDrive/Desktop/python/project/flights.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for i in lines:           #if we delete any location from the file, all the flights connected to that locations deletes
            if location not in i:
                file.write(i)
    print("Entered location and all related flights have now been deleted successfully :)")



