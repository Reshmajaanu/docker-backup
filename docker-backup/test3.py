first_name='Rahul'
last_name='Mathod'
age=23
print ("Hi my name is "+first_name+' '+last_name+ " and i am "+str(age)+ " " +"years old")
print(f"Hi my name is {first_name} {last_name} and i am {age} years old")
print ("Hi my name is {} {} and i am {} years old".format(first_name,last_name,age))
x='something'
print(x[0])
#x[0]='S'
#print (x[0])
x='India win'
print (x)
y='reshma','jaanu'
print (y)
lst = ["virat","kohli",32,20.0,10+20j,[10,202,30]]
print(type (lst))
lst1=list(("some","none","nothing", 29,60))
print (lst)
print (lst1)
countries= ['IND',"SL","AUS","NZ",'SA']
print (countries)
print (countries[0])
print (len(countries))
print (countries[::-1])
print (countries[-1])
countries.append ("ENG")
countries.insert(2,"AFG")
print (countries)
countries1=["RUS","ARG","NETH","SCOT","BAN"]
#countries.append(countries1)
print (countries)
print (len(countries))
countries.extend(countries1)
print (countries)
print (len(countries))
#countries.remove("SCOT")
countries.pop()
#countries.clear()
print (countries)
for data in countries:
    print(f"the country name is {data}")
countries.sort()
print (countries)
xy=['X','x','y','A','b','C',12,76,77,78,'a']
