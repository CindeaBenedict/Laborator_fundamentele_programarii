# The palindrome of a number is the number obtained by reversing the order of its digits
# (e.g the palindrome of 237 is 732).
# For a given natural number n, determine its palindrome.


def palindrome(n):
    n_rev = 0

    while n > 0:
        n_rev = n_rev * 10 + n % 10
        n //= 10

    return n_rev


def main():
    print("This program determines the palindrome of a natural number.")
    n = int(input("Enter a natural number: "))

    result = palindrome(n)

    print("The palindrome of the number is:", result)


if __name__ == "__main__":
    main()


#explanation time
#soo, number n
#its reversal where i will build the number
#while n still has digits, i take the last digit using n % 10
#then i add it to n_rev by first moving the digits already there one position to the left
#with n_rev * 10
#after adding the digit, i remove it from n using integer division by 10
#this keeps going until there are no digits left in n
#for example 190 becomes 91 because reversing it would give 091
#but a natural number cannot keep a zero at the beginning, so Python represents it as 91