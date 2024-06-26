def handle(x):
  import art
  if 0 <= x <= 999999:
    hundreds_digit = x // 100
    tens_digit = (x % 100) // 10
    ones_digit = x % 10

    if x >= 100000:
      # Print in thousands format
      hundreds_digit = x // 100000
      tens_digit = x % 100000 // 10000
      ones_digit = (x % 100000 % 10000) // 1000
      tenths_digit = x % 100000 % 10000 % 1000 // 100
      # Split the lines of each digit representation
      dec_lines = art.dec.split('\n')
      button_lines = art.button_art.split('\n')
      hundreds_lines = art.digits[hundreds_digit].split('\n')
      tens_lines = art.digits[tens_digit].split('\n')
      ones_lines = art.digits[ones_digit].split('\n')
      tenths_lines = art.digits[tenths_digit].split('\n')
      for i, (buttons_art, hundreds_line, tens_line, ones_line, dot, tenths_line) in enumerate(zip(
    button_lines, hundreds_lines, tens_lines, ones_lines, dec_lines,
    tenths_lines)):
        if i == 5:
          print(buttons_art + hundreds_line + tens_line + ones_line + dot + tenths_line, "K")
        else:
          print(buttons_art + hundreds_line + tens_line + ones_line + dot + tenths_line)
    elif x >= 10000:
      # Print in thousands format
      tens_digit = x // 10000
      ones_digit = x % 10000 // 1000
      tenths_digit = (x % 10000 % 1000) // 100
      # Split the lines of each digit representation
      dec_lines = art.dec.split('\n')
      button_lines = art.button_art.split('\n')
      tens_lines = art.digits[tens_digit].split('\n')
      ones_lines = art.digits[ones_digit].split('\n')
      tenths_lines = art.digits[tenths_digit].split('\n')
      for buttons_art, tens_line, ones_line, dot, tenths_line in zip(
          button_lines, tens_lines, ones_lines, dec_lines,
          tenths_lines):
        print(buttons_art + tens_line + ones_line + dot + tenths_line)
    elif x >= 1000:
      # Print in thousands format
      thousands_digit = x // 1000
      hundreds_digit = x % 1000 // 100
      # Split the lines of each digit representation
      dec_lines = art.dec.split('\n')
      button_lines = art.button_art.split('\n')
      thousands_lines = art.digits[thousands_digit].split('\n')
      hundreds_lines = art.digits[hundreds_digit].split('\n')
      for buttons_art, thousands_line, dot, hundreds_line in zip(
          button_lines, thousands_lines, dec_lines, hundreds_lines):
        print(buttons_art + thousands_line + dot + hundreds_line)
    elif x >= 100:
      # Split the lines of each digit representation
      button_lines = art.button_art.split('\n')
      hundred_lines = art.digits[hundreds_digit].split('\n')
      tens_lines = art.digits[tens_digit].split('\n')
      ones_lines = art.digits[ones_digit].split('\n')
      # Zip the lines together and concatenate them
      for buttons_art, hundreds_line, tens_line, ones_line in zip(
          button_lines, hundred_lines, tens_lines, ones_lines):
        print(buttons_art + hundreds_line + tens_line + ones_line)
    elif x >= 10:
      # Split the lines of each digit representation
      button_lines = art.button_art.split('\n')
      tens_lines = art.digits[tens_digit].split('\n')
      ones_lines = art.digits[ones_digit].split('\n')
      # Zip the lines together and concatenate them
      for buttons_art, tens_line, ones_line in zip(button_lines, tens_lines,
                                                   ones_lines):
        print(buttons_art + tens_line + ones_line)
    else:
      # Print ASCII art for ones place
      ones_lines = art.digits[ones_digit].split('\n')
      for line in ones_lines:
        print(line)
  else:
    print("Number out of range.")


handle(123456)
