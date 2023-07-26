"""
System under test A is a generic unit with functions (methods) to be called and evaluated.

Please include this on your main testing script to be able to use its functions:
=========================================================================================
SYSTEM A REQUIREMENTS:
*   performTask0 does calculations. It shall return a value LESS THAN 11 
*   performTask1 takes a string "triggerTask1" input. It shall return a boolean EQUAL TO True
*   performTask2 does internal calculations it returns the time it took complete. It shall complete WITHIN 2 seconds
"""
import time

systemUnderTest = "System A"

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
    timeWait(5)
    print(systemUnderTest," is running\n")

def performTask0():
    """
    REQ: returned value has to be LESS THAN 11
    """
    count = 0
    print(systemUnderTest," performing task 0")
    timeWait(2)
    for _ in range(0,10):
        count+=1
    return count

def performTask1(input):
    """
    REQ: Returns a True value when it receives "triggerTask1"
    """
    print(systemUnderTest," performing task 1")
    if (input == "triggerTask1"):
        return True
    return False

def performTask2():
    """
    REQ: Returns time it took to complete. It shall complete within 2 seconds
    """
    count = 0
    print(systemUnderTest," performing task 2")
    timeWait(2)
    for i in range(0,5):
        count+=1
    return count
