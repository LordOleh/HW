# 1 TASK
hello_text = "Hello, Python World!"
print(hello_text)

# 2 TASK
first_num = int(input())
second_num = int(input())
print(first_num + second_num)
print(first_num - second_num)
print(first_num * second_num)
print(first_num / second_num)

# 3 TASK
first_str = "Hello "
second_str = "World!"
res = first_str + second_str
print(f"{res}, {len(res)}")

# 4 TASK
user_num = int(input())
if user_num % 2 == 0:
    print("Парне")
else:
    print("Непарне")

# 5 TASK
for i in range(1,11):
   print(i)


# 6 TASK
num = float(input())
if num > 0:
    print("Позитивний")
elif num < 0:
    print("Негативний")
elif num == 0:
    print("Нуль")

# 7 TASK
for i in range(2,11,2):
    print(i)

# 8 TASK
n = int(input())
sum = 0
for i in range(n+1):
    sum += i
print(sum)

# 9 TASK
for i in range(10,0,-1):
    print(i)

# 10 TASK
for i in range(1,11):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)
