# Input
name = input("Enter your name: ")
print("Hello, " + name)
# Output
print("Hello there" "Python Programming", sep=',', end='\n')

# Formatted string using f-strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")



# String Formatting with % Operator
# Example 1: Formatting with a Single Value
name = "Alice"
greeting = "Hello, %s!" % name
print(greeting)

# Example 2: Formatting Multiple Values
name = "Bob"
age = 25
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)

# Example 3: Formatting with Floats
pi = 3.14159
formatted_pi = "The value of pi is approximately %.2f" % pi
print(formatted_pi)

# Example 4: Padding and Alignment
number = 42
formatted_number_right = "Number: %5d" % number  # 5 spaces wide, right-aligned
print(formatted_number_right)

formatted_number_left = "Number: %-5d" % number  # 5 spaces wide, left-aligned
print(formatted_number_left)

# Example 5: Hexadecimal and Octal Formatting
number = 255
hex_number = "Hex: %x" % number
octal_number = "Octal: %o" % number
print(hex_number)
print(octal_number)

#  String Formatting with str.format()
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
