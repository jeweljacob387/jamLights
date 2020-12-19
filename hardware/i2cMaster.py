from frames import Frame
from nodes import nodes
from i2cHelper import writeToDevice
from time import sleep, strftime, time
import re
import os

startTime = time()


def setFrame(frame: Frame):
    # os.system('clear')
    for node in nodes:
        if node.name in [frameNode.name for frameNode in frame.nodes]:
            turnOnNode(node)
        else:
            turnOffNode(node)
    # print('\033[37m', "...")
    sleep(196.5/1000)


def turnOnNode(node):
    writeToDevice(node.group, node.deviceIndex, 1)
    # print('\033[32m', "Turn on group", node.group, "'s device", node.deviceIndex,
        #   "at", time() - startTime)
    return


def turnOffNode(node):
    writeToDevice(node.group, node.deviceIndex, 0)
    # print('\033[31m', "Turn off group", node.group, "'s device", node.deviceIndex,
        #   "at",  time() - startTime)
    return
