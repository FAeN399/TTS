from gtts import gTTS

def text_to_speech(text, output_filename='output.mp3'):
    if not text:
        raise ValueError("Text cannot be empty")
        
    tts = gTTS(text=text, lang='en')
    tts.save(output_filename)
    return True