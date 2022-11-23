
import random
from time import sleep

#Continuing with Part#1 code
def Check_Lock(key, Status_Lock):
    #Type in lock value
    if key == 4 and Status_Lock is False: 
        print("The lock will be locked")
        return True
    #Type in unlock value 
    elif key == 1 and Status_Lock is True:
        print("The lock will be unlocked")
        return False
    else:
        #check the security system
        if (key == 1) or (key == 4): 
            if Status_Lock is True:
                print("Still Locked")
            else:
                print("Still Unlocked")
        return Status_Lock

def Digit(number, n):
    return number


def numDigits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count


def Check_Door(door):
    if door is False:
        print("Unlocked")
    else:
        print("Locked")
    return door

def main():
    secs = 0
    Lock_Status = True # current status of lock
    Rand_Code = random.randint(0,99999) #random values
    print("Code is:",Rand_Code)
    State = numDigits(Rand_Code) - 1  #FSM - current state
    Cur_State = State # current state

    sleep(3)
    print("Part 2")
    while(True): 
        #Check the lock
        if Check_Door(Lock_Status) is False: 
            print(secs, "seconds")
            break

        #Use random generator to enter values one by one
        value = random.randint(0,9)
        key = Digit(Rand_Code, Cur_State)
        secs += 1
        print(" >> ", value)

        if value == key: 
            Cur_State -= 1
        #if sequence is broken
        else: 
            Cur_State = State
        #if code ends
        if Cur_State == -1: 
            rand_val = random.randint(0,9) 
            print("key >> ", rand_val)
            Lock_Status = Check_Lock(rand_val, Lock_Status)
            Cur_State = State 

if __name__ == "__main__":
    main()
