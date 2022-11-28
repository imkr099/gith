class Bank:
    def __init__(self, money, name):
        self.__money = money
        self.__name = name

    def setmon(self, money):
        self.__money = money

    def getmon(self):
        return self.__money

    def setnm(self, name):
        self.__name = name

    def getnm(self):
        return self.__name

    def moneyX(self):
        user = input('Внесите депозит:')
        return f'Вы успешно внесли депозит! \nВаш счет:{self.getmon() + int(user)}'

    def _kill(self):
        return f'Вы успешно обнулили счет \nВаш счет:{self.getmon() - self.getmon()}'

    def __jackpot(self):
        return f'Поздравляем! Ваш счет приумножился в 10 раз! \nВаш счет:{self.__money * 10}'


us = Bank(0, 'Islambek')
us.setnm('Islam')
us.setmon(1000)
print(f'Ваше имя:{us.getnm()} \nВаши деньги:{us.getmon()}')
print(us.moneyX())
print(us._kill())
print(us._Bank__jackpot())