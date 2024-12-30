import os
import json


class MENU:
    def __init__(self):
        self.options = {
            "1": self.select_theme,
            "2": self.theme_maker,
            "3": self.reset_to_default,
            "4": self.select_image,
            "5": self.salir,
        }

    def menu(self):
        while True:
            number_option = input("#: ")
            action = self.options.get(number_option)
            if action:
                action()
            else:
                print("Option not valid")

    def select_theme(self):
        
        content = os.listdir(os.getcwd()+"/Faster/default_themes")
        for index, item in enumerate(content, 1):
            print(f"{index}.{item.replace(".jsonc", "")}")
        theme = input("\n#: ")
        os.system('fastfetch -c /home/d4mag3/Documentos/Programacion/Back/Faster/default_themes/all.jsonc')
        try:
            with open(theme) as file:
                data = json.load(file)
                print("Theme loaded:", data)

                
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")

    def theme_maker(self):
        print("1. Change color")
        theme = input("#: ")

    def reset_to_default(self):
        print("Are you sure you want to reset to default? (y/n)")
        theme = input("#:S ")

    def select_image(self):
        print("Select image")
        theme = input("#: ")

    def load_json(self) -> dict:
        try:
            with open('/home/d4mag3/Documentos/Programacion/Back/Faster/Banners/banner.json') as f:
                return json.load(f)["logo"]["string"]
        
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
        #os.system('clear')

    def __str__(self):
        return "Faster Class"


if __name__ == "__main__":
    fast = Faster()
    fast.menu()
