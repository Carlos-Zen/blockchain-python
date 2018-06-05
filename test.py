# coding:utf-8
from rpc import get_clients

def test_clients():
    cs = get_clients()
    for c in cs: 
        print(c.ping())

test_clients()        