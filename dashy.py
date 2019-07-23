from morseapi import MorseRobot
from pynput.keyboard import Key, Listener
import random
bot = MorseRobot("E8:3C:9F:0E:20:60")
bot.reset()
bot.connect()
prev = None

bot.say("hi")

def onPress(key):
	global prev
	if key == prev:
		return
	print ('Pressed {0}'.format(key))
	prev = key
	if key == Key.esc:
		bot.stop()
		exit()
	if key == Key.space:
		bot.say("hi")
	if key == Key.up:
		bot.drive(200)
	if key == Key.down:
		bot.drive(-200)
	if key == Key.right:
		bot.spin(-200)	
	if key == Key.left:
		bot.spin(200)
		
def onRelease(key):
	global prev
	print ('Released {0}'.format(key))
	bot.stop()
	prev = None
	
with Listener(on_press=onPress, on_release=onRelease, suppress=True) as l:
	l.join()  
