# coding:utf-8
from account import *
from rpc import get_clients, BroadCast, start_server
from transaction import *
from database import *
from block import *
import sys
from miner import mine
import multiprocessing
import rpc 

MODULES = ['account','tx','blockchain','miner']
def pprint(tag,content):
    max = 12
    if len(tag) < max:
        tag = tag + (max-len(tag)) * ' '
    print("[ %s ] : \n %s \n" % (tag,content))

def upper_first(string):
    return string[0].upper()+string[1:]

class Miner():
    def start(self, args):
        print(args)
        p = multiprocessing.Process(target=rpc.start_server,args=('127.0.0.1',int(args[0])))
        p.start()
        print('s')
        while True :
            pprint('Miner new block',mine().to_dict())

class Account():

    def create(self):
        ac = new_account()
        pprint('MESSAGE','===Please remember your private key===')
        pprint('Private Key',ac[0])
        pprint('Public Key',ac[1])
        pprint('Address',ac[2])

    def get(self):
        pprint('All Account',AccountDB().read())

class Blockchain():

    def list(self):
        for t in BlockChainDB().find_all():
            pprint('Blockchain',str(t))

class Tx():

    def list(self):
        for t in TransactionDB().find_all():
            pprint('Transaction',str(t))

    def new(self,args):
        pass

if __name__ == '__main__':
    module = sys.argv[1]
    if module not in MODULES:
        pprint('Error', 'First arg shoud in %s' % (str(MODULES,)))
    mob = globals()[upper_first(module)]()
    method = sys.argv[2]
    getattr(mob, method)(sys.argv[3:])