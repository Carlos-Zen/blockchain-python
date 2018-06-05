# coding:utf-8
import time
import json
import bitcoin

class Model():
    
    def __getitem__(self,key):
        if hasattr(self,key):
            return getattr(self,key)
        else:
            return None

    def __setitem__(self,key,value):
        if hasattr(self,key):
            setattr(self,key,value)
        else:
            pass

    def __str__(self):
        return str(self.__dict__.items()
        )
        
    def json(self):
        return json.dumps(self.__dict__)

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
        self.timestamp = time.time()
        self.vin = vin
        self.vout = vout
        self.hash = self.gen_hash()

    def gen_hash(self):
        return  bitcoin.sha256((str(self.timestamp) + str(self.vin) + str(self.vout)).encode('utf-8'))