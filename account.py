# coding:utf-8
import hashlib
import lib.common
from model import Model
from lib.common import pubkey_to_address
from database import AccountDB

def new_account():
    private_key = lib.common.random_key()
    public_key = lib.common.hash160(private_key.encode())
    address = pubkey_to_address(public_key.encode())
    adb = AccountDB()
    adb.insert({'pubkey': public_key, 'address':address})
    return private_key, public_key, address

def get_account():
    adb = AccountDB()
    return adb.find_one()