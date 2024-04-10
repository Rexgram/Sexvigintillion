button_art = (".=-::::::::::::::::::::::::::::::::::::-+.\n"+
              ".#                                      %.\n"+
              ".#            CLICK FOR $$$             %.\n"+
              ".#            =============             %.\n"+
              ".#                                      %.\n"+
              ".=-::::::::::::::::::::::::::::::::::::-+.")

def print_number(x):
    zero = '''
     000  
    0   0 
    0   0 
    0   0 
     000  
    '''
    one = '''
      1   
     11   
      1   
      1   
    11111 
    '''
    two = '''
     222  
    2   2 
       2  
      2   
    22222 
    '''
    three = '''
     333  
    3   3 
      33  
    3   3 
     333  
    '''
    four = '''
    4   4 
    4   4 
    44444 
        4 
        4 
    '''
    five = '''
    55555 
    5     
    5555  
        5 
    5555  
    '''
    six = '''
     666  
    6     
    6666  
    6   6 
     666  
    '''
    seven = '''
    77777 
       7  
      7   
     7    
    7     
    '''
    eight = '''
     888  
    8   8 
     888  
    8   8 
     888  
    '''
    nine = '''
     999  
    9   9 
     9999 
        9 
     999  
    '''

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]

    if 0 <= x <= 99:
        tens_digit = x // 10
        ones_digit = x % 10

        if x >= 10:
            # Split the lines of each digit representation
            tens_lines = digits[tens_digit].split('\n')
            ones_lines = digits[ones_digit].split('\n')
            # Zip the lines together and concatenate them
            for tens_line, ones_line in zip(tens_lines, ones_lines):
                print(tens_line + ones_line)
        else:
            print(digits[ones_digit])
    else:
        print("Number out of range.")
        
from threading import Thread
from time import sleep

number = 0
     
while True:
        number += 1
        sleep(0.5)
        print(print_number(number))