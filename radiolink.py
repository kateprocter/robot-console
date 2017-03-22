#!/usr/bin/env python

import time
from RF24 import *
import RPi.GPIO as GPIO

irq_gpio_pin = None

radio = RF24(22, 0);

ROBOT_NOP       = 0x00

SIMON_SAYS      = 0x10
UNSIMON_SAYS    = 0x20
MUST            = 0x40

COMMAND_MASK    = 0x0F

SIMON_SPIN      = 0x00
SIMON_FORWARD   = 0x01
SIMON_BACKWARD  = 0x02
SIMON_FLASH     = 0x03
SIMON_RAINBOW   = 0x04
SIMON_SLEEP     = 0x05
SIMON_BLINK     = 0x06
SIMON_CROSS_EYE = 0x07
SIMON_MAX       = 0x08

GO_IDLE         = 0x09
THIS_BOT_OUT    = 0x0A
OTHER_BOT_OUT   = 0x0B
BOT_WINS        = 0x0C

I_AM_BUSY       = 0x01
I_AM_IDLE       = 0x02
I_AM_WRONG      = 0x03

class Robot:
	pass

redBot = Robot()
blueBot = Robot()
greenBot = Robot()
pinkBot = Robot()

redBot.address = bytearray([0xCA, 0xCA, 0xCA, 0xCA, 0x01])
blueBot.address = bytearray([0xCA, 0xCA, 0xCA, 0xCA, 0x02])
greenBot.address = bytearray([0xCA, 0xCA, 0xCA, 0xCA, 0x03])
pinkBot.address = bytearray([0xCA, 0xCA, 0xCA, 0xCA, 0x04])

gameBots = [redBot, blueBot, greenBot, pinkBot]


def sendGameInstruction(simon, instruction):

	
	if simon:
		instruction = instruction | SIMON_SAYS
	else:
	        instruction = instruction | UNSIMON_SAYS

	packet = bytearray([instruction])

    	for bot in gameBots:

        	if bot.inPlay:
            		radio.openWritingPipe(bot.address)
            		radio.write(packet)


def sendCommand(command):

    	packet = bytearray([command | MUST])
		 
    	for bot in gameBots:

        	if bot.inPlay:
            		radio.openWritingPipe(bot.address)
            		radio.write(packet)

def setUpLink():

	radio.begin()
	radio.setAutoAck(1)
	radio.enableAckPayload()
	radio.enableDynamicPayloads()
	radio.setRetries(5,15)
	radio.stopListening()


def startGame():

    	for bot in gameBots:
        	bot.inPlay = True

    	sendCommand(GO_IDLE)


def countRobotsInPlay():

	return len([b for b in gameBots if b.inPlay])

	


