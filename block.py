# coding:utf-8
import bitcoin
class Block:
    def __init__(self, index, timestamp, tx, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.tx = tx
        self.previous_block = previous_hash
        self.next_block = previous_hash

    def hash(self):
        return bitcoin.sha256((str(self.index) + str(self.timestamp) + str(self.tx) + str(self.previous_block)).encode('utf-8'))