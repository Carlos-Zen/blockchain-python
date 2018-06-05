# Simple Blockchain   

The blockchain is very simple and imprecise.Just for study.
The simple blockchain implements simple blockchain and transactions. Currently, the implementation already has mining, transaction, communication between nodes, and file persistence of blocks and transactions.   
The communication between nodes is via rpc based on http, rather than p2p network. Because the implementation of P2p is more complicated, it is too complicated to understand the framework of blockchain.   
The verification based on cryptography has not yet been realized, and the verification of blocks between nodes and the verification of transactions have not yet been realized.

区块链实现比较简单也不够严谨，主要为了学习参考而分享
简单区块链实现了简单的区块链和交易，目前实现已经具备了挖矿、交易、节点间通讯、以及区块和交易的文件持久化。
节点间通讯通过建立在http基础之上的rpc，而非p2p网络，因为P2p的实现比较复杂，对于了解区块链的框架来说过于复杂。
建立在密码学基础上的校验暂未实现，节点间对区块的校验，以及交易的校验目前还未能实现。

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install requirements.  

```
$ pip install -r requirements.txt
``` 

3. Run the server:
    * `$ pipenv run python main.py` 

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

