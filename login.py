def loginsys():

    #welcome message
    welcome = input("Are you a member? Please type ['Y'] or ['N'] ")
    #stored users and passwords
    stored_username = ["eliteninja", "Jimmybuckets", "nytrogamer", "oasisedit", "e"]
    stored_pass = ["candykiller123", "IEATsocks23", "rui324f", "ewnastycake521", "e"]
    #just variables
    inc = "Username or Password incorrect!"
    suc = "Login Successful!"

    #starts with the "y" user input. will go through if statements to see if is users inputs match the stored users
    if welcome.upper() == 'Y':
        print("Welcome back please log in!")
        loginuser = input("User name: ")
        loginpass = input("Password: ")
        if loginuser in stored_username and loginpass in stored_pass:
            print(suc)
        elif loginuser not in stored_username and loginpass not in stored_pass:
            print(inc)
            running = True
            while running:
                print("Please try again")
                loopusers = input("User name: ")
                looppass = input("Password: ")
                if loopusers in stored_username and looppass in stored_pass:
                    print(suc)
                    break
                elif loopusers not in stored_username and looppass not in stored_pass:
                    print(inc)

        #if no users match stored users or passwords it will loop untill you get it right
        #if you do get it right the loop will break and will output 
    #if user says no to welcome message it will ask them to sign up and it will store their username and password
    if welcome.upper() == 'N':
        print("Please Sign up!")
        signupuser = input("User name: ")
        signuppass = input("Password: ")
        stored_username[-1] = signupuser
        stored_pass[-1] = signuppass
        print("Thank you please login!")
        loginuser = input("User name: ")
        loginpass = input("Password: ")
        if loginuser in stored_username and loginpass in stored_pass:
            print(suc)
        elif loginuser not in stored_username and loginpass not in stored_pass:
            print(inc)
            running = True
            while running:
                print("Please try again")
                loopusers = input("User name: ")
                looppass = input("Password: ")
                if loopusers in stored_username and looppass in stored_pass:
                    print(suc)
                    break
                elif loopusers not in stored_username and looppass not in stored_pass:
                    print(inc)
loginsys()       