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
        if stored_username[0] == loginuser and stored_pass[0] == loginpass:
            print("Login Successful!")
        elif loginuser == stored_username[1] and loginpass == stored_pass[1]:
            print("Login Successful!")
        elif loginuser == stored_username[2] and loginpass == stored_pass[2]:
            print("Login Successful!")
        elif loginuser == stored_username[3] and loginpass == stored_pass[3]:
            print("Login Successful!")
        elif stored_username[4] == loginuser and stored_pass[4] == loginpass:
            print("Login Successful!")
        else:
            print(inc)

        #if no users match stored users or passwords it will loop untill you get it right
        #if you do get it right the loop will break and will output 

        if loginuser not in stored_username or loginpass not in stored_pass:
            running = True
            while running:
                print("Please try again")
                loginusers = input("User name: ")
                loginpasss = input("Password: ")
                if stored_username[4] == loginusers and stored_pass[4] == loginpasss:
                    print(suc)
                    break
                elif loginusers == stored_username[1] and loginpasss == stored_pass[1]:
                    print(suc)
                    break
                elif loginusers == stored_username[2] and loginpasss == stored_pass[2]:
                    print(suc)
                    break
                elif loginusers == stored_username[3] and loginpasss == stored_pass[3]:
                    print(suc)
                    break
                elif loginusers == stored_username[-1] and loginpasss == stored_pass[-1]:
                    print(suc)
                    break
                else:
                    print(inc)
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
        if stored_username[0] == loginuser and stored_pass[0] == loginpass:
            print("Login Successful!")
        elif loginuser == stored_username[-1] and loginpass == stored_pass[-1]:
            print(suc)
        elif loginuser == stored_username[1] and loginpass == stored_pass[1]:
            print("Login Successful!")
        elif loginuser == stored_username[2] and loginpass == stored_pass[2]:
            print("Login Successful!")
        elif loginuser == stored_username[3] and loginpass == stored_pass[3]:
            print("Login Successful!")
        elif stored_username[4] == loginuser and stored_pass[4] == loginpass:
            print("Login Successful!")
        else:
            print(inc)
        if loginuser not in stored_username or loginpass not in stored_pass:
            running = True
            while running:
                print("Please try again")
                loginusers = input("User name: ")
                loginpasss = input("Password: ")
                if stored_username[4] == loginusers and stored_pass[4] == loginpasss:
                    print(suc)
                    break
                elif loginusers == stored_username[1] and loginpasss == stored_pass[1]:
                    print(suc)
                    break
                elif loginusers == stored_username[2] and loginpasss == stored_pass[2]:
                    print(suc)
                    break
                elif loginusers == stored_username[3] and loginpasss == stored_pass[3]:
                    print(suc)
                    break
                elif loginusers == stored_username[-1] and loginpasss == stored_pass[-1]:
                    print(suc)
                    break
                else:
                    print(inc)


loginsys()       