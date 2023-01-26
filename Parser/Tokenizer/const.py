import enum

class TokenTypes(enum.Enum):
   ADD = 100
   SUB = 101
   DIV = 102
   MUL = 103
   POW = 104
   LEFTPARN = 200
   RIGHTPARN = 201
   UNKNOWN = 300
   NUMBER = 301
   EOF = 400