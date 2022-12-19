from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except:
            error=error+1
    return error

def speedTime(timeS,timeE,userinput):
    timeDelay=timeE-timeS 
    timeR=round(timeDelay,2)
    speed=len(userinput)/timeR 
    return round(speed)

test=["Update the salary of an employee using a stored procedure",
      "Before updating check whether the employee id exists or not",
      "If successfully updated, fire a trigger which enters the date"]
test1=r.choice(test)
print("***** Typing Speed *****")
print()
print(test1)
print()
print()
time_1=time()
testinput=input(" Type Exactly same as above line : ")
time_2=time()

print('Speed: ',speedTime(time_1,time_2,testinput),"w/sec")
print('Eror: ',mistake(test1,testinput))