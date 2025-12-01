name = input("What is your name? ")

age= int(input("What is your age? "))

nxt_year= age + 1

def greet(name, age):
    return f"Hello {name}! You will be  {age} next years!"

message = greet(name, nxt_year)
print(message)
