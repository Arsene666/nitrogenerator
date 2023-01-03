import time
import random 
import string
import pyautogui

def nitroGenerator(amount):
    x=0
    while x< amount:
        length=19
        d="discord.gift/"
        upper=string.ascii_uppercase
        lower=string.ascii_lowercase
        digits=string.digits
        generator=upper+lower+digits
        nGenerator="".join(random.sample(generator,length))
        fully=d+nGenerator+"\n"
        print(fully)
        x=x+1

#"Write the amount of codes you want generated in the functions parameter. Must be a int"
nitroGenerator(5)
