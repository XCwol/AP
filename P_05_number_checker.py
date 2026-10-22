# Ask the user for width and loop until they
# enter a number that is more than zero

#Welcoming the user
print("\nWelcome to number checker\n")

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
    
# Main Routine Goes Here
for item in range(2):
    width = num_check("Please enter your width:\n ")
    print(width)
    
    
for item in range(2):
    height = num_check("Please enter your height: ")
    print(height)