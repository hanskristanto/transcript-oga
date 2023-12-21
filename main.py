import os
import speech_recognition as sr
import subprocess
from pydub import AudioSegment


def prepare_voice_file(path: str) -> str:
    """
    Converts the input audio file to WAV format if necessary and returns the path to the WAV file.
    """
    if os.path.splitext(path)[1] == '.wav':
        return path
    elif os.path.splitext(path)[1] in ('.mp3', '.m4a', '.ogg', '.oga', '.flac'):
        audio_file = AudioSegment.from_file(
            path, format=os.path.splitext(path)[1][1:])
        wav_file = os.path.splitext(path)[0] + '.wav'
        audio_file.export(wav_file, format='wav')
        return wav_file
    else:
        raise ValueError(
            f'Unsupported audio format: {format(os.path.splitext(path)[1])}')


def transcribe_audio(audio_data) -> str:
    """
    Transcribes audio data to text using Google's speech recognition API.
    """
    r = sr.Recognizer()
    text = r.recognize_google(audio_data, language='ES')
    return text


def write_transcription_to_file(text, output_file) -> None:
    """
    Writes the transcribed text to the output file.
    """
    with open(output_file, 'w') as f:
        f.write(text)


def speech_to_text(input_path: str, output_path: str) -> None:
    """
    Transcribes an audio file at the given path to text and writes the transcribed text to the output file.
    """
    wav_file = prepare_voice_file(input_path)
    with sr.AudioFile(wav_file) as source:
        audio_data = sr.Recognizer().record(source)
        text = transcribe_audio(audio_data)
        write_transcription_to_file(text, output_path)
        print('Transcription is ready at {}'.format(output_path))


def convert_oga_to_ogg(input_path: str, output_path: str) -> None:
    """
    Convert OGA file from Whatsapp's voice messages to OGG
    """
    process = subprocess.run(['ffmpeg', '-i', whatsapp_voice_input, converted_ogg_input])


if __name__ == '__main__':
    whatsapp_voice_input = 'test.oga'
    transcribe_output = 'test.txt'
    converted_ogg_input = 'test.ogg'
    
    convert_oga_to_ogg(whatsapp_voice_input, converted_ogg_input)
    speech_to_text(converted_ogg_input, transcribe_output)
    os.system('rm test.ogg test.wav')