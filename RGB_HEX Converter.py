def rgb_hex():
  invalid_msg = "The value you entered is not valid"
  red = int(raw_input("enter red (R) value: "))
  if red > 255 or red < 0:
    print invalid_msg
  green = int(raw_input("enter green (G) value: "))  
  if green > 255 or green < 0:
    print invalid_msg
  blue = int(raw_input("enter blue (B) value: "))  
  if blue > 255 or blue < 0:
    print invalid_msg
  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()
  
def hex_rgb():
  hex_val = raw_input("Enter hex value: ")	
  if hex_val.length != 6:
    print invalid_msg
  else: 
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  
  
  print "Red: %s Green: %s Blue: %s" % (red, green, blue)
  
def convert():
  while True:
    option = "Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:"
    if option == "1":
      print "RBG to Hex..."
      rgb_hex()
    elif option == "2":
      print "Hex to RGB..."
      hex_rgb()
    elif option == "X" or option == "x":
      break
    else:
      print "Error"
  
convert()