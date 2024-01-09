from docx import Document
import os, re, time, subprocess
from ..main import rootPath

assets = f"{rootPath}\\assets"


def reemplazar_palabra(doc, palabra_antigua, palabra_nueva):
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if palabra_antigua in run.text:
                print(f"Antes del reemplazo: {run.text}")
                run.text = re.sub(re.escape(palabra_antigua), palabra_nueva, run.text)
                print(f"Después del reemplazo: {run.text}")

if __name__ == "__main__":
    datosContrato = ['nombreArrendador', 'testigoArrendador', 'sexArrendatario', 'nombreArrendatario', 'contactoArrendatario', 'tesArrendatario', 'domicilioTestigo', 'telefonoTestigo', 'fechaActual', 'direccionCasa', 'tipoInmueble', 'valorRenta', 'diaCobro', 'valorPenalizacion', 'duracionContrato', 'fechaInicio', 'fechaFin', 'numeroMedidor', 'numeroServicio', 'zonaRenta']
    nuevos_datos = ['Axel', 'Braulio', 'el', 'Ismael', '55 1839 2955', 'Felipe', 'Domicilio 1', '55 2929 5151', 'hoy merito', 'Mordor jaja', 'Cuarto', '3,000.00', '666', '6,000.00', '99', 'EL inicio', 'El final', 'Num Medidor', 'Num Servicio', 'Valle de Solidaridad']

    ruta_archivo = 'contratoVanilla.docx'

    try:
        doc = Document(ruta_archivo)

        for palabra_antigua, palabra_nueva in zip(datosContrato, nuevos_datos):
            reemplazar_palabra(doc, palabra_antigua, palabra_nueva)

        ruta_escritorio = os.path.join(os.path.expanduser("~"), 'Desktop')

        if not os.path.exists(ruta_escritorio):
            os.makedirs(ruta_escritorio)

        ruta_guardado = os.path.join(ruta_escritorio, 'contrato_modificado.docx')
        doc.save(ruta_guardado)

        print(f"El documento modificado ha sido guardado en {ruta_guardado}")
        # Esperar 500ms antes de abrir el archivo
        time.sleep(0.5)

        # Abrir el archivo recién modificado
        subprocess.Popen(['start', 'winword', ruta_guardado], shell=True)

    except Exception as e:
        print(f"Error: {e}")

    



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