import click

import speech_recognition as sr

class AudioRecorder():
    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    
    def run(self):        
        with self.microphone as source:
            click.echo("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            click.echo("Speak now...")
            audio = self.recognizer.listen(source)
        try:
            click.echo("Transcribing...")
            transcription = self.recognizer.recognize_google(audio)
            click.secho(transcription, fg='blue')
            result = transcription
        except sr.UnknownValueError:
            click.echo("Google Speech Recognition could not understand audio")
            result = None
        except sr.RequestError as e:
            click.echo(f"Could not request results from Google Speech Recognition service; {e}")
            result = None
        return result

