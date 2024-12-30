#IMPORTS --------------
import os
import json
import time 
from colorama import Fore

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
        os.system(f'echo "{fast.load_json()}" | lolcat')
        while True:
            fast.load_json()
            print("""1 - Select from default themes
2 - Theme maker
3 - Reset to default
4 - Select image
5 - Exit""")
            number_option = input("#: ")
            action = self.options.get(number_option)
            if action:
                action()
            else:
                print("Option not valid")

#APLY THEMES  --------------

#SELECT THEME --------------

    def select_theme(self):
        
        content = os.listdir(os.getcwd()+"/default_themes")
        for index, item in enumerate(content, 1):
            print(f"{index}.{item.replace(".jsonc", "")}")

#VISUALIZE THEME --------------
        data = {str(idx): i for idx, i in enumerate(content, 1)}
        theme = input("\n#: ")
        directory = os.getcwd()
        
        os.system(f'fastfetch -c {directory}/default_themes/{data[theme]}')
        
        print("¿Apply Theme?")
        apply_theme = input("1 - Yes\n2 - No\n#: ")
        
        if apply_theme == "1":
            print("Theme applied.")
            time.sleep(1.5)

            os.system(f'~/.config/fastfetch/config.jsonc')
            fast.menu()
        else:
            print("Theme not applied.") 
    
        try:
            with open(theme) as file:
                data = json.load(file)
                 
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")
            
        

#THEME MAKER --------------

    def theme_maker(self):
        print("1. Change color")
        theme = input("#: ")

#THEME RESET --------------

    def reset_to_default(self):
        print("Are you sure you want to reset to default? (y/n)")
        theme = input("#:S ")

#IMAGE SELECT --------------

    def select_image(self):
        print("Select image")
        theme = input("#: ")

#JSON LOAD BANNER --------------

    def load_json(self) -> dict:
        try:
            directory = os.getcwd()
            with open(directory+'/Banners/banner.json') as f:
                return (json.load(f)["logo"]["string"])
        
        except FileNotFoundError:
            print("File not found.")

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
