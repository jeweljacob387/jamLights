import nodes


class Frame:
    def __init__(self, nodes, duration):
        self.nodes = nodes
        self.duration = duration


frames = [
    Frame([nodes.tree1, nodes.tree2], 100),
    Frame([nodes.tree2], 20),
    Frame([nodes.tree2, nodes.tree3], 56),
    Frame([nodes.tree3], 54),
    Frame([nodes.tree1, nodes.tree2, nodes.tree3], 600),
]
