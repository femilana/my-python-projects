new_password = input("Enter your password: ") #takes in the user password
re_enter_password = input("Re-enter your password: ")#reaffirming the user password

if new_password != re_enter_password: #check if the password match
    print('Password does not match')
else:
    for trial in range(3):
        password = input("Input your password: ")
        if password == re_enter_password:
            print("correct password, proceed to account".upper())
            break
        else:
            trial_left = 2 - trial
            if trial_left == 0:
                print("You have exceeded the all trial and password is incorrect")
            else:
                print("incorrect password. {} trial left, Try again".format(trial_left))
    else:
        print("You have exceeded the maximum number of trial")
