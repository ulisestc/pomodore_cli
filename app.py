import time, os

POMODORE_TIME_DEFAULT = 25
SHORT_REST_TIME_DEFAULT = 5
LONG_REST_TIME_DEFAULT = 15
NUMBER_OF_ROUNDS_DEFAULT = 4

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    is_default = "Y"
    is_default = input("""
                        Welcome to pomodore CLI, do you want to use default settings?
                        (Y/n)
                        """)
    
    if is_default == "": is_default = "Y" # si no se elige nada => Y, como si fuera linux
    clear_terminal()
    # DEBUG
    # print(f"is_default:{is_default}")

    if is_default == "n":
        exit = False
        while not exit:
            option_to_modify = input("""
                                        What timer do you want to modify?
                                        1. Focus time (25 mins)
                                        2. Short rest (5 mins)
                                        3. Long Rest (15 mins)
                                        4. Number of rounds
                                        5. Exit
                                    """)
            if option_to_modify > 5 or option_to_modify < 1:
                clear_terminal()
            
            # ESTP SE PUEDE SUPER OPTIMIZAR
            if option_to_modify == 1: 
                # POMODORE_TIME_DEFAULT = input("Focus time:")
                ans = input("Focus time:")
                if ans.isnumeric():
                    POMODORE_TIME_DEFAULT = ans
                else:
                    print("Enter a number, please.")
            elif option_to_modify == 2: 
                SHORT_REST_TIME_DEFAULT = input("Short rest:")
            elif option_to_modify == 3: 
                LONG_REST_TIME_DEFAULT = input("Long rest:")
            elif option_to_modify == 4: 
                NUMBER_OF_ROUNDS_DEFAULT = input("# of rounds:")
            elif option_to_modify == 5: 
                exit = True
        # if option_to_modify != 1 and option_to_modify != 2 and option_to_modify != 3 and option_to_modify and 4:
        # else:
        #     print()
    else: 
        print(f"""Using default values:
            FOCUS: {POMODORE_TIME_DEFAULT}
            REST: {SHORT_REST_TIME_DEFAULT}
            LONG_REST: {LONG_REST_TIME_DEFAULT}
            ROUNDS: {NUMBER_OF_ROUNDS_DEFAULT}
        """)





if __name__ == '__main__':
    main()


# SOURCES:
#  ESTE PROYECTO TIENE COMO PRINCIPAL OBJETIVO EL AFIANZAR MIS CONOCIMIENTOS Y LÓGICA DE PROGRAMACIÓN MEDIANTE
#  LA INVESTIGACIÓN PROPIA DE MANERA PRAGMÁTICA, PARA MEDIR CUANTITATIVAMENTE ANOTARÉ TODA FUENTE DE CONSULTA 
#     26/11/2025
#     https://www.programiz.com/python-programming/main-function
#     https://www.geeksforgeeks.org/python/python-or-operator/ 