# coding:utf-8
from rpc import get_clients
from transaction import *
from database import *
from block import *
from block import coinbase

def test_clients():
    cs = get_clients()
    for c in cs: 
        print(c.ping())

def test_transaction():
    vi = Vin("testaddress",10)
    vo = Vout("testaddress",10)
    tx = Transaction(vi,vo)
    print(vi,vo,tx.to_dict())

def test_database():
    vi = Vin("testaddress",10)
    vo = Vout("testaddress",10)
    tx = Transaction(vi,vo)
    tdb = TransactionDB()
    tdb.insert(tx.to_dict())

    b = Block(0, time.time(), {
        "proof-of-work": 9,
        "transactions": [tx.hash]},
        "0")

def test_block():
    cb= coinbase()
    print(cb)
# test_database()
test_block()
