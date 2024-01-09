from flet import *

#Styles: Colores
violetaClaro = "#965FD4"
violetaObscuro = "#1D1A2F"
verdeClaro = "#8BD450"
verdeObscuro = "#3F6D4E"
rosaClaro = "#C99EC7"

class textInput(UserControl):    
    def __init__(self, text: str, capitalization:str) -> None:
        """_summary_

        Args:
            text (str): Descripcion del text field
            capitalization (str): none, words, sentences, characters
        """        
        super().__init__()
        self.text = text
        self.capitalization = capitalization
        self.textField = None  # Añade un atributo para almacenar la instancia de TextField

    
    def build(self) -> TextField:
       self.textField = TextField(label=self.text, border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, capitalization=self.capitalization)
       return self.textField