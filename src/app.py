import time, os
import readchar
import shutil
import math

from handle_config import config_handler

columns = shutil.get_terminal_size().columns

def print_centered(text):
    separated_lines = text.splitlines()
    for line in separated_lines:
        print(line.center(columns))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_program():
    print_centered("Press any key to continue...")
    readchar.readkey()
    clear_terminal()

def run_timer(timer, message):
    for i in range(timer): 
        clear_terminal()
        print_centered(message)
        print_centered(f"Time left: {timer} seconds.")
        time.sleep(1)
        timer-=1

def main():

    ascii = r'''
    ______   ____   _____   ____   __| _/___________   ____  
    \____ \ /  _ \ /     \ /  _ \ / __ |/  _ \_  __ \_/ __ \ 
    |  |_> >  <_> )  Y Y  (  <_> ) /_/ (  <_> )  | \/\  ___/ 
    |   __/ \____/|__|_|  /\____/\____ |\____/|__|    \___  >
    |__|                                                     
    '''

    clear_terminal()
    print_centered(ascii)
    time.sleep(2)

    # instanciar handler de configuración
    configuration = config_handler()
    
    clear_terminal()

    is_default = "Y"

#     print_centered("""
# Welcome to pomodore CLI, do you want to use default settings?
# (Y/n)
#     """)
    print_centered("Welcome to pomodore CLI, do you want to use the following settings? (Y/n)")
    print()
    for key, value in configuration.data["user"].items():
        print_centered(f"{key}:{value}")
    for key, value in configuration.data["configuration"].items():
        print_centered(f"{key}:{value}")

    is_default = input().lower()
    
    if is_default == "": is_default = "Y" # si no se elige nada => Y, como si fuera linux
    clear_terminal()
    # DEBUG
    # print(f"is_default:{is_default}")

    if is_default == "n":

        options = ["Focus time", "Short rest time", "Long rest time", "Number of rounds", "Username"]
        
        while True:
            #bucle infinito hasta que se ingrese un int
            while True:
                clear_terminal()
                try:
                    print_centered(f"""
What configuration do you want to modify?
1. Focus time ({configuration.data["configuration"]["pomodore_time"]} mins)
2. Short rest ({configuration.data["configuration"]["short_rest_time"]} mins)
3. Long Rest ({configuration.data["configuration"]["long_rest_time"]} mins)
4. Number of rounds ({configuration.data["configuration"]["number_of_rounds"]})
5. Username: ({configuration.data["user"]["username"]})
6. Reset to Defaults
7. Continue
                    """)

                    option_to_modify = int(input())

                    if(option_to_modify <= 7 and option_to_modify >= 1):
                        break
                    else:
                        clear_terminal()
                        print_centered("Please enter only a valid number between 1 and 7")
                        pause_program()

                except ValueError:
                    clear_terminal()
                    print_centered("Please enter only a valid number")
                    pause_program()
        
            if option_to_modify == 7:
                # exit = True
                break

            if option_to_modify == 6:
                configuration.set_default_config()
                break
            
            #Bucle infinito hasta que se ingrese un int
            while True:
                try:
                    clear_terminal()
                    print_centered(f"insert the new value for {options[option_to_modify-1]}:")
                    if option_to_modify == 5:
                        ans = str(input())
                        break
                    else:
                        ans = int(math.fabs(int(input())))
                        break
                except ValueError:
                    clear_terminal()
                    print_centered("Please enter only a valid number")
                    pause_program()

            if option_to_modify == 1:
                configuration.data["configuration"]["pomodore_time"] = ans
            elif option_to_modify == 2:
                configuration.data["configuration"]["short_rest_time"] = ans
            elif option_to_modify == 3:
                configuration.data["configuration"]["long_rest_time"] = ans
            elif option_to_modify == 4:
                configuration.data["configuration"]["number_of_rounds"] = ans
            elif option_to_modify == 5:
                configuration.data["user"]["username"] = ans

            clear_terminal()

    clear_terminal()

    configuration.save_config(configuration.data)

    print_centered(f"""
Using values:
1. Focus time ({configuration.data["configuration"]["pomodore_time"]} mins)
2. Short rest ({configuration.data["configuration"]["short_rest_time"]} mins)
3. Long Rest ({configuration.data["configuration"]["long_rest_time"]} mins)
4. Number of rounds ({configuration.data["configuration"]["number_of_rounds"]})
5. Username: ({configuration.data["user"]["username"]})
""")

    pause_program()

    # EMPIEZA LO BUENO --------------------------------------------------------------

    for i in range(configuration.data["configuration"]["number_of_rounds"]):

        # cuenta regresiva de cinco segundos
        for j in range(5):
            clear_terminal()
            print_centered(f"Starting Pomodore no. {i+1} in {5-j}")
            time.sleep(1)

        run_timer(configuration.data["configuration"]["pomodore_time"]*60, f"Pomodore no. {i+1}")

        if (i+1) == configuration.data["configuration"]["number_of_rounds"]:
            run_timer(configuration.data["configuration"]["long_rest_time"]*60, f"Long rest") #PARA LONG REST
        else:
            run_timer(configuration.data["configuration"]["short_rest_time"]*60, f"Short rest no. {i+1}")

#   Se termina la sesión
    clear_terminal()
    print_centered("Pomodore session finished")
    pause_program()

if __name__ == '__main__':
    main()


# SOURCES:
#  ESTE PROYECTO TIENE COMO PRINCIPAL OBJETIVO EL AFIANZAR MIS CONOCIMIENTOS Y LÓGICA DE PROGRAMACIÓN MEDIANTE
#  LA INVESTIGACIÓN PROPIA DE MANERA PRAGMÁTICA, PARA MEDIR CUANTITATIVAMENTE ANOTARÉ TODA FUENTE DE CONSULTA 

#  MENCIÓN HONORIFICA: GOOGLE GEMINI COMO TUTOR (NO VIBECODE!!! 🤓)

#     26/11/2025
#     https://www.programiz.com/python-programming/main-function
#     https://www.geeksforgeeks.org/python/python-or-operator/ 
#     https://www.w3schools.com/python/ref_string_isnumeric.asp   
#     https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python

#     07/12/2025
#     https://stackoverflow.com/questions/74412503/cannot-access-local-variable-a-where-it-is-not-associated-with-a-value-but
#     https://search.brave.com/search?q=python+input+to+int&summary=1&conversation=b1457da7883e657cf43a76

#     08/12/2025
#     https://www.geeksforgeeks.org/python/make-python-wait-for-a-pressed-key/
#     https://stackoverflow.com/questions/11552320/correct-way-to-pause-a-python-program/56819619#56819619
#     https://stackoverflow.com/questions/29780053/how-do-i-print-in-the-middle-of-the-screen

#     10/12/2025
#     https://www.w3schools.com/python/python_for_loops.asp

#     24/12/2025
#     https://stackoverflow.com/questions/50281190/center-multi-line-text-in-python-output
#     https://stackoverflow.com/questions/50281190/center-multi-line-text-in-python-output

#     02/01/2026
#     https://www.snaplogic.com/blog/json-vs-yaml-whats-the-difference-and-which-one-is-right-for-your-enterprise

#     15/01/2026
#     https://python.land/data-processing/python-yaml
#     https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory

#     17/01/2026
#     https://www.w3schools.com/python/gloss_python_check_if_dictionary_item_exists.asp
#     https://www.geeksforgeeks.org/python/how-to-print-a-dictionary-in-python/
#     https://docs.python.org/3/library/math.html#math.fabs
    



# APRENDIZAJES: 
# Principio DRY (Dont Repeat Yourself)
# Graceful Degradation
# Desacoplamiento y Responsabilidad Única (SRP)
