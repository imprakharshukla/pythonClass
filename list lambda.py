#write a program of list comprehension and lambda function

#list comprehension
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [i for i in list1 if i%2==0]
print(list2)

#lambda function
a = lambda x,y:x+y
print(a(2,3))
