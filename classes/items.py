import flet
from flet import *
from flet import colors
import string

#Styles: Colores
violetaClaro = "#965FD4"
violetaObscuro = "#1D1A2F"
verdeClaro = "#8BD450"
verdeObscuro = "#3F6D4E"
rosaClaro = "#C99EC7"

class textInput(UserControl):    
    def __init__(self, text: str, capitalization:str, hint: str) -> None:
        """_summary_

        Args:
            text (str): Descripcion del text field
            capitalization (str): none, words, sentences, characters
            hint (str): Placeholder
        """        
        super().__init__()
        self.text = text
        self.capitalization = capitalization
        self.hint = hint
        self.textField = None

    
    def build(self) -> TextField:
       self.textField = TextField(label=self.text, border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, capitalization=self.capitalization, hint_text=f"{self.hint}")
       return self.textField




#Banners
class banner(UserControl):    
    def __init__(self, title: str, iconName:str) -> None:
        """_summary_

        Args:
            title (str): Titulo del banner
            iconName (str): Nombre del icono con extensión, los iconos disponibles se encuentran en /assets/icons
        """        
        super().__init__()
        self.title = title
        self.iconName = iconName
        self.banner = None  # Añade un atributo para almacenar la instancia de TextField

    
    def build(self) -> Row:
       #self.banner = TextField(label=self.text, border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, capitalization=self.capitalization)
       self.banner = Row(
        [
        Container(
            padding = padding.all(5),
            border = border.all(3, flet.colors.with_opacity(0.8, "black")),
            bgcolor = flet.colors.with_opacity(0.8, verdeClaro),
            border_radius = border_radius.all(10),
            content=Text(f"{self.title}",color=flet.colors.with_opacity(0.8, violetaObscuro) ,size=18, font_family="Gill Sans Bold", text_align = "center"),
            height=50),

        Container(
            content=Image(
            src=f"assets\\icons\\{self.iconName}",
            width=50,
            height=50
		)),
        ],alignment="center",
        height=45
    )
       return self.banner
    
def estilizarFecha(dia: str, mes: str, anio: str):
    mes = mes.lower()
    return f"{dia} del mes de {mes} del año {anio}"
