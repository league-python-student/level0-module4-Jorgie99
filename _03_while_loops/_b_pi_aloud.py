"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi = '3.1415926535897932384'
    str(pi)
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit
    print(pi[0])
    print(pi[2])
    print(pi[3])
    # TODO) Use a while loop to keep asking for the next digit of pi
    # TODO) If they are correct, print "correct".
    #  If they are not, print "incorrect" and break out of the while loop
    d = 4
    count = 0
    while True:
        nd = pi[d]
        next_digit = simpledialog.askstring(None, prompt='What is the next digit?')
        if next_digit == nd:
            print("correct")
        else:
            print("incorrect")
            break
        d += 1
        count += 1
    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
    print(count)