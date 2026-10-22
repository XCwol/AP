# enter a number that is more than zero

# Welcoming the user
print("\nWelcome to number checker\n")
# Creating the function
def num_check(question):

    # creating an error message
    error = "Please enter a number that is more than zero\n"
    while True:
        
        try:
            # ask the user for a number
            response = float(input(question))
            
            # check that the response is more than 0
            if response > 0:
                return response
            
            # if it is not more than 0 then print error message
            else:
                print(error)
                
        # if it is not a number then print error message
        except ValueError:
            print(error)
    
# Main routine starts here...

keep_going = ""
while keep_going == "":
    
    # Get width and height
    width = num_check("Please enter your width: ")
    height = num_check("Please enter your height: ")
    
    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print(f"\nYour perimeter is: {perimeter} units.")
    print(f"\nYour area is: {area} square units.\n")
    
    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. \n")

print("Thank you for using the area / perimeter calculator")
    