def main():

    # ex1()
    # ex2()
    ex3()




# #
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#
# Hint: Use 'continue' statement.
def ex1():

    for nums in range(7):

        if nums == 3 or nums == 6:
            continue

        print(nums)

# Write a Python program to count the number of even and odd numbers from a series of numbers.

def ex2():

    runtotalEven = 0
    runtotalOdd = 0

    for i in range(1,10):
        if i % 2 == 0:
            runtotalEven +=1


        else :
            runtotalOdd +=1

    print("Number of even numbers: " + str(runtotalEven))
    print("Number of odd numbers: " + str(runtotalOdd))




# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output after User enters a blank line to end.

def ex3():

    term = ""
    bigString = ""


    while(True):
        seq = input("enter a sentence. leave blank to quit")
        if seq == term:
            break
        bigString += (seq + "\n")

    print(bigString)






































if __name__ == '__main__':
    main()