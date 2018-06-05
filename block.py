# coding:utf-8
import bitcoin
class Block():
    def __init__(self, index, timestamp, tx, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.tx = tx
        self.previous_block = previous_hash
        self.next_block = previous_hash

    def hash(self):
        return bitcoin.sha256((str(self.index) + str(self.timestamp) + str(self.tx) + str(self.previous_block)).encode('utf-8'))

def coinbase():
    
    return Block(0, time.time(), {
        "proof-of-work": 9,
        "transactions": None},
        "0")
        
class BlockChain():
