import pyfiglet
import termcolor

inp = str(input('ENTER TEXT:'))
inp1 = str(input('ENTER TEXT COLOR:'))

l = inp1.lower()
fl = pyfiglet.figlet_format(inp)

cf = termcolor.colored(fl, l)

print(cf)