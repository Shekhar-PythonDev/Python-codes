#tuple + tuple
t1 = (1,2,3)
t2 = (4,5,6)
s = t1 + t2
print(s)  #// output:(1,2,3,4,5,6)

# tuple + list
t1 = (1,2,3)
l2 = [4,5,6]
s = t1 + l1
print(s) # // TypeError: can only concatenate tuple (not "list") to tuple

# list + set 

list = [12,2,10.5] 
set = {45,1,20.3}
reasult = list + set
print(reasult) # //TypeError: can only concatenate list (not "set") to list

# set + dictionary
set = {"om", "sai"}
dictionary = {"ram"}
s = set + dictionary
print(s)  #// TypeError: can only concatenate set (not "dict") to set


#tuple*tuple
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
result = tup1 * tup2  # TypeError


# list*set
lst = [1, 2, 3]
st = {4, 5, 6}
result = lst * st  # TypeError

# /--> division operator
a = 10
b = 6
print(a/b)  # 1.6666666666666667
c = 33.4
print(c/b) # 5.566666666666666
print(c/a) # 3.34

# //--> floor division
s = 56
x = 5
print(s//x)  # 11

d = 10
k = 3
print(d//k)  # 3

# %--> Modulo operator
v = 23
p = 11
print(v%p) # 1