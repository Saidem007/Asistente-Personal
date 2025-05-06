#SpeechRecognition
#SpaCy python 3.7
#google-api-python-client:
#PyAutoGUI y Selenium
#Requests
#plyer
#Coqui TTS
#pywinauto
#subprocess 
#pywhatkit
#Vocode
import pyautogui
import pyttsx3
import subprocess
import speech_recognition as sr
import spacy
nlp = spacy.blank("es")
engine = pyttsx3.init()
def convertidor():
    
    # Crear una instancia del reconocedor de voz
    Almacenador = sr.Recognizer()

    # Usar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Escuchando...")
        # Ajustar el nivel de ruido ambiental
        Almacenador.adjust_for_ambient_noise(source)
         # Escuchar el audio
        audio = Almacenador.listen(source)
        # Convierte el audio a texto
        texto = Almacenador.recognize_google(audio, language="es-ES")  
        x=nlp(texto.lower())
        return x
        
        
    
def verificador(x): 
        #Iteramos la variable "token" en el npl en texto "x"       
        for token in x:
            #Convertimos cada palabra en texto y identifica si hay "abrir" o "abre" 
            if token.text in ["abrir", "abre"]:
                #Iteramos la variable "ent" en el npl en texto "x" para identificar que quiere abrir
                for ent in x:
                    if ent.text == "notepad":
                        subprocess.run(["notepad.exe"])
                        hablar("Abriendo Notepad")
                    elif ent.text == "chrome":
                        subprocess.run(['start', 'chrome'], shell=True)
                        hablar("Abriendo Chrome")
            elif token.text == "escribir":
                pyautogui.write("Hola desde el asistente!")
                hablar("Escribiendo texto")
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()



