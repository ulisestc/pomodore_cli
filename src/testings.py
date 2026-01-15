# # import os
# # import readchar

# # print("leyendo")
# # readchar.readkey()
# # # print (os.name)


# # # TODO
# # #investigar sobre click.echo para funcionar en todos los environments de cli como bash cshell y cmd(windows) para convertir
# # #en multiplataforma

# # #la librería click también permitirá iniciar la app con un entry point, por ejemplo "pomodore" desde la terminal

# import shutil
# import textwrap

# columns = shutil.get_terminal_size().columns

# def print_center_text(text):
#     separated_lines = text.splitlines()
#     for line in separated_lines:
#         print(line.center(columns))

# text = r'''
# ______   ____   _____   ____   __| _/___________   ____  
# \____ \ /  _ \ /     \ /  _ \ / __ |/  _ \_  __ \_/ __ \ 
# |  |_> >  <_> )  Y Y  (  <_> ) /_/ (  <_> )  | \/\  ___/ 
# |   __/ \____/|__|_|  /\____/\____ |\____/|__|    \___  >
# |__|                                                     
# '''

# print("Texto centrado:".center(columns))


# print_center_text(text)



# TEST PRINT CENTERED INPUT
import shutil

columns = shutil.get_terminal_size().columns

def print_center_text(text):
    separated_lines = text.splitlines()
    for line in separated_lines:
        print(line.center(columns))

print_center_text( "Ingrese su nombre: " )
name = input()
print_center_text( f"Hola, {name}!" )
