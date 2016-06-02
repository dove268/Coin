'''
import os,sys,pprint
print(os.getcwd())
pprint.pprint(sys.path)
'''
import module
btc = module.Tcapi('api',url='https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny')
c=btc.save_data_to_file()
