from java.io import File
from javax.sound.sampled import AudioInputStream
from javax.sound.sampled import AudioSystem
from javax.sound.sampled import Clip
from java.lang import Thread,Runnable

file = File("C:\\Users\\Sony\\Desktop\\jython-prac-prog\\network\\sample_audio.wav")
stream = AudioSystem.getAudioInputStream(file)
clip = AudioSystem.getClip()
print (type(clip))

class f(Runnable):
	def __init__(self,x):
		self.x = x

	def run(self):
		
		self.x.open(stream)
		self.x.start()
		

g = f(clip)
k = Thread(g)
k.start()
Thread.sleep(500)
print("End")
#Thread.sleep(35000)
stream.close()