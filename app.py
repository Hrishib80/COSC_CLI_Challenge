from __future__ import print_function, unicode_literals
from pyfiglet import Figlet
import colorama
from termcolor import colored, cprint
from InquirerPy import prompt 

colorama.just_fix_windows_console()
#Fonts: big, bulbhead, block, chunky, contessa, crawford, (cyberlarge, cybermedium, cybersmall), nvscript, ogre, puffy
root = Figlet(font='ogre',justify='center', width=120)

#Fore
""" 
black, red, green, yellow, blue, magenta, cyan, white,
light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
light_magenta, light_cyan.
 """

#Back
""" 
on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
on_light_blue, on_light_magenta, on_light_cyan.

 """

#attrs
""" 
    bold, dark, underline, blink, reverse, concealed.
 """

print(colored(root.renderText("Temperatur Converter"), color='magenta', attrs=['bold', 'blink']))


def conversion(response):
    temp = float(response['tempt'])
    if(response['type_of_conversion'] == 'Celcius to Fahrenheit'):
        temp = (temp*(9/5)) + 32
        cprint(f"The temperature in Farenheit is {temp}", color='green',attrs=['bold'])
    else:
        temp = (temp-32)*(5/9)
        cprint(f"The temperature in Celcius is {temp}", color='green',attrs=['bold'])

question = [
        {
            'type': 'list',
            'name': 'type_of_conversion',
            'message': 'Celcius -> Fahrenheit (or) Fahrenheit -> Celcius ?',
            'choices':
            [
                'Celcius to Fahrenheit', 'Fahrenheit to Celcius'
            ]
        },

        {
            'type':'input',
            'name':'tempt',
            'message':'Type the temperature for conversion: '
        }
]

response = prompt(question)
conversion(response)