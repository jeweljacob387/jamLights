import groups


class Node:
    def __init__(self, group: int, deviceIndex: int):
        self.group = group
        self.deviceIndex = deviceIndex


tree1 = Node(groups.middleCenter, 1)
tree2 = Node(groups.middleCenter, 2)
tree3 = Node(groups.middleCenter, 3)
star1 = Node(groups.middleCenter, 1)
star2 = Node(groups.middleCenter, 2)
star3 = Node(groups.middleCenter, 3)
streetLight1 = Node(groups.middleCenter, 1)
streetLight2 = Node(groups.middleCenter, 2)
streetLight3 = Node(groups.middleCenter, 3)
