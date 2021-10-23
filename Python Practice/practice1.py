# mydir = {"John": 44, "Mary": 48, "Jane": 42, "Harry": 0}
# mydir.update({"Harry": 45})
# mysum = sum(mydir.values())
# mylen = len(mydir)
# myavg = mysum / mylen;
# print(mysum, mylen, myavg) 



# for x, y in mydir.items():
#     print(x, y)
    
# for x in mydir.values():
#     print(x)
    
# for x in mydir.keys():
#     print(x)  



#practice

# def convertstr(str):
#     capitalized = str.capitalize()
#     interogatives = ("how", "why", "where")
    
#     if str.startswith(interogatives):
#         return f"{capitalized}?"
#     else:
#         return f"{capitalized}."


# responses = []
# while True:
#     user_input = input("Say Something: ")
    
#     if user_input == '\end':
#         break;
#     else:
#         responses.append(convertstr(user_input))

# print(" ".join(responses))


#indefinate number of arguments
# def maxNum(*args):
#     return max(args)

# print(maxNum(2, 3, 4))
# print(maxNum(2, 3, 4, 5, 6, 7))
# print(maxNum(2, 3, 4, 77, 199, 1000, 101, 999))
# print(maxNum(2, 3))
# print(maxNum(2))
        
        
# File Processing
# myfile = open("fruits.txt")
# content = myfile.read()
# content2 = myfile.read()

# myfile.close()

# print(content)  

# Standard Library built in python (written in c++)
import time
# Standard Library but not builtin python (written in python)
import os
# Third Party Library (written in python)
import pandas

while True:
    if os.path.exists('temps_today.csv'):
        data = pandas.read_csv('temps_today.csv')
        print(data.mean())  
    else :
        print("file does not exist")
    time.sleep(10)

    