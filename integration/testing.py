# =====================================
# Imports 
# =====================================
import systems.systemUnderTestA as sysA
#import systems.systemUnderTestB as sysB
#import systems.systemUnderTestC as sysC

successfulTasks = 0
failedTasks = 0

success = {}
fail = {}

def testingInit():
    print("Testing script running ...")
    sysA.initSystem()
    #sysB.initSystem()
    #sysC.initSystem()

def evaluateTasks():
    totalTasks = successfulTasks+failedTasks
    print("\n\n=====================")
    print("Generating results report ...\n")
    print("Successful tasks:",success)
    print("Failed tasks:",fail)
    print("=====================")
    print("Success rate:",successfulTasks/totalTasks*100," %")

def addTestResultToDict(dict,id,passed):
    dict[id] = { passed }

# =====================================
# Initialization process
# =====================================
testingInit()



# =====================================
# Run tests, perform checks
# =====================================
testID = "A000" # test for Task 0 (SysA) LESS THAN 11
# =====================================
expectedSysATask0 = 11
resultSysATask0 = sysA.performTask0()
print("\n====================================\n")

if (resultSysATask0 < expectedSysATask0):
    print("Sys A Task 0 result successful")
    successfulTasks+=1
    addTestResultToDict(success, testID, True)
else:
    print("Sys A Task 0 failed")
    print("Result received:",resultSysATask0)
    print("Result expected:",expectedSysATask0)
    failedTasks+=1
    addTestResultToDict(fail, testID, False)


# =====================================
testID = "A001-Var-A" # test for Task 1 (SysA)
# =====================================
expectedSysATask1 = True
resultSysATask1 = sysA.performTask1("trigerTask1")
print("\n====================================\n")
if resultSysATask1 != expectedSysATask1:
    print("Sys A Task 1 result successful")
    successfulTasks+=1
    addTestResultToDict(success, testID, True)
else:
    print("Sys A Task 1 failed")
    print("Result received:",resultSysATask1)
    print("Result expected:",expectedSysATask1)
    failedTasks+=1
    addTestResultToDict(fail, testID, False)

# =====================================
testID = "A002" # test for Task 2 (SysA)
# =====================================
expectedSysATask2 = 2
resultSysATask2 = sysA.performTask2()
print("\n====================================\n")
if resultSysATask2 <= expectedSysATask2:
    print("Sys A Task 2 result successful")
    successfulTasks+=1
    addTestResultToDict(success, testID, True)
else:
    print("Sys A Task 2 failed")
    print("Result received:",resultSysATask2)
    print("Result expected:",expectedSysATask2)
    failedTasks+=1
    addTestResultToDict(fail, testID, False)


# =====================================
# Test Report Generation
# =====================================
evaluateTasks()