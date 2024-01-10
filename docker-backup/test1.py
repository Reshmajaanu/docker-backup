#how many characters are there in a word
data='RahulJaanu'
print (data)
print (len(data))
print (data[0])
print (data[5])
print (data[3])
print (data[1])
print (data[0])
print (data[len(data)-1]) #to print the last letter
print ("my name is",data) # to print the value of variable with my text using comma for separating
print ("the length of the given data is",len(data) )
print (data.startswith("R"))
print (data.startswith("a"))
print (data[0:])    
print (data[1:])
print (data[0:1])
print (data[0:3])
print (data[2:4])
print (data[1:7:2])
print (data[1:9:2])
print (data[1:9:-1]) #this wont work
print (data[::-1])
data1= (data[1:5][::-1])
print (data1)
print (data.upper())
print (data1.capitalize())
data2= '             Alternatively, you can also execute the script by             '
data3= data2.strip()
print (data3,len(data3))
data4= data2.rstrip()
print (data4,len(data4))
data5= data2.lstrip()
print(data5,len(data5))
#datacent='''Let's say required_length is set to 5 and the input is "rahul reshama." awk would split the input into two fields, "rahul" and "reshama." The substr function then extracts the first 5 characters from the first field, which is "rahul," and prints it. So, the output of this command would be "rahul."'''
#data6= (datacent.center(10))
#print (data6)
num="567"
print (data.isdigit())
print (num.isdigit())
print (data2.replace('can','cannot'))
