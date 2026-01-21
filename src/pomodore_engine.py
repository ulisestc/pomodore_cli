# config = diccionario de configuración de config_handler
# current_round = ronda actual del pomodore
# is_running = estado del pomodore (activo o en descanso)
# is_break = si toca descanso
# max_rounds = a las cuantas rondas es el long rest

# P . s . P . s . P . s . P . l 


class pomodore_engine:
    def __init__(self, config):
        self.config = config
        self.current_round = 1
        self.is_running = False
        self.is_break = False
        self.max_rounds = config["configuration"]["number_of_rounds"]

    def get_info(self):
        #Si no toca descanso asignamos duración y mensaje a el pomodoro respectivo
        if not self.is_break: 
            duration = self.config["configuration"]["pomodore_time"]*60
            message = f"Pomodore no. {self.current_round}"
        elif self.is_break and self.current_round < self.max_rounds: #Si toca descanso y todavía no llegamos a max_rounds, toca short rest
            duration = self.config["configuration"]["short_rest_time"]*60
            message = f"Short rest no. {self.current_round}"
        else: # Casp contrario is_break = True y current_round == max_rounds => Long rest
            duration = self.config["configuration"]["long_rest_time"]*60
            message = f"Long rest, prepare for next session"
        
        #Finalizando la decisión de que toca: se invierte valor de is_break y se suma la ronda actual
        # para preparar la siguiente iteración

        if self.is_break: self.current_round += 1 #Si se terminó el descanso, suma ronda
        if self.current_round > self.max_rounds: self.current_round = 1 #Si ya nos pasamos, resetear para que toque el short rest correspondiente
        self.is_break = not self.is_break #invertir polaridad de break

        return duration, message    

    def run_next_session(self, duration):
        self.is_running = True
