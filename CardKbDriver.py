from machine import Pin, I2C
from time import sleep_ms
 
i2c = I2C(1, scl=Pin(7), sda=Pin(6))
cardkb = i2c.scan()[0]  # should return 95
if cardkb != 95:
    print("!!! Check I2C config: " + str(i2c))
    print("!!! CardKB not found. I2C device", cardkb,
          "found instead.")
    exit(1)
 
ESC = chr(27)
NUL = '\x00'
CR = "\r"
LF = "\n"
c = ''
 
print("*** APPALLING TYPEWRITER ***")
print("** Type stuff, Esc to end **")
 
while (c != ESC):
    # returns NUL char if no character read
    c = i2c.readfrom(cardkb, 1).decode()
    if c == CR:
        # convert CR return key to LF
        c = LF
    if c != NUL or c != ESC:
        print(c, end='')
    sleep_ms(5)
