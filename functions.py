Theory Questions:




QUESTION 1- What is the difference between a function and a method in Python ?

SOLUTION 1-

Difference between Function and Method:
Function:

A function is an independent block of code that performs a specific task.
It is defined using the def keyword and can be called by its name.
Functions are not tied to any object or class.
Method:

A method is similar to a function but is associated with an object (an instance of a class).
Methods are defined inside a class and are called on objects of that class.
The first parameter of a method is usually self, which refers to the instance of the class.
    

Function Example:

# Function definition
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))

METHOD EXAMPLE:
class Person:
    # Method definition inside a class
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# Creating an instance of the class
person = Person("Alice")

# Calling the method on the object
print(person.greet())







QUESTION 2- Explain the concept of function arguments and parameters in Python.

SOLUTION 2-
In Python, function arguments and parameters refer to the inputs a function can receive. Here's the distinction between the two:

Parameters are the names listed in the function definition. They act as placeholders for the values that will be passed to the function.
Arguments are the actual values that are passed to the function when it is called.

EXAMPLE:
# Function with parameters and different types of arguments
def describe_person(name, age, city="Unknown", *hobbies, **additional_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
    # Hobbies passed as arbitrary positional arguments
    if hobbies:
        print(f"Hobbies: {', '.join(hobbies)}")
    
    # Additional info passed as arbitrary keyword arguments
    for key, value in additional_info.items():
        print(f"{key.capitalize()}: {value}")

# Calling the function with positional arguments
describe_person("Alice", 25)

# Calling the function with a mix of positional and keyword arguments
describe_person("Bob", 30, city="New York", hobby1="Painting", hobby2="Cycling")

# Calling the function with arbitrary positional and keyword arguments
describe_person("Charlie", 40, "San Francisco", "Reading", "Traveling", job="Engineer", pet="Dog")


OUTPUT:
Name: Alice
Age: 25
City: Unknown

Name: Bob
Age: 30
City: New York

Name: Charlie
Age: 40
City: San Francisco
Hobbies: Reading, Traveling
Job: Engineer
Pet: Dog







QUESTION 3- What are the different ways to define and call a function in Python?

SOLUTION 3-
1. Standard Function Definition and Call
This is the most basic way to define and call a function.

Definition: A function is defined using the def keyword, followed by the function name and parentheses containing optional parameters.

EXAMPLE:
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))


Function with Default Arguments
A function can have parameters with default values. If the caller doesn’t provide an argument, the default value is used.

EXAMPLE:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Calling with and without the default argument
print(greet("Alice"))           # Uses default greeting
print(greet("Bob", "Hi"))       # Overrides default greeting






QUESTION 4- What is the purpose of the `return` statement in a Python function?

SOLUTION 4-
 Purpose of the return statement:
1-Return a Value: It sends the result of a function’s computation back to the caller.
2-Terminate the Function: It stops further execution of the function once encountered.

EXAMPLE:
def add(a, b):
    return a + b

# Calling the function and storing the result
result = add(3, 5)
print(result)  # Output: 8







QUESTION 5-  What are iterators in Python and how do they differ from iterables?

SOLUTION 5-
Definitions:
Iterable:

An iterable is an object that can return its elements one at a time. This means that you can iterate over it using a loop (like a for loop).
Common examples of iterables include lists, tuples, strings, dictionaries, and sets.
An iterable must implement the __iter__() method, which returns an iterator.
Iterator:

An iterator is an object that represents a stream of data; it fetches the elements of an iterable one at a time using the __next__() method.
Iterators are created from iterables and are used to iterate through the iterable's elements.
An iterator must implement two methods: __iter__() (which returns the iterator object itself) and __next__() (which returns the next item and raises a StopIteration exception when there are no more items).


EXAMPLE:
# An example iterable (a list)
my_list = [1, 2, 3, 4, 5]

# Using the iter() function to create an iterator from the iterable
my_iterator = iter(my_list)

# Using the next() function to fetch elements from the iterator
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# Continuing to use next() until StopIteration is raised
try:
    print(next(my_iterator))  # Output: 4
    print(next(my_iterator))  # Output: 5
    print(next(my_iterator))  # This will raise StopIteration
except StopIteration:
    print("Reached the end of the iterator.")

# Example of a custom iterable class
class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyIterator(self.start, self.end)

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Using the custom iterable
my_iterable = MyIterable(1, 5)
for value in my_iterable:
    print(value)  # Output: 1 2 3 4







QUESTION 6-. Explain the concept of generators in Python and how they are defined.

