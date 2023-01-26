
class Node:
    def __init__(self,type, value=None) -> None:
        self.children = []
        self.value = value
        self.type = type

    def __str__(self) -> str:
        return f"Node Value : {self.value}, Node Type:{self.type}"

class VariableNode:
    def __init__(self, powerValue=None, multiplierValue=None) -> None:
        self.powerValue = powerValue
        self.multiplierValue = multiplierValue