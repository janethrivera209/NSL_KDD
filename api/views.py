# api/views.py
import os
from django.http import JsonResponse, Http404
from django.shortcuts import render
from pathlib import Path

# Definimos la base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta de los archivos ARFF dentro del proyecto
ARFF_DIR = os.path.join(BASE_DIR, "arffs")  # <-- asegúrate de que la carpeta se llame "arffs" y esté en el proyecto

def listar_archivos(request):
    """Lista todos los archivos .arff en la carpeta"""
    try:
        archivos = [f for f in os.listdir(ARFF_DIR) if f.endswith(".arff")]
        return JsonResponse({"archivos": archivos})
    except FileNotFoundError:
        return JsonResponse({"error": "Directorio no encontrado"}, status=404)

def leer_archivo(request, nombre_archivo):
    """Lee un archivo ARFF y devuelve atributos y datos"""
    ruta_archivo = os.path.join(ARFF_DIR, nombre_archivo)
    if not os.path.exists(ruta_archivo):
        return JsonResponse({"error": "Archivo no encontrado"}, status=404)
    
    try:
        columnas = []
        datos = []
        with open(ruta_archivo, "r") as f:
            for line in f:
                line = line.strip()
                if line == "" or line.startswith("%"):
                    continue
                if line.upper().startswith("@RELATION"):
                    continue  # Ignoramos la línea @relation
                if line.upper().startswith("@ATTRIBUTE"):
                    partes = line.split()
                    columnas.append(partes[1])
                elif line.upper().startswith("@DATA"):
                    continue
                else:
                    datos.append([x.strip() for x in line.split(",")])
        
        atributos_json = [[col, ""] for col in columnas]

        return JsonResponse({
            "attributes": atributos_json,
            "data": datos[:100]  # Devuelve solo primeras 100 filas para que no tarde tanto
        })

    except Exception as e:
        return JsonResponse({"error": f"Error al leer archivo: {str(e)}"}, status=500)

def index(request):
    """Muestra la página principal con el front-end"""
    return render(request, 'index.html')