SOLUTION 6-
Generators in Python are a special type of iterable that allow you to create iterators in a more concise and readable way. 
They are defined using a function with the yield statement instead of return. When a generator function is called, it doesn't 
execute the code immediately; instead, it returns a generator object that can be iterated over.

EXAMPLE:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  # Yield the current value of 'a'
        a, b = b, a + b  # Update 'a' and 'b' to the next Fibonacci numbers

# Using the generator
fib_gen = fibonacci(10)

# Iterating over the generator
for num in fib_gen:
    print(num)







QUESTION 7-  What are the advantages of using generators over regular functions?

SOLUTION 7-
Generators offer several advantages over regular functions, particularly when it comes to memory efficiency and ease of use 
in scenarios involving large datasets or streams of data. 

1. Memory Efficiency
2. Representing Infinite Sequences
3. Improved Readability and Simplicity

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num)







QUESTION 8-What is a lambda function in Python and when is it typically used?

SOLUTION 8-
Key Characteristics of Lambda Functions:
Anonymous: They do not require a name, making them ideal for situations where you need a function for a short duration.
Single Expression: Lambda functions can contain only one expression. This expression is evaluated and returned.
Return Value: The value of the expression is returned automatically without needing an explicit return statement.

Typical Use Cases:
Short Functions: Used for simple operations, such as mathematical calculations or string manipulations.
Higher-Order Functions: Commonly used with functions like map(), filter(), and sorted() where a function is required as an argument.
Callbacks: Suitable for defining small callback functions in event-driven programming.
    
EXAMPLE:
# Defining a lambda function to add two numbers
add = lambda x, y: x + y

# Calling the lambda function
result = add(5, 3)
print(result)  # Output: 8






QUESTION 9- Explain the purpose and usage of the `map()` function in Python.

SOLUTION 9-
Purpose of map()
Transformation of Data: map() allows you to apply a transformation function to every item in an iterable.
Concise Syntax: It reduces the need for verbose loops, making the code more concise and readable.
Efficiency: Since it returns an iterator, it can be more memory-efficient compared to list comprehensions when working with large datasets.

Usage of map()
The map() function takes two arguments:

Function: A function that takes one or more arguments and returns a value.
Iterable(s): One or more iterables whose elements will be passed to the function.

EXAMPLE:
# Define a function to square a number
def square(x):
    return x ** 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each number
squared_numbers = map(square, numbers)

# Convert the map object to a list
squared_list = list(squared_numbers)

print(squared_list)  # Output: [1, 4, 9, 16, 25]







QUESTION 10:What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?

SOLUTION 10-

Summary of Differences:
Function	                                Purpose	Returns
map()	    Applies a function to each item in an iterable	An iterator of transformed items
filter()	Filters items based on a condition	An iterator of filtered items
reduce()	Applies a binary function cumulatively to the iterable	A single reduced value

EXAMPLE:
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Using map to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Output: [1, 4, 9, 16, 25, 36]

# Using filter to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, squared_numbers))  # Output: [4, 16, 36]

# Using reduce to sum the even numbers
sum_of_evens = reduce(lambda x, y: x + y, even_numbers)  # Output: 56

print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)
print("Sum of Even Squares:", sum_of_evens)


OUTPUT:
Squared Numbers: [1, 4, 9, 16, 25, 36]
Even Numbers: [4, 16, 36]
Sum of Even Squares: 56






QUESTION -11-  Using pen & Paper write the internal mechanism for sum operation using  reduce function on this given
list:[47,11,42,13]; 

SOLUTION ARE IN - ATTACHED IMAGE.



Practical Questions: ****************************************

QUESTION 1-Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in
the list.

SOLUTION 1-
def sum_of_even_numbers(numbers):
    # Use a generator expression to filter and sum even numbers
    return sum(num for num in numbers if num % 2 == 0)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers)
print(f"The sum of even numbers is: {result}")  # Output: The sum of even numbers is: 30






QUESTION 2-Create a Python function that accepts a string and returns the reverse of that string.

SOLUTION 2-

def reverse_string(input_string):
    # Return the reversed string using slicing
    return input_string[::-1]

# Example usage
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print(f"The reversed string is: '{reversed_str}'")  # Output: The reversed string is: '!dlroW ,olleH'





QUESTION 3- Implement a Python function that takes a list of integers and returns a new list containing the squares of
each number.

SOLUTION 3-
def square_numbers(numbers):
    # Use a list comprehension to create a new list with squares of each number
    return [num ** 2 for num in numbers]

# Example usage
input_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_list)
print(f"The squares of the numbers are: {squared_list}")  # Output: The squares of the numbers are: [1, 4, 9, 16, 25]




QUESTION 4-Write a Python function that checks if a given number is prime or not from 1 to 200.

SOLUTION 4-
def is_prime(num):
    # Check if the number is less than 2 (not prime)
    if num < 2:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a factor, so it's not prime
    return True  # No factors found, it's prime

# Example usage for numbers from 1 to 200
for number in range(1, 201):
    if is_prime(number):
        print(f"{number} is a prime number.")





QUESTION 5-Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of
terms.

SOLUTION 5-
class FibonacciIterator:
    def __init__(self, terms):
        self.terms = terms  # Total number of terms
        self.current = 0    # Current term index
        self.a, self.b = 0, 1  # Initial Fibonacci numbers

    def __iter__(self):
        return self  # Return the iterator object itself

    def __next__(self):
        if self.current < self.terms:
            # Return the current Fibonacci number
            self.current, self.a, self.b = self.current + 1, self.b, self.a + self.b
            return self.a
        else:
            # StopIteration exception to indicate end of iteration
            raise StopIteration

# Example usage
terms = 10  # Number of terms in the Fibonacci sequence
fibonacci_sequence = FibonacciIterator(terms)

print(f"Fibonacci sequence up to {terms} terms:")
for number in fibonacci_sequence:
    print(number, end=' ')  # Output: 1 1 2 3 5 8 13 21 34 55







QUESTION 6-Write a generator function in Python that yields the powers of 2 up to a given exponent.

SOLUTION 6-
def powers_of_two(exponent):
    """Generator function that yields powers of 2 up to the given exponent."""
    for i in range(exponent + 1):  # Include the given exponent
        yield 2 ** i

# Example usage
exponent = 10  # Specify the maximum exponent
print(f"Powers of 2 up to 2^{exponent}:")
for power in powers_of_two(exponent):
    print(power, end=' ')  # Output: 1 2 4 8 16 32 64 128 256 512 1024






QUESTION 7- Implement a generator function that reads a file line by line and yields each line as a string.

SOLUTION 7-
def read_file_line_by_line(file_path):
    """Generator function that reads a file line by line."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yield each line after stripping whitespace

# Example usage
file_path = 'example.txt'  # Replace with your file path
try:
    for line in read_file_line_by_line(file_path):
        print(line)  # Print each line from the file
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")









QUESTION 8-. Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.

SOLUTION 8-
# Sample list of tuples
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (4, 'date')]

# Sorting the list of tuples based on the second element
sorted_data = sorted(data, key=lambda x: x[1])

# Output the sorted list
print("Sorted list of tuples based on the second element:")
print(sorted_data)




QUESTION 9-Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.

SOLUTION 9-
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# List of temperatures in Celsius
celsius_temps = [0, 20, 37, 100]

# Using map() to convert Celsius to Fahrenheit
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

# Output the converted temperatures
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)




QUESTION 10-Create a Python program that uses `filter()` to remove all the vowels from a given string.

SOLUTION 10-
def remove_vowels(input_string):
    """Remove vowels from the input string using filter()."""
    # Define a function that returns True if the character is not a vowel
    def is_not_vowel(char):
        return char.lower() not in 'aeiou'

    # Use filter() to keep only non-vowel characters
    filtered_characters = filter(is_not_vowel, input_string)

    # Join the filtered characters back into a string
    return ''.join(filtered_characters)

# Example usage
input_str = "Hello, World!"
result = remove_vowels(input_str)
print("Original string:", input_str)
print("String without vowels:", result)





QUESTION 11-Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

Order Number     Book Title and Author                          Quantity                     Price per Item
34587                   Learning Python, Mark Lutz                   4                               40.95
98762                   Programming Python, Mark Lutz           5                               56.80
77226                     Head First Python, Paul Barry               3                               32.95
88112                    Einführung in Python3, Bernd Klein      3                                24.99


Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the product of the 
price per item and the quantity. The product should be increased by 10,- € if the value of the order is smaller than 100,00 €.

Write a Python program using lambda and map.


SOLUTION 11-
# Sample order data
orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

# Function to calculate order totals
def calculate_order_totals(order):
    order_number = order[0]
    quantity = order[2]
    price_per_item = order[3]
    
    # Calculate the total price
    total_price = quantity * price_per_item
    
    # Increase by 10 if the total is less than 100
    if total_price < 100:
        total_price += 10
    
    return (order_number, total_price)

# Using map() with a lambda function to apply the calculation
order_totals = list(map(lambda order: calculate_order_totals(order), orders))

# Output the results
print("Order Number and Adjusted Total:")
for order in order_totals:
    print(order)


OUTPUT:
Order Number and Adjusted Total:
(34587, 163.8)
(98762, 284.0)
(77226, 99.85)
(88112, 84.97)


