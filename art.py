button_art = '''
.=-::::::::::::::::::::::::::::::::::::-+.
.#                                      %.
.#            CLICK FOR $$$             %.
.#            =============             %.
.#                                      %.
.=-::::::::::::::::::::::::::::::::::::-+.
        '''

def print_number(x):
    button_art = '''
.=-::::::::::::::::::::::::::::::::::::-+.
.#                                      %.
.#            CLICK FOR $$$             %.
.#            =============             %.
.#                                      %.
.=-::::::::::::::::::::::::::::::::::::-+.
        '''
    
    dec = '''
          
          
    ::::: 
    ::::: 
    ::::: 
    '''

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
    22222 
        2 
    22222 
    2     
    22222 
    '''
    three = '''
    33333 
        3 
     3333 
        3 
    33333 
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

    if 0 <= x <= 999:
        hundreds_digit = x // 100
        tens_digit = (x % 100) // 10
        ones_digit = x % 10

        if x >= 100:
            # Split the lines of each digit representation
            button_lines = button_art.split('\n')
            hundred_lines = digits[hundreds_digit].split('\n')
            tens_lines = digits[tens_digit].split('\n')
            ones_lines = digits[ones_digit].split('\n')
            # Zip the lines together and concatenate them
            for buttons_art, hundreds_line, tens_line, ones_line in zip(button_lines, hundred_lines, tens_lines, ones_lines):
                print(buttons_art + hundreds_line + tens_line + ones_line)
        elif x >= 10:
            # Split the lines of each digit representation
            button_lines = button_art.split('\n')
            tens_lines = digits[tens_digit].split('\n')
            ones_lines = digits[ones_digit].split('\n')
            # Zip the lines together and concatenate them
            for buttons_art, tens_line, ones_line in zip(button_lines, tens_lines, ones_lines):
                print(buttons_art + tens_line + ones_line)
        else:
            # Print ASCII art for ones place
            ones_lines = digits[ones_digit].split('\n')
            for line in ones_lines:
                print(line)
    elif x >= 1000:
        # Print in thousands format
        thousands_digit = x // 1000
        hundreds_digit = x % 1000 // 100
        # Split the lines of each digit representation
        dec_lines = dec.split('\n')
        button_lines = button_art.split('\n')
        thousands_lines = digits[thousands_digit].split('\n')
        hundreds_lines = digits[hundreds_digit].split('\n')
        for buttons_art, thousands_line, dot, hundreds_line in zip(button_lines, thousands_lines, dec_lines, hundreds_lines):
                print(buttons_art + thousands_line + dot + hundreds_line)
        #print("K")
    else:
        print("Number out of range.")