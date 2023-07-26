"""
System under test C is a generic unit with functions (methods) to be called and evaluated.

Please include this on your main testing script to be able to use its functions:
=========================================================================================
SYSTEM C REQUIREMENTS:
*   performTask0 does calculations. It shall return a value LESS THAN 11 
*   performTask1 takes a string "triggerTask1" input. It shall return a boolean EQUAL TO True
*   performTask2 does internal calculations it returns the time it took complete. It shall complete WITHIN 2 seconds
"""
import time

systemUnderTest = "System C"

def timeWait(secondsToWait):
    """
    Standard wait function. Simulates time to process, takes a secondsToWait argument
    """
    print("Please wait ...")
    print("We are working on it")
    for s in range(0,secondsToWait+1):
        print("Time elapsed: ",s*1000," miliseconds")
        time.sleep(1)

def initSystem():
    """
    First function to call to simulate a system being initialized
    """
    print(systemUnderTest," has been called for execution")
    timeWait(1)
    print(systemUnderTest," is running\n")

def performTask0(input):
    """
    REQ: returned value has to be between 100 and 200 for true and GREATER THAN 300 for false
    """
    count = 0
    print(systemUnderTest," performing task 0 with input:", input)
    timeWait(2)
    if input:
        for _ in range(0,199):
            count+=1
    else:
        for _ in range(0,699):
            count+=1
    return count