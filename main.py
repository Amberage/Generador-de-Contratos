from flet import *
import flet as ft
import classes.items as it
import os, sys, locale

rootPath = getattr(sys, '_MEInew_direccionCasa = "wittch"', os.path.dirname(os.path.abspath(__file__)))
locale.setlocale(locale.LC_ALL, '')  # Formato de moneda local (Ejemplo: 1500 -> 1,500.00)

def main(page: ft.Page):
    
    #Configuracion APP
    page.title = "Generador de Contratos"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width = 600
    page.window_height = 900
    page.window_resizable = False
    page.padding = 25
    page.scroll=ft.ScrollMode.HIDDEN

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

    page.theme = ft.Theme(font_family="Gill Sans")

    # ! AppBar
    page.appbar = ft.AppBar(
	toolbar_height=90,
	bgcolor=violetaObscuro,
    
	title=Row(
        [
		Container(
		padding = padding.all(10),
		border = border.all(3, ft.colors.with_opacity(0.8, "black")),
        bgcolor = ft.colors.with_opacity(0.8, violetaClaro),
		border_radius = border_radius.all(10),
		content=Text("GENERADOR DE CONTRATOS",color=ft.colors.with_opacity(0.8, "white") ,size=18, font_family="Gill Sans")
		),
		Container(
		content=Image(
		src=f"assets\\icons\\law.ico",
		width=100,
		height=70
		)

		),
		],alignment="spaceBetween"),
	)

    #Headers
    headerDueno = it.banner("Datos del Dueño", "datosDueno.ico")
    headerCliente = it.banner("Datos del Cliente", "datosCliente.ico")
    headerContrato = it.banner("Datos del Contrato", "datosContrato.ico")

    # ! Formulario
    
    #Datos arrendador
    #form_nombreArrendador = it.textInput("Nombre del Dueño", "words", "Nombre, Apellido Paterno y Apellido Materno")
    form_nombreArrendador = ft.Dropdown(
        border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro,
        hint_text="Nombre del Dueño",
        options=[
            ft.dropdown.Option("Alejandro Galicia Hernández"),
            ft.dropdown.Option("Roberto Alejandro Galicia Vega")
        ]
    )

    form_testigoArrendador = it.textInput("Nombre del Testigo", "words", "Nombre, Apellido Paterno y Apellido Materno")

    #! Datos Arrendatario
    form_generoArrendatario = ft.Dropdown(
        width=100, border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro,
        hint_text="Sexo",
        options=[
            ft.dropdown.Option("Hombre"),
            ft.dropdown.Option("Mujer"),
        ]
    )
    form_nombreArrendatario = it.textInput("Nombre del Cliente", "words", "Nombre, Apellido Paterno y Apellido Materno")
    form_contactoArrendatario = TextField(label="Telefono del Cliente", border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, input_filter=ft.NumbersOnlyInputFilter(), max_length=10)
    form_nombreTestigo = it.textInput("Nombre del Testigo", "words", "Nombre, Apellido Paterno y Apellido Materno")
    form_domicilioTestigo = it.textInput("Domicilio del Testigo", "none", "Calle, Numero, Manzana, Colonia, Municipio y Estado")
    form_telefonoTestigo = TextField(label="Telefono del Testigo", border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, input_filter=ft.NumbersOnlyInputFilter(), max_length=10)
    

    #! Datos del contrato
    #form_direccionCasa = it.textInput("Dirección del Inmueble", "none", "Dirección de la casa en renta")
    form_direccionCasa = ft.Dropdown(
        border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro,
        hint_text="Dirección del Inmueble",
        options=[
            ft.dropdown.Option("Caseta Vieja"),
            ft.dropdown.Option("División del Norte"),
            ft.dropdown.Option("El Molino"),
            ft.dropdown.Option("Nezahualcóyotl")
        ]
    )
    form_tipoInmueble = ft.Dropdown(
        border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, width = 100,
        hint_text="Tipo",
        options=[
            ft.dropdown.Option("Cuarto"),
            ft.dropdown.Option("Local")
        ]
    )
    form_valorRenta = TextField(label="Precio de Renta", border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, input_filter=ft.NumbersOnlyInputFilter(), hint_text="Precio sin centavos")
   
    form_diaCobro = ft.Dropdown(
        border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, width = 125, hint_text="Día Cobro",
        options=[ft.dropdown.Option("1"), ft.dropdown.Option("2"), ft.dropdown.Option("3"), ft.dropdown.Option("4"), ft.dropdown.Option("5"), ft.dropdown.Option("6"), ft.dropdown.Option("7"), ft.dropdown.Option("8"), ft.dropdown.Option("9"),ft.dropdown.Option("10"), ft.dropdown.Option("11"), ft.dropdown.Option("12"), ft.dropdown.Option("13"), ft.dropdown.Option("14"), ft.dropdown.Option("15"),
                 ft.dropdown.Option("16"), ft.dropdown.Option("17"), ft.dropdown.Option("18"), ft.dropdown.Option("19"), ft.dropdown.Option("20"), ft.dropdown.Option("21"), ft.dropdown.Option("22"), ft.dropdown.Option("23"), ft.dropdown.Option("24"), ft.dropdown.Option("25"), ft.dropdown.Option("26"), ft.dropdown.Option("27"), ft.dropdown.Option("28"), ft.dropdown.Option("29"), ft.dropdown.Option("30"), ft.dropdown.Option("31")])
    
    form_valorPenalizacion = TextField(label="Precio Penalización", border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, input_filter=ft.NumbersOnlyInputFilter(), hint_text="Precio sin centavos")
    
    form_zonaRenta = ft.Dropdown(
        border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro,
        hint_text="Municipio del Inmueble", width= 335,
        options=[
            ft.dropdown.Option("Valle de Chalco Solidaridad"),
            ft.dropdown.Option("Ixtapaluca"),
            ft.dropdown.Option("Nezahualcóyotl")
        ]
    )
    form_numeroMedidor = it.textInput("Número del medidor CFE", "characters", "Consultar en el recibo de CFE")
    form_numeroServicio = it.textInput("Número del servicio CFE", "characters", "Consultar en el recibo de CFE")

    form_duracionContrato = ft.Dropdown(border_color=verdeObscuro, focused_border_color=verdeClaro, border_radius=15, color=violetaClaro, focused_color=rosaClaro, hint_text="Duración del Contrato",
        options=[ft.dropdown.Option("3 MESES"), ft.dropdown.Option("6 MESES"), ft.dropdown.Option("9 MESES"), ft.dropdown.Option("12 MESES"), ft.dropdown.Option("15 MESES"), ft.dropdown.Option("18 MESES"), ft.dropdown.Option("21 MESES"), ft.dropdown.Option("24 MESES")])
   
    form_fechaInicio = it.textInput("Fecha de inicio del contrato, formato: 01 del mes de enero del año 2023", "none", "hint")
    form_fechaFin = it.textInput("Fecha de termino del contrato, formato: 01 del mes de enero del año 2023", "none", "hint")
    form_fechaActual = it.textInput("Fecha de firma del contrato, formato: 01 del mes de enero del año 2023", "none", "hint")

    datosDueno = Column([
        #* Datos del arrendador
        headerDueno,
        form_nombreArrendador,
        form_testigoArrendador
    ], visible= True)

    datosCliente = Column([
        #* Datos del arrendatario
        headerCliente,
        Row([form_generoArrendatario, Container(form_nombreArrendatario, width= 420)]),
        form_contactoArrendatario,
        form_nombreTestigo,
        form_domicilioTestigo,
        form_telefonoTestigo
    ], visible=True)

    datosContrato = Column([
        # Datos del contrato
        headerContrato,
        Row([Container(form_direccionCasa, width = 260), Container(form_duracionContrato, width= 265)]),
        Row([form_tipoInmueble, Container(form_valorRenta, width=290), form_diaCobro]),
        Row([Container(form_valorPenalizacion, width=190), form_zonaRenta]),
        Row([Container(form_numeroMedidor, width=260), Container(form_numeroServicio, width=265)]),
        
        #TODO: Pendiente
        form_fechaInicio,
        form_fechaFin,
        form_fechaActual,
        Container(height=80)
    ], visible=False)

    #! Botones
    def nextButton(e):
        datosDueno.visible = False
        datosCliente.visible = False
        datosContrato.visible = True
        botonSiguiente.visible = False
        botonAtras.visible = True
        botonGenerar.visible = True
        page.update()

    def backButton(e):
        datosDueno.visible = True
        datosCliente.visible = True
        datosContrato.visible = False
        botonSiguiente.visible = True
        botonAtras.visible = False
        botonGenerar.visible = False
        page.update()

    def generarContrato(e):
        #Datos arrendador
        new_nombreArrendador = form_nombreArrendador.value
        new_testigoArrendador = form_testigoArrendador.textField.value
        #Datos arrendatario
        new_sexArrendatario = form_generoArrendatario.value
        new_nombreArrendatario = form_nombreArrendatario.textField.value
        new_contactoArrendatario = form_contactoArrendatario.value
        new_tesArrendatario = form_nombreTestigo.textField.value
        new_domicilioTestigo = form_domicilioTestigo.textField.value
        new_telefonoTestigo = form_telefonoTestigo.value
        #Datos del contrato
        new_fechaActual = form_fechaActual.textField.value
        new_direccionCasa = form_direccionCasa.value

        #Conversiones pendientes que se realizaran dentro del else
        new_tipoInmueble = form_tipoInmueble.value
        new_valorRenta = form_valorRenta.value
        new_valorPenalizacion = form_valorPenalizacion.value

        new_diaCobro = form_diaCobro.value
        new_duracionContrato = form_duracionContrato.value
        new_fechaInicio = form_fechaInicio.textField.value
        new_fechaFin = form_fechaFin.textField.value
        new_numeroMedidor = form_numeroMedidor.textField.value
        new_numeroServicio = form_numeroServicio.textField.value
        new_zonaRenta = form_zonaRenta.value
        
        nuevosDatosContrato = [
                new_nombreArrendador,
                new_testigoArrendador,
                new_sexArrendatario,
                new_nombreArrendatario,
                new_contactoArrendatario,
                new_tesArrendatario,
                new_domicilioTestigo,
                new_telefonoTestigo,
                new_fechaActual,
                new_direccionCasa,
                new_tipoInmueble,
                new_valorRenta,
                new_diaCobro,
                new_valorPenalizacion,
                new_duracionContrato,
                new_fechaInicio,
                new_fechaFin,
                new_numeroMedidor,
                new_numeroServicio,
                new_zonaRenta,
            ]
        
        validarCampos = False
        for element in nuevosDatosContrato:
            if element == '':
                print(f"Error, rellena todos los campos del formulario")
                validarCampos = False
                break
        else:
            nuevosDatosContrato[10] = new_tipoInmueble.lower()
            nuevosDatosContrato[11] = locale.format_string('%0.2f', int(form_valorRenta.value), grouping=True)
            nuevosDatosContrato[13] = locale.format_string('%0.2f', int(form_valorPenalizacion.value), grouping=True)
            if new_direccionCasa == "Caseta Vieja":
                nuevosDatosContrato[9] = "Calle Norte 15, Mz. 433, Lt.10, Colonia San Isidro, Valle de Chalco Solidaridad"
            elif new_direccionCasa == "División del Norte":
                nuevosDatosContrato[9] = "Calle División del Norte, Mz. 495, Lt. 39, Colonia San Isidro, Valle de Chalco Solidaridad"
            elif new_direccionCasa == "El Molino":
                nuevosDatosContrato[9] = "Calle Carolina, Mz. 74, Lt. 32, Colonia El Molino, Ixtapaluca"
            elif new_direccionCasa == "Nezahualcóyotl":
                nuevosDatosContrato[9] = "Calle Cariño, Mz. 419, Lt. D, No. Exterior 164, Colonia Aurora Oriente, Nezahualcóyotl"

            validarCampos = True
        
        if validarCampos == True:
            print(nuevosDatosContrato)

    botonSiguiente = ft.ElevatedButton("Siguiente", on_click=nextButton, bgcolor=it.violetaObscuro, color=it.rosaClaro)
    botonAtras = ft.ElevatedButton("Volver", on_click=backButton, visible=False, bgcolor=it.violetaObscuro, color=it.rosaClaro)
    botonGenerar = ft.ElevatedButton("Generar Contrato", visible= False, on_click=generarContrato, bgcolor=it.violetaObscuro, color=it.rosaClaro)

    botones = Container(Row([
        botonAtras,
        botonSiguiente,
        botonGenerar
    ], alignment="center"),
    )

    #TODO: Zona de testing


    page.add(
        datosDueno,
        datosCliente,
        datosContrato,
        botones
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