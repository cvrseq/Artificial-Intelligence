x = 5 >= 2
a = {1, 3, 7, 8}
b = {2, 4, 5, 10, "apple"}
c = a & b
df = "Антонова Антонина", 34, "ж"
z = "type"
d = [1, "title", 2, "content"]

print(x, " ", type(x))

print(a, " " , type(a))

print(b, " " , type(b))

print(c, " " , type(c))

print(d, " " , type(d))

print(z, " " , type(z))

print(df, " " , type(df))

#True   <class 'bool'>
#{8, 1, 3, 7}   <class 'set'>
#{2, 4, 5, 'apple', 10}   <class 'set'>
#set()   <class 'set'>
#[1, 'title', 2, 'content']   <class 'list'>
#type   <class 'str'>
#('Антонова Антонина', 34, 'ж')   <class 'tuple'>
