
def add(a, b):
    print(f"Adding {a} and {b}")  # Debugging line
    return a + b

result = add(3, 5)
print(f"Result: {result}")


import pdb

def add(a, b):
    pdb.set_trace()  # Start the debugger here
    return a + b

result = add(3, 5)
print(result)

# Commands within pdb:
# n (next): Execute the next line of code.
# c (continue): Continue execution until the next breakpoint.
# p <variable>: Print the value of <variable>.