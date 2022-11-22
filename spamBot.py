from time import sleep

from pynput.mouse import Button
from pynput.keyboard import Key


from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()



i = int(input('How Much Spam?: '))



while i != 0:
    mouse.position = ()
    #Pixel coordinates of the writing field on your screen
    sleep(0.05)

    mouse.click(Button.left, 1)
    sleep(0.05)

    keyboard.type('Spam')
    sleep(0.05)

    mouse.position = ()
    #Pixel coordinates of the sending button on your screen
    sleep(0.05)

    mouse.click(Button.left, 1)

    i -= 1







