items = [1,2,3]
items_plus = []

for item in items:
	items_plus.append(item + 1)

print(items_plus)
# Выведет [2, 3, 4]

items = [1,2,3]

items_plus = [item +1 for item in items]

print(items_plus)
# Выведет [2, 3, 4]

items = [1,2,3]
items_exp = []

for item in items:
	items_exp.append(item ** 2)

print(items_exp)
# Выведет [1, 4, 9]

items = [1,2,3]

items_exp = [item ** 2 for item in items]

print(items_exp)
# Выведет [1, 4, 9]

items = ["1", "2", "3"]

items_int = []

for item in items:
    items_int.append(int(item))

print(items_int)
# Выведет [1, 2, 3]

items = ["1", "2", "3"]

items_int = [int(item) for item in items]

print(items_int)
# Выведет [1, 2, 3]

numbers = [1, 2, 3]

[print(num) for num in numbers]

words = ["ракушка", "кукушка", "рыбка"]
words_with_r = [word for word in words if "р" in word]
[print(w) for w in words_with_r]
