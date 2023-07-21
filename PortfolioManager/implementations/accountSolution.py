#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account

from PortfolioManager.interfaces.positionInterface import positionInterface
from typing import Set, Iterable, Dict, Any
from PortfolioManager.interfaces.accountInterface import accountInterface
from PortfolioManager.interfaces.securityInterface import securityInterface

class account(accountInterface):
    def __init__(self, positions: Set[positionInterface], accountName: str):
        super().__init__(positions, accountName)
        self.name = accountName
        self.positions = {pos.getSecurity().getName(): pos for pos in positions}

    def getName(self) -> str:
        return self.name

    def getAllPositions(self) -> Iterable[positionInterface]:
        return self.positions.values()

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        return {pos.getSecurity().getName() : pos.getSecurity() for pos in self.positions
                if pos.getSecurity().getName() in [x.getName() for x in securities]}

    def addPositions(self, positions: Set[positionInterface]) -> None:
        for position in positions:
            self.positions[position.getSecurity().getName()] = position

    def removePositions(self, securities: Set) -> None:
        for security in securities:
            if security.getName() in self.positions:
                del self.positions[security.getName()]

    def getCurrentFilteredMarketValue(self, securitiesList):
        value = 0

        if securitiesList is not None and len(securitiesList) > 0:
            securitiesList = [sec.getName() if isinstance(sec, securityInterface) else sec for sec in securitiesList]
            for position in self.positions.values():
                if position.getSecurity().getName() not in securitiesList:
                    continue
                value += position.getCurrentMarketValue()
        else:
            for position in self.positions.values():
                value += position.getCurrentMarketValue()

        return value

    def getCurrentMarketValue(self):
        return self.getCurrentFilteredMarketValue([pos.getSecurity().getName() for pos in self.positions.values()])

