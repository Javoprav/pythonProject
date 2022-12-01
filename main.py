employees = {'Alice' : 100000,
'Bob' : 99817,
'Carol' : 122908,
'Frank' : 88123,
'Eve' : 93121}
top_earners = []
for key, val in employees.items():
 if val >= 100000:
  top_earners.append((key,val))
print(top_earners)
# [('Alice', 100000), ('Carol', 122908)]

print([(key,val) for key, val in employees.items() if val >= 100000])