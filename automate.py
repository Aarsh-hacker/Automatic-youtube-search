from pyautogui import click
from time import sleep 
from os import startfile
from keyboard import press
from keyboard import write
import webbrowser
from time import sleep

chrome= 'chrome-browser-path'
print("Type what do you want me to search on youtube!!!!")
website_ame = input("=>")

def SEARCH(website_ame):
    webbrowser.get(chrome).open("https://www.youtube.com/")
    sleep(10)
    click(x=400,y=100)
    write(website_ame)
    sleep(2)
    click(x=950,y=100)

SEARCH(website_ame)