#!/usr/bin/env python
from os import system
from subprocess import Popen, PIPE

def runTetris():
    system("python -m arbalet.apps.tetris -w -ng")

def runSnake():
        system("python -m arbalet.apps.snake -w -ng")

def runColors():
        #system("python ./menu.py")
        process = Popen(["python", "./colors.py", "-w", "-ng"], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        return output

def runMenu():
        #system("python ./menu.py")
        process = Popen(["python", "./menu.py", "-w", "-ng"], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        return output

while True:
    selection = runMenu()
    if "Tetris" in selection:
        runTetris()
    elif "Snake" in selection:
        runSnake()
    else:
        runColors()
