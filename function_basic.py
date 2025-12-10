"""Basic function exercises."""
import math

def print_hello():
    """Print "hello"."""
    print("Hello")
    
def get_hello(hello) -> str:
    """Return "hello"."""
    return hello

def ask_name_and_greet_user():
    """
    Ask name and greet user.

    The user has to enter his/her name. The function prints the greeting.

    Regular greeting: Hi, [name]. Would you like to have a Hamburger?
    [name] is capitalized, meaning first letter is capital, the rest is lower.

    If the name is Thanos (case insensitive, so thanos and THANOS also count):
    Get out of here, Thanos! Nobody wants to play with you!
    """
name = input("Insert your name: ")
name = name.lower().capitalize()
if name == ("Thanos"):
    print("Get out of here, Thanos! Nobody wants to play with you!")
else:
    print("Hi," +  (name) + ". Would you like to have a Hamburger?")
    
def calculate_hypotenuse_length(a: float, b: float) -> float:
    #"""Return hypotenuse value."""
    return(math.sqrt(a ** 2 + b ** 2))

def calculate_cathetus_length(a: float, c: float) -> float:
    """Return cathetus value."""
    return(math.sqrt(c ** 2 - a ** 2))
    