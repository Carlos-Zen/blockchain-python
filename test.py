# coding:utf-8
from rpc import get_clients, BroadCast, start_server
from transaction import *
from database import *
from block import *
from transaction import select_outputs_greedy,Vout,Transaction

def test_clients():
    cs = get_clients()
    for c in cs: 
        print(c.ping())

def test_transaction():
    # vi = Vin("testaddress",10)
    # vo = Vout("testaddress",10)
    # tx = Transaction(vi,vo)
    # print(vi,vo,tx.to_dict())
    from_addr = '1L8Q3xJyk5MnWoV1Qz6sfT57yGB6bA7DgR'
    to_addr = '145wtdP4dwgvMkYp2Jv6GWHmRkYQCnqvuU'
    # unspent = Vout.get_unspent('1L8Q3xJyk5MnWoV1Qz6sfT57yGB6bA7DgR',)
    found = Transaction.transfer(from_addr, to_addr, 10)
    print(found)

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

def test_broadcast():
    bc = BroadCast()
    bc.add_block()

def test_node_name():
    BlockChainDB()
# test_database()
# test_block()
# test_broadcast()
test_transaction()
# test_node_name()
