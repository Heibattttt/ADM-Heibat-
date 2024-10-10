# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n%2==1 :
   print("Weird")
elif n%2==0 and n in range(2,5) :
   print("Not Weird")
elif n%2==0 and n in range(6,21):
   print("Weird")
elif n%2==0 and n>20:
   print("Not Weird")

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print (a+b)
print (a-b)
print (a*b)

# Print Function
if __name__ == '__main__':
    n = int(input())
for i in range (1,n+1) :
    print (i,end="")

# Loops
if __name__ == '__main__':
    n = int(input())
    
i=0
while(i<n):
    print(pow(i,2))
    i=i+1
    

# Write a function
def is_leap(year):
    leap = False
    if (year%4==0 and year%100!=0) or (year % 400==0):
        leap=True
    else:
        leap=False
    
    
    return leap

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr =map(int, input().split())
scores=set(arr)
sortscores =sorted(scores,reverse=True)
print(sortscores[1])

# Lists
if __name__ == '__main__':
    N = int(input())
 
my_list = []   
 
for _ in range(N):
    command = input().strip().split()
    command_type = command[0]
    if command_type == "insert":
        i = int(command[1])
        e = int(command[2])
        my_list.insert(i, e)
    elif command_type == "print":
        print(my_list)
    elif command_type == "remove":
        e = int(command[1])
        my_list.remove(e)
    elif command_type == "append":
        e = int(command[1])
        my_list.append(e)
    elif command_type == "sort":
        my_list.sort()
    elif command_type == "pop":
        if my_list: 
            my_list.pop()
    elif command_type == "reverse":
        my_list.reverse()

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
numbers = tuple(integer_list)

print(hash(numbers))

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
def get_average_marks(query_name, marks_dict):
    if query_name in marks_dict:
        marks = marks_dict[query_name]
        average = sum(marks) / len(marks)
        # Print the average with 2 decimal places
        print(f"{average:.2f}")
    else:
        print(f"Student {query_name} not found.")

get_average_marks(query_name, student_marks)

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
cordinates = [[i, j, k] for i in range(x + 1) 
                         for j in range(y + 1) 
                         for k in range(z + 1) 
                         if i + j + k != n]

print(cordinates)

# Nested Lists
if __name__ == '__main__':
    students = [] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

scores = sorted(list(set([score for name, score in students])))
second_lowest_score = scores[1]
second_lowest_students = sorted([name for name, score in students if score == second_lowest_score])
for name in second_lowest_students:
    print(name)

# sWAP cASE
def swap_case(s):
    return s.swapcase()

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first_name, last_name):
    print("Hello "+first_name +" "+ last_name+"! You just delved into python.")
    # Write your code here

# Mutations
def mutate_string(string, position, character):
    strings =string[:position] + character + string [position+1: ]
    return strings

# Find a string
def count_substring(string, sub_string):
    num = 0
    
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
         num += 1
     
    return num
 

# String Validators
if __name__ == '__main__':
    s = input()
print(any(char.isalnum() for char in s)) 
print(any(char.isalpha() for char in s)) 
print(any(char.isdigit() for char in s))  
print(any(char.islower() for char in s))  
print(any(char.isupper() for char in s))

# Capitalize!

# Complete the solve function below.
def solve(s):
    
          words = s.split()
    
    # Capitalize the first letter of each word and leave the rest of the word unchanged
          capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words with a space and return the result
          return ' '.join(capitalized_words)
      

# String Split and Join

def split_and_join(line):
    # write your code here
    line=line.split(" ")
    return "-".join(line)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Text Alignment
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input the thickness
thickness = int(input())  # This must be an odd number
c = 'H'
# Top cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
# Top pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
# Middle belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))
# Bottom pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
# Bottom cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

# Text Wrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_door_mat(n, m):
    # Top part
    for i in range(1, n, 2):
        pattern = (".|." * i).center(m, '-')
        print(pattern)
    
    # Middle part (WELCOME)
    print("WELCOME".center(m, '-'))
    
    # Bottom part (mirror of the top)
    for i in range(n-2, -1, -2):
        pattern = (".|." * i).center(m, '-')
        print(pattern)
# Input the dimensions N (odd number) and M (3 times N)
N, M = map(int, input().split())
# Call the function to print the mat design
print_door_mat(N, M)

