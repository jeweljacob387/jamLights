import nodes
from json import load


class Frame:
    def __init__(self, nodes, duration):
        self.nodes = nodes
        self.duration = duration


frames = [
    Frame([nodes.tree1, nodes.streetLight3], 10000),
    Frame([nodes.tree2], 2000),
    Frame([nodes.tree2, nodes.tree3], 5000),
    Frame([nodes.tree3], 5400),
    Frame([nodes.tree1, nodes.streetLight3, nodes.tree3], 3000),
    Frame([nodes.tree1, nodes.tree2], 1000)
]

with open('../framesJons/frames.json') as f:
    data = load(f)

frames = data['frames']
duration = len(frames[0]['nodes'][0]['frameSates'])
print(duration)
for i in range(duration):
    for frame in frames:
        for node in frame['nodes']:
            for time in node['frameSates']:
                if time:
                    print(time)
