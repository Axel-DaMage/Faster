import os
import json


class MENU:
    def __init__(self):
        self.options = {
            "1": self.select_theme,
            "2": self.theme_maker,
            "3": self.reset_to_default,
            "4": self.select_image,
            "5": self.salir
    }

    def menu(self):
        while True:
            number_option = input("#:")
            action = self.options.get(number_option)
            if action:
                action()
            else:
                print("Option not valid")

    def select_theme(self):
        print("1. Default")
        theme = input("#:")
        with open(theme) as file:
            file = json.load(file)


    def theme_maker(self):
        print("1. Change color")
        theme = input("#:")

    def reset_to_default(self):
        print("Are you sure you want to reset to default? (y/n)")
        theme = input("#:")

    def select_image(self):
        print("Select image")
        theme = input("#:")
        
    def load_json(sefl) -> dict:
        with open('/home/d4mag3/Documentos/Programacion/Back/Faster/Json/banner.json') as f:
            return json.load(f)["logo"]["string"]
        
    def salir(self):
        exit()

    def __str__(self):
        pass
        
class Faster(MENU):

    def __init__(self):
        super().__init__()
        os.system('clear')
        super().load_json()

    def menu(self):
        super().menu()

    def select_theme(self):
        super().select_theme()
        
    def theme_maker():
        super().theme_maker()
        
    def reset_to_default(self):
        super().reset_to_default()
        
    def select_image(self):
        super().select_image()
    
    def __str__(self):
        pass

fast = Faster()
fast.menu()

if __name__ == "__main__":
    main()