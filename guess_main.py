from collatz_class import CollatzCalculator


#Create the OOP
def main():

    choice = 'y'

    #Gice the option of keep doing it 
    while choice == 'y':

        #Ask the user for input 
        num = int(input("Enter a number: "))

        #Call the OOP from the other program 
        sequence, steps = CollatzCalculator.calculate_sequence(num)
        print(sequence)
        #print(f"Steps: {steps}")

        play_guessing_game(num, steps)

        #Here is where you give the choice of keep going 
        choice = input("\nDo you want to continue (yes/no)? ").lower()

# Function to play the guessing game
def play_guessing_game(num, actual_steps):
    guess = int(input("\nGuess the number of steps to reach 1: "))
    if guess == actual_steps:
        print("Congratulations! You guessed it right.")
    else:
        print(f"Sorry, that's incorrect. The actual number of steps was {actual_steps}.")
        

#Run the program 
if __name__ == "__main__":
    main()
