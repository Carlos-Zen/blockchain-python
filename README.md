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

# Introduce 
## About block
The blockchain is a data structure that is linked sequentially from back to forward by blocks containing transaction information. SHA256 cryptographic hashing is performed on each block header to generate a hash value. A bitcoin block is as follows:   
区块链是由包含交易信息的区块从后向前有序链接起来的数据结构,对每个区块头进行SHA256加密哈希，可生成一个哈希值。一个比特币区块如下：   
```
{
 "size":43560,
 "version":2,

 "previousblockhash":"00000000000000027e7ba6fe7bad39faf3b5a83daed765f05f7d1b71a1632249",
 "merkleroot":"5e049f4030e0ab2debb92378f53c0a6e09548aea083f3ab25e1d94ea1155e29d",
 "time":1388185038,
 "difficulty":1180923195.25802612,
 "nonce":4215469401,
 "tx":["257e7497fb8bc68421eb2c7b699dbab234831600e7352f0d9e6522c7cf3f6c77",
  #[...many more transactions omitted...]
  "05cfd38f6ae6aa83674cc99e4d75a1458c165b7ab84725eda41d018a09176634"
 ]
}
```
A blockchain is a linked list structure of blocks. The essence of mining is a new block, based on existing information such as parent block hash, timestamp, transaction merkle hash, plus a nonce (number from 0)   
A sha256 representation string is generated after the connection. If the preceding digits start with several zeroes, the number of zeros is the difficulty of mining, and half is dynamically adjusted based on the remaining number and the generation speed of the previous block, such as:   

区块链就是区块组成的链表结构。而挖矿的本质就是一个新区块，根据现有的一些信息比如父区块hash、时间戳、交易的merkle数根hash再加上一个nonce(从0开始增长的数字)    
连接后生成一个sha256的表现字符串。如果前面数位是几个0开头，0的个数就是挖矿难度，一半根据剩余数量和上一个区块的生成速度动态调整，比如:   
```
00000000000000027e7ba6fe7bad39faf3b5a83daed765f05f7d1b71a1632249
```
Successful mining, block generation   
挖矿成功，区块生成   

## About miner

The sha256 used by the mining algorithm, Bitcoin's algorithm is based on the block header +Nouce (a number) as a string. Simple blockchain simplifies the header information, but the mechanism and Bitcoin are constant.
The blockchain is stored locally in the file in json format. The generation of a block is related to the transaction information, so the block information is also stored when the block is stored.
There will be rewards for mining, and the reward will be recorded as the first transaction in the blockchain.
- Rewards for mining are rewarded by the generated block itself
- The miner also gets the amount entered for all transactions in the block - the amount of money that was exported
- There will be some sorting rules for the transactions to be certified, sorting according to the block age, transaction fee, transaction amount, etc.

We simplified the implementation and only implemented rewards. Rewards will be awarded to the current account.

挖矿算法使用的sha256，比特币的算法是根据区块头信息+Nouce(一个数字）作为字符串。简单区块链简化的头部信息，但是机制和比特币是一直的。
区块链在本地以json格式化存储在文件中。一个区块的生成与交易信息是有关联的，所以区块存储的同时，交易信息也会存储下来。
挖矿会有奖励，奖励会作为区块链的第一笔交易记录下来.
- 挖矿的奖励一个是来源于生成区块本身的奖励
- 矿工还会获取纳入区块中的所有交易 输入的金额-输出的金额 的金额
- 待认证的交易会有一些排序规则，根据区块链龄，交易费，交易金额等来做排序

我们简化了实现，只实现奖励的机制。奖励会奖励给当前账户。


## About network 

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



## About transaction
比特币采用的是 UTXO 模型,并不直接存在“余额”这个概念，余额需要通过遍历整个交易历史得来。我们也实现这个机制。
![tx](./img/blockchain-info-tx.png)
一笔交易由一些输入（input）和输出（output）组合而来，在我们的交易中，也会接受多个输入然后产生多个输出。
- 输出会包含一个锁定脚本(`ScriptPubKey`)，要花这笔钱，必须要解锁该脚本
- 交易会有严格的校验过程

我们的实现会简化这个过程，通过一个字段unspent来表示是否花费，也省区了校验的过程。
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

