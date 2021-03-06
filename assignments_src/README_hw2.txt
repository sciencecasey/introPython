Casey Richards 
Intro to Programming with Python, Module 2
Homework 2
Approach: I used the base class of python input and print commands to prompt the user to enter their 
interest rate, principle, and loan period to calculate the total interest paid and total amount paid. 
Next I used the same commands to calculate the interest rate given the total paid and the principle. 
The assignment was coded in a miniconda environment through Pycharm IDE.  
The program runs successfully through command line with the prompt:

python3 interest.py

python3 rate.py

*Note that if you are not in the directory the script is located you will need to run with the full path to file as below\

python3 <path to file >


There is a bug in the rate.py file, as the interest rate calculator is not accurate.  First, the calculation seemed to be off by a factor of 10, so that was added to the calculation, but algebraically shouldn't be happening. 
I checked the calculation with another who also didn't see an issue, so it may be a prioritization issue that I couldn't figure out through rewriting.  

Even without the factor of 10, the rate calculator is imprecise, likely due to the fact that I formatted the double in the interest.py, so the double value was cut off after 2 decimals as well as the way that Python stores doubles in memory.  