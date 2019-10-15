from .DepthMove import DepthMove
from ..Base.BaseStrategyModule import BaseStrategyModule


class FromSoptToFutureModule(DepthMove, BaseStrategyModule):
    """

    """

    def filter_order(self, orders) -> 'orders':
        pass

    def filter_order_part1(self):
        self.filter_order_part2()

    def filter_order_part2(self):
        pass
