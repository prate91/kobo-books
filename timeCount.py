import time

def startTime():
    ora = time.asctime( time.localtime(time.time()))
    print ("START: " + ora)
    millis0 = int(time.time())
    return millis0

def getTime(time0):
    millis = int(time.time())
    timeExecution = millis-time0
    return timeExecution