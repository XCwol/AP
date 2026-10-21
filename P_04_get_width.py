# Ask the user for width and loop until they
# enter a number that is more than zero
error = "Please enter a number that is more than zero\n"

while True:
    
    try:
        # ask the user for the width
        width = float(input("Width: "))
        
        # check that the width is more than 0
        if width > 0:
            break
        
        # if it is not more than 0 then print error message
        else:
            print(error)
            
     # if it is not a number then print error message
    except ValueError:
        print(error)
    