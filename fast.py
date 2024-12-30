import os
import json

def load_json(file):
    with open('banner.jsonc',encoding='utf-8') as f:
        return json.load(f)

def main():
    while True:
        print(load_json())
        print("¡Wellcome to Fast!, Select an option:")
        print("1. View and select integrated themes")
        print("2. Theme maker")
        print("3. Reset to default fastfetch theme")
        print("4. Select image")
        print("5. Exit")
        print("!You can summit your own theme! For more details visit the repository and go to Summit section.")
        
        option = input("#:")

        if option == '1':
            os.system('clear')
            select_theme()
        elif option == '2':
            os.system('clear')
            theme_maker()
        elif option == '3':
            os.system('clear')
            reset_to_default()
        elif option == '4':
            os.system('clear')
            select_image()
        elif option == '5':
            os.system('clear')
            print("Exit")
            break
        else:
            os.system('clear')
            print("Invalid option")

#Opcion 1
def select_theme():
    # Esto se debe hacer con Json
    print("1. Default")
    theme = input("#:")

#Opcion 2
def theme_maker():
    # Esto se debe hacer con Json
    print("1. Change color")
    theme = input("#:")

#Opcion 3
def reset_to_default():
    print("Are you sure you want to reset to default? (y/n)")
    theme = input("#:")

#Opcion 4
def select_image():
    print("Select image")
    theme = input("#:")

if __name__ == "__main__":
    main()