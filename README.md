# Simple Blockchain   

A blockchain implementation in Python only for study.

The simple blockchain implements simple blockchain and transactions. Currently, the implementation already has mining, transaction, communication between nodes, and file persistence of blocks and transactions.   
The communication between nodes is via rpc based on http, rather than p2p network. Because the implementation of P2p is more complicated, it is too complicated to understand the framework of blockchain.   
The verification based on cryptography has not yet been realized, and the verification of blocks between nodes and the verification of transactions have not yet been realized.

简单区块链实现了简单的区块链和交易，目前实现已经具备了挖矿、交易、节点间通讯、以及区块和交易的文件持久化。
节点间通讯通过建立在http基础之上的rpc，而非p2p网络，因为P2p的实现比较复杂，对于了解区块链的框架来说过于复杂。
建立在密码学基础上的校验暂未实现，节点间对区块的校验，以及交易的校验目前还未能实现。

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Git Clone
```
$ git clone https://github.com/Carlos-Zen/blockchain.git
$ cd blockchain
```

## Usage

- Create Account
```
$ python console.py createaccount
```
- Run the miner.  
```
$ python console.py miner   
``` 
- Transaction.   

```
$ python console.py trans to_address
``` 

## About node 

The blockchain network is a P2P (Peer-to-Peer, end-to-end) network. We use Python's own RPC mechanism for simplification.   
- Different nodes can be connected by adding node operations   
- Unicom's nodes will automatically spread new transaction information   
- The new node will synchronize all the data of other node's blockchain while ensuring the maximum chain   
- Digging out new blocks will notify other nodes to synchronize   

区块链网络是一个 P2P（Peer-to-Peer，端到端）的网络。我们为了简单化，使用了python自带的RPC机制。   
- 通过添加节点操作，可以联通不同节点   
- 联通的节点会自动传播新的交易信息
- 新节点会同步其他节点的区块链的所有数据，同时保证最大链条
- 挖出新的区块会通知其他节点同步   

## About miner

The sha256 used by the mining algorithm, Bitcoin's algorithm is based on the block header +Nouce (a number) as a string. Simple blockchain simplifies the header information,but the mechanism and Bitcoin are constant.    
The blockchain is stored locally in the file in json format. The generation of a block is related to the transaction information, so the block information is also stored when the block is stored.      
Mining will be rewarded, and the reward will be recorded as the first transaction in the blockchain.    

挖矿算法使用的sha256，比特币的算法是根据区块头信息+Nouce(一个数字）作为字符串。简单区块链简化的头部信息，但是机制和比特币是一直的。
区块链在本地以json格式化存储在文件中。一个区块的生成与交易信息是有关联的，所以区块存储的同时，交易信息也会存储下来。
挖矿会有奖励，奖励会作为区块链的第一笔交易记录下来.
- 挖矿的奖励一个是来源于生成区块本身的奖励
- 矿工还会获取纳入区块中的所有交易 输入的金额-输出的金额 的金额
- 待认证的交易会有一些排序规则，根据区块链龄，交易费，交易金额等来做排序

我们简化了实现，只实现奖励的机制。奖励会奖励给当前账户。


## About transaction
比特币采用的是 UTXO 模型,并不直接存在“余额”这个概念，余额需要通过遍历整个交易历史得来。我们也实现这个机制。
![tx](./img/blockchain-info-tx.png)
一笔交易由一些输入（input）和输出（output）组合而来，在我们的交易中，也会接受多个输入然后产生多个输出。
- 输出会包含一个锁定脚本(`ScriptPubKey`)，要花这笔钱，必须要解锁该脚本
- 交易会有严格的校验过程

我们的实现会简化这个过程，通过一个字段unspent来表示是否花费，也省区了校验的过程。
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

