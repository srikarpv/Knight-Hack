from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
import pyaudio
import wave
import sys
import base64
import json

def get_speech_service_obj():
    """
    Returns an object that can execute Google Cloud API services
    """
    DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                     'version={apiVersion}')
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)
    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)


def speech_to_text(speech_content_file):
    with open(speech_content_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())
    speech_service_obj = get_speech_service_obj()
    service_request = speech_service_obj.speech().syncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRate': 44100,
                'languageCode': 'en-US',
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })

    service_response = service_request.execute()
    print(json.dumps(service_response, indent=2))

def record_audio_file():
    """
    Records audio and writes the audio content to a file

    Reference: https://gist.github.com/mabdrabo/8678538
    """
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "file.wav"
    audio = pyaudio.PyAudio()
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

if __name__ == '__main__':
    record_audio_file()
    speech_to_text("file.wav")
