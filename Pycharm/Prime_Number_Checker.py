def is_prime(num):
    if num <= 1:
        return(False)
    
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is divisible by: {i}") 
        
    return f"{num} is a prime number."


print(is_prime(1231341642374))