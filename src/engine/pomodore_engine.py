# config = diccionario de configuración de config_handler
# current_round = ronda actual del pomodore
# is_running = estado del pomodore (activo o en descanso)
# is_break = si toca descanso
# max_rounds = a las cuantas rondas es el long rest

import time
import math

class PomodoreEngine:
    def __init__(self, config):
        self.config = config
        self.current_round = 1
        self.is_running = False
        self.is_break = False
        self.max_rounds = config["configuration"]["number_of_rounds"]
        self.message = ""

    def prepare_next_session(self):
        #Si no toca descanso asignamos duración y mensaje a el pomodoro respectivo
        if not self.is_break: 
            duration = self.config["configuration"]["pomodore_time"]*60
            self.message = f"Pomodore no. {self.current_round}"
        elif self.is_break and self.current_round < self.max_rounds: #Si toca descanso y todavía no llegamos a max_rounds, toca short rest
            duration = self.config["configuration"]["short_rest_time"]*60
            self.message = f"Short rest no. {self.current_round}"
        else: # Casp contrario is_break = True y current_round == max_rounds => Long rest
            duration = self.config["configuration"]["long_rest_time"]*60
            self.message = f"Long rest, prepare for next session"
        
        #Finalizando la decisión de que toca: se invierte valor de is_break y se suma la ronda actual
        # para preparar la siguiente iteración

        if self.is_break: self.current_round += 1 #Si se terminó el descanso, suma ronda
        if self.current_round > self.max_rounds: self.current_round = 1 #Si ya nos pasamos, resetear para que toque el short rest correspondiente
        self.is_break = not self.is_break #invertir polaridad de break

        return duration, self.message    

    def run_timer(self, duration, callback_func):
        #get_info se encargará de la lógica por lo que esta func. solo se encarga de la lógica del tiempo
        self.is_running = True
        start_time = time.time()
        end_time = start_time + duration

        while time.time() < end_time: 
            remaining_time = math.ceil(end_time - time.time())
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            
            callback_func(self.message,"{:02d}:{:02d}".format(minutes, seconds))
            time.sleep(.5)
