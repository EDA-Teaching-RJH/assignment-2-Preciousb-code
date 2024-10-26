import random
random_numbers = [random.randint(1,100) for numbers in range (10)]
print("Original list:", random_numbers) 

for num in random_numbers[:]:  
    while num % 2 == 0:  
         random_numbers.pop(random_numbers.index(num))
         break  

    print("Odd numbers:", random_numbers)