import flet as ft
import classes.items as it
import os, sys

rootPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

def main(page: ft.Page):
    #Configuracion APP
    page.title = "Generador de Contratos"
    page.theme_mode = ft.ThemeMode.SYSTEM

    #Styles: Colores
    violetaClaro = "#965FD4"
    violetaObscuro = "#1D1A2F"
    verdeClaro = "#8BD450"
    verdeObscuro = "#3F6D4E"
    rosaClaro = "#C99EC7"

    #Styles: Fonts
    page.fonts = {
        "Gill Sans": f"{rootPath}\\assets\\fonts\\GillSans.TTF",
        "Gill Sans Bold": f"{rootPath}\\assets\\fonts\\GillSans_Bold.TTF",
        "Gill Sans Italic": f"{rootPath}\\assets\\fonts\\GillSans_Italic.TTF",
        "Gill Sans BoldItalic": f"{rootPath}\\assets\\fonts\\GillSans_BoldItalic.TTF",
    }

    #Configuracion de la pagina

    #Alineado de items
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #AppBar
    page.appbar = ft.AppBar(
        title = ft.Text("Generador de Contratos", color=violetaObscuro, font_family="Gill Sans Bold"),
        bgcolor=violetaClaro
    )


    #Formulario
    tf_nombreArrendador = ft.TextField(label="Nombre del arrendador (Dueños)", border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, capitalization="words")
    tf_testigoArrendador = ft.TextField(label="Nombre del testigo del arrendador (Dueños)")
    tf_loquesea = it.textInput("sadasdasd mundo", "characters")
    
    page.add(
        tf_nombreArrendador,
        tf_testigoArrendador,
        tf_loquesea,
        )


ft.app(target=main)

""" 
Datos Arrendador:
{nombreArrendador}: Nombre del dueño de la casa.
{testigoArrendador}: Nombre del tesdtigo del arrendador

Datos Arrendatario:
{generoArrendatario}: al / a la
{nombreArrendatario}: Nombre de la persona que renta
{contactoArrendatario}: Numero de telefono del arrendatario
{nombreTestigo}: Nombre del testigo.
{domicilioTestigo}: Domicilio del testigo
{telefonoTestigo}: Numero de telefono del testigo


Datos del Contrato:
{fechaActual}: Día de firma del contrato con el formato: 01 del mes de enero del año 2023
{direccionCasa}: Dirección de la casa donde se rentara.
{tipoInmueble}: cuarto/local
{valorRenta}: Valor de renta con este formato: 1,500.00
{diaCobro}: Número entero que representa el día de cobro al mes.
{valorPenalizacion}: El doble del valorRenta
{duracionContrato}: Número entero que representa el número de meses que durará el presente contrato.
{fechaInicio}: Fecha con el formato: 01 del mes de enero del año 2023 
{fechaFin}: Fecha con el formato: 01 del mes de enero del año 2023 
{numeroMedidor}: Numero del medidor CFE 
{numeroServicio}: Numero de servicio de la CFE
{zonaRenta}: Valle de Chalco, Nezahualcoyol o Ixtapaluca
 """