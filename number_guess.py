def is_input_a_number(user_input):
    if user_input.isnumeric() == True: #IF is setting wheather its a number or not.
        #if is setting the statement
        their_number = int(user_input)
         #print(user_input)
        return their_number
    #else is setting what is not "if"
    else:
        return -1
    





def main():
    #user_input='Hello World!'
    my_number = 15
    user_guess = False
    while user_guess == False:
        user_input = input('Guess My Number: ')
        # . = method, its a function that runs on "userinput"
        their_number = is_input_a_number(user_input)
        if their_number == -1:
             print("We only accept postive numbers, try again.")
             continue
        if their_number < my_number:
            print('Guess Higher')
        elif their_number > my_number:
            print("Guess Lower")
        else: 
            print('Congrats! You guessed my number!')
            user_guess = True

if __name__ == "__main__":
    main()
    