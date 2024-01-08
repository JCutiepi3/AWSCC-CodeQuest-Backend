print("[Fizz-Buzz]")
print("<Conditions>")
print("if divisible by 3 = Fizz")
print("if divisible by 5 = Buzz")
print("if divisible by 3 and 5 = Fizz-Buzz")

# user input prompting desired inputs
user_limit = int(input("Enter the limit for Fizz Buzz: "))

# Conditions for FIZZ-BUZZ
for i in range(1, user_limit + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz-Buzz!')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
