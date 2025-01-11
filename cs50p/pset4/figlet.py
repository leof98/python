'''
Prompts the user for a str of text
Outputs that text in the desired font.
11.22
'''
import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 2:
    sys.exit('Invalid usage')

if len(sys.argv) == 1:
    inp = str(input('Input: '))
    figlet.setFont(font=random.choice(font_list))
    print(figlet.renderText(inp))

elif len(sys.argv) == 3:
    if sys.argv[2] not in font_list:
        sys.exit('Invalid usage')
        
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        inp = str(input('Input: '))
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(inp))
    else:
        sys.exit('Invalid usage')
