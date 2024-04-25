import requests
import base64
import pygame
from io import BytesIO

ENDPOINT = 'https://tiktok-tts.weilnet.workers.dev'
MAX_TEXT_LENGTH = 300

def generate_audio(text, voice):
    url = f'{ENDPOINT}/api/generation'
    data = {'text': text, 'voice': voice}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        audio_data = response.json()['data']
        return base64.b64decode(audio_data)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def main():
    text = input("Enter the text you want to convert to audio: ")
    voice = 'en_us_001'

    audio_data = generate_audio(text, voice)
    if audio_data:
        # Save audio to a BytesIO object
        audio_bytes = BytesIO(audio_data)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load audio from BytesIO object
        pygame.mixer.music.load(audio_bytes)
        
        # Play audio
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            continue

        print("Audio generated and played successfully!")
    else:
        print("Failed to generate audio.")

if __name__ == "__main__":
    main()
