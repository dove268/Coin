from urllib.request import urlopen
import json


class TcApi(object):
    def __init__(self, name, url=None):
        self.name = name
        self.url = url

    def get_data(self):
        data = urlopen(self.url).read().decode('utf-8')
        return data

    def json(self):
        data = json.loads(self.get_data())
        return data

    def save_data_to_file(self):
        opx = open(self.name, 'a+')
        opx.write(str(self.json()))
        opx.close()


class BtcApi(TcApi):
    def __init__(self):
        super(BtcApi, self).__init__(name='btc')
        self.url = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny'


class BtcDepth(TcApi):
    def __init__(self):
        super(BtcDepth, self).__init__(name='btc_depth')
        self.url = 'https://www.okcoin.cn/api/v1/depth.do?symbol=btc_cny'


class BtcTrades(TcApi):
    def __init__(self):
        super(BtcTrades, self).__init__(name='btc_trades')
        self.url = 'https://www.okcoin.cn/api/v1/trades.do?symbol=btc_cny'


class LtcApi(TcApi):
    def __init__(self):
        super(LtcApi, self).__init__(name='ltc')
        self.url = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny'


class LtcDepth(TcApi):
    def __init__(self):
        super(LtcDepth, self).__init__(name='ltc_depth')
        self.url = 'https://www.okcoin.cn/api/v1/depth.do?symbol=ltc_cny'


class LtcTrades(TcApi):
    def __init__(self):
        super(LtcTrades, self).__init__(name='ltc_trades')
        self.url = 'https://www.okcoin.cn/api/v1/trades.do?symbol=ltc_cny'
