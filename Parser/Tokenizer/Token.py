
class Token:
    def __init__(self, tokenValue, tokenType) -> None:
        self.tokenValue = tokenValue
        self.tokenType = tokenType
        
    def __str__(self) -> str:
        return f"Token Type:{self.tokenType} , TokenValue: {self.tokenValue}"