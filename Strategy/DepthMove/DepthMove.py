from ..Base.BaseStrategy import BaseStrategy
from ...Exchanges.BaseExchange import BaseExchange

class DepthMove(BaseStrategy):
    """
    NickName:Access-Key Name:access_key Type:bool   Description:""
    NickName:源交易所 Name:origin_exchange Type:exchange    Description:""
    NickName:价格精度 Name:origin_exchange.price_precision Type:exchange    Description:""
    """
    def __init__(self):
        self.origin_exchange = BaseExchange()
        self.origin_exchange_price_precision = "asdasd"