# from pocketsphinx import StreamSpeech
# path = "D:\\SoundsYoutube\\video_Hg5l7h4hNhs.wav"
# f = open(path, 'rb')

# def callback():
#     return f.read(2048)

# for phrase in StreamSpeech(callback=callback): print(phrase)

# # importing libraries 
# import speech_recognition as sr 
# import os 
# from pydub import AudioSegment
# from pydub.silence import split_on_silence

# # create a speech recognition object
# r = sr.Recognizer()

# # a function that splits the audio file into chunks
# # and applies speech recognition
# def get_large_audio_transcription(path):
#     """
#     Splitting the large audio file into chunks
#     and apply speech recognition on each of these chunks
#     """
#     # open the audio file using pydub
#     sound = AudioSegment.from_wav(path)  
#     # split audio sound where silence is 700 miliseconds or more and get chunks
#     chunks = split_on_silence(sound,
#         # experiment with this value for your target audio file
#         min_silence_len = 500,
#         # adjust this per requirement
#         silence_thresh = sound.dBFS-14,
#         # keep the silence for 1 second, adjustable as well
#         keep_silence=500,
#     )
#     folder_name = "audio-chunks"
#     # create a directory to store the audio chunks
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     whole_text = ""
#     # process each chunk 
#     for i, audio_chunk in enumerate(chunks, start=1):
#         # export audio chunk and save it in
#         # the `folder_name` directory.
#         chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
#         audio_chunk.export(chunk_filename, format="wav")
#         # recognize the chunk
#         with sr.AudioFile(chunk_filename) as source:
#             audio_listened = r.record(source)
#             # try converting it to text
#             try:
#                 text = ""
#                 print("*--------Before ------------")
#                 print(text)
#                 text = r.recognize_google(audio_listened, show_all=True)
#                 print("*--------After ------------")
#                 print(text)
#             except sr.UnknownValueError as e:
#                 print("Error:", str(e))
#             else:
#                 print(text)
#                 # text = f"{text.capitalize()}. "
#                 # print(chunk_filename, ":", text)
#                 whole_text += " ".join(text)
#     # return the text for all chunks detected
#     return whole_text

# path = "D:\\SoundsYoutube\\video_Hg5l7h4hNhs.wav"
# print("\nFull text:", get_large_audio_transcription(path))


import speech_recognition as sr

path = "D:\\SoundsYoutube\\output3.wav"
# obtain audio from the microphone
r = sr.Recognizer()
audio_file = sr.AudioFile(path)
with audio_file as source:
    print("Say something!")
    audio = r.listen(source)

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said : \n " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said : \n" + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



# #import library
# import speech_recognition as sr
# import wave
# import contextlib
# # Initialize recognizer class (for recognizing the speech)
# r = sr.Recognizer()

# # Reading Audio file as source
# # listening the audio file and store in audio_text variable

# fname = 'D:\\SoundsYoutube\\output.wav'
# duration = 0

# with contextlib.closing(wave.open(fname,'r')) as f:
#     frames = f.getnframes()
#     rate = f.getframerate()
#     duration = frames / float(rate)
#     print(duration)

# audio_file = sr.AudioFile(fname)
# with audio_file as source:
#     r.adjust_for_ambient_noise(source, duration=0.5)
#     audio_file = r.record(source)
#     result = r.recognize_google(audio_data=audio_file, language="en-IN")
# text = result
# print(text)

# #     audio_text = r.listen(source)
    
# # # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
# #     try:
# #         print(audio_text)
# #         # using google speech recognition
# #         text = r.recognize_google(audio_text, language="en-EN", show_all=True)
# #         print('Converting audio transcripts into text ...')
# #         print(text)
# #     # except sr.UnknownValueError as e:
# #     #     print(e)
# #     #     print('Sorry.. run again... ')
# #     except sr.RequestError as ex:
# #         print(ex) 