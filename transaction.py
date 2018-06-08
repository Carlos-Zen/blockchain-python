# coding:utf-8
import time
import json
import bitcoin
from model import Model
from database import TransactionDB

class Vin(Model):
    def __init__(self, sender, amount):
        self.sender = sender
        self.amount = amount
        # self.unLockSig = unLockSig
        # self.pubKey = pubKey

class Vout(Model):
    def __init__(self, receiver, amount):
        self.receiver = receiver
        self.amount = amount
        self.unspent = True
        # self.lockSig = lockSig
    
    @classmethod
    def get_unspent(cls, addr):
        txs = TransactionDB().find_unspent(addr)
        return [cls(tx['receiver'], tx['amount']) for tx in txs]

class Transaction():
    def __init__(self, vin, vout,):
        self.timestamp = int(time.time())
        self.vin = vin
        self.vout = vout
        self.hash = self.gen_hash()

    def gen_hash(self):
        return  bitcoin.sha256((str(self.timestamp) + str(self.vin) + str(self.vout)).encode('utf-8'))

    @staticmethod
    def transfer(self, from_addr, to_addr, amount):
        unspents = Vout.get_unspent(from_addr)

    def to_dict(self):
        dt = self.__dict__
        if not isinstance(self.vin, list):
            self.vin = [self.vin]
        if not isinstance(self.vout, list):
            self.vout = [self.vout]
        dt['vin'] = [i.__dict__ for i in self.vin]
        dt['vout'] = [i.__dict__ for i in self.vout]
        return dt

def select_outputs_greedy(unspent, min_value): 
    if not unspent: return None 
    # 分割成两个列表。
    lessers = [utxo for utxo in unspent if utxo.amount < min_value] 
    greaters = [utxo for utxo in unspent if utxo.amount >= min_value] 
    key_func = lambda utxo: utxo.amount
    if greaters: 
        # 非空。寻找最小的greater。
        min_greater = min(greaters)
        change = min_greater.amount - min_value 
        return [min_greater], change 
    # 没有找到greaters。重新尝试若干更小的。
    # 从大到小排序。我们需要尽可能地使用最小的输入量。
    lessers.sort(key=key_func, reverse=True)
    result = []
    accum = 0
    for utxo in lessers: 
        result.append(utxo)
        accum += utxo.amount
        if accum >= min_value: 
            change = accum - min_value
            return result, "Change: %d Satoshis" % change 
    # 没有找到。
    return None, 0