def loginsys():
    # stored username and stored password

    welcome = input("Are you a member? Please type ['Y'] or ['N'] ")
    stored_username = ["eliteninja", "Jimmybuckets", "nytrogamer", "oasisedit", "e"]
    stored_pass = ["candykiller123", "IEATsocks23", "rui324f", "ewnastycake521", "e"]
    inc = "Username or Password incorrect!"
    suc = "Login Successful!"
    succ = "Login Successful"

    if welcome.upper() == 'Y':
        print("Welcome back please log in!")
        loginuser = input("User name: ")
        loginpass = input("Password: ")
        if stored_username[4] == loginuser and stored_pass[4] == loginpass:
            print(suc)
            if loginuser == stored_username[1] and loginpass == stored_pass[1]:IEATsocks23
                print(suc)
                if loginuser == stored_username[2] and loginpass == stored_pass[2]:
                    print(suc)
                    if loginuser == stored_username[3] and loginpass == stored_pass[3]:
                        print(suc)

        if loginuser != stored_username[4] or loginpass != stored_pass[4]:
            print(' ')
            if loginuser != stored_username[1] or loginpass != stored_pass[1]:
                print(" ")
                if loginuser != stored_username[2] or loginpass != stored_pass[2]:
                    if loginuser != stored_username[3] or loginpass != stored_pass[3]:
                        while inc:
                            print("Please try again")
                            loginuser = input("User name: ")
                            loginpass = input("Password: ")
                            if stored_username[4] == loginuser and stored_pass[4] == loginpass:
                                print(suc)
                                return suc
                                if loginuser == stored_username[1] and loginpass == stored_pass[1]:
                                    print(suc)
                                    return suc
                                    if loginuser == stored_username[2] and loginpass == stored_pass[2]:
                                        print(suc)
                                        break
                                        if loginuser == stored_username[3] and loginpass == stored_pass[3]:
                                            print(suc)
                                            break
                                            if loginuser == stored_username[-1] and loginpass == stored_pass[-1]:
                                                print(suc)
                                                break
                            else:
                                print(inc)

    if welcome.upper() == 'N':
        print("Please Sign up!")
        signupuser = input("User name: ")
        signuppass = input("Password: ")
        stored_username[-1] = signupuser
        stored_pass[-1] = signuppass
        print("Thank you please login!")
        loginuser = input("User name: ")
        loginpass = input("Password: ")
        if stored_username[4] == loginuser and stored_pass[4] == loginpass:
            print(suc)
            if loginuser == stored_username[1] and loginpass == stored_pass[1]:
                print(suc)
                if loginuser == stored_username[2] and loginpass == stored_pass[2]:
                    print(suc)
                    if loginuser == stored_username[3] and loginpass == stored_pass[3]:
                        print(suc)
        else:
            print(inc)
        while len(inc) == 30:
            if len(suc) == 16:
                break
            print("Please try again")
            loginuser = input("User name: ")
            loginpass = input("Password: ")
            if stored_username[4] == loginuser and stored_pass[4] == loginpass:
                print(suc)
                break
                if loginuser == stored_username[1] and loginpass == stored_pass[1]:
                    print(suc)
                    break
                    if loginuser == stored_username[2] and loginpass == stored_pass[2]:
                        print(suc)
                        break
                        if loginuser == stored_username[3] and loginpass == stored_pass[3]:
                            print(suc)
                            break
                            if loginuser == stored_username[-1] and loginpass == stored_pass[-1]:
                                print(suc)
                                break
            else:
                print(inc)


loginsys()                                                    
                                                                                                                                                       
                                                                                                                                                         
                                                                                                                                       