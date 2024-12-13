def mobile():
    # Ask if the user wants a mobile if user says's yes prints okay if no prints thank u for visiting
    sale = input("Do you want a mobile? (1.Yes /2.No): ")
    if sale == 'Yes':
        print("Okay.")
    elif sale == 'No':
        print("Thank you for visiting.")
        return
    else:
        print("Invalid input! please try again.")
        return
    
    # Ask for the brand of the phone
    brand = input("Which phone do you want (1.Samsung/2.IPhone)? ")
    if brand == 'Samsung':
        print("Okay.")
    elif brand == 'Iphone':
        print("Okay.")
    else:
        print("Invalid input, try again.")
        return
    
    # Ask for the model of the phone
    if brand == 'Samsung':
        model = input("1.S21,2.S23,S24")
         
        if model in ['S21', 'S23', 'S24']:
            print("Okay.")
        else:
            print("Invalid input, try again.")
            return
    elif brand == 'Iphone':
        model = input("Which model do you want (1.Iphone 13/2.Iphone 14/3.Iphone 15)? ")
        if model in ['Iphone 13', 'Iphone 14', 'Iphone 15']:
            print("Okay.")
        else:
            print("Invalid input, try again.")
            return
    
    # Ask for the color of the phone
    color = input("Which color do you prefer (1.Red/2.Blue/3.Black)? ")
    if color in ['Red', 'Blue', 'Black']:
        print("Okay.")
    else:
        print("Incorrect, try again.")
        return
    
    # Ask for the variant of the phone
    variant = input("Which variant do you want (1.128/2.256/3.512)? ")
    if variant in ['128', '256', '512']:
        print("Okay.")
        print("Here is your Phone sir")
    else:
        print("Incorrect, try again.")
        return
        
    return

mobile()