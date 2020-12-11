from groups import groups


class Node:
    def __init__(self, name: str, group: int, deviceIndex: int):
        self.name = name
        self.group = group
        self.deviceIndex = deviceIndex


nodes = set()
