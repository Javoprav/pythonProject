def get_min_sec(sec):
  min_sec = {}
  for k,v in min_sec.items():
    min_sec['min'] = sec // 60
    min_sec['sec'] = sec % 2
  return min_sec
 # return print(f'"min": {min}, "sec": {s}')

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_min_sec(value)
print(result)