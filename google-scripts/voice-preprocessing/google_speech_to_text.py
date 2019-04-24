#!/usr/bin/env python

import io
import os
import glob
import json

# Imports the Google Cloud client library
# [START speech_python_migration_imports]
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
    
def get_text(file_name):

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        #sample_rate_hertz=16000,
        language_code='en-US')
    
    #instantiate a client
    client = speech.SpeechClient()
    
    # Detects speech in the audio file
    response = client.recognize(config, audio)
    text = ""

    for result in response.results:
        text += result.alternatives[0].transcript
        #print('Transcript: {}'.format(result.alternatives[0].transcript))
    return text

def run_quickstart(file_dir):
    
    
    errors={}
    i = 0
    j = 0
    k = 0
    
    for direc in os.listdir(file_dir):
        print(direc)
        loc=os.path.join(file_dir,direc)
        os.chdir(loc)
        try:
            #file = glob.glob("*.wav")[0]
            file_name = os.path.join(file_dir,direc,'path.wav')
            text = get_text(file_name) 
            f = open(os.path.join(file_dir,direc,"text.txt"), "w")
            f.write(text)
            f.close()
            i = i+1
        except Exception as o:
            print(o)
            j = j+1            
            errors[loc]=str(o)
        
        k = k+1
        
    print("Out of total {} files, converted {} files successfully to text and {} files errored out!".format(k,i,j))
    # f = open(os.path.join(file_dir,"error.json"), "w")
    with open(os.path.join(file_dir,'error.json'), 'w') as outfile:
        json.dump(errors, outfile)
    return errors
        
      
    

if __name__ == '__main__':
    file_dir = 'file directory' 
    run_quickstart(file_dir)
