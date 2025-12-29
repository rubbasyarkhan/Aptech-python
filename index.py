# # print("hello world")

# # arr=["grape","apple","banana","orange"]
# # print(arr)

# # arr[0]="kiwi"


# # print(arr)

# # arr.reverse()
# # print(arr)

# # arr.remove("apple")
# # print(arr)

# # numberarray=[1,5,3,5,8,5,5,4,7,2,6]
# # print(numberarray)
# # numberarray.sort()
# # print(numberarray)
# # print(numberarray.count(5))

# # tuple can not be changed but list can be changed
# # tuple=(1,2,3,4,5)
# # tuple=tuple+(6,)
# # print(tuple)    


# # in python dictionary is a key value pair and it is mutable .
# dictionary={"name":"John","age":36,"city":"New York","country":"USA","gender":"male","married":False}
# # print(dictionary)
# dictionary["name"]="jane"
# # print(dictionary)
# # dictionary.pop("age")
# # print(dictionary)
# # dictionary.clear()
# # print(dictionary)
# dictionary.keys
# print 
# # for key,value in dictionary.items():
# #     print(key,value)




def calculate(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        return num1/num2
    else:
        return "invalid operation"

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Enter the operation:")
result=calculate(num1,num2,operation)
print(result)

