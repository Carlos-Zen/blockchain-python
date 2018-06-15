# coding:utf-8
import multiprocessing
import rpc
from database import NodeDB
from common import cprint

def start_node(hostport='127.0.0.1:3009'):
    try:
        if hostport.find('.') != -1:
            host,port = hostport.split(':')
        else:
            host = '127.0.0.1'
            port = hostport
    except Exception:
        cprint('ERROR','params must be {port} or {host}:{port} , ps: 3009 or 0.0.0.0:3009')
    p = multiprocessing.Process(target=rpc.start_server,args=(host,int(port)))
    p.start()
    cprint('INFO','Node start success. Listen at %s.' % (hostport,))

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