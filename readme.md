
# Playground for Speech-to-Text

Playground for converting Whatsapp's OGA into text. Inspired from https://github.com/Kini218/speech-to-text, the script basically does the following:

* Read the Whatsapp's OGA file and convert it into OGG file. Note that the ffmpeg library is required to be installed in the machine.
* Convert the OGG file into WAV file.
* Start the transcription using Google's speech recognizition.

## Challenge

* We must explicitly provide the language of the audio file when calling ``r.recognize_google`` function in order to get the best result. The problem is that we do not know at a glance on what the language is going to be. Hence it would be ideal if we could call a function to transcribe the audio file without needing to provide hint on the language.

