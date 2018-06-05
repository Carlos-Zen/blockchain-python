# coding:utf-8
import multiprocessing
import rpc

NODES = ['http://127.0.0.1:8301']
PORT = 8301

def start_node():
    p = multiprocessing.Process(target=rpc.start_server,args=('127.0.0.1',))
    p.start()

def get_nodes():
    return NODES

def add_node(address):
    NODES.append(address)

def check_node(address):
    pass

if __name__=='__main__':
    start_node()