import nodes


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
    Frame([nodes.tree1, nodes.tree2], 1000),
    Frame([nodes.tree2], 2000),
    Frame([nodes.tree2, nodes.tree3], 5000),
    Frame([nodes.tree3], 5400),
    Frame([nodes.tree1, nodes.tree2, nodes.tree3], 3000),
    Frame([nodes.streetLight1, nodes.tree2], 1000),
    Frame([nodes.tree2], 2000),
    Frame([nodes.tree2, nodes.tree3], 5000),
    Frame([nodes.tree3], 5400),
    Frame([nodes.tree1, nodes.star3, nodes.tree3], 3000),
    Frame([nodes.tree1, nodes.tree2], 1000),
    Frame([nodes.tree2], 2000),
    Frame([nodes.tree2, nodes.tree3], 5000),
    Frame([nodes.tree3], 5400),
    Frame([nodes.tree1, nodes.tree2, nodes.tree3], 3000),
    Frame([nodes.tree1, nodes.tree2], 1000),
    Frame([nodes.tree2], 2000),
    Frame([nodes.tree2, nodes.star1], 5000),
    Frame([nodes.tree3], 5400),
    Frame([nodes.tree1, nodes.tree2, nodes.tree3], 3000)
]
