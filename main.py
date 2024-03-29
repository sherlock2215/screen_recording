import cv2
import numpy as np
import pyautogui
import time
import sounddevice as sd
import wave
import threading
def record_audio(frames):
    duration = 10  # Adjust as needed
    fs = 44100
    print("* Recording audio...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    frames.extend(myrecording)
    print("* Finished recording audio")
    wf = wave.open("audio.wav", 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
SCREEN_SIZE=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("output.avi",fourcc,20.0,(SCREEN_SIZE))
fps=120
prev=0

while True:
    time_elapsed=time.time()-prev
    img=pyautogui.screenshot()
    if time_elapsed>1.0/fps:
        prev=time.time()
        frame=np.array(img)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
    cv2.waitKey(100)
cv2.destroyAllWindows()
out.release()
audio_thread.join()