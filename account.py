# coding:utf-8
import hashlib
import bitcoin

def new_account():
    private_key = bitcoin.random_key()
    public_key = bitcoin.hash160(private_key.encode())
    print(public_key)

new_account()