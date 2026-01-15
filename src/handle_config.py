import yaml
import pathlib


class config_handler:
    
    def __init__(self):
        # path absoluto del src
        self.src_path = pathlib.Path(__file__).parent.resolve()
        #path de configuración yaml
        self.config_path = self.src_path / "config.yaml"

        if self.config_path.exists():
            print("HAY CONFIG")
        else: 
            print("NO HAY CONFIG")
    

if __name__ == "__main__":
    print("ERROR: THIS FILE MUST NOT BE EXECUTED AS MAIN FILE")