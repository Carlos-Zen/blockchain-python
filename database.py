# coding:utf-8
import json
import os

BLOCKFILE = 'data/blockchain'
TXFILE = 'data/tx'
UNTXFILE = 'data/untx'
ACCOUNTFILE = 'data/account'

class BaseDB():
    filepath = ''

    def read(self):
        raw = ''
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath,'r+') as f:
            raw = f.readline()
        return json.loads(raw)

    def write(self, item):
        data = self.read()
        data.append(item)
        with open(self.filepath,'w+') as f:
            f.write(json.dumps(data))
        return True

    def clear(self):
        with open(self.filepath,'w+') as f:
            f.write('')

class AccountDB(BaseDB):

    def __init__(self):
        self.filepath = ACCOUNTFILE  

    def find_one(self):
        ac = self.read()
        return ac[0]

    def insert(self, account):
        self.write(account)  

class BlockChainDB(BaseDB):

    def __init__(self):
        self.filepath = BLOCKFILE

    def find_all(self):
        return self.read()

    def last(self):
        bc = self.read()
        if len(bc) > 0:
            return bc[-1]
        else:
            return []

    def find(self, hash):
        one = {}
        for item in self.find_all():
            if item['hash'] == hash:
                one = item
                break
        return one

    def insert(self, block):
        self.write(block)

class TransactionDB(BaseDB):
    """
    Transactions that save with blockchain.
    """
    def __init__(self):
        self.filepath = TXFILE
    
    def find_all(self):
       return self.read() 

    def find(self, hash):
        one = {}
        for item in self.find_all():
            if item['hash'] == hash:
                one = item
                break
        return one

    def find_unspent(self, addr):
        unspent = []
        for item in self.find_all():
            # vout receiver is addr and the vout hasn't spent yet.
            # 地址匹配且未花费
            if item['vout']['receiver'] == addr and item['vout']['unspent'] == True:
                unspent.append(item['vout'])
        return unspent

    def insert(self, txs):
        if isinstance(txs, dict):
            txs = [txs]
        for tx in txs:
            self.write(tx)

class UnTransactionDB(TransactionDB):
    """
    Transactions that doesn't store in blockchain.
    """
    def __init__(self):
        self.filepath = UNTXFILE

    def all_hashes(self):
        hashes = []
        for item in self.find_all():
            hashes.append(item['hash'])
        return hashes