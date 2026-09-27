for i in range(2, 11):
    print(i)


for i in range(1, 21):
    if i % 2 == 0:
        print(i)

total = 0

for i in range(1, 11):
    total = total + i

print(total)

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse:", rev)

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Count:", count)

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)

n = int(input("Enter a number: "))

original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")