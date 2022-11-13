import time
class StopWatch:
    def __init__(self):
        self.startTime = 0
        self.stopTime = 0
        self.running = False

    def start(self):
        self.startTime = time.time()
        self.running = True
    
    
    def stop(self):
        self.stopTime = time.time()
        self.running = False
    

    # Elaspsed time in seconds
    def getElapsedTime(self):
        elapsed = 0
        if (self.running):
            elapsed = (time.time() - self.startTime)
        
        else:
            elapsed = (self.stopTime - self.startTime)
        
        return elapsed
    
        
    #/* Elaspsed time in milliseconds */
    def getElapsedTimeSecs(self):
        elapsed = 0
        if (self.running): 
            elapsed = ((time.time() - self.startTime) * 1000)
        
        else :
            elapsed = ((self.stopTime - self.startTime) * 1000)
        
        return elapsed