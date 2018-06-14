# coding:utf-8
import multiprocessing
import rpc
from database import NodeDB

NODES = ['http://127.0.0.1:8301']

def start_node(port):
    p = multiprocessing.Process(target=rpc.start_server,args=('127.0.0.1',port))
    p.start()

def get_nodes():
    return NodeDB().find_all()

def add_node(address):
    ndb = NodeDB()
    all_nodes = ndb.find_all()
    if address.find('http') != 0:
        address = 'http://' + address
    all_nodes.append(address)
    ndb.clear()
    ndb.write(rm_dup(all_nodes))
    return address

def check_node(address):
    pass

def rm_dup(nodes):
    return sorted(set(nodes)) 
    
if __name__=='__main__':
    start_node(8301)