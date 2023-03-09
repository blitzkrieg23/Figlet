from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    font = sys.argv[2]
    if font not in figlet.getFonts():
        sys.exit('Invalid usage')
    figlet.setFont(font=font)
elif len(sys.argv) != 1:
    sys.exit('Invalid usage')
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))

user_input = input('Input: ')
print("Output:")
print(figlet.renderText(user_input))
