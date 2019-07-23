import time
import pygatt
from morseapi import MorseRobot
from pynput.keyboard import Key, Listener

prev = None 
speed = 0
rotational_speed = 0

def onPress(key):
	global prev, speed, rotational_speed
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
		speed = 200
		bot.drive(speed, rotational_speed)
	if key == Key.down:
		speed = -200
		bot.drive(speed, rotational_speed)
	if key == Key.left:
		rotational_speed = 200
		bot.drive(speed, rotational_speed)
	if key == Key.right:
		rotational_speed = -200
		bot.drive(speed, rotational_speed)
		
def onRelease(key):
	global prev, speed, rotational_speed
	print ('Released {0}'.format(key))
	if key == Key.up:
		speed = 0
		bot.drive(speed, rotational_speed)
	if key == Key.down:
		speed = 0
		bot.drive(speed, rotational_speed)
	if key == Key.left:
		rotational_speed = 0
		bot.drive(speed, rotational_speed)
	if key == Key.right:
		rotational_speed = 0
		bot.drive(speed, rotational_speed)
	prev = None

with Listener(on_press=onPress, on_release=onRelease, suppress=True) as l:		
	while True:
		try:
			print ("Connecting...")
			bot = MorseRobot("E8:3C:9F:0E:20:60")
			bot.reset()
			bot.connect()
			bot.say("hi")
			prev = None
			l.join()	
		except pygatt.exceptions.NotConnectedError as e:
			print(e)
			time.sleep(1000)
		
			
