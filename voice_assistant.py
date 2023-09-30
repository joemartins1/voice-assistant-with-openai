import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "VOTRE_API_KEY"

# Initialisation
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
syst_init = {"role":"system", "content": "Tu es un assistant spécialisé en mini plantes"}
add_rlhf = [syst_init]

while True:
  # Input
  with sr.Microphone() as source:
    print("Ecoute...")
    audio = r.listen(source)
    
  # Completion
  user_text = r.recognize_google(audio, language="fr-FR")
  print(user_text)
  #user_text = input("User: ")
  user_text_format = {"role":"user", "content": user_text}
  add_rlhf.append(user_text_format)
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = add_rlhf )
  response = completion.choices[0].message.content
  print("IA: ", response)

  # Output vocal
  engine.setProperty('voice', voices[0].id)
  engine.say(response)
  engine.runAndWait()
  add_rlhf.append({"role":"assistant", "content": response})