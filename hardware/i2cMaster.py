from frames import Frame
import nodes
from time import sleep, strftime, time
import re
import os

nodesList = []
startTime = time()


def setFrame(frame: Frame):
    os.system('clear')
    for node in nodesList:
        if node in frame.nodes:
            turnOnNode(node)
        else:
            turnOffNode(node)
    print('\033[37m', "...")
    sleep(frame.duration/1000.0)


def setNodesList():
    global nodesList
    nodeNames = [node for node in nodes.__dict__.keys()
                 if not re.search('^_', node)][2:]
    for nodeName in nodeNames:
        nodesList.append(getattr(nodes, nodeName))
    # print("Total ",len(nodesList), " nodes")


def turnOnNode(node: nodes.Node):
    print('\033[32m', "Turn on group", node.group, "'s device", node.deviceIndex,
          "at", time() - startTime)


def turnOffNode(node: nodes.Node):
    print('\033[31m', "Turn off group", node.group, "'s device", node.deviceIndex,
          "at",  time() - startTime)
