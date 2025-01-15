#IMPORTS --------------
import os
import json
import time 
from colorama import Fore, Style, init

init(autoreset=True)
directory = os.getcwd()
class MENU:
    def __init__(self):
        
        self.options = {
            "1": self.select_theme,
            "2": self.theme_maker,
            "3": self.reset_to_default,
            "4": self.select_logo,
            "5": self.show,
            "6": self.salir,
        }

#MENU --------------

    def menu(self):
        os.system('clear')
        os.system(f'echo "{fast.load_json()}" | lolcat')
        while True:
            fast.load_json()
            print(Fore.CYAN + "Wellcome to the Faster Wizard, please select an option from below.")
            print(Fore.GREEN + "1 - Select from default themes" + Fore.RESET + "   " + Fore.YELLOW + "2 - Theme maker")
            print(Fore.RED + "3 - Reset to default" + Fore.RESET + "             " + Fore.MAGENTA + "4 - Select logo")
            print(Fore.BLUE + "5 - Show my configuration" + Fore.RESET + "        " + Fore.WHITE + "6 - Exit")
            number_option = input(Fore.CYAN + "#: " + Fore.RESET)
            action = self.options.get(number_option)
            if action:
                action()
            else:
                print(Fore.RED + "Invalid option" + Fore.RESET)

#SELECT THEME --------------

    def select_theme(self):
        while True:
            os.system('clear')
            content = os.listdir(os.getcwd()+"/default_themes")
            print(Fore.RED + "0. Exit")
            for index, item in enumerate(content, 1):
                print(Fore.YELLOW + f"{index}.{item.replace('.jsonc', '')}")
            print(Fore.BLUE + "Select a theme for preview\nPlease use fullscreen for a better look\n" + Fore.RESET)

    #VISUALIZE THEME --------------
            data = {str(idx): i for idx, i in enumerate(content, 1)}
            theme = input("\n#: ")

            if theme == "":
                print(Fore.RED + "Invalid option" + Fore.RESET)
                time.sleep(0.5)
                self.select_theme()
            elif theme == "0":
                fast.menu()
            elif theme not in data:
                print(Fore.RED + "Invalid option" + Fore.RESET)
                time.sleep(0.5)
                self.select_theme()
                
            
            directory = os.getcwd()
            os.system(f'fastfetch -c {directory}/default_themes/{data[theme]}')

            print("¿Apply Theme?")
            apply_theme = input("1 - Yes\n2 - No\n#: ")
            
            if apply_theme == "1":
                print("Applying theme...")
                time.sleep(1)
                os.system('clear')
                id = data[theme]
                os.system(f'rm ~/.config/fastfetch/config.jsonc')
                time.sleep(0.5)
                os.system(f'cp default_themes/{id} ~/.config/fastfetch/')
                time.sleep(0.5)
                os.system(f'mv ~/.config/fastfetch/{id} ~/.config/fastfetch/config.jsonc')
                print("Theme applied! Check your terminal.")
                time.sleep(1.5)
                fast.menu()
                try:
                    with open(theme) as file:
                        data = json.load(file)
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
        print("1 - Change color")
        theme = input("#: ")

#THEME RESET --------------

    def reset_to_default(self):
        os.system('clear')
        print(Fore.RED + "Are you sure you want to reset to default? (y/n)." + Fore.RESET)
        theme = input(Fore.CYAN + "#: " + Fore.RESET)
        if theme == "y":
            print(Fore.YELLOW + "Reseting to default..." + Fore.RESET)
            os.system('fastfetch --gen-config-force')
            time.sleep(1)
            os.system('fastfetch')
            print(Fore.GREEN + "Reset completed." + Fore.RESET)
        else:
            print(Fore.YELLOW + "Returning to menu..." + Fore.RESET)
            time.sleep(1)
            os.system('clear')
            fast.menu()

#LOGO SELECT --------------

    def select_logo(self):
        os.system('clear')
        print(Fore.GREEN + "1 - Logo list" + Fore.RESET + "\n" + Fore.YELLOW + "2 - Show all logos in terminal" + Fore.RESET + "\n" + Fore.CYAN + "3 - Select path to custom image or ASCII." + Fore.RESET)
        theme = input(Fore.CYAN + "#: " + Fore.RESET)

        if theme == "1":
            os.system('clear')
            os.system('fastfetch --list-logos')
            print(Fore.BLUE + "Select a logo number from the list." + Fore.RESET)
            logo = input(Fore.CYAN + "#: " + Fore.RESET)
        
        elif theme == "2":
            os.system('clear')
            os.system('fastfetch --print-logos')
            print(Fore.BLUE + "Press enter to return to the menu." + Fore.RESET)
            input()
            self.menu()

        elif theme == "3":
            os.system('clear')
            print(Fore.BLUE + "Select path to custom image or ASCII.\nIf the path incorrect, the default logo will be used.\nIf you select an image you need a terminal that can support it." + Fore.RESET)
            logo = input(Fore.CYAN + "#: " + Fore.RESET)
            os.system(f'fastfetch --logo {logo}')

        else:
            self.select_logo()

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
    
#EXIT --------------

    def salir(self):
        print(Fore.RED + "Exiting..." + Fore.RESET)
        exit()

#SHOW CURRENT CONFIGURATION --------------

    def show(self):
        os.system('clear')
        print("Your current configuration is:")
        os.system('fastfetch')
        print(Fore.BLUE+"Press enter to return to the menu.")
        input()
        fast.menu()

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
    