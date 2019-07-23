from morseapi import MorseRobot
import random
bot = MorseRobot("E8:3C:9F:0E:20:60")
bot.connect()
while True:
	bot.eye(random.random() * 256)
	bot.turn(45)
	bot.say("hi")
