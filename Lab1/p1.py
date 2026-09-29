# For a given natural number n find the minimal natural number m formed with the same digits
def find_min_number(a):
    min_number = 0 #where i keep the final number
    power = 1 #the thing with the 10^power soo i can build the number or well, remove parts of the og one
    #first count how many zeroes we have
    aux = a
    zero_count = 0
    while aux != 0:
        digit = aux % 10

        if digit == 0:
            zero_count += 1

        aux //= 10
    #we nee the first digit to not be zero, otherwise python just deletes it from existence basically
    aux = a
    first_digit = 9

    while aux != 0:
        digit = aux % 10

        if digit != 0 and digit < first_digit:
            first_digit = digit

        aux //= 10

    #start the number with the smallest NON ZERO digit
    min_number = first_digit

    #now put all the zeroes after the first digit
    for i in range(zero_count):
        min_number *= 10

    #remove the first digit and all the zeroes from a, cause we already added them
    aux = a
    new_number = 0
    power = 1
    removed = False

    while aux != 0:
        l_digit = aux % 10
        aux //= 10

        if l_digit == first_digit and not removed:
            removed = True
        elif l_digit != 0:
            new_number += l_digit * power
            power *= 10

    #dont forget to reset aux, cause basically that will skip the lower part
    #why? that is between god and the interpreter
    a = new_number # reset a to new number, why???? glad you asked, soo if you reset to new numbe
    while a != 0:
        aux = a #copy the original to an auxiliary so we dont destroy it
        min_digit = 9 #smth to compare to (largest single digit number)

        while aux != 0:
            l_digit = aux % 10

            if l_digit < min_digit:
                min_digit = l_digit

            aux //= 10

        min_number = min_number * 10 + min_digit
        #dont forget to reset aux, cause basically that will skip the lower part
        #why? that is between god and the interpreter
        aux = a

        # remove one occurrence of min_digit from aux
        new_number = 0 #not the same as min number, basically i remove the occurence of the smallest digit, in case there are copies
        power = 1
        removed = False

        while aux != 0:
            l_digit = aux % 10
            aux //= 10

            if l_digit == min_digit and not removed:
                removed = True
            else:
                new_number += l_digit * power
                power *= 10
        #basically reset the number to this thing soo when it goes back it keeps going with the new number
        a = new_number
    return min_number


def main():
    print("This program finds the smallest natural number that can be formed using the same digits.")
    n = int(input("Enter a natural number: "))
    result = find_min_number(n)
    print("The smallest number formed using the same digits is:", result)
if __name__ == "__main__":
    main()


#ok, explanation time (Prof, don't read this, its for me to be able to explain what i did)
#Soo i take first the number a-> then a min number zero so i can build the end number
#power is useful towards the end to pick the digit
#first i count the number of zeroes
#i need this cause zero cannot be the first digit of the number
#for example 0159 is basically just 159, so we would lose a digit
#then i find the smallest digit that InsT zero
#that becomes the first digit of min_number
#after that i add all the zeroes immediately after it for example with 9015, first digit is 1, then the zero -> 10
#then i rebuild a, but remove the first digit once and remove all the zeroes
#cause those are already inside min_number
# i iterate with while through a while it isnt zero, make the copy to basically not destroy it
# min digit is a comparison factor, 9 is the highest 1 digit number
# then iterate through auxiliary and keep taking off the last digit until I find the smallest one
# then i add to min number the one with zero to build the final one
#then we reset aux cause if we dont it skips the rest of the two whiles
# anyway, to keep going, i have new_number to basically rebuild a after removing the thing (digit)
# and removed, to keep track of it, the second while basically takes the last digit and checks if the last digit is the same as min digit then sets it to true
#Bare with me, im bad at explaining, soo, if it has been removed new we rebuild by summing the thing and skipping the min digit