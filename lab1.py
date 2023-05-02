
###############################PART 1######################################

# 1-Write a Python program which accepts the user's first and last name and print them inreverse order with a space between them.
# fname=input("Enter Your First Name:")
# lname=input("Enter Your Last Name:")
# full_name = lname[::-1] + " " + fname[::-1]
# print(full_name)

#2-Write a Python program that accepts an integer (n) and computes the value ofn+nn+nnn.
# n=int(input("Enter number: "))
# nn = int(str(n) + str(n))
# nnn = int(str(n) + str(n) + str(n))
# value = n + nn + nnn
# print(f"Value = {value}")


#4- Write a Python program to get the volume of a sphere with radius 6.
# import math
# r=6
# v = (4/3) * math.pi * math.pow(r,3)
# print(f"volume of a sphere with radius {r} = is {v}")

#5- Write a Python program that will accept the base and height of a triangle and compute the area.
# height=float(input("Enter Height of a Triangle: "))
# base=float(input("Enter a Base of a Triangle: "))
# area=0.5*height*base
# print(f"The area of the triangle is: {area}")

#6- Write a Python program to construct the following pattern, using a nested for loop.
# for i in range(5):
#     for j in range(i+1):
#         print("*", end="") #end="". This ensures that the asterisks are printed on the same line without any whitespace between them.
#     print()
    
# for i in range(4, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

#7- Write a Python program that accepts a word from the user and reverse it.
# word=input("Enter word: ")
# print(word[::-1])

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# for i in range(7):
#     if i==3 or i==6:
#         continue
#     print(i)

#9- Write a Python program to get the Fibonacci series between 0 to 50
# a, b = 0, 1
# while b <= 50:
#     print(b,end=" ")
#     a, b = b, a + b

#10- Write a Python program that accepts a string and calculate the number of digits andletters. 
# def count_digits(s):
#     count_digit=count_letter = 0
#     for char in s:
#         if char.isdigit():
#             count_digit += 1
#         elif char.isalpha():
#             count_letter +=1
#     print(f"Number of digits in string is {count_digit} and Number of Letters is {count_letter}")

# s = input("Enter Your String: ")
# count_digits(s)   # prints 9


####################################PART 2 ##################################################

#import random
#1-Given a list of numbers, create a function that returns a list where all similar adjacentelements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]

#def reduce_elements(list):
   # result = []
    #for num in list:
       # if len(result) == 0 or num != result[-1]:
           # result.append(num)
    #return result
#print(reduce_elements([1,2,3,3]))  

#Case1:The length is even, the front and back halves are the same length.
#Case2:The length is odd, we’ll say that the extra char goes in the front half.E.g. ‘abced’, the front half is ‘abc’, the back half’de.
#def front_back(a, b):
    # a_len = len(a)
    # b_len = len(b)
    # a_half = a_len // 2 + a_len % 2
#     b_half = b_len // 2 + b_len % 2
#     return a[:a_half] + b[:b_half] + a[a_half:] + b[b_half:]
# print(front_back('abc', 'xy')) 

#3- Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# def all_different(seq):
#     return len(set(seq)) == len(seq)
# print(all_different([1,2,7,9]))  
# print(all_different([1,2,2,7,9])) 

#4-Given unordered list, sort it using algorithm bubble sort
# def bubble_sort(list):
#     n = len(list)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#                 swapped = True
#         if not swapped:
#             break
#     return list
#print(bubble_sort([3,1,5,10,7]))

#5-Guessing game
# def guessing_game():
#     the_number = random.randint(1, 100)
#     tries = 10
#     prev_guesses = []
    
#     while tries > 0:
#         guess = input("Guess a number between 1 and 100: ")
#         if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
#             print("Please enter a number between 1 and 100.")
#             continue
        
#         guess = int(guess)
        
#         if guess in prev_guesses:
#             print("Guessed Already. Try again.")
#             continue
        
#         tries -= 1
#         prev_guesses.append(guess)

#         if guess == the_number:
#             print("Congrats! You guessed right", 10 - tries, "tries.")
#             play_again = input("Do you want to play again? (y/n): ")
#             if play_again.lower() == 'y':
#                 guessing_game()
#             else:
#                 print("Thanks for playing!")
#             return
        
#         elif guess < the_number:
#             print("Too low. Guess again.")
#         else:
#             print("Too high. Guess again.")

#     print("Sorry, you had only 10 tries. The number was", the_number)
#     play_again = input("Do you want to play again? (y/n): ")
#     if play_again.lower() == 'y':
#         guessing_game()
#     else:
#         print("Thanks for playing!")

#guessing_game()

