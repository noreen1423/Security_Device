#PART 1
def Lock(key, Status_Lock):
    #Type in lock value
    if key == 4 and Status_Lock is False: 
        print("The device will be locked")
        return True
    #Type in unlock value
    elif key == 1 and Status_Lock is True: 
        print("The device will be unlocked")
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
    return number[n]


def main():
    #student ID = A20502963
    Code = "02963" 
    # current status of the lock
    Lock_Status = True 
    State = 0  #FSM - current status

    print("Part 1")

    while(True): 
        #Enter a value one by one
        value = input(">> ")
        key = Digit(Code, State)

        #if sequence is matched
        if value is key: 
            State += 1
        #if sequence is broken
        else: 
            State = 0
        #if code ends
        if State == 5: 
            Val = int(input("key >> "))
            Lock_Status = Lock(Val, Lock_Status)
            State = 4 


if __name__ == "__main__":
    main()
