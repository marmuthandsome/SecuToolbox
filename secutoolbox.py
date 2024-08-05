# main.py
from menu import print_menu, display_menu, get_user_choice, handle_choice

def main():
    print_menu()
    while True:
        display_menu()
        choice = get_user_choice()
        if not handle_choice(choice):
            break

if __name__ == "__main__":
    main()
