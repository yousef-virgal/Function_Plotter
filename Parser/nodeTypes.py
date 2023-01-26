import enum

class NodeTypes(enum.Enum):
    ROOT = 000
    ADD = 100
    MUL = 101
    DIV = 102
    SUB = 103
    VARIABLE = 200
    