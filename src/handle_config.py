import yaml
import pathlib


class config_handler:
    
    def __init__(self):
        # path absoluto del src
        self.src_path = pathlib.Path(__file__).parent.resolve()
        #path de configuración yaml
        self.config_path = self.src_path / "config.yaml"

        #Si no hay config, se crea.
        if self.config_path.exists():
            print("HAY CONFIG")
        else: 
            print("NO HAY CONFIG")
            # cargar configuración
            default_config = """
                user:
                    username: default_user

                configuration:
                    pomodore_time: 25
                    short_rest_time: 5
                    long_rest_time: 15
                    number_of_rounds: 4
            """
            config = yaml.safe_load(default_config)

            with open(self.config_path, 'w') as file:
                yaml.dump(config, file)
            
            print("SE CREÓ ARCHIVO DE CONFIGURACIÓN DEFAULT:", config, sep = "\n")


if __name__ == "__main__":
    print("ERROR: THIS FILE MUST NOT BE EXECUTED AS MAIN FILE")