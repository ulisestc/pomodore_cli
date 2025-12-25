import time, os
import readchar
import shutil

columns = shutil.get_terminal_size().columns

def print_centered(text):
    separated_lines = text.splitlines()
    for line in separated_lines:
        print(line.center(columns))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_program():
    print("Press any key to continue...")
    readchar.readkey()
    clear_terminal()

def run_timer(timer, message):
    for i in range(timer): 
        clear_terminal()
        print(message)
        print(f"Time left: {timer} seconds.")
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

    config = {
        "POMODORE_TIME" : 25,
        "SHORT_REST_TIME" : 5,
        "LONG_REST_TIME" : 15,
        "NUMBER_OF_ROUNDS" : 4
    }
    
    clear_terminal()

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

        options = ["Focus time", "Short rest time", "Long rest time", "Number of rounds"]
        
        while True:
            #bucle infinito hasta que se ingrese un int
            while True:
                try:
                    option_to_modify = int(input(f"""
                                                What timer do you want to modify?
                                                1. Focus time ({config["POMODORE_TIME"]} mins)
                                                2. Short rest ({config["SHORT_REST_TIME"]} mins)
                                                3. Long Rest ({config["LONG_REST_TIME"]} mins)
                                                4. Number of rounds ({config["NUMBER_OF_ROUNDS"]})
                                                5. Continue
                                            """))
                    break
                except ValueError:
                    clear_terminal()
                    print("Please enter only a valid number")
            
            if option_to_modify > 5 or option_to_modify < 1:
                clear_terminal()
        
            if option_to_modify == 5:
                # exit = True
                break
            
            #Bucle infinito hasta que se ingrese un int
            while True:
                try:
                    ans = int(input(f"insert the new value for {options[option_to_modify-1]}:"))
                    break
                except ValueError:
                    clear_terminal()
                    print("Please enter only a valid number")

            if option_to_modify == 1:
                config["POMODORE_TIME"] = ans
            elif option_to_modify == 2:
                config["SHORT_REST_TIME"] = ans
            elif option_to_modify == 3:
                config["LONG_REST_TIME"] = ans
            elif option_to_modify == 4:
                config["NUMBER_OF_ROUNDS"] = ans

            clear_terminal()
            
    print(f"""Using values:
        FOCUS time: {config["POMODORE_TIME"]} mins
        REST time: {config["SHORT_REST_TIME"]} mins
        LONG_REST time: {config["LONG_REST_TIME"]} mins
        nuber of ROUNDS: {config["NUMBER_OF_ROUNDS"]}
    """)

    pause_program()

    print("Press any key to start Pomodore Session")
    pause_program()

    # EMPIEZA LO BUENO 

    for i in range(config["NUMBER_OF_ROUNDS"]):

        for j in range(5):
            clear_terminal()
            print(f"Starting Pomodore no. {i+1} in {5-j}")
            time.sleep(1)

        run_timer(config["POMODORE_TIME"]*60, f"Pomodore no. {i+1}")

        if (i+1) == config["NUMBER_OF_ROUNDS"]:
            run_timer(config["LONG_REST_TIME"]*60, f"Long rest") #PARA LONG REST
        else:
            run_timer(config["SHORT_REST_TIME"]*60, f"Short rest no. {i+1}")

#   Se termina la sesión
    clear_terminal()
    print("Pomodore session finished")
    pause_program()

if __name__ == '__main__':
    main()


# SOURCES:
#  ESTE PROYECTO TIENE COMO PRINCIPAL OBJETIVO EL AFIANZAR MIS CONOCIMIENTOS Y LÓGICA DE PROGRAMACIÓN MEDIANTE
#  LA INVESTIGACIÓN PROPIA DE MANERA PRAGMÁTICA, PARA MEDIR CUANTITATIVAMENTE ANOTARÉ TODA FUENTE DE CONSULTA 

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