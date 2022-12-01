A function with,

def function():
    i=0
    return i
    i+=1 #This will be skipped

def generator ():
    i=0
    yield i
    I+=1 # This will not be skipped

print ('-------------')

def num_list():
     num =""
     for n in "3445":
         num += n
         yield num
print(list(num_list()))

output : ['3', '34', '344', '3445']