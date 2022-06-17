import time
def countdownTimer(n):
    if n==0:#base condition
        print(n,"Times up!")
    else:    
        print(n)   
        time.sleep(1) #pause for 1 sec
        return countdownTimer(n-1) #recursive call
secs=5
print(f"Counting down from {secs}") #formatted display
countdownTimer(secs)