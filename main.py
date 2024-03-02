import PySimpleGUI as sg
from elevenlabs import clone, generate, play
from openai import OpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv

#Getting API keys from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Api keys for both openAI and ElevenLabs
openAiKey = os.environ.get("OPENAI_API_KEY")
elevenLabKey = os.environ.get("ELEVEN_API_KEY")

client = OpenAI(api_key=openAiKey,)

#Function that takes in the users submitted MP3 and will create a new voice.
def cloneVoice(usermp3, vName, vDescription):
    voice = clone(
        api_key=elevenLabKey,
        name=vName,
        description=vDescription,
        files=[usermp3],
    )
    sg.popup("Voice Successfully Created")
    



# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)


layout = [
    [sg.Text("Input MP3 Audio File"), sg.Input(key="MP3"), sg.FileBrowse(file_types=(("MP3 Files", "*.mp3*")))],
    [sg.Text("Voice Name"), sg.Input(key="name")],
    [sg.Multiline(size=(30, 5), key="textbox")],  # identify the multiline via key option
    [sg.Exit(), sg.Button("Clone MP3 Voice")],
]

window = sg.Window("FriendAi", layout)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Clone MP3 Voice":
        cloneVoice(values["MP3"], values["name"], values["textbox"])
window.close()

    