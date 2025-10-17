"""Loop exercises."""


#def sum_between(start: int, end: int) -> int:
   # """
    #Return sum of integers between start and end (both included).

    #print(sum_between(3, 5)) => 3 + 4 + 5 = 12
    #print(sum_between(5, 5)) => 5
   #"""
    #return sum(range(start, end + 1))

#def sum_of_even_numbers(n: int) -> int:
    #"""
    #Return sum of even numbers from 0 up to n (included).

    #print(sum_of_even_numbers(5)) => 0 + 2 + 4 = 6
    #print(sum_of_even_numbers(0)) => 0
    #"""
    #return sum(i for i in range(0, n+1, 2))

#def sum_of_multiples(n: int, end: int) -> int:
    #"""
    #Return sum of numbers which are multiples of n between 0 and end (included).
    
    #print(sum_of_multiples(3, 10)) => 3 + 6 + 9 = 18
    #print(sum_of_multiples(7, 10)) => 7
    #print(sum_of_multiples(11, 10)) => 0
    #"""
    #total = 0
    #for num in range(n, end + 1):
        #if num % n == 0:
            #total += num
    #return total

#print(sum_of_multiples(3, 10))

#def cross_sum(numbers: str) -> int:
    #"""
    #Return cross sum of numbers.
    
    #print(cross_sum("1234")) => 1 + 2 + 3 + 4 = 10
    #print(cross_sum("0")) => 0
    #print(cross_sum("4129458")) => 33
    #"""
    #summa = 0
    #symbol = ""
    #for symbol in numbers:
        #summa += int(symbol)
    #return summa
#print(cross_sum("1234"))
#print(cross_sum("0"))
#print(cross_sum("4129458"))   
    #return sum(int(digit) for digit in numbers)

def multiply_between(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    return math.prod(range(start, end + 1))
    
    
    
    

        


