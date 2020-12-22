from nodes import Node, nodes
from groups import groups
from json import load

frames = []


class Frame:
    def __init__(self, nodes):
        self.nodes = nodes

def loadFrames(fileName):
    frames.clear()
    with open('/home/pi/xmas2k20/jamLights/framesJsons/'+fileName+'.json') as file:
        data = load(file)

    framesData = data['groups']
    duration = len(framesData[0]['nodes'][0]['frameSates'])
    print(duration)
    for time in range(duration):
        nodesOnInFrame = []
        for group in framesData:
            for node in group['nodes']:
                nodeName = str(groups[group['name']]) + \
                    '-'+str(node['deviceIndex'])
                mappedNode = Node(
                    nodeName, groups[group['name']], node['deviceIndex']
                )
                if nodeName not in [savedNode.name for savedNode in nodes]:
                    nodes.add(mappedNode)
                if node['frameSates'][time]:
                    nodesOnInFrame.append(mappedNode)
        frames.append(Frame(nodesOnInFrame))
