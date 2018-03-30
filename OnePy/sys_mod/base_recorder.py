from OnePy.environment import Environment


class RecorderBase(object):
    env = Environment

    def __init__(self):
        self.env.recorders.update({self.__class__.__name__: self})
        self.env.recorder = self

    def run(self):
        pass

    def update(self):
        """根据最新价格更新账户信息"""
        pass


class AbstractAccount(object):

    def __init__(self):
        pass

    def cash(self):
        pass

    def frozen_cash(self):
        pass

    def market_value(self):
        pass

    def transaction_cost(self):
        pass

    def positions(self):
        pass

    def get_state(self):
        pass

    def set_state(self):
        pass


class AbstractPosition(object):

    def __init__(self):
        pass

    def market_value(self):
        pass

    def transaction_cost(self):
        pass

    def positions(self):
        pass

    def get_state(self):
        pass

    def set_state(self):
        pass
