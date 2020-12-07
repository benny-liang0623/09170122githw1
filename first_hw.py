str1="  Python".strip()
str2="is   ".rstrip()
str3="  easy".lstrip()
print(str1+" "+str2+" "+str3)
print(str1+" "+str2.title()+" "+str3.title())
print(str1,str2.title(),str3.title())


a=[1,2,3,4,5,6]
b=a[0]+a[0]
print(b)

fruits=["apple","orange","banana"]
fruits[1]="pineapple"
fruits2=["guava","lemon"]
fruits += fruits2
fruits3= fruits * 3
print(fruits3)


title="Benny"
print("/%s/"%title.center(50))
print("/%s/"%title.rjust(50))
print("/%s/"%title.ljust(50))



cars=[1,2,3]
cars.append(4)
cars.insert(1,6)
cars.insert(2,8)
del cars[0]
cars1=cars.pop(0)
cars.remove(4)
print(cars)
print(cars1)

cars=[]
cars.append("Ford")
cars.append("Honda")
print(cars)






      
