#!/usr/bin/env python
from os import system
from subprocess import Popen, PIPE

runOnHardware = False

def runTetris():
    if(runOnHardware):
        system("python -m arbalet.apps.tetris -w -ng")
    else:
        system("python -m arbalet.apps.tetris")


def runSnake():
        if(runOnHardware):
            system("python -m arbalet.apps.snake -w -ng")
        else:
            system("python -m arbalet.apps.snake")

def runGifs():
    if(runOnHardware):
        process = Popen(["python", "./images.py", "-w", "-ng"], stdout=PIPE)
    else:
        process = Popen(["python", "./images.py"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    return output


def runColors():
        if(runOnHardware):
            process = Popen(["python", "./colors.py", "-w", "-ng"], stdout=PIPE)
        else:
            process = Popen(["python", "./colors.py"], stdout=PIPE)

        (output, err) = process.communicate()
        exit_code = process.wait()
        return output

def runMenu():
        if(runOnHardware):
            process = Popen(["python", "./menu.py", "-w", "-ng"], stdout=PIPE)
        else:
            process = Popen(["python", "./menu.py"], stdout=PIPE)

        (output, err) = process.communicate()
        exit_code = process.wait()
        return output

while True:
    selection = runMenu()
    if "Tetris" in selection:
        runTetris()
    elif "Snake" in selection:
        runSnake()
    elif "Gifs" in selection:
        runGifs()
    else:
        runColors()
