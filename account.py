# coding:utf-8
import hashlib
import common
from model import Model
from common import pubkey_to_address
from database import AccountDB


def new_account():
    private_key = common.random_key()
    public_key = common.hash160(private_key.encode())
    address = pubkey_to_address(public_key.encode())
    adb = AccountDB()
    adb.insert(address)
    return private_key, public_key, address

def get_account():
    adb = AccountDB()
    return adb.find_one()