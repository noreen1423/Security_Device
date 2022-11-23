# Programming Assignment CS330
* **Requirements**

Think of simulating a security installation very similar to those installed in many offices and homes. The installation has a keypad and an engine (a controller) used to decide whether the user has entered the correct access code or not.

The keypad has ten keys, labeled from '0' to '9'. The security engine will unlock the lock when it finds the correct un-locking access code in the input string. Likewise, the security engine will lock the lock when it finds the correct locking access code in the input string.

For example, let's assume that the un-locking code is 33441. If the user enters the string 91352033441245, then the lock will be unlocked as soon as the engine finds the last correct letter of the access code in the input string. The engine will lock the lock again when the user enters the locking code. Assuming that the locking code is 33444 then the lock will be locked and unlocked as described below:

913520**33441**(unlock)24510**33444**(lock)123970001112**334451**(unlock)334410101
                  

DDDDD1 is the unlocking code DDDDD4 is the locking code, where DDDDD are the least significant five digits in your student ID A20502963. As soon as the last digit of the access code is entered, your program will signal the action taken (lock or unlock).

* **Cloning the Repository** 
We have to clone the repository to run the program using
    * ```git clone https://github.com/noreen1423/Programming_Assignment_CS330.git```
  
Run the program on Linux system using Python3. 
    * ```python3 part1.py```
    * ```python3 part2.py```
  
  
## Tested Platform
The code has been tested on linux platform. The code gives the desired results if valid input is entered and it gives an error if invalid input is entered. 
  
  
  
 
