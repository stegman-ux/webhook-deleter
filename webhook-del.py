import requests
import colorama
from colorama import Fore
import clear
import os
os.system('pip install clear')
os.system('pip install colorama')
os.system('pip install requests')
clear.clear()

def delet_webhook():
    webhook = input(Fore.BLUE+"[$]entrée l'url du webhook a supprimer : ")
    requests.delete(webhook)
    clear.clear()
    print(Fore.WHITE+'Appuyer sur entrée pour fermer ce terminal..')
    input(Fore.BLUE+'[$]Le webhook a été supprimer avec succées ! ')


ascii_art = Fore.RED+"""
                        $$\       $$\                           $$\                     $$\           $$\ 
                        $$ |      $$ |                          $$ |                    $$ |          $$ |
$$\  $$\  $$\  $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$\          $$$$$$$ | $$$$$$\  $$ |
$$ | $$ | $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$$$$$\ $$  __$$ |$$  __$$\ $$ |
$$ | $$ | $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$$$  / \______|$$ /  $$ |$$$$$$$$ |$$ |
$$ | $$ | $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  _$$<          $$ |  $$ |$$   ____|$$ |
\$$$$$\$$$$  |\$$$$$$$\ $$$$$$$  |$$ |  $$ |\$$$$$$  |\$$$$$$  |$$ | \$$\         \$$$$$$$ |\$$$$$$$\ $$ |
 \_____\____/  \_______|\_______/ \__|  \__| \______/  \______/ \__|  \__|         \_______| \_______|\__|
"""
print(ascii_art)
delet_webhook()

# simple py script
# you can make this script in just 7 lines but for the style, I made more lines
