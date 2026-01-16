import yaml
import pathlib

#self.src_path -> path absoluto del src
#self.config_path -> path del archivo de configuración yaml
#self.data -> datos cargados del archivo de configuración

##TODO -> Esta clase no debería tener prints, solo para debuggear

class config_handler:
    
    def __init__(self):
        # path absoluto del src
        self.src_path = pathlib.Path(__file__).parent.resolve()
        #path de configuración yaml
        self.config_path = self.src_path / "config.yaml"

        #Si hay config, se guarda en self.data
        if self.config_path.exists():
            with open(self.config_path, 'r') as file:
                self.data = yaml.safe_load(file)
            print("HAY CONFIG:", self.data, sep = "\n")
        else: # SI NO, se crea el default
            # cargar configuración
            self.set_default_config()
            print("NO HAY CONFIG; SE CREÓ ARCHIVO DE CONFIGURACIÓN DEFAULT:", self.data, sep = "\n")

    def load_config(self):
        pass

    def save_config(self, new_data):
        pass

    @staticmethod
    def get_default_config():
        return """
                user:
                    username: default_user

                configuration:
                    pomodore_time: 25
                    short_rest_time: 5
                    long_rest_time: 15
                    number_of_rounds: 4
            """

    def set_default_config(self):
        self.data = yaml.safe_load(self.get_default_config())

        try:
            with open(self.config_path, 'w') as file:
                yaml.dump(self.data, file)
            return True
        except Exception as e:
            print("Error al resetear valores de configuración:", e)
            return False

if __name__ == "__main__":
    print("ERROR: THIS FILE MUST NOT BE EXECUTED AS MAIN FILE")


# TODO: 
#     load_config debe cargar el yaml a self.data para manejar errores y simplificar constructor
#     implementar save_config para que set_default_config la use y se simplifique la función