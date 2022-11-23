#Lock Check Method
import random
from time import sleep

# using the same code from part 1 to solidify the same problem
def Check_Lock(key, Status_Lock):
    if key == 4 and Status_Lock is False: #putting in the lock value and the lock is unlocked
        print("The lock will be locked")
        return True
    elif key == 1 and Status_Lock is True: #putting in the unlock value and the lock is locked
        print("The lock will be unlocked")
        return False
    else:
        if (key == 1) or (key == 4): #to check if security system is all good.
            if Status_Lock is True:
                print("Still Locked")
            else:
                print("Still Unlocked")
        return Status_Lock

def Digit(number, n):
    return number // 10**n % 10


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
    # variables
    secs = 0
    Lock_Status = True # current status of lock
    Rand_Code = random.randint(0,99999) #random code values
    print("Code is:",Rand_Code)
    State = numDigits(Rand_Code) - 1  # Current state in FSM
    Cur_State = State # current state

    sleep(3)
    #Main method
    print("Part 2")
    while(True): 
        
        if Check_Door(Lock_Status) is False: #Checking the lock
            print(secs, "seconds")
            break

        # enter value in one at a time and this is using the random generator
        value = random.randint(0,9)
        key = Digit(Rand_Code, Cur_State)
        secs += 1
        print(" >> ", value)

        if value == key: #if the the nth digit in key matched in sequence
            currState -= 1
        else: #if you break the sequence
            Cur_State = State

        if Cur_State == -1: #if you reach end of code
            rand_val = random.randint(0,9) # random values
            print("key >> ", rand_val)
            Lock_Status = Check_Lock(rand_val, Lock_Status)
            Cur_State = State 


if __name__ == "__main__":
    main()
