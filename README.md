# Simple Blockchain   

The blockchain is very simple and imprecise.Just for study.
The simple blockchain implements simple blockchain and transactions. Currently, the implementation already has mining, transaction, communication between nodes, and file persistence of blocks and transactions.   
The communication between nodes is via rpc based on http, rather than p2p network. Because the implementation of P2p is more complicated, it is too complicated to understand the framework of blockchain.   
The verification based on cryptography has not yet been realized, and the verification of blocks between nodes and the verification of transactions have not yet been realized.

区块链实现比较简单也不够严谨，主要为了学习参考而分享。
简单区块链实现了简单的区块链和交易，目前实现已经具备了挖矿、交易、节点间通讯、以及区块和交易的文件持久化。
节点间通讯通过建立在http基础之上的rpc，而非p2p网络，因为P2p的实现比较复杂，对于了解区块链的框架来说过于复杂。
建立在密码学基础上的校验暂未实现，节点间对区块的校验，以及交易的校验目前还未能实现。

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Create Account
```
$ python account.py
```
2. Run the miner.  

```
$ python miner.py
``` 

3. Run the server:
    * `$ python main.py` 

## About miner

The sha256 used by the mining algorithm, Bitcoin's algorithm is based on the block header +Nouce (a number) as a string. Simple blockchain simplifies the header information,but the mechanism and Bitcoin are constant.    
The blockchain is stored locally in the file in json format. The generation of a block is related to the transaction information, so the block information is also stored when the block is stored.    
Mining will be rewarded, and the reward will be recorded as the first transaction in the blockchain.    
挖矿算法使用的sha256，比特币的算法是根据区块头信息+Nouce(一个数字）作为字符串。简单区块链简化的头部信息，但是机制和比特币是一直的。
区块链在本地以json格式化存储在文件中。一个区块的生成与交易信息是有关联的，所以区块存储的同时，交易信息也会存储下来。
挖矿会有奖励，奖励会作为区块链的第一笔交易记录下来.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

