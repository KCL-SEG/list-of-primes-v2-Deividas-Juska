"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 1
    prime = False
    if (number_of_primes > 0):
        list.append(2)
        while(len(list) < number_of_primes):
            count += 1
            for num2 in range(2,count):
                if (count % num2 == 0):
                    prime = False
                    break
                else:
                    prime = True  
            if(prime):
                list.append(count)
        return list   
    else:
        raise ValueError("Inputted value should be greater than 0")
