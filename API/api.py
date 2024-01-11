from docx import Document
import re, time, subprocess, os
from typing import List



contracrtFilename = "contratoVanilla.docx"
contracrtPath = os.path.join(os.path.dirname(__file__), contracrtFilename)

def reemplazar_palabra(doc, palabra_antigua, palabra_nueva):
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if palabra_antigua in run.text:
                run.text = re.sub(re.escape(palabra_antigua), palabra_nueva, run.text)

def generarArchivo(newData, nombreCliente, casa):
    datosContrato = ['nombreArrendador', 'testigoArrendador', 'sexArrendatario', 'nombreArrendatario', 'contactoArrendatario', 'tesArrendatario', 'domicilioTestigo', 'telefonoTestigo', 'fechaActual', 'direccionCasa', 'tipoInmueble', 'valorRenta', 'diaCobro', 'valorPenalizacion', 'duracionContrato', 'fechaInicio', 'fechaFin', 'numeroMedidor', 'numeroServicio', 'zonaRenta']
    try:
        doc = Document(contracrtPath)

        for palabra_antigua, palabra_nueva in zip(datosContrato, newData):
            reemplazar_palabra(doc, palabra_antigua, palabra_nueva)

        ruta_escritorio = os.path.join(os.path.expanduser("~"), 'Desktop')

        if not os.path.exists(ruta_escritorio):
            os.makedirs(ruta_escritorio)

        ruta_guardado = os.path.join(ruta_escritorio, f'Contrato {nombreCliente} - {casa}.docx')
        doc.save(ruta_guardado)

        print(f"El documento modificado ha sido guardado en {ruta_guardado}")
        time.sleep(0.5)
        subprocess.Popen(['start', 'winword', ruta_guardado], shell=True)

    except Exception as e:
        print(f"Error: {e}")