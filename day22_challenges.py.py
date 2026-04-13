#  Day22 - Mixed Practice Challenges

# 1. count even numbers from 1 to n
n = int(input("enter number:"))
even_count = 0
for i in range(1,n+1):
    if i % 2 == 0:
        even_count += 1
print("Total even numbers:", even_count)



# 2. count numbers divisible by 3 and 5
n = int(input("enter number:"))
count_3 = 0
count_5 = 0
for i in range(1,n+1):
    if i % 3 == 0:
        count_3 += 1
    if i % 5 == 0:
        count_5 += 1
print( "divisible by 3:", count_3)
print( "divisible by 5:", count_5)


# 3. Even and Odd Sum
n = int(input("enter number:"))
even_sum = 0
odd_sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)

# 4. FizzBuzz
n = int(input("enter number:"))
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)