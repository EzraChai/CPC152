i = 1
while i < 5:
    print(i)
    i+= 1

count = 0
while (count < 3):
    count = count +1
    print("Hello USM")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("I'm a false statement")
    print("I can only run once.")

# 1
# 3
for i in range(1,5,2):
    print(i)

# 2 5 8 11
for x in range(2,14,3):
    print(x, end=' ')

print()

# 0 1 2 3 4
for y in range(5):
    print(y, end=' ')

print()
# 5 4 3 2
for x in range(5,1,-1):
    print(x, end=' ')

print()

print("First 10 Natural Numbers")
i = 1;
while i <= 10:
    print(i, end=' ')
    i+= 1

print()

print("First 10 Natural Numbers")
for i in range(1,11):
    print(i, end=' ')

print()

# total = 0 
# for i in range(10):
#     total += int(input("Enter the number: "))

# print("Sum of these numbers: "+ str(total))
# print("Average of these numbers: " + str(total/10))

# T
# i
# g
# e
# r
for x in 'Tiger':
    print(x)

# Tiger
# Elephant
# Zebra
animals = ["Tiger", "Elephant", "Zebra"]
for x in animals:
    print(x)