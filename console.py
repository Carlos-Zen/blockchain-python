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
from node import *
from common import cprint

MODULES = ['account','tx','blockchain','miner','node']

def upper_first(string):
    return string[0].upper()+string[1:]

class Node():

    def add(self, args):
        add_node(args[0])
        rpc.BroadCast().add_node(args[0])
        cprint('Allnode',get_nodes())
    
    def run(self, args):
        p = multiprocessing.Process(target=rpc.start_server,args=('127.0.0.1',int(args[0])))
        p.start()

class Miner():
    def start(self, args):
        if get_account() == None:
            cprint('ERROR','Please create account before start miner.')
            exit
        p = multiprocessing.Process(target=rpc.start_server,args=('127.0.0.1',int(args[0])))
        p.start()
        while True :
            cprint('Miner new block',mine().to_dict())

class Account():
    def create(self, args):
        ac = new_account()
        cprint('MESSAGE','===Please remember your private key===')
        cprint('Private Key',ac[0])
        cprint('Public Key',ac[1])
        cprint('Address',ac[2])

    def get(self, args):
        cprint('All Account',AccountDB().read())

class Blockchain():

    def list(self):
        for t in BlockChainDB().find_all():
            cprint('Blockchain',str(t))

class Tx():

    def list(self):
        for t in TransactionDB().find_all():
            cprint('Transaction',str(t))

    def transfer(self,args):
        tx = Transaction.transfer(args[0], args[1], args[2])
        print(Transaction.unblock_spread(tx))
        cprint('Transaction tranfer',tx)

if __name__ == '__main__':
    module = sys.argv[1]
    if module not in MODULES:
        cprint('Error', 'First arg shoud in %s' % (str(MODULES,)))
    mob = globals()[upper_first(module)]()
    method = sys.argv[2]
    print(sys.argv[3:])
    try:
        getattr(mob, method)(sys.argv[3:])
    except AttributeError as e:
        cprint('ERR',str(e))