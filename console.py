#!/usr/bin/env python

import Tkinter
import tkMessageBox
import time
import radiolink

blueButton = "#42c2f4"
greenButton="#48f442"

buttonWidth = 10
buttonHeight = 2

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
    enableButtons()

def simonSaysForward():
    gameMessage.configure(text="Simon Says\n'Forward'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_FORWARD)	
    enableButtons()

def simonSaysBackward():
    gameMessage.configure(text="Simon Says\n'Backward'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_BACKWARD)	
    enableButtons()

def simonSaysBlink():
    gameMessage.configure(text="Simon Says\n'Blink'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_BLINK)	
    enableButtons()

def simonSaysCrossEyes():
    gameMessage.configure(text="Simon Says\n'CrossEyes'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_CROSS_EYE)
    enableButtons()

def simonSaysFlash():
    gameMessage.configure(text="Simon Says\n'Flash'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_FLASH)	
    enableButtons()

def simonSaysRainbow():
    gameMessage.configure(text="Simon Says\n'Rainbow'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_RAINBOW)	
    enableButtons()

def simonSaysSleep():
    gameMessage.configure(text="Simon Says\n'Sleep'")
    disableButtons()
    radiolink.sendGameInstruction(True, radiolink.SIMON_SLEEP)	
    enableButtons()

def spin():
    gameMessage.configure(text="Spin")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_SPIN)
    enableButtons()
    
def forward():
    gameMessage.configure(text="Forward")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_FORWARD)	
    enableButtons()

def backward():
    gameMessage.configure(text="Backward")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_BACKWARD)
    enableButtons()

def blink():
    gameMessage.configure(text="Blink")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_BLINK)
    enableButtons()

def crossEyes():
    gameMessage.configure(text="Cross Eyes")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_SPIN)
    enableButtons()

def flash():
    gameMessage.configure(text="Flash")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_FLASH)
    enableButtons()

def rainbow():
    gameMessage.configure(text="Rainbow")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_RAINBOW)
    enableButtons()

def sleep():
    gameMessage.configure(text="Sleep")
    disableButtons()
    radiolink.sendGameInstruction(False, radiolink.SIMON_SLEEP)
    enableButtons()

def ack():
    ackButton.grid_remove()
    enableButtons()
    gameMessage.configure(text = "Let's Play!")

def robotsOut(red, green, blue, pink):

    out = 0
    message = ""


    if red:
        message = message + "Red Robot"
        out = out + 1

    if green:
        if out>0:
            message = message + " and \nGreen Robot"
        else:
            message = message + "Green Robot"
        
        out = out + 1
        
    if blue:
        if out > 0:
            message = message + "and \nBlue Robot"
        else:
            message = "Blue Robot"
        
        out = out + 1

    if pink:
        if out > 0:
            message = message + "and \nPink Robot"
        else:
            message = "Pink Robot"

        out = out + 1

    if out > 1:
        message = message + " are out!"

    else:
        message = message + " is out!"


    gameMessage.config(text = message)
    ackButton.grid(row=3, column = 2)
        
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

ackButton = Tkinter.Button(             play,
                                        text = "OK",
                                        command = ack,
                                        width = 10)

gameMessage.configure(bg="white")

gameMessage.config(font = ("Arial", 20))

play.grid()

simonSpinButton.grid(row=0, column=0, padx=5, pady=10)
simonForwardButton.grid(row=0, column=1, padx=5, pady=10)
simonBackwardButton.grid(row=1, column=0, padx=5, pady=10)
simonBlinkButton.grid(row=1, column=1, padx=5, pady=10)
simonCrossEyesButton.grid(row=2, column=0, padx=5, pady=10)
simonFlashButton.grid(row=2, column=1, padx=5, pady=10)
simonRainbowButton.grid(row=3, column=0, padx=5, pady=10)
simonSleepButton.grid(row=3, column=1, padx=5, pady=10)

spinButton.grid(row=0, column=3, padx=5, pady=10)
forwardButton.grid(row=0, column=4, padx=5, pady=10)
backwardButton.grid(row=1, column=3, padx=5, pady=10)
blinkButton.grid(row=1, column=4, padx=5, pady=10)
crossEyesButton.grid(row=2, column=3, padx=5, pady=10)
flashButton.grid(row=2, column=4, padx=5, pady=10)
rainbowButton.grid(row=3, column=3, padx=5, pady=10)
sleepButton.grid(row=3, column=4, padx=5, pady=10)

gameMessage.grid(row=0, rowspan=3, column=2, padx=5, pady=10)

radiolink.setUpLink()
radiolink.startGame()


game.mainloop()


