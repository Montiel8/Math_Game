class CollatzCalculator:
    @staticmethod
    def calculate_sequence(n):

        #Create the list 
        sequence = []

        steps = 0

        #Here you take the integer for the calculation 
        while n != 1:
            if n % 2 == 0:
                n = n // 2

                steps += 1
                
            else:
                n = 3 * n + 1

                # Increment step count
                steps += 1

            #You put the list in the list from above     
            sequence.append(n)

        #Return the program to the main to be displayed 
        return sequence, steps
        
