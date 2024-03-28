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
        print(f"Steps: {steps}")

        #Here is where you give the choice of keep going 
        choice = input("\nDo you want to continue (yes/no)? ").lower()
        

#Run the program 
if __name__ == "__main__":
    main()
