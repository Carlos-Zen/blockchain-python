# coding:utf-8
from block import Block
import time
from transaction import Vout, Transaction
from account import get_account
from database import BlockChainDB, TransactionDB, UnTransactionDB
from common import unlock_sig, lock_sig

MAX_COIN = 21000000
REWARD = 20

def reward():
    reward = Vout(get_account(), REWARD)
    tx = Transaction([], reward)
    return tx

def coinbase():
    """
    First block generate.
    """
    rw = reward()
    cb = Block(0, int(time.time()), [rw.hash], "")
    nouce = cb.pow()
    cb.make(nouce)
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    TransactionDB().insert(rw.to_dict())
    return cb

def get_all_untransactions():
    UnTransactionDB().all_hashes()

def mine():
    last_block = BlockChainDB().last()
    untxdb = UnTransactionDB()
    untxs = untxdb.find_all()
    untx_hashes = untxdb.all_hashes()
    # untxdb.clear()
    rw = reward()
    # Miner reward is the first transaction.
    untx_hashes.insert(0,rw.hash)
    cb = Block( last_block['index'] + 1, int(time.time()), untx_hashes, last_block['hash'])
    nouce = cb.pow()
    cb.make(nouce)
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    TransactionDB().insert(untxs)

def init():
    """
    Init download blockchain from block network before starting miner.
    在开始挖矿前，初始化会从区块网络上下载完整区块链条
    """
    pass

# coinbase()
# print(unlock_sig('ss','ss'))
mine()
