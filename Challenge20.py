import base64
import wave

string = input("Enter the string to decode")
string.replace("\n" , "")

decoded = base64.b64decode(string, altchars = None, validate = False)

indian = open("indian.wav" , "wb")
indian.write(audio)

w = wave.open('indian.wav', 'rb')

h = wave.open("result.wav", "wb")

print(w.getnchannels())
print(w.getsampwidth())
print(w.getframerate())
h.setnchannels(w.getnchannels())
h.setsampwidth(w.getsampwidth()//2)
h.setframerate(w.getframerate()*2)
frames = w.readframes(w.getnframes())
wave.big_endiana = 1
h.writeframes(frames)

h.close()
