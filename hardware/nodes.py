import groups


class Node:
    def __init__(self, group, deviceIndex):
        self.group = group
        self.deviceIndex = deviceIndex


tree1 = Node(groups.middleCenter, 1)
tree2 = Node(groups.middleCenter, 2)
tree3 = Node(groups.middleCenter, 3)
