# Blockchain-python

Python实现的简单区块链，主要用于学习使用

实现了简单的区块链和交易，已经具备了挖矿、交易、节点间通讯、以及区块和交易的文件持久化。
节点间通讯通过建立在http基础之上的rpc，而非p2p网络，因为p2p的实现比较复杂，对于了解区块链的框架来说过于复杂。
建立在密码学基础上的校验暂未实现，节点间对区块的校验，以及交易的校验目前还未能实现。

## 安装

为了简单，blockchain-python没有任何软件包的依赖，直接执行源码就可以了。

1. 安装[Python 3.6+](https://www.python.org/downloads/) . 
2. 下载源码，Git Clone 
```
$ git clone https://github.com/Carlos-Zen/blockchain.git
$ cd blockchain
```

## 使用指导

- 创建账户
```
$ python console account create
```
- 开始挖矿
```
$ python console miner start 3008
```
- 转账交易
```
$ python console tx transfer from_address to_address amount
```
- 交易记录
```
$ python console tx list
```
- 查看所有区块
```
$ python console blockchain list
```

### 节点网络

复制源码到一个新的目录，作为新的节点.或者复制到另一台机器上。下面代码演示本机两个节点：
- 启动新节点   
```
$ cd {another_blockchain_directory}
$ python console node add 3008 
$ python console node run 3009
```
- 回到初始的源码目录下，要保证挖矿正在进行当中，然后添加新的节点：   
```
$ python console node add 127.0.0.1:3009
```
当一个新的区块块被挖掘时，新的区块和交易将广播给其他节点。
多个节点情况下，只要一个节点被添加，所有节点网络会同步。

## 命令行大全
使用如下:   
```
$ python console [module] [action] params...
```
比如:
```
$ python console tx list
```

|  Module  |  Action    |  Params                            |  Desc                                            |
|----------|------------|------------------------------------|--------------------------------------------------|
| account  |  create    |  NONEED                            |  建立新帐户                                       |
| account  |  get       |  NONEED                            |  显示所有帐户                                     |
| account  |  current   |  NONEED                            |  矿工奖励账户                                     |
| miner    |  start     |  ip:port/port                      |  如3008或127.0.0.1:3008                          |
| node     |  run       |  ip:port/port                      |  如3008或127.0.0.1:3008                          |
| node     |  list      |  NONEED                            |  显示将广播到的所有节点                            |
| node     |  add       |  ip:port                           |  添加一个将广播到的节点                            |
| tx       |  transfer  |  from_address to_address   amount  |  coin从from_address转移到to_address               |
| tx       |  list      |  NONEED                            |  显示所有交易                                     |

# 原理简介 

## 关于区块

### 比特币区块原理简述

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
区块链就是区块组成的链表结构。而挖矿的本质就是一个新区块，根据现有的一些信息比如父区块hash、时间戳、交易的merkle数根hash再加上一个nonce(从0开始增长的数字)    
连接后生成一个sha256的表现字符串。如果前面数位是几个0开头，0的个数就是挖矿难度，一半根据剩余数量和上一个区块的生成速度动态调整，比如:   
```
00000000000000027e7ba6fe7bad39faf3b5a83daed765f05f7d1b71a1632249
```
挖矿成功，区块生成。   

### Blockchain-python区块简述

Blockchain-python简化的区块结构，一个Blockchain-python的区块数据如下：
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
区块hash的计算与比特币大致相同，我们的难度设置的比较低，所以这个区块的hash前面只有4个0,这是为了更方便的挖矿以了解原理，一般几秒钟可以产出一个区块。另，比特币的tx字段，代表的是交易hash组成的merkle树的根节点hash，我们为了简单，就直接放入了交易hash组成的数组。   

## 关于挖矿

挖矿算法使用的sha256，比特币的算法是根据区块头信息+Nouce(一个数字）作为字符串。简单区块链简化的头部信息，但是机制和比特币是一直的。
区块链在本地以json格式化存储在文件中。一个区块的生成与交易信息是有关联的，所以区块存储的同时，交易信息也会存储下来。
挖矿会有奖励，奖励会作为区块链的第一笔交易记录下来.
- 挖矿的奖励一个是来源于生成区块本身的奖励
- 矿工还会获取纳入区块中的所有交易 输入的金额-输出的金额 的金额
- 待认证的交易会有一些排序规则，根据区块链龄，交易费，交易金额等来做排序

我们简化了实现，只实现奖励的机制。奖励会奖励给当前账户，如果当前账户不存在，请通过下面的命令行生成一个账户：
```
$ python console account create
```

## 关于节点网络

区块链网络是一个 P2P（Peer-to-Peer，端到端）的网络。我们为了简单化，使用了python自带的RPC机制。   
- 通过添加节点操作，可以联通不同节点   
- 联通的节点会自动传播新的交易信息
- 新节点会同步其他节点的区块链的所有数据，同时保证最大链条
- 挖出新的区块会通知其他节点进行同步   

## 关于交易

比特币采用的是 UTXO 模型,并不直接存在“余额”这个概念，余额需要通过遍历整个交易历史得来。我们也实现这个机制。   
一笔交易由一些输入（input）和输出（output）组合而来，在我们的交易中，也会接受多个输入然后产生多个输出。   
- 余额的计算通过未消费的已验证交易输出-已消费交易输出得到，也就是通常所说的UTXO   
- 未被放入新区块的交易，将会被广播到所有节点，等待被验证   
- 交易会等待矿工挖到新的区块之后，被当作区块的附属信息存入交易数据库中   

交易的正确性校验，正在开发中。   

# 贡献

非常欢迎提交代码。

