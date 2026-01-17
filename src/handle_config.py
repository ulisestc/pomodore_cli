import yaml
import pathlib

#self.src_path -> path absoluto del src
#self.config_path -> path del archivo de configuración yaml
#self.data -> datos cargados del archivo de configuración

class config_handler:
    
    def __init__(self):
        # path absoluto del src
        self.src_path = pathlib.Path(__file__).parent.resolve()
        #path de configuración yaml
        self.config_path = self.src_path / "config.yaml"

        if not self.load_config():
            self.set_default_config()
            print("NO HAY CONFIG o ESTA CORRUPTO; SE CREÓ ARCHIVO DE CONFIGURACIÓN DEFAULT:", self.data, sep = "\n")
        else:
            print("Config cargada correctamente")


    @staticmethod
    def is_config_valid(config_data):
        if isinstance(config_data,dict):
            
            try:
                #valida si hay user y configuration
                username = config_data["user"]["username"]
                pomodore_time = config_data["configuration"]["pomodore_time"]
                short_rest_time = config_data["configuration"]["short_rest_time"]
                long_rest_time = config_data["configuration"]["long_rest_time"]
                number_of_rounds = config_data["configuration"]["number_of_rounds"]
            except(KeyError, TypeError): #Si falta valor o no es diccionario valido
                return False
            # checamos cada instancia (tipo)
            if isinstance(username, str) and isinstance(pomodore_time, int) and isinstance(short_rest_time, int) and isinstance(long_rest_time, int) and isinstance(number_of_rounds, int):
                # checamos >= 0
                if pomodore_time >= 1 and short_rest_time >= 1 and long_rest_time >= 1 and number_of_rounds >= 1:
                    return True
        else:
            return False

    def load_config(self):
        try:
            with open(self.config_path, 'r') as file:
                self.data = yaml.safe_load(file)
            
            if self.is_config_valid(self.data):
                return True
            else:
                print("archivo existente pero formato incorrecto")
                return False
        except Exception as e:
            print("ERROR AL CARGAR LA CONFIGURACIÓN:", e, "RESTABLECIENDO VALORES POR DEFECTO. . .")
            return False

    def save_config(self, new_data):
        if not self.is_config_valid(new_data):
            self.set_default_config()
            print("Formato de nueva configuración incorrecto, regresando a valores predeterminados")
            return False
        else:
            try:
                self.data = new_data
                with open(self.config_path, 'w') as file:
                    yaml.dump(self.data, file)
                return True
            except Exception as e:
                print("ERROR AL GUARDAR LA CONFIGURACIÖN: ", e ,"REGRESANDO A VALORES DE FABRICA. . .")
                return False

    @staticmethod
    def get_default_config():
        return {
            'user': {
                'username': 'default_user'
            },
            'configuration':{
                'pomodore_time': 25,
                'short_rest_time': 5,
                'long_rest_time': 15,
                'number_of_rounds': 4
            }
        }

    def set_default_config(self):
        # self.data = yaml.safe_load(self.get_default_config())
        try:
            self.save_config(self.get_default_config())
            return True
        except Exception as e:
            print("ERROR AL RESTABLECER LA CONFIGURACIÓN POR DEFECTO:", e)
            return False

if __name__ == "__main__":
    print("ERROR: THIS FILE MUST NOT BE EXECUTED AS MAIN FILE")
