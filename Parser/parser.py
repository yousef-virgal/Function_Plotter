
from Parser.Tokenizer.Tokenizer import Tokenizer
from Parser.Tokenizer.const import TokenTypes
from Parser.node import Node, VariableNode
from Parser.nodeTypes import NodeTypes

class Parser:

    def __init__(self) -> None:
        self.tokens = []
        self.currentToken = 0
    
    def setTokens(self, tokens):
        """
        A function that sets the list of tokens of the parser
        
        Arguments:
            tokens: the list of tokens to set the parser's list to
        Returns:
            None
        """
        self.tokens = tokens

    def isMultiplyOrDivide(self):
        """
        A function that checks if the current token is multiply or divide token and creates a new node  
        to represent it 
        
        Arguments:
            None
        Returns:
            a Node that represents the operation 
        """
        if (self.match(TokenTypes.MUL)):
            return Node(type=NodeTypes.MUL, value="*")
        elif (self.match(TokenTypes.DIV)):
            return Node(type=NodeTypes.DIV, value="/")
        return None

    def isAddOrSub(self):
        """
        A function that checks if the current token is addtion or subtraction token and creates a new node  
        to represent it 
        
        Arguments:
            None
        Returns:
            a Node that represents the operation
        """
        if (self.match(TokenTypes.SUB)):
            return Node(type=NodeTypes.SUB, value="-")
        elif (self.match(TokenTypes.ADD)):
            return Node(type=NodeTypes.ADD, value="+")
        return None

   
    def mulOrDivExperssion(self):
        """
        A function that parses an experssion that conatins multiplication or divison opertion
        
        Arguments:
            None
        Returns:
            a Node that represents the head of the paresd experssion 
        """
        leftPart =  self.node()
        if leftPart.type == NodeTypes.VARIABLE and leftPart.value.multiplierValue == None:
            raise Exception("Invalid Expersion")
        operation = self.isMultiplyOrDivide()
        if operation != None:
            rightPart = self.mulOrDivExperssion()
            if rightPart.type == NodeTypes.VARIABLE and rightPart.value.multiplierValue == None:
                raise Exception("Invalid Expersion")
            operation.children.append(leftPart)
            operation.children.append(rightPart)
            return operation
        else:
            return leftPart
    
    def node(self):
        """
        A function that parses an experssion that can contain a number or variable 
        
        Arguments:
            None
        Returns:
            a Node that represents the head of the paresd experssion 
        """
        node = Node(type=NodeTypes.VARIABLE)
        values = VariableNode()

        if self.match(TokenTypes.NUMBER,False):
            values.multiplierValue = self.tokens[self.currentToken].tokenValue
            self.currentToken += 1
        elif self.match(TokenTypes.UNKNOWN, False):
            values.multiplierValue = 1

        if (self.match(TokenTypes.UNKNOWN)):
            if self.match(TokenTypes.POW):
                if self.match(TokenTypes.NUMBER,False):
                    values.powerValue = self.tokens[self.currentToken].tokenValue
                    self.currentToken += 1
                else:
                    raise Exception("Expected a Number after ^")
            else:
                values.powerValue = 1
        else:
            values.powerValue = 0

        node.value = values 
    
        return node 

        
    def match(self, matchValue, consume=True):
        """
        A function that checks if a the current token matches a certain token value and consumes the token if the flag is set to true
        
        Arguments:
            matchValue: the token value to comapre to
            consume: a flag to indicate whether to cosnume the token or not
        Returns:
            a boolean indicating if the current token matched a certain value 
        """
        if (self.currentToken > len(self.tokens) - 1):
            return False
        if self.tokens[self.currentToken].tokenType == matchValue:
            if consume:
                self.currentToken += 1
            return True
        return False
    
    def peek(self):
        """
        A function that retuns the next token in the list
        
        Arguments:
            None
        Returns:
            the next token in the list if exists else it will return -1
        """
        if (self.currentToken + 1 > len(self.tokens) - 1):
            return -1
        return self.tokens[self.currentToken]

    def parse(self):
        """
        A function that parses an experssion that conatins addition or subtraction opertion
        
        Arguments:
            None
        Returns:
            a Node that represents the head of the paresd experssion 
        """
        leftPart = self.mulOrDivExperssion()
        if leftPart.type == NodeTypes.VARIABLE and leftPart.value.multiplierValue == None:
            raise Exception("Invalid Expersion")
        operation = self.isAddOrSub()
        if (operation != None):
            rightPart = self.parse()
            if rightPart.type == NodeTypes.VARIABLE and rightPart.value.multiplierValue == None :
                raise Exception("Invalid Expersion")
            operation.children.append(leftPart)
            operation.children.append(rightPart)
            return operation
        else:
            return leftPart

if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokenizer.setText("10X^2-10X+20X")
    # [number,X,^,number,+,Number,X,^,number]
    list = tokenizer.tokenize()
    pasrer = Parser()
    pasrer.setTokens(list)
    tree = pasrer.parse()
    