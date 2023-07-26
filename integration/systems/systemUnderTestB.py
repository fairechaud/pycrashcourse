"""
System under test B is a generic unit with functions (methods) to be called and evaluated.

Please include this on your main testing script to be able to use its functions:
=========================================================================================
SYSTEM B REQUIREMENTS:
*   performTask0 does calculations. It shall return a value between 100 and 200 when input is true and GREATER THAN 300 when input is false
*   performTask1 takes a string input = "0x3b2 IgnStatus = RUN". It shall return a string = "0x3b3 IgnStatus = RUN"
"""

import time

systemUnderTest = "System B"

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
    timeWait(2)
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

def performTask1(input):
    """
    REQ: Returns "0x3b3 RUN" value when it receives "0x3b2 RUN"
    """
    print(systemUnderTest," performing task 1")
    if (input == "0x3b2 IgnStatus = RUN"):
        return "0x3b3 IgnStatus = RUN"
    return "0x3b3 IgnStatus = OFF"