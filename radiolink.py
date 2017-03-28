#!/usr/bin/env python

import time
from RF24 import *
import RPi.GPIO as GPIO

irq_gpio_pin = None

radio = RF24(22, 0);

ROBOT_NOP       = 0x00
RADIO_SORBET    = 0x80

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
redBot.name = "Red Robot"
greenBot.address = bytearray([0xCA, 0xCA, 0xCA, 0xCA, 0x02])
greenBot.name = "Green Robot"
blueBot.address = bytearray([0xCA, 0xCA, 0xCA, 0xCA, 0x03])
blueBot.name = "Blue Robot"
pinkBot.address = bytearray([0xCA, 0xCA, 0xCA, 0xCA, 0x04])
pinkBot.name = "Pink Robot"

wrongBots = []

gameBots = [redBot, blueBot, greenBot, pinkBot]

def send(bot, packet):
    ack = 0
    radio.stopListening()
    radio.openWritingPipe(bot.address)
    radio.write(packet)
    if(radio.available()):
        ack = ord(radio.read(1))
    radio.write(bytearray([RADIO_SORBET]))
    if(radio.available()):
        radio.read(1)
    return ack


def sendGameInstruction(simon, instruction):

    wrongBots = []

    if simon:
        instruction = instruction | SIMON_SAYS
    else:
        instruction = instruction | UNSIMON_SAYS

    packet = bytearray([instruction])

    for bot in gameBots:

        if bot.inPlay:
            bot.busy = True
            bot.wrong = False
            send(bot, packet)


def isRobotPresent(bot):

    for i in range(3):

        if send(bot, bytearray([GO_IDLE | MUST])):
            return True

    return False


def sendCommand(command):

    packet = bytearray([command | MUST])

    for bot in gameBots:

        if bot.inPlay:
            send(bot, packet)


def pollRobots():

    poll = bytearray([ROBOT_NOP])
    finished = True

    for bot in gameBots:

        if bot.inPlay and bot.busy:
            response = send(bot, poll)

            if response == I_AM_IDLE:
                bot.busy = False
            if response == I_AM_WRONG:
                bot.busy = False
                bot.wrong = True
            if response == I_AM_BUSY:
                finished = False

    return finished


def areAllOut():
    return (len(wrongBots) == countRobotsInPlay())


def getListWrong():
    wrongList = []
    for bot in gameBots:
        if bot.inPlay and bot.wrong:
            wrongList.append(bot.name)

    return wrongList


def doWeHaveAWinner():
    return (countRobotsInPlay() == 1)


def getWinner():
    for bot in gameBots:
        if bot.inPlay:
            return bot.name


def putRobotsOut():

    for bot in gameBots:
        if bot.inPlay and bot.wrong :
            bot.inPlay = False
            send(bot, bytearray([MUST | THIS_BOT_OUT]))
        elif bot.inPlay and not bot.wrong :
            bot.busy = True
            send(bot, bytearray([MUST | OTHER_BOT_OUT]))


def giveAnotherChance():

    for bot in gameBots:
        if bot.inPlay:
            send(bot, bytearray([MUST | GO_IDLE]))


def robotHasWon():

    for bot in gameBots:
        if bot.inPlay:
            send(bot, bytearray([MUST | BOT_WINS]))
            bot.busy = True


def setUpLink():

    radio.begin()
    radio.setAutoAck(1)
    radio.enableAckPayload()
    radio.enableDynamicPayloads()
    radio.setRetries(5,15)
    while(radio.available()):
        radio.read(1)
    radio.stopListening()


def startGame():

    for bot in gameBots:
        #bot.inPlay = isRobotPresent(bot)
        bot.inPlay = True
        bot.busy = False
        bot.wrong = False

    sendCommand(GO_IDLE)


def countRobotsInPlay():

    return len([b for b in gameBots if b.inPlay])
