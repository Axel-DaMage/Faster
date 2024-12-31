#IMPORTS --------------
import os
import json
import time 
from colorama import Fore
directory = os.getcwd()
class MENU:
    def __init__(self):
        
        self.options = {
            "1": self.select_theme,
            "2": self.theme_maker,
            "3": self.reset_to_default,
            "4": self.select_image,
            "5": self.salir,
        }

#MENU --------------

    def menu(self):
        os.system('clear')
        os.system(f'echo "{fast.load_json()}" | lolcat')
        while True:
            fast.load_json()
            print("1 - Select from default themes\n2 - Theme maker\n3 - Reset to default\n4 - Select image\n5 - Exit")
            number_option = input("#: ")
            action = self.options.get(number_option)
            if action:
                action()
            else:
                print("Option not valid")

#APPLY THEMES  --------------

#SELECT THEME --------------

    def select_theme(self):
        while True:
            os.system('clear')
            content = os.listdir(os.getcwd()+"/default_themes") #No mover ruta
            print("Select a theme for preview\nPlease use fullscreen for a better look\n")
            print("0 - Exit")
            for index, item in enumerate(content, 1):
                print(f"{index}.{item.replace(".jsonc", "")}")

    #VISUALIZE THEME --------------
            data = {str(idx): i for idx, i in enumerate(content, 1)}
            theme = input("\n#: ")

            if theme == "0":
                fast.menu()
            directory = os.getcwd()
            
            os.system(f'fastfetch -c {directory}/default_themes/{data[theme]}') #No mover ruta
            
            print("¿Apply Theme?")
            apply_theme = input("1 - Yes\n2 - No\n#: ")
            
            if apply_theme == "1":
                try:
                    with open(theme) as file:
                        data = json.load(file)
                        print("Theme applied.")
                        time.sleep(1)
                        os.system('clear')
                        #os.system(f'nano ~/.config/fastfetch/config.jsonc') #No mover ruta solo comando
                        fast.menu()
                        os.system('clear')
                except FileNotFoundError:
                        self.select_theme()
                except json.JSONDecodeError:
                        print("Invalid JSON format.")
            else:
                print("Theme not applied.")
                time.sleep(1)
                os.system('clear')
                
        

#THEME MAKER --------------

    def theme_maker(self):
        os.system('clear')
        print("1. Change color")
        theme = input("#: ")

#THEME RESET --------------

    def reset_to_default(self):
        os.system('clear')
        print("Are you sure you want to reset to default? (y/n)")
        theme = input("#:S ")

#IMAGE SELECT --------------

    def select_image(self):
        os.system('clear')
        print("Select image")
        theme = input("#: ")

#JSON LOAD BANNER --------------

    def load_json(self) -> dict:
        try:
            directory = os.getcwd()
            with open(directory+'/Banners/banner.json') as f: #No mover ruta 
                return (json.load(f)["logo"]["string"])
        
        except FileNotFoundError:
            print("File not found.")
            print(directory)

        except json.JSONDecodeError:
            print("Invalid JSON format.")
        return {}

    def salir(self):
        print("Exiting program.")
        exit()

    def __str__(self):
        return "MENU Class"


class Faster(MENU):
    def __init__(self):
        super().__init__()
        os.system('clear')
        

    def __str__(self):
        return "Faster Class"


if __name__ == "__main__":
    fast = Faster()
    fast.menu()
    