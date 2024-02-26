import speech_recognition as sr
import wikipedia
import openai
import youtube_dl
import pyttsx3
import webbrowser
from googletrans import Translator
from youtube_search import YoutubeSearch
import webview
engine =pyttsx3.init()
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0) #valor entre 0.0 y 1.0
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)


def wiki():
    print ("wikipedia está en línea")
    engine.say("wikipedia está en línea")
    engine.runAndWait()
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        print("Usted dijo: " + r.recognize_google(audio, language="es-ES"))
    except sr.UnknownValueError:
        print("Could not understand audio")
        pepe()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    wikipedia.set_lang("es")
    
    
    engine.say(wikipedia.summary(r.recognize_google(audio, language="es-ES"), sentences=3))
    print(wikipedia.summary(r.recognize_google(audio, language="es-ES"), sentences=3))
    engine.runAndWait()

    wikipedia.set_lang("es")
    
    engine.say(wikipedia.summary(r.recognize_google(audio, language="es-ES"), sentences=3))
    print(wikipedia.summary(r.recognize_google(audio, language="es-ES"), sentences=3))
    engine.runAndWait()
    return

def chat():
    print ("abriendo chat gpt")
    engine.say("abriendo chat gpt")
    engine.runAndWait()
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio_data = r.record(source, duration=3, offset=1)   

    try:
        texto= r.recognize_google(audio_data, language="es-ES")
        print("Usted dijo: " + r.recognize_google(audio_data, language="es-ES"))
    except sr.UnknownValueError:
        print("Could not understand audio")
        #pepe()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    engine.say("buscando: un momento, por favor")
    engine.runAndWait()        
    openai.api_key="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"
    respuesta = openai.Completion.create(engine="text-davinci-003",
                         prompt=texto,
                         n=1, max_tokens=2048)
    print(respuesta.choices[0].text)
    engine.say(respuesta.choices[0].text)
    engine.runAndWait() 
    return


import speech_recognition as sr
import youtube_dl
import webbrowser

def reconocer_voz():
       # Crear un objeto de reconocimiento de voz
    reconocimiento = sr.Recognizer()

    with sr.Microphone() as source:
        engine.say("Estoy en youtube, di el nombre de la canción que quieres escuchar...")
        engine.runAndWait()
        audio = reconocimiento.listen(source)

    try:
        # Utilizar el reconocimiento de voz de Google para convertir el audio en texto
        texto = reconocimiento.recognize_google(audio, language="es")

        # Buscar la canción en YouTube
        resultados = YoutubeSearch(texto, max_results=1).to_dict()
        if len(resultados) > 0:
            video_id = resultados[0]['id']
            url = f"https://www.youtube.com/watch?v={video_id}"
            # Abrir la URL en el navegador predeterminado para reproducir el video
            webbrowser.open(url)
            print("Canción encontrada y reproducida.")
        else:
            print("No se encontraron resultados para la canción.")

    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print(f"Error al enviar la solicitud al servicio de reconocimiento de voz: {e}")

    return





def escuchar_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        engine.say("DI ALGO")
        engine.runAndWait()
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
        return ""
    except sr.RequestError:
        print("No se pudo obtener respuesta del servicio de reconocimiento de voz.")
        return ""

def traducir(texto, idioma_destino):
    translator = Translator()
    traduccion = translator.translate(texto, dest=idioma_destino)
    return traduccion.text

def obtener_idioma_destino():
    idiomas = {
        "inglés": "en",
        "francés": "fr",
        "español": "es",
        "alemán": "de",
        "italiano": "it",
        "portugués": "pt",
        "chino": "zh-cn",
        "japonés": "ja",
        "coreano": "ko"
    }

    while True:
        
        engine.say("Di el idioma al que quieres traducir:")
        engine.runAndWait()
        frase = escuchar_audio()

        if frase.lower() == "salir":
            return None

        for idioma, codigo in idiomas.items():
            if idioma in frase.lower():
                return codigo

        print("Idioma no reconocido. Por favor, intenta de nuevo.")

def ejecutar_traductor_por_comando_voz():
    idioma_destino = obtener_idioma_destino()

    if idioma_destino:
        while True:
            engine.say("Di la frase que quieres traducir")
            engine.runAndWait()
            frase = escuchar_audio()

            if frase.lower() == "salir":
                break

            print("Frase detectada:", frase)

            resultado = traducir(frase, idioma_destino)
            engine.say("La traduccion es:")
            engine.say(resultado)
            print(resultado)
            engine.runAndWait()
            print()
            return



def abrir_cine_colombia():
    webview.create_window("Cine Colombia", "https://www.cinecolombia.com/")
    webview.start()
    return

import speech_recognition as sr
import webbrowser

def buscar_en_google():
    reconocimiento = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di lo que quieres buscar en Google...")
        audio = reconocimiento.listen(source)

    try:
        busqueda = reconocimiento.recognize_google(audio, language="es")
        print(f"Realizando búsqueda en Google: {busqueda}")
        busqueda = busqueda.replace(" ", "+")
        url = f"https://www.google.com/search?q={busqueda}"
        webbrowser.open(url)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print(f"Error al enviar la solicitud al servicio de reconocimiento de voz: {e}")
    return

# Llamada a la función para buscar en Google








while 1:
    engine.say("hola señor: en qué puedo servirle")
    engine.runAndWait()
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio_data = r.record(source, duration=3, offset=1)   

    try:
        texto= r.recognize_google(audio_data, language="es-ES")
        print("Usted dijo: " + r.recognize_google(audio_data, language="es-ES"))
    except sr.UnknownValueError:
        print("Could not understand audio")
        #pepe()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    

    if "Wikipedia" in texto:
        wiki()
    if "chat gpt" in texto:
        chat()
    if "YouTube" in texto:
        reconocer_voz()
    if "Traducir" in texto:
        ejecutar_traductor_por_comando_voz()
    if "cine" in texto:
        abrir_cine_colombia()
    if "Buscar" in texto:
        buscar_en_google()
    if "casa inteligente" in texto:
        print ("la activación de domótica para casa inteligente está lista")
        engine.say("la activación de domótica para casa inteligente está lista")
        engine.runAndWait()