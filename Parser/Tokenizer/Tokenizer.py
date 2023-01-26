from Parser.Tokenizer.Token import Token
from Parser.Tokenizer.const import TokenTypes

class Tokenizer:

    def __init__(self) -> None:
        self.text:str = "" 
        self.currentIndex = 0
        self.__numbers = ["0","1","2","3","4","5","6","7","8","9"]

    def tokenize(self):
        """
        A function that tokenizes the text
        
        Arguments:
            None
        Returns:
            A list of tokens that represent the text 
        """
        tokenList = []
        while self.currentIndex < len(self.text):
            self.checkWhiteSpace()
            if (self.match("-")):
                tokenList.append(Token(tokenType=TokenTypes.SUB, tokenValue="-"))
            elif(self.match("*")):
                tokenList.append(Token(tokenType=TokenTypes.MUL, tokenValue="*"))
            elif (self.match("/")):
                tokenList.append(Token(tokenType=TokenTypes.DIV, tokenValue="/"))
            elif(self.match("+")):
                tokenList.append(Token(tokenType=TokenTypes.ADD, tokenValue="+"))
            elif(self.match("^")):
                tokenList.append(Token(tokenType=TokenTypes.POW, tokenValue="^"))
            
            elif(self.match("X") or self.match("x")):
                tokenList.append(Token(tokenType=TokenTypes.UNKNOWN, tokenValue="X"))

            elif(self.text[self.currentIndex] in self.__numbers):
                number = self.text[self.currentIndex]
                while self.peek() in self.__numbers:
                    self.currentIndex += 1
                    number += self.text[self.currentIndex]

                if (self.peek() == "."):
                    self.currentIndex += 1
                    number += self.text[self.currentIndex]

                    if self.peek() not in self.__numbers:
                        raise Exception(f"Invalid float: {number}")

                    while self.peek() in self.__numbers:
                        self.currentIndex += 1
                        number += self.text[self.currentIndex]

                self.currentIndex += 1
                tokenList.append(Token(tokenType=TokenTypes.NUMBER, tokenValue=float(number)))
            
            else:
                raise Exception(f"Invalid Token: {self.text[self.currentIndex]} at {self.currentIndex + 1}")

        return tokenList

    def checkWhiteSpace(self):
        """
        A function that skips whitespace in the text  
        
        Arguments:
            None
        Returns:
            None
        """
        while self.text[self.currentIndex] == " " or self.text[self.currentIndex] == "\t":
            self.currentIndex += 1

    def setText(self, text):
        """
        A function that sets the text of the tokenizer
        
        Arguments:
            text: the string value to set the tokenizer text to
        Returns:
            None
        """
        self.text = text
    
    def match(self,matchValue):
        """
        A function that checks if a text item matches a certain value and consumes the text item if it does
        
        Arguments:
            matchValue: the value to compare the text item to
        Returns:
            a boolean indicating if the item matched or not  
        """
        if self.currentIndex >  len(self.text) - 1:
            return False

        if self.text[self.currentIndex] == matchValue:
            self.currentIndex += 1
            return True 

        return False

    def peek(self):
        """
        A function that retuns the next item in the text if it exists
        
        Arguments:
            None
        Returns:
            the next item in the text or -1 if it doesn't exist 
        """
        if self.currentIndex + 1 > len(self.text) - 1:
            return -1 
        else:
            return self.text[self.currentIndex + 1] 

if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokenizer.setText("10X^2+5X^3")
    list = tokenizer.tokenize()
    for token in list:
        print(token)