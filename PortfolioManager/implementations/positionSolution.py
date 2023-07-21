#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
from PortfolioManager.implementations.securitySolution import security
from PortfolioManager.interfaces.positionInterface import positionInterface
from PortfolioManager.interfaces.securityInterface import securityInterface

class position(positionInterface):
    def __init__(self, _security, initialPosition: int) -> None:
        if isinstance(_security, str):
            self.security = security(_security)
        else:
            self.security = _security
        self.setPosition(initialPosition)

    def getSecurity(self) -> securityInterface:
        return self.security

    def getPosition(self) -> int:
        return self.position

    def setPosition(self, inputValue: int) -> None:
        if inputValue < 0:
            raise Exception('Input value cannot be negative.')
        self.position = inputValue

    def addPosition(self, inputValue: int) -> None:
        if self.position + inputValue < 0:
            raise Exception('Input value cannot be negative.')
        self.position += inputValue

    def getCurrentMarketValue(self):
        return self.security.getCurrentMarketValue() * self.position

