from pytube import YouTube
from colorama import Fore, Style, init
import os
import time

texto = r"""
______________________________________________________________________________
|    ____ _       __    _    __________  __________  ________  ______  ______|
|   / __ \ |     / /   | |  / /  _/ __ \/ ____/ __ \/_  __/ / / / __ )/ ____/|
|  / / / / | /| / /____| | / // // / / / __/ / / / / / / / / / / __  / __/   |
| / /_/ /| |/ |/ /_____/ |/ // // /_/ / /___/ /_/ / / / / /_/ / /_/ / /___   |
|/_____/ |__/|__/      |___/___/_____/_____/\____/ /_/  \____/_____/_____/   |
|____________________________________________________________________________|
"""
init(autoreset=True)
texto_azul = f"{Fore.BLUE}{texto}{Style.RESET_ALL}"
print(texto_azul)

print('Descargador de videos de YouTube creado por Steven Layna Gonzalez.')
print('Nota: Para pegar la URL del video solo presiona click Derecho.')

while True:
    try:
        # Obtenemos la URL del Archivo
        print("")
        url_video = input(str(f"{Fore.BLUE}Ingresa el link (url) del video (o escribe 'exit' para salir): {Style.RESET_ALL}"))

        if url_video.lower() == 'exit':
            break

        # Obtenemos el formato del video
        print(f"Si deseas descargarlo como Audio a continuación escribe {Fore.GREEN}'.mp3'{Style.RESET_ALL} de lo contrario presiona Enter.")
        format_video = input(str('Formato:'))

        # Inicialización del Objeto para las descargas
        dw_videotube = YouTube(url_video)

        if format_video == '.mp3':
            format_video = format_video
            print(f"{Fore.GREEN}Descargando archivo en formato {format_video} ...{Style.RESET_ALL}")
            # Obtener el stream de audio en formato MP3
            audio_stream = dw_videotube.streams.filter(only_audio=True).first()
        else:
            format_video = '.mp4'
            print(f"{Fore.GREEN}Descargando archivo en formato {format_video} ...{Style.RESET_ALL}")
            # Obtener el stream de video y audio en formato MP4
            audio_stream = dw_videotube.streams.filter(file_extension='mp4', res='720p').first()

        # Obtener el directorio actual del ejecutable
        script_directory = os.getcwd()

        # Crear el directorio "Archivos" si no existe
        archivos_directory = os.path.join(script_directory, "Archivos")
        os.makedirs(archivos_directory, exist_ok=True)

        # Limpiar el título del video para un nombre de archivo seguro
        video_title = "".join(c for c in dw_videotube.title if c.isalnum() or c.isspace() or c in ['_', '-'])

        # Construir la ruta completa para la descarga en la carpeta "Archivos"
        dw_download_path = os.path.join(archivos_directory, f"{video_title}{format_video}")

        # Descargar el archivo
        audio_stream.download(output_path=archivos_directory, filename=f"{video_title}{format_video}")

        print(f"{Fore.GREEN}El archivo se descargó de manera Exitosa {Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}Error al descargar el video: {e}{Style.RESET_ALL}")

    # Esperar 3 segundos antes de limpiar la pantalla y pedir la próxima descarga
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
