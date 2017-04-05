#!/usr/bin/env python

import Tkinter
import tkMessageBox
import time
import radiolink

blueButton = "#42c2f4"
greenButton="#48f442"

buttonWidth = 10
buttonHeight = 3

pollInterval = 250

winner = False;

def disableButtons():
    simonSpinButton.config(state="disabled")
    simonForwardButton.config(state="disabled")
    simonBackwardButton.config(state="disabled")
    simonBlinkButton.config(state="disabled")
    simonFlashButton.config(state="disabled")
    simonRainbowButton.config(state="disabled")
    simonCrossEyesButton.config(state="disabled")
    simonSleepButton.config(state="disabled")
    spinButton.config(state="disabled")
    forwardButton.config(state="disabled")
    backwardButton.config(state="disabled")
    blinkButton.config(state="disabled")
    flashButton.config(state="disabled")
    rainbowButton.config(state="disabled")
    crossEyesButton.config(state="disabled")
    sleepButton.config(state="disabled")

def enableButtons():
    simonSpinButton.config(state="normal")
    simonForwardButton.config(state="normal")
    simonBackwardButton.config(state="normal")
    simonBlinkButton.config(state="normal")
    simonFlashButton.config(state="normal")
    simonRainbowButton.config(state="normal")
    simonCrossEyesButton.config(state="normal")
    simonSleepButton.config(state="normal")
    spinButton.config(state="normal")
    forwardButton.config(state="normal")
    backwardButton.config(state="normal")
    blinkButton.config(state="normal")
    flashButton.config(state="normal")
    rainbowButton.config(state="normal")
    crossEyesButton.config(state="normal")
    sleepButton.config(state="normal")

def simonSaysSpin():
    gameMessage.configure(text="Simon Says\n'Spin'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_SPIN)
    game.after(pollInterval, pollRobots)

def simonSaysForward():
    gameMessage.configure(text="Simon Says\n'Forward'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_FORWARD)
    game.after(pollInterval, pollRobots)

def simonSaysBackward():
    gameMessage.configure(text="Simon Says\n'Backward'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_BACKWARD)
    game.after(pollInterval, pollRobots)

def simonSaysBlink():
    gameMessage.configure(text="Simon Says\n'Blink'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_BLINK)
    game.after(pollInterval, pollRobots)

def simonSaysCrossEyes():
    gameMessage.configure(text="Simon Says\n'CrossEyes'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_CROSS_EYE)
    game.after(pollInterval, pollRobots)

def simonSaysFlash():
    gameMessage.configure(text="Simon Says\n'Flash'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_FLASH)
    game.after(pollInterval, pollRobots)

def simonSaysRainbow():
    gameMessage.configure(text="Simon Says\n'Rainbow'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_RAINBOW)
    game.after(pollInterval, pollRobots)

def simonSaysSleep():
    gameMessage.configure(text="Simon Says\n'Sleep'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_SLEEP)
    game.after(pollInterval, pollRobots)

def spin():
    gameMessage.configure(text="Spin")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_SPIN)
    game.after(pollInterval, pollRobots)

def forward():
    gameMessage.configure(text="Forward")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_FORWARD)
    game.after(pollInterval, pollRobots)

def backward():
    gameMessage.configure(text="Backward")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_BACKWARD)
    game.after(pollInterval, pollRobots)

def blink():
    gameMessage.configure(text="Blink")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_BLINK)
    game.after(pollInterval, pollRobots)

def crossEyes():
    gameMessage.configure(text="Cross Eyes")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_CROSS_EYE)
    game.after(pollInterval, pollRobots)

def flash():
    gameMessage.configure(text="Flash")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_FLASH)
    game.after(pollInterval, pollRobots)

def rainbow():
    gameMessage.configure(text="Rainbow")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_RAINBOW)
    game.after(pollInterval, pollRobots)

def sleep():
    gameMessage.configure(text="Sleep")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_SLEEP)
    game.after(pollInterval, pollRobots)

def ackOut():
    radiolink.putRobotsOut()
    ackOutButton.config(state = "disabled")
    game.after(pollInterval, pollRobots)

def ackNotOut():
    radiolink.giveAnotherChance()
    ackNotOutButton.grid_remove()
    gameMessage.config(text = "Let's Play")
    enableButtons();

def ackWin():
    radiolink.robotHasWon()
    ackWinButton.grid_remove()
    game.after(pollInterval, pollRobots)

def newGame():
    global winner
    radiolink.startGame()
    winner = False
    newGameButton.grid_remove()
    ackWinButton.grid_remove()
    enableButtons()
    gameMessage.config(text = "Let's Play")

def pollRobots():

    if not radiolink.pollRobots():
        game.after(pollInterval, pollRobots)

    else:
        handleEndRound()

def handleEndRound():

    global winner

    if winner:
        newGameButton.grid(row = 3, column=2)
        return

    if radiolink.doWeHaveAWinner():
        winner = True;
        robotWon()
        return

    if radiolink.areAllOut():
        haveAnotherGo()
        return

    outList = radiolink.getListWrong()

    if len(outList) > 0:
        robotsOut(outList)
        return

    ackOutButton.grid_remove()
    ackNotOutButton.grid_remove()
    gameMessage.config(text = "Let's Play")
    enableButtons()


def robotsOut(outList):

    if len(outList) == 1:
        message = outList[0] + "\n is out"
    else :
        message = outList[0] + " and \n" + outList[1]

        if len(outList) == 3:
            message = message + " and \n" + outList[2]

        message = message + "\n are out"

    gameMessage.config(text = message)
    ackOutButton.config(state="normal")
    ackOutButton.grid(row=3, column = 2)

def haveAnotherGo():
    gameMessage.config(text = "All the robots \ngot it wrong! \nLet's give them \nanother try...")
    ackNotOutButton.config(state="normal")
    ackNotOutButton.grid(row=3, column=2)

def robotWon():
    message = radiolink.getWinner()
    message = message + "\n is the winner!!!!"
    gameMessage.config(text = message)
    ackWinButton.grid(row=3, column=2)


game = Tkinter.Tk()
game.configure(bg="white")
game.title("Simon Says")

play = Tkinter.Frame(game)
play.configure(bg="white")


simonSpinButton = Tkinter.Button(       play,
                                        text="Simon Says \nSpin",
                                        command=simonSaysSpin,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=blueButton)

simonForwardButton = Tkinter.Button(    play,
                                        text="Simon Says \nForward",
                                        command=simonSaysForward,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=blueButton)

simonBackwardButton = Tkinter.Button(   play,
                                        text="Simon Says \nBackward",
                                        command=simonSaysBackward,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg= blueButton)

simonBlinkButton = Tkinter.Button(      play,
                                        text="Simon Says \nBlink",
                                        command=simonSaysBlink,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=blueButton)

simonCrossEyesButton = Tkinter.Button(  play,
                                        text="Simon Says \nCross eyes",
                                        command=simonSaysCrossEyes,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=blueButton)

simonFlashButton = Tkinter.Button(      play,
                                        text="Simon Says \nFlash",
                                        command=simonSaysFlash,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=blueButton)

simonRainbowButton = Tkinter.Button(    play,
                                        text="Simon Says \nRainbow",
                                        command=simonSaysRainbow,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=blueButton)

simonSleepButton = Tkinter.Button(      play,
                                        text="Simon Says \nSleep",
                                        command=simonSaysSleep,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=blueButton)

spinButton = Tkinter.Button(            play,
                                        text="Spin",
                                        command=spin,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

forwardButton = Tkinter.Button(         play,
                                        text="Forward",
                                        command=forward,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

backwardButton = Tkinter.Button(        play,
                                        text="Backward",
                                        command=backward,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

blinkButton = Tkinter.Button(           play,
                                        text="Blink",
                                        command=blink,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

crossEyesButton = Tkinter.Button(       play,
                                        text="Cross eyes",
                                        command=crossEyes,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

flashButton = Tkinter.Button(           play,
                                        text="Flash",
                                        command=flash,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

rainbowButton = Tkinter.Button(         play,
                                        text="Rainbow",
                                        command=rainbow,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

sleepButton = Tkinter.Button(           play,
                                        text="Sleep",
                                        command=sleep,
                                        width=buttonWidth,
                                        height=buttonHeight,
                                        bg=greenButton)

gameMessage = Tkinter.Label(            play,
                                        text = "Let's Play!",
                                        width =20,
                                        justify = "center")

ackOutButton = Tkinter.Button(          play,
                                        text = "OK",
                                        command = ackOut,
                                        width = 10)

ackWinButton = Tkinter.Button(          play,
                                        text = "OK",
                                        command = ackWin,
                                        width = 10)

ackNotOutButton = Tkinter.Button(       play,
                                        text = "OK",
                                        command = ackNotOut,
                                        width = 10)

newGameButton = Tkinter.Button( play,
                    text = "Start Game",
                    command = newGame,
                    width=15)

gameMessage.configure(bg="white")

gameMessage.config(font = ("Arial", 20))

play.grid()

simonSpinButton.grid(row=0, column=0, padx=5, pady=12)
simonForwardButton.grid(row=0, column=1, padx=5, pady=12)
simonBackwardButton.grid(row=1, column=0, padx=5, pady=12)
simonBlinkButton.grid(row=1, column=1, padx=5, pady=12)
simonCrossEyesButton.grid(row=2, column=0, padx=5, pady=12)
simonFlashButton.grid(row=2, column=1, padx=5, pady=12)
simonRainbowButton.grid(row=3, column=0, padx=5, pady=12)
simonSleepButton.grid(row=3, column=1, padx=5, pady=12)

spinButton.grid(row=0, column=3, padx=5, pady=12)
forwardButton.grid(row=0, column=4, padx=5, pady=12)
backwardButton.grid(row=1, column=3, padx=5, pady=12)
blinkButton.grid(row=1, column=4, padx=5, pady=12)
crossEyesButton.grid(row=2, column=3, padx=5, pady=12)
flashButton.grid(row=2, column=4, padx=5, pady=12)
rainbowButton.grid(row=3, column=3, padx=5, pady=12)
sleepButton.grid(row=3, column=4, padx=5, pady=12)

gameMessage.grid(row=0, rowspan=3, column=2, padx=5, pady=12)

radiolink.setUpLink()
radiolink.startGame()


game.mainloop()
