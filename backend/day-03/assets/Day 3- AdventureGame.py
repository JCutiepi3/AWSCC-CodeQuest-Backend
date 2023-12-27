print("<< A Choice in life >>")
print("<<You are in purgatory>>")
print("<<You are tasked to judge people correctly>>")
print("<< If you correctly organize the souls to enter or deny access to salvation you are rewarded>>")
print("<< Fail, you'll face a fiery demise >>")

Choice = input("But First, what's your name? ")
Agreement = input("Do you understand the guide? A = Yes / B = No ")

if Agreement.upper() == 'A':
    print("Great! Here's your First Client:")
    print("Susan Sparks (57 yrs old)")
    print("Served in the military as Medic")
    print("And always donates a portion of her bonuses to charity")

    first_client_judgment = input("Is the client granted access or denied? A = Yes / B = No ")

    if first_client_judgment.upper() == 'A':
        print("Access granted. You are on the path to salvation!")

        print("Here's your Second Client:")
        print("Jacob Batumbakal (26 yrs old)")
        print("Helped many of his friends for power")
        print("Trampled others for his own gain")

        second_client_judgment = input("Is the client granted access or denied? A = Yes / B = No ")

        if second_client_judgment.upper() == 'A':
            print("Access granted. Beware of the consequences! Your choice was a mistake. Game over.")
        elif second_client_judgment.upper() == 'B':
            print("Access denied. You made the right choice. Well done! You are rewarded salvation.")
        else:
            print("Invalid input. Please choose A or B.")
    else:
        print("Access denied. Beware of the consequences! Your choice was a mistake. Game over.")
else:
    print("You have chosen not to understand. Prepare for a fiery demise!")
