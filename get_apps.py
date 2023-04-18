import subprocess

comando = 'powershell.exe explorer.exe shell:AppsFolder" > prueba.txt' # comando de ejemplo para listar los archivos .exe en la carpeta System32 de Windows
resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)



# with open("dom_apps.txt", "r") as file:
#     texto = file.readlines()

# rutas = []
# for linea in texto:
#     if linea[:len("InstallLocation")] == "InstallLocation":
#         linea = linea.replace("\n", "")
#         rutas.append(linea[len("InstallLocation   : "):])

# rutas_aplicaciones = []
# for ruta in rutas:
#     with open(ruta+"\AppxManifest.xml", "r") as file:
#         manifest = file.readlines()

#     identificador = "Executable="
#     for linea in manifest:
#         #leer manifest
#         if identificador in linea:
#             #identificar en qué parte de la línea está el "Executable="
#             num = linea.index(identificador)
#             #obtener el ejecutable
#             ruta_aplicacion = ruta + "\\" + linea[num+len(identificador):].split('"')[1]
#             rutas_aplicaciones.append(ruta_aplicacion)
# print(rutas_aplicaciones)


