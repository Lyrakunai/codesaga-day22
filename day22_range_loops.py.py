# day 22 - range() practice

# 1. print 1 to 10
for i in range(1,10):
    print(i)

# 2. Even numbers
for i in range(2,21,2):
    print(i)

# 3. Reverse 10 to 1
for i in range(10,0,-1):
    print(i)

# 4. Sum or 1 to 10
sum = 0 
for i in range(1,11):
    sum = sum + i
print("sum:",sum)

# 5. Count even numbers
count = 0 
for i in range(2,21,2):
    count = count + 1
print("count:",count)