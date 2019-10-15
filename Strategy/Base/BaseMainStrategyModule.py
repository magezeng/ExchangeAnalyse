from abc import abstractmethod

from .BaseStrategyModule import BaseStrategyModule


class BaseMainStrategyModule(BaseStrategyModule):
    @abstractmethod
    def run(self):
        raise NotImplementedError
