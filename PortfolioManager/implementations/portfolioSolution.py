#Uncomment line above & run cell to save solution
#TODO Define class that implements portFolioInterface & allows for the management of a portfolio

from typing import Set, Iterable
from PortfolioManager.interfaces.accountInterface import accountInterface
from PortfolioManager.interfaces.securityInterface import securityInterface
from PortfolioManager.interfaces.portfolioInterface import portfolioInterface

class portfolio(portfolioInterface):
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        self.name = portfolioName
        self.accounts = {account.getName() : account for account in accounts}

    def getName(self):
        return self.name

    def getAllAccounts(self) -> Iterable[accountInterface]:
        return self.accounts.values()

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        ret = [account for account in self.accounts.values()]

        if accountNamesFilter is not None and len(accountNamesFilter) > 0:
            ret = [account for account in ret if account.getName() in accountNamesFilter]

        if securitiesFilter is not None and len(securitiesFilter) > 0:
            ret = [account for account in ret if self._allMatches(account, securitiesFilter) ]

        print(accountNamesFilter, securitiesFilter, [account.getName() for account in ret])
        return ret

    def _allMatches(self, account, securitiesFilter):
        securities = [position.getSecurity().getName() for position in account.getAllPositions()]
        for name in securitiesFilter:
            if name not in securities:
                return False
        return True

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        for account in accounts:
            self.accounts[account.getName()] = account

    def removeAccounts(self, accountNames: Set[str]) -> None:
        for account in accountNames:
            if account in self.accounts:
                del self.accounts[account]

    def getCurrentMarketValue(self):
        cache = {}

        value = 0
        for account in self.accounts.values():
             for position in account.getAllPositions().values():
                security = position.getSecurity()
                name = security.getName()
                if name not in cache:
                    cache[name] = security.getCurrentMarketValue()
                value += cache[name] * position.getPosition()
        return value

        pass