# String Formatting
def print_formatted(number):
    # your code goes here
     width = len(bin(number)) - 2  # bin(n) returns '0b...' so subtract 2 for '0b'
    # Loop through each number from 1 to n
     for i in range(1, number + 1):
        # Print the four values with appropriate formatting and padding
        print(str(i).rjust(width),        # Decimal
              oct(i)[2:].rjust(width),    # Octal (strip '0o')
              hex(i)[2:].upper().rjust(width),  # Hexadecimal (strip '0x' and capitalize)
              bin(i)[2:].rjust(width))

# Alphabet Rangoli
import string 
def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
   
    lines = []
    for i in range(size):
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        
        lines.append(s.center(4*size-3, '-'))
    
    print('\n'.join(lines[::-1] + lines[1:]))

# Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        # Get the substring of length 'k'
        substring = string[i:i+k]
        
        # Initialize an empty result string for unique characters
        unique_chars = ""
        
        # Iterate over each character in the substring
        for char in substring:
            # Add the character if it'string not already in the result string
            if char not in unique_chars:
                unique_chars += char
        
        # Print the result string for the current substring
        print(unique_chars)

# The Minion Game
def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    n = len(string)
    
    # Loop through each character in the string
    for i in range(n):
        if string[i] in vowels:
            # Kevin's turn (vowel)
            kevin_score += (n - i)
        else:
            # Stuart's turn (consonant)
            stuart_score += (n - i)
    
    # Determine the winner
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

# Map and Lambda Function
cube = lambda x: x ** 3
def fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""
    fibonacci_numbers = []
    a, b = 0, 1  # Starting values for Fibonacci
    for _ in range(n):
        fibonacci_numbers.append(a)  # Append the current Fibonacci number
        a, b = b, a + b  # Update to the next Fibonacci number
    return fibonacci_numbers


# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
numb = int(input())
# Loop through each test case
for _ in range(numb):
    try:
    
        a, b = map(int, input().split())
        
      
        result = a // b
        
        # Print the result
        print(result)
        
    except ZeroDivisionError as e:
        print("Error Code:", e)  
    except ValueError as e:
        print("Error Code:", e)  

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
date_input = input().strip()
month, day, year = map(int, date_input.split())

date_obj = datetime.date(year, month, day)
day_of_week = date_obj.strftime("%A").upper()

print(day_of_week)

# Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
     timestamp_format = "%a %d %b %Y %H:%M:%S %z"
   
     dt1 = datetime.strptime(t1, timestamp_format)
     dt2 = datetime.strptime(t2, timestamp_format)
    
     return str(int(abs((dt1 - dt2).total_seconds())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    # Read the number of shoes
    n = int(input())
    
    # Read the space-separated list of shoe sizes
    shoe_sizes = list(map(int, input().split()))
    
    # Create a dictionary to count available shoes of each size
    shoe_inventory = {}
    for size in shoe_sizes:
        if size in shoe_inventory:
            shoe_inventory[size] += 1
        else:
            shoe_inventory[size] = 1
            
    # Read the number of customers
    num_customers = int(input())
    
    # Initialize total earnings
    total_earnings = 0
    
    # Process each customer
    for _ in range(num_customers):
        # Read the desired size and price
        size, price = map(int, input().split())
        
        # Check if the desired size is available in the inventory
        if size in shoe_inventory and shoe_inventory[size] > 0:
            total_earnings += price  # Add the price to total earnings
            shoe_inventory[size] -= 1  # Decrease the count of available shoes
    
    # Print the total earnings
    print(total_earnings)

# DefaultDict Tutorial
from collections import defaultdict
# Step 1: Read n and m
n, m = map(int, input().strip().split())
# Step 2: Create a defaultdict to hold lists of indices
group_a_indices = defaultdict(list)
# Step 3: Read words in Group A and store their indices
for index in range(1, n + 1):
    word = input().strip()
    group_a_indices[word].append(index)
# Step 4: For each word in Group B, check its occurrence in Group A
for _ in range(m):
    word = input().strip()
    if word in group_a_indices:
        # Print indices if the word exists in Group A
        print(" ".join(map(str, group_a_indices[word])))
    else:
        # Print -1 if the word does not exist in Group A
        print(-1)

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
# Step 1: Read the number of students
n = int(input().strip())
# Step 2: Read the column names
columns = input().strip().split()
# Step 3: Create a named tuple with the specified column names
Student = namedtuple('Student', columns)
# Step 4: Initialize a variable to accumulate the marks
total_marks = 0
# Step 5: Read each student's data and accumulate the marks
for _ in range(n):
    student_data = input().strip().split()
    student = Student(*student_data)  # Unpack the data into the named tuple
    total_marks += int(student.MARKS)  # Add the marks to total_marks
# Step 6: Calculate the average marks
average_marks = total_marks / n
# Step 7: Print the average marks rounded to 2 decimal places
print(f"{average_marks:.2f}")

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
# Step 1: Read the number of items
n = int(input().strip())
# Step 2: Create an OrderedDict to store items and their net prices
item_prices = OrderedDict()
# Step 3: Process each item
for _ in range(n):
    # Read the line, split by space and extract item name and price
    item = input().strip().rsplit(' ', 1)
    item_name = item[0]
    price = int(item[1])
    
    # If the item already exists in the dictionary, add the price to its current total
    if item_name in item_prices:
        item_prices[item_name] += price
    else:
        item_prices[item_name] = price  # Initialize with the price if it's the first occurrence
# Step 4: Print the item names and their net prices
for item_name, net_price in item_prices.items():
    print(f"{item_name} {net_price}")

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Read the number of words
n = int(input().strip())
# Step 2: Initialize a list for unique words and a dictionary for counting occurrences
unique_words = []
word_count = {}
# Step 3: Read each word and count occurrences
for _ in range(n):
    word = input().strip()
    
    # Update the dictionary
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        unique_words.append(word)  # Add to unique_words list only if it's the first occurrence
# Step 4: Output the number of distinct words
print(len(unique_words))
# Step 5: Output the occurrences of each unique word
print(" ".join(str(word_count[word]) for word in unique_words))

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
# Step 1: Initialize the deque
d = deque()
# Step 2: Read the number of operations
n = int(input().strip())
# Step 3: Perform operations
for _ in range(n):
    operation = input().strip().split()  # Read operation and its parameters
    command = operation[0]  # The method name
    if command == 'append':
        d.append(int(operation[1]))  # Append an element to the right
    elif command == 'appendleft':
        d.appendleft(int(operation[1]))  # Append an element to the left
    elif command == 'pop':
        d.pop()  # Remove an element from the right
    elif command == 'popleft':
        d.popleft()  # Remove an element from the left
# Step 4: Output the final elements of the deque
print(" ".join(map(str, d)))

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
        s = input().strip()
# Step 2: Count the occurrences of each character
counter = Counter(s)
# Step 3: Sort the characters by their occurrence count and alphabetically
# First by count in descending order, then alphabetically
sorted_chars = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
# Step 4: Print the top three characters and their counts
for i in range(min(3, len(sorted_chars))):  # Ensure we don't exceed the available characters
    char, count = sorted_chars[i]
    print(char, count)

# Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
def can_stack_cubes(test_cases):
    results = []
    
    for _ in range(test_cases):
        n = int(input())  # Read the number of cubes
        cubes = list(map(int, input().split()))  # Read the lengths of the cubes
        # Initialize left and right pointers
        left = 0
        right = n - 1
        last_cube = float('inf')  # Start with a very large value
        
        possible = True
        
        while left <= right:
            # Select the larger of the two ends
            if cubes[left] >= cubes[right]:
                current_cube = cubes[left]
                left += 1
            else:
                current_cube = cubes[right]
                right -= 1
            
            # Check if the current cube can be placed on top of the last cube
            if current_cube > last_cube:
                possible = False
                break
            last_cube = current_cube  # Update the last placed cube
        results.append("Yes" if possible else "No")
    
    return results

# Input handling
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    results = can_stack_cubes(t)
    for result in results:
        print(result)

# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the first line to create set A
A = set(input().split())
# Read the number of other sets
n = int(input())
# Initialize a flag to check if A is a strict superset of all other sets
is_strict_superset = True
# Loop through each of the other sets
for _ in range(n):
    # Read the current set and convert it to a set
    current_set = set(input().split())
    
    # Check if A is a strict superset of current_set
    if not (A > current_set):  # A must be a strict superset
        is_strict_superset = False
        break
# Print the result
print(is_strict_superset)

# Introduction to Sets
def average(array):
    # your code goes here
   
    distinct_heights = set(array)
    
    # Calculate the average of distinct heights
    avg = sum(distinct_heights) / len(distinct_heights)
    
    # Return the average rounded to three decimal places
    return round(avg, 3)


# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_happiness(n, m, array, A, B):
    # Initialize happiness
    happiness = 0
    
    # Convert A and B to sets for O(1) average time complexity on membership checks
    set_A = set(A)
    set_B = set(B)
    
    # Calculate happiness based on the array
    for number in array:
        if number in set_A:
            happiness += 1  # Liked
        elif number in set_B:
            happiness -= 1  # Disliked
    return happiness
if __name__ == '__main__':
    # Read the first line of input
    n, m = map(int, input().split())
    
    # Read the array of integers
    array = list(map(int, input().split()))
    
    # Read the liked integers (set A)
    A = list(map(int, input().split()))
    
    # Read the disliked integers (set B)
    B = list(map(int, input().split()))
    
    # Calculate and print the final happiness
    result = calculate_happiness(n, m, array, A, B)
    print(result)

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the size of set a
m = int(input())
# Read the elements of set a and create a set
a = set(map(int, input().split()))
# Read the size of set b
n = int(input())
# Read the elements of set b and create a set
b = set(map(int, input().split()))
# Calculate the symmetric difference
symmetric_difference = a.symmetric_difference(b)
# Sort the result and print each element
for value in sorted(symmetric_difference):
    print(value)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the total number of country stamps
n = int(input())
# Initialize an empty set to store distinct country names
country_stamps = set()
# Loop through the number of stamps and add each to the set
for _ in range(n):
    country = input().strip()  # Read country name and remove any leading/trailing whitespace
    country_stamps.add(country) # Add the country to the set
# Output the number of distinct country stamps
print(len(country_stamps))

# Set .discard(), .remove() & .pop()

# Read the number of elements in the set
n = int(input())
# Read the elements of the set and create the set
elements = map(int, input().split())
s = set(elements)
# Read the number of commands
m = int(input())
# Execute the commands
for _ in range(m):
    command = input().split()
    action = command[0]
    
    if action == "pop":
        s.pop()  # Removes and returns an arbitrary element
    elif action == "remove":
        value = int(command[1])
        s.remove(value)  # Removes the specified element
    elif action == "discard":
        value = int(command[1])
        s.discard(value)  # Removes the specified element if it exists
# Print the sum of the remaining elements in the set
print(sum(s))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of students subscribed to the English newspaper
n_english = int(input())
# Read the roll numbers of students subscribed to the English newspaper
english_students = set(map(int, input().split()))
# Read the number of students subscribed to the French newspaper
n_french = int(input())
# Read the roll numbers of students subscribed to the French newspaper
french_students = set(map(int, input().split()))
# Find the union of both sets
all_subscribers = english_students.union(french_students)
# Print the total number of unique students
print(len(all_subscribers))

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of students subscribed to the English newspaper
n_english = int(input())
# Read the roll numbers of students subscribed to the English newspaper
english_students = set(map(int, input().split()))
# Read the number of students subscribed to the French newspaper
n_french = int(input())
# Read the roll numbers of students subscribed to the French newspaper
french_students = set(map(int, input().split()))
# Find the intersection of both sets
common_subscribers = english_students.intersection(french_students)
# Print the total number of students who subscribed to both newspapers
print(len(common_subscribers))

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of students subscribed to the English newspaper
n_english = int(input())
# Read the roll numbers of students subscribed to the English newspaper
english_students = set(map(int, input().split()))
# Read the number of students subscribed to the French newspaper
n_french = int(input())
# Read the roll numbers of students subscribed to the French newspaper
french_students = set(map(int, input().split()))
# Find the difference: students who are only in the English set
only_english_subscribers = english_students.difference(french_students)
# Print the total number of students who are subscribed only to the English newspaper
print(len(only_english_subscribers))

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of students subscribed to the English newspaper
n_english = int(input())
# Read the roll numbers of students subscribed to the English newspaper
english_students = set(map(int, input().split()))
# Read the number of students subscribed to the French newspaper
n_french = int(input())
# Read the roll numbers of students subscribed to the French newspaper
french_students = set(map(int, input().split()))
# Find the symmetric difference: students who are in either set but not both
either_but_not_both = english_students.symmetric_difference(french_students)
# Print the total number of students who are subscribed to either newspaper but not both
print(len(either_but_not_both))

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of elements in the initial set
n = int(input())
# Read the elements of the initial set
initial_set = set(map(int, input().split()))
# Read the number of other sets/operations
m = int(input())
# Perform operations
for _ in range(m):
    # Read operation and length (length is not used)
    operation_info = input().split()
    operation_name = operation_info[0]
    length = int(operation_info[1])  # Read length (not used)
    # Read elements of the other set
    other_set = set(map(int, input().split()))
    # Perform the specified operation
    if operation_name == "update":
        initial_set.update(other_set)
    elif operation_name == "intersection_update":
        initial_set.intersection_update(other_set)
    elif operation_name == "difference_update":
        initial_set.difference_update(other_set)
    elif operation_name == "symmetric_difference_update":
        initial_set.symmetric_difference_update(other_set)
# Calculate the sum of the elements in the final set
result = sum(initial_set)
# Output the result
print(result)

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
# Read the group size
group_size = int(input())
# Read the room numbers into a list
room_numbers = list(map(int, input().split()))
# Count occurrences of each room number
room_count = Counter(room_numbers)
# Find the Captain's room number (the one that appears exactly once)
for room, count in room_count.items():
    if count == 1:
        captain_room = room
        break
# Output the Captain's room number
print(captain_room)

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of test cases
n = int(input())
for _ in range(n):
    # Read set A
    size_A = int(input())
    A = set(map(int, input().split()))
    
    # Read set B
    size_B = int(input())
    B = set(map(int, input().split()))
    
    # Check if A is a subset of B and print the result
    print(A.issubset(B))

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of students and subjects
n, m = map(int, input().split())
# Initialize a list to hold marks for each subject
marks = []
# Read the marks for each subject
for _ in range(m):
    subject_marks = list(map(float, input().split()))
    marks.append(subject_marks)
# Transpose the marks to get marks per student
student_marks = zip(*marks)
# Calculate and print the average for each student
for scores in student_marks:
    average = sum(scores) / m
    print(f"{average:.1f}")

# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
def custom_sort(s):
    # Separate characters into categories
    lower = sorted([char for char in s if char.islower()])  # All lowercase letters
    upper = sorted([char for char in s if char.isupper()])  # All uppercase letters
    odd_digits = sorted([char for char in s if char.isdigit() and int(char) % 2 != 0])  # Odd digits
    even_digits = sorted([char for char in s if char.isdigit() and int(char) % 2 == 0])  # Even digits
    
    # Combine all sorted characters
    sorted_string = ''.join(lower + upper + odd_digits + even_digits)
    return sorted_string
# Input string
input_string = input()
# Get the sorted result
result = custom_sort(input_string)
# Print the sorted string
print(result)

# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sorted_athletes = sorted(arr, key=lambda x: x[k])
# Output the sorted results
for arr in sorted_athletes:
    print(' '.join(map(str,arr)))

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def is_valid_float(s):
    # Regular expression to match a valid floating-point number
    float_pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'
    
    # Check if the string matches the float pattern
    if re.match(float_pattern, s):
        try:
            # Try converting to float
            float(s)
            return True
        except ValueError:
            return False
    return False
# Input reading
n = int(input())
for _ in range(n):
    test_string = input().strip()
    print(is_valid_float(test_string))

# Re.split()
	# Do not delete 'r'.
regex_pattern = r"[,.]"

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# Read the input string
s = input()
# Use regex to find the first occurrence of a repeating alphanumeric character
match = re.search(r'([a-zA-Z0-9])\1', s)
# Check if we found a match and print the result
if match:
    print(match.group(1))  # Print the first repeating character
else:
    print(-1)  # Print -1 if no repeating characters are found

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# Read the input string
s = input()
# Define the regex pattern
# This pattern matches substrings that contain 2 or more vowels and are surrounded by consonants
pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
# Find all matching substrings
matches = re.findall(pattern, s)
# Print the results
if matches:
    print("\n".join(matches))
else:
    print(-1)

# Re.start() & Re.end()

import re
# Read the input strings
string = input().strip()  # Main string
substring = input().strip()  # Substring to search for
# Start position for searching
start = 0
results = []
# Loop to find all occurrences of the substring
while True:
    # Use re.search to find the next occurrence starting from 'start'
    match = re.search(substring, string[start:])
    if match:
        # Append the start and end indices (adjusting for the overall string)
        results.append((start + match.start(), start + match.end() - 1))
        # Move the start index to the next character after the current match's start
        start += match.start() + 1
    else:
        break
# Check if we found any matches
if results:
    for result in results:
        print(result)
else:
    print((-1, -1))

# Matrix Script
#!/bin/python3
import math
import os
import random
import re
import sys
import re
# Read the input dimensions
n, m = map(int, input().strip().split())
# Read the matrix rows
matrix = [input() for _ in range(n)]
# Decode the script by reading column-wise
decoded_script = ''.join(matrix[j][i] for i in range(m) for j in range(n))
# Replace non-alphanumeric characters with space where appropriate
decoded_script = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_script)
# Print the final result
print(decoded_script)


# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# Read the number of lines
n = int(input())
# Initialize an empty list to hold the lines of text
lines = []
# Read each line and store it in the list
for _ in range(n):
    lines.append(input())
# Define a function to replace '&&' and '||' with 'and' and 'or'
def replace_symbols(text):
    # Replace '&&' with 'and'
    text = re.sub(r'(?<= )&&(?= )', 'and', text)
    # Replace '||' with 'or'
    text = re.sub(r'(?<= )\|\|(?= )', 'or', text)
    return text
# Process each line and print the modified text
for line in lines:
    print(replace_symbols(line))

# Validating Postal Codes
regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.
import re
# Regex for integer in range 100000 to 999999
regex_integer_in_range = r'^[1-9][0-9]{5}$'
# Regex for alternating repetitive digit pairs
regex_alternating_repetitive_digit_pair = r'(?=(\d)(?=\d\1))'
# Example postal code input
P = input().strip()
# Validate the postal code
is_valid_postal_code = (bool(re.match(regex_integer_in_range, P)) and 
                        len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
# Output the result
print(is_valid_postal_code)


# Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def is_valid_uid(uid):
    # Check the length of the UID
    if len(uid) != 10:
        return False
    
    # Check for uppercase letters, digits, and unique characters
    upper_case_count = sum(1 for c in uid if c.isupper())
    digit_count = sum(1 for c in uid if c.isdigit())
    
    # Ensure all characters are alphanumeric and check for duplicates
    if not uid.isalnum() or len(set(uid)) != len(uid):
        return False
    
    # Check for minimum counts
    if upper_case_count < 2 or digit_count < 3:
        return False
    
    return True
# Read number of test cases
n = int(input())
for _ in range(n):
    uid = input().strip()
    if is_valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# Regular expression pattern for a valid mobile number
pattern = r'^[789]\d{9}$'
# Read the number of inputs
n = int(input())
for _ in range(n):
    mobile_number = input().strip()  # Read each mobile number input
    # Check if the mobile number matches the pattern
    if re.match(pattern, mobile_number):
        print("YES")
    else:
        print("NO")

# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    current_level = level + 1
    # Update the maximum depth if the current level is greater
    if current_level > maxdepth:
        maxdepth = current_level
    # Recur for each child of the current element
    for child in elem:
        depth(child, current_level)

# Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def validate_credit_card(card_number):
    # Regular expression for validating credit card numbers
    pattern = r'^(?!.*(\d)(?:-?\1){3})(?:[4-6]\d{3}(?:-?\d{4}){3})$'
    return bool(re.match(pattern, card_number))
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        card_number = input().strip()
        if validate_credit_card(card_number):
            print('Valid')
        else:
            print('Invalid')

# XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    count = len(node.attrib)  # Count attributes of the current node
    # Iterate over all child nodes
    for child in node:
        count += get_attr_number(child)  # Add the count of attributes from child nodes
    return count  # Return the total count

# HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        # Print attributes if they exist
        for attr in attrs:
            attr_name, attr_value = attr
            print(f"-> {attr_name} > {attr_value if attr_value else 'None'}")
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        # Print attributes if they exist
        for attr in attrs:
            attr_name, attr_value = attr
            print(f"-> {attr_name} > {attr_value if attr_value else 'None'}")
    def handle_comment(self, data):
        # Ignore comments
        pass
if __name__ == '__main__':
    n = int(input())  # Read number of lines
    html = ""
    for _ in range(n):
        html += input().strip()  # Read each line of HTML
    parser = MyHTMLParser()
    parser.feed(html)  # Feed the HTML to the parser

# HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    
  
    def handle_comment(self, data):
        # Check if the comment is multiline or single-line
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    def handle_data(self, data):
        # Only print data if it is not just whitespace or a newline
        if data.strip():
            print(">>> Data")
            print(data)
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Print the tag name
        print(tag)
        # Print each attribute with its value
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
    def handle_endtag(self, tag):
        # We don't need to do anything for end tags
        pass
    def handle_startendtag(self, tag, attrs):
        # Print the tag name for empty tags
        print(tag)
        # Print each attribute with its value
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
# Read input
n = int(input())
html = ""
for _ in range(n):
    html += input().rstrip() + '\n'
# Create an instance of the parser and feed the HTML data
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Validating Roman Numerals

import re
# Regular expression for validating Roman numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# Print the result as True or False

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
# Regular expression for validating email addresses
email_regex = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{2,5}$'
# Read the number of email addresses
n = int(input())
# Process each name and email
for _ in range(n):
    line = input().strip()
    name, email_address = email.utils.parseaddr(line)  # Parse the name and email address
    # Check if the email address is valid
    if re.match(email_regex, email_address):
        # Print the valid name and email address in the required format
        print(f"{name} <{email_address}>")

# Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
       return numpy.array(arr, dtype=float)[::-1]

# Shape and Reshape
import numpy as np
input_data = input().strip().split()
array_data = list(map(int, input_data))
# Create a NumPy array and reshape it to 3x3
array_2d = np.array(array_data).reshape(3, 3)
# Print the resulting 3x3 array
print(array_2d)

# Transpose and Flatten
import numpy as np
n, m = map(int, input().strip().split())
# Read the matrix elements
matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)
# Convert the list of lists into a NumPy array
array = np.array(matrix)
# Print the transposed array
print(np.transpose(array))
# Print the flattened array
print(array.flatten())


# Concatenate
import numpy as np
# Read the dimensions of the arrays
N, M, P = map(int, input().strip().split())
# Initialize the first array
array_1 = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    array_1.append(row)
# Initialize the second array
array_2 = []
for _ in range(M):
    row = list(map(int, input().strip().split()))
    array_2.append(row)
# Convert lists to NumPy arrays
array_1 = np.array(array_1)
array_2 = np.array(array_2)
# Concatenate the arrays along axis 0
result = np.concatenate((array_1, array_2), axis=0)
# Print the concatenated array
print(result)

# Zeros and Ones
import numpy as np
# Read the shape from input
shape = tuple(map(int, input().strip().split()))
# Create a zeros array with the specified shape and integer type
zeros_array = np.zeros(shape, dtype=int)
# Create a ones array with the specified shape and integer type
ones_array = np.ones(shape, dtype=int)
# Print the arrays
print(zeros_array)
print(ones_array)

# Eye and Identity
import numpy as np
# To align the output properly, set print options
np.set_printoptions(legacy='1.13')
# Read the dimensions from input
n, m = map(int, input().strip().split())
# Create an N x M array with zeros
array = np.zeros((n, m))
# Set the diagonal elements to 1
# The np.fill_diagonal function is used to set the diagonal elements
np.fill_diagonal(array, 1)
# Print the resulting array
print(array)



# Array Mathematics

import numpy as np
# Read the dimensions of the arrays
n, m = map(int, input().strip().split())
# Read the first array
array1 = np.array([list(map(int, input().strip().split())) for _ in range(n)])
# Read the second array
array2 = np.array([list(map(int, input().strip().split())) for _ in range(n)])
# Perform the required operations
# Addition
add_result = array1 + array2
# Subtraction
sub_result = array1 - array2
# Multiplication
mul_result = array1 * array2
# Integer Division
div_result = np.floor_divide(array1, array2)
# Modulus
mod_result = array1 % array2
# Power
pow_result = array1 ** array2
# Print the results in the required format
print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(mod_result)
print(pow_result)


# Floor, Ceil and Rint
import numpy as np
# Read the input array
A = np.array(list(map(float, input().strip().split())))
# Calculate the floor, ceil, and rint
floor_values = np.floor(A)
ceil_values = np.ceil(A)
rint_values = np.rint(A)
# Print the results
print(floor_values)
print(ceil_values)
print(rint_values)


# Sum and Prod


import numpy as np
# Step 1: Read input for N and M
N, M = map(int, input().split())
# Step 2: Read the N lines of input to form the array
array = np.array([input().split() for _ in range(N)], int)
# Step 3: Compute the sum along axis 0 (column-wise sum)
sum_along_axis_0 = np.sum(array, axis=0)
# Step 4: Compute the product of the resulting sums
result = np.prod(sum_along_axis_0)
# Step 5: Print the result
print(result)

# Min and Max

import numpy as np
# Step 1: Read input for N and M
N, M = map(int, input().split())
# Step 2: Read the N lines of input to form the array
array = np.array([input().split() for _ in range(N)], int)
# Step 3: Compute the min along axis 1 (row-wise min)
min_along_axis_1 = np.min(array, axis=1)
# Step 4: Compute the max of the row-wise minimum values
result = np.max(min_along_axis_1)
# Step 5: Print the result
print(result)


# Mean, Var, and Std

import numpy as np
# Step 1: Read input for N and M
N, M = map(int, input().split())
# Step 2: Read the N lines of input to form the array
array = np.array([input().split() for _ in range(N)], int)
# Step 3: Compute the mean along axis 1 (row-wise mean)
mean_along_axis_1 = np.mean(array, axis=1)
# Step 4: Compute the variance along axis 0 (column-wise variance)
var_along_axis_0 = np.var(array, axis=0)
# Step 5: Compute the standard deviation along the entire array
std_along_none = np.std(array)
# Step 6: Print the results
print(mean_along_axis_1)
print(var_along_axis_0)
print(round(std_along_none, 11))  # Rounded to 11 decimal places as per sample output


# Dot and Cross
import numpy as np
# Step 1: Read input for the size of the matrices
N = int(input())
# Step 2: Read the next N lines for matrix A
A = np.array([list(map(int, input().split())) for _ in range(N)])
# Step 3: Read the next N lines for matrix B
B = np.array([list(map(int, input().split())) for _ in range(N)])
# Step 4: Compute the matrix product
result = np.dot(A, B)
# Step 5: Print the result
print(result)


# Inner and Outer

import numpy as np
# Step 1: Input the elements of array A
A = np.array(list(map(int, input().split())))
# Step 2: Input the elements of array B
B = np.array(list(map(int, input().split())))
# Step 3: Compute the inner product
inner_product = np.inner(A, B)
# Step 4: Compute the outer product
outer_product = np.outer(A, B)
# Step 5: Print the inner product
print(inner_product)
# Step 6: Print the outer product
print(outer_product)


# Polynomials
import numpy as np
# Step 1: Input the polynomial coefficients
coefficients = list(map(float, input().split()))
# Step 2: Input the value of x
x = float(input())
# Step 3: Evaluate the polynomial at x
result = np.polyval(coefficients, x)
# Step 4: Print the result
print(result)



# Linear Algebra
import numpy as np
# Step 1: Input the size of the square matrix
N = int(input())
# Step 2: Input the matrix elements
matrix = [list(map(float, input().split())) for _ in range(N)]
# Step 3: Compute the determinant using np.linalg.det()
determinant = np.linalg.det(matrix)
# Step 4: Round the determinant to 2 decimal places
rounded_determinant = round(determinant, 2)
# Step 5: Print the rounded determinant
print(rounded_determinant)



# Any or All
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Input the number of integers N
N = int(input())
# Step 2: Input the list of integers
numbers = list(map(int, input().split()))
# Step 3: Check if all integers are positive
all_positive = all(num > 0 for num in numbers)
# Step 4: Check if any integer is palindromic
any_palindromic = any(str(num) == str(num)[::-1] for num in numbers)
# Step 5: Print True if all integers are positive and at least one is palindromic
print(all_positive and any_palindromic)

# Input()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Input the values of x and k
x, k = map(int, input().split())
# Step 2: Input the polynomial expression
polynomial = input()
# Step 3: Evaluate the polynomial at x using eval() and check if it equals k
# Use eval to substitute x in the polynomial
result = eval(polynomial)
# Step 4: Compare result with k and print True or False
print(result == k)

# Python Evaluation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Read the input expression
expression = input()
# Step 2: Evaluate the expression using eval()
eval(expression)

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
     
        sorted_people = sorted(people, key=lambda person: int(person[2]))
        # Apply the name_format function to each sorted person
        return [f(person) for person in sorted_people]
    return inner

# Validating Email Addresses With a Filter
import re
def fun(s):
    # return True if s is a valid email, else return False
       
    pattern = r'^[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,}$'
    # Return True if the email matches the pattern
    return re.match(pattern, s) is not None

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    # Find the maximum height of the candles
    tallest = max(candles)
    # Count how many candles have the tallest height
    return candles.count(tallest)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    
    # Calculate if they will land on the same position at the same time
    # Use the condition derived above
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    # Write your code here
    total_likes = 0
    people = 5  # initial people seeing the ad
    
    for day in range(n):
        likes_today = people  // 2 
        total_likes += likes_today   # accumulate total likes
        people = likes_today * 3      # those who liked the ad share with 3 friends each
    return total_likes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    # Write your code here
    def calculate_super_digit(num):
        if len(num) == 1:
            return int(num)
        else:
            digit_sum = sum(int(d) for d in num)
            return calculate_super_digit(str(digit_sum))
    
    # Compute the initial sum of digits in n and multiply by k
    initial_sum = sum(int(d) for d in n) * k
    
    # Compute the super digit of the resulting number
    return calculate_super_digit(str(initial_sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    last_element = arr[-1]
    
    # Start from the second last element
    i = n - 2
    
    # Shift elements until the correct position for last_element is found
    while i >= 0 and arr[i] > last_element:
        arr[i + 1] = arr[i]  # Shift the element to the right
        print(*arr)  # Print the current state of the array
        i -= 1
    
    # Insert the last element in the correct position
    arr[i + 1] = last_element
    print(*arr)  # Print the final state of the array
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    # Write your code here
    # Iterate through the array starting from the second element
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        
        # Shift elements of arr[0..i-1], that are greater than current_value,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place current_value at its correct position
        arr[j + 1] = current_value
        
        # Print the current state of the array after each insertion
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

