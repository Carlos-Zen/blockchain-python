# coding:utf-8
import time
import json
import bitcoin
from model import Model

class Vin(Model):
    def __init__(self, sender, amount):
        self.sender = sender
        self.amount = amount

class Vout(Model):
    def __init__(self, receiver, amount):
        self.receiver = receiver
        self.amount = amount
        self.unspent = True

class Transaction():
    def __init__(self, vin, vout,):
        self.timestamp = int(time.time())
        self.vin = vin
        self.vout = vout
        self.hash = self.gen_hash()

    def gen_hash(self):
        return  bitcoin.sha256((str(self.timestamp) + str(self.vin) + str(self.vout)).encode('utf-8'))

    def to_dict(self):
        dt = self.__dict__
        if not isinstance(self.vin, list):
            self.vin = [self.vin]
        if not isinstance(self.vout, list):
            self.vout = [self.vout]
        dt['vin'] = [i.__dict__ for i in self.vin]
        dt['vout'] = [i.__dict__ for i in self.vout]
        return dt