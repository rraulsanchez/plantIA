import re

def cargar_plantilla(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()

def validar_campos(contenido):
    errores = []

    def buscar_pregunta(titulo):
        patron = rf"\*\*{re.escape(titulo)}\*\*\s*:?[\r\n]+(.+?)(?=\n\n|\Z)"
        match = re.search(patron, contenido, re.DOTALL)
        return match.group(1).strip() if match else ""

    # Validaciones clave
    if not buscar_pregunta("Nombre del sitio o proyecto"):
        errores.append("❌ Falta el nombre del sitio o proyecto.")

    if not buscar_pregunta("Ubicación"):
        errores.append("❌ Falta la ubicación del proyecto.")

    if "[x]" not in contenido.lower():
        errores.append("❌ No se ha seleccionado ningún tipo de proyecto.")

    if not buscar_pregunta("Público objetivo"):
        errores.append("❌ No se ha definido el público objetivo.")

    if not buscar_pregunta("¿Cuál es el objetivo principal de tu web?"):
        errores.append("❌ Falta el objetivo principal de la web.")

    resumen = buscar_pregunta("Resumen breve de tu proyecto")
    if len(resumen.split()) < 10:
        errores.append("❌ El resumen del proyecto es demasiado corto (<10 palabras).")

    redes = buscar_pregunta("Redes sociales que quieres mostrar")
    if not any(s in redes.lower() for s in ["instagram", "facebook", "tiktok"]):
        errores.append("❌ No se han indicado redes sociales.")

    estilo = buscar_pregunta("Colores preferidos")
    if not estilo:
        errores.append("❌ No se han definido colores preferidos o estilo visual.")

    legales = buscar_pregunta("Textos legales existentes")
    if not legales:
        errores.append("⚠️ No se han especificado textos legales (puede ser opcional).")

    return errores

# Ruta al archivo .md
ruta_plantilla = "plantilla-web.md"  # Asegúrate de que esté en la misma carpeta

contenido = cargar_plantilla(ruta_plantilla)
resultados = validar_campos(contenido)

if not resultados:
    print("✅ Todos los campos básicos están correctamente rellenados.")
else:
    print("Revisión de la plantilla:")
    for error in resultados:
        print(error)
