[中文说明](https://github.com/Carlos-Zen/blockchain_python/blob/master/README_zh.md)

# Blockchain-python

A blockchain implementation in Python only for study.

The Blockchain-python implements simple blockchain and transactions. Currently, the implementation already has mining, transaction, communication between nodes, and file persistence of blocks and transactions.   
The communication between nodes is via rpc based on http, rather than p2p network. Because the implementation of P2p is more complicated, it is too complicated to understand the framework of blockchain.   
The verification based on cryptography has not yet been realized, and the verification of blocks between nodes and the verification of transactions have not yet been realized.

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
$ python console account create
```
- Run the miner
```
$ python console miner start 3008
```
- Transaction transfer.   
```
$ python console tx transfer from_address to_address amount
```
- Transaction list.   
```
$ python console tx list
```
- Blockchain shows.   
```
$ python console blockchain list
```
### Node Network
Copy the code resource to a new directory.While the miner before was running then:
```
$ cd {another_blockchain_directory}
$ python console node add 3008 
$ python console node run 3009
```
When a new block mined , block and transactions will broadcast to other nodes.

## All command
Use like this:   

```
$ python console [module] [action] params...
```
Such as:
```
$ python console tx list
```

|  Module  |  Action    |  Params                            |  Desc                                            |
|----------|------------|------------------------------------|--------------------------------------------------|
| account  |  create    |  NONEED                            |  Create new account                              |
| account  |  get       |  NONEED                            |  Show all account                                |
| account  |  current   |  NONEED                            |  The miner reward account                        |
| miner    |  start     |  ip:port/port                      |  Such as 3008 or 127.0.0.1:3008                  |
| node     |  run       |  ip:port/port                      |  Such as 3008 or 127.0.0.1:3008                  |
| node     |  list      |  NONEED                            |  Show all node that will broadcast   to          |
| node     |  add       |  ip:port                           |  Add a node that will broadcast   to             |
| tx       |  transfer  |  from_address to_address   amount  |  Transfer coin from from_address to   to_address |
| tx       |  list      |  NONEED                            |  Show all transactions                           |

# Introduce 
## About block
The blockchain is a data structure that is linked sequentially from back to forward by blocks containing transaction information. SHA256 cryptographic hashing is performed on each block header to generate a hash value. A bitcoin block is as follows:   
  
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
```
00000000000000027e7ba6fe7bad39faf3b5a83daed765f05f7d1b71a1632249
```
Successful mining, block generation   

### About Blockchain-python block

Blockchain-python simplified block structure, a blockchain-python block data is as follows:
```
{
	"index": 7,
	"timestamp": 1528972070,
	"tx": [
        "b959b3d2099ca304c67087edbf05b79d1f2501b1f407df5e51a1a8c22bb3334d",
        "613e4af7266e01ea338d30681ef606bad26e4cdfa4ec7a6f431e22420c8291fd",
        "be7095a764cb241606a67c9064bc8dbc2da2370d49459bd492473ea5ce304cb3"
    ],
	"previous_block": "00003e17e04d9c9d2c2f5629de20bda58f59af36417a7e50eb77a74a028b026a",
	"nouce": 11063,
	"hash": "00006805c75d0db1685616d9ea5730f6203eda744a16fcc78ef1f3c244083ea4"
}
```
The calculation of block hash is roughly the same as that of Bitcoin. Our difficulty setting is relatively low, so the hash in front of this block has only 4 zeros.    
This is for easier mining to understand the principle and generally can be produced in a few seconds. One block. In addition, Bitcoin's tx field represents the root node hash of the merkle tree that consists of the transaction hash.    
For simplicity, we put it directly into the array of transaction hash.   

## About miner

The sha256 used by the mining algorithm, Bitcoin's algorithm is based on the block header +Nouce (a number) as a string. Simple blockchain simplifies the header information, but the mechanism and Bitcoin are constant.
The blockchain is stored locally in the file in json format. The generation of a block is related to the transaction information, so the block information is also stored when the block is stored.
There will be rewards for mining, and the reward will be recorded as the first transaction in the blockchain.
- Rewards for mining are rewarded by the generated block itself
- The miner also gets the amount entered for all transactions in the block - the amount of money that was exported
- There will be some sorting rules for the transactions to be certified, sorting according to the block age, transaction fee, transaction amount, etc.

We simplified the implementation and only implemented rewards. The reward will be awarded to the current account. If the current account does not exist, please generate an account through the following command line:
```
$ python console account create
```

## About network 

The blockchain network is a P2P (Peer-to-Peer, end-to-end) network. We use Python's own RPC mechanism for simplification.   
- Different nodes can be connected by adding node operations   
- Unicom's nodes will automatically spread new transaction information   
- The new node will synchronize all the data of other node's blockchain while ensuring the maximum chain   
- Digging out new blocks will notify other nodes to synchronize   

## About transaction

Bitcoin uses the UTXO model and does not directly exist in the concept of “balance”. The balance needs to be obtained by traversing the entire transaction history. We also implement this mechanism.
A transaction is a combination of some input and output. In our transaction, we accept multiple inputs and generate multiple outputs.
- The calculation of the balance is made through the unconsumed verified transaction output - the output of the consumer transaction, which is commonly known as UTXO
- Transactions not placed in new block will be broadcast to all nodes waiting to be verified
- After waiting for the miner to dig into a new block, the trade will be saved as transaction information in the transaction database.

The correctness check of the transaction is under development.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

