# First level
# 1
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
print(sum(ex_list))

# 2
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
print(min(ex_list))

# 3
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
for i in ex_list[::-1]:
    print(i, end=" ")
print("")

# 4
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
for i in ex_list:
    if i % 2 != 0:
        print(i, end=" ")
print("")

# 5
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
k = int(input())
for i in ex_list:
    print(i*k, end=" ")
print("")


# Second LEVEL

# 1
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
user_x = int(input())
for i in ex_list:
    if i > user_x:
        print(i, end=" ")
print("")

# 2
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
avg_num = 0
for i in ex_list:
    if i > 0:
        avg_num += i
print(avg_num/len(ex_list))

# 3
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
less_q = 0
user_x = int(input())
for i in ex_list:
    if i < user_x:
        less_q += 1
print(less_q)

# 4
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
user_choice = int(input())
num_sum = 0
for i in ex_list:
    if i % user_choice == 0:
        num_sum += i
print(num_sum)

# 5
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
new_list = []
for i in ex_list:
    new_list.append(i*i)
print(new_list)

# 6
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
new_list = []
for i in ex_list:
    if i > 0:
        new_list.append(i)
print(new_list)

# 7
ex_list = ["кішка", "кіт", "коромисло"]
n = input()
for i in ex_list:
    if i.startswith(n):
        print(i, end=" ")
print(" ")

# 8
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
n = int(input())
num_sum = 0
for i in ex_list[:n:1]:
    num_sum += i
print(num_sum)

# 9
ex_list = ["око", "оса", "олло", "замок"]
for i in ex_list:
    if i == i[::-1]:
        print(i, end=" ")

# 10
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
bool_list = []
d = int(input())
for i in ex_list:
    if i % d == 0:
        bool_list.append(True)
    else:
        bool_list.append(False)
print(bool_list)

# Third level

# 1
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
user_x = int(input())
user_y = int(input())
for i in ex_list:
    if i % user_x == 0 and i % user_y != 0:
        print(i, end=" ")
print("")

# 2
ex_list = [[6, 3, 2], [-3, -2, -9], [True, False, True]]
new_list = []
for i in ex_list:
    for j in i:
        new_list.append(j)
print(new_list)

# 3
ex_list = ["ОкулЯри", "ПирІЖки", "ШКАРПЕТКА", "каша"]
for i in ex_list:
    for j in i:
        if j.isupper():
            print(j, end=" ")
    print(" ")

# 4
ex_list = [6, 2, 3, 9, 9, 2, 8, 10]
new_list = []
ex_list.sort(reverse=True)
ex_dict = {}

for i in ex_list:
    if i in ex_dict:
        ex_dict[i] = ex_dict[i] + 1
    else:
        ex_dict[i] = 1

while ex_dict != {}:
    val_list = list(ex_dict.values())
    key_list = list(ex_dict.keys())
    if max(val_list) in val_list:
        element = key_list[val_list.index(max(val_list))]
        i = 0
        while i < ex_dict[element]:
            new_list.append(element)
            i += 1
        del ex_dict[element]
print(new_list)

# 5
list_first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_second = [-2, -3, -8, -23, -24, -81, 0]
new_list = []
for i in list_first:
    if i % 2 == 0:
        new_list.append(i)
for i in list_second:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)

# 6
ex_dict = {'яблуко': 6,'груша': 2, 'вишня': 2}
print(sum(list(ex_dict.values())))

# 7
ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in ex_list:
    if i % 2 == 0:
        ex_list[ex_list.index(i)] = "парне"
print(ex_list)

# 8
ex_list = ["Окуляри", "Пиріг", "Шкарпекааа", "каш?"]
x_len = int(input())
count = 0
for i in ex_list:
    if len(i) > x_len:
        count += 1
print(count)

# 9
list_first = ["Окуляри", "Пиріг", "Шкарпекааа", "каш?"]
list_second = ["Штані", "Торт", "Шорти", "Макарони", "Навушники", "павер"]
ex_len = max(len(list_first), len(list_second))
new_list = []

i = 0
while i < ex_len:
    if i < len(list_first):
        new_list.append(list_first[i])
    if i < len(list_second):
        new_list.append(list_second[i])
    i += 1
print(new_list)

# 10
ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_choice = int(input("Помножити на: "))
x_choice = int(input("Більше за: "))

for i in ex_list:
    if i > x_choice:
        print(i*y_choice, end = " ")





