# coding:utf-8
import json
BLOCKFILE = 'data/blockchain'
TXFILE = 'data/tx'

class Base():
    filepath = ''

    def read(self):
        raw = ''
        with open(self.filepath,'r+') as f:
            raw = f.readline()
        return json.loads(raw)

    def write(self, item):
        data = self.read()
        data.append(item)
        with open(self.filepath,'w') as f:
            f.write(json.dumps(data))
        return True
        
class BlockChain(Base):

    def __init__(self):
        self.filepath = BLOCKFILE

    def find_all(self):
        return self.read()

    def find(self, hash):
        one = {}
        for item in self.find_all():
            if item['hash'] == hash:
                one = item
                break
        return one

    def insert(self, block):
        self.write(block)

class Tx(Base):

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