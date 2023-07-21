#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security

from PortfolioManager.interfaces.securityInterface import securityInterface
from PortfolioManager.generators.priceDataGenerator import priceData

pD = priceData()

class security(securityInterface):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name

    #Return the security's name
    def getName(self) -> str:
        return self.name

    #Return the current security's market value
    def getCurrentMarketValue(self) -> float:
        return pD.getCurrentPrice(self.name)

    def __str__(self):
        return f'(name={self.name}, value=None)'

