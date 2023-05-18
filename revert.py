from web3 import Web3
from multiprocessing import Pool

rpc = "https://little-rough-sailboat.ethereum-goerli.discover.quiknode.pro/c1ef06badd81579c1b00dde6921f2fc760b19446/"
web3 = Web3(Web3.HTTPProvider(rpc))

mtmsku = open('/', 'r', encoding='utf-8').read().splitlines()
addresa = []
for i in range(len(mtmsku)):
    addr = mtmsku[i]
    addresa.append(addr)


def transfer(adrs):
    parts = adrs.split(':')

    wallet = Web3.toChecksumAddress(parts[0])
    private_key = parts[1]
    destination = Web3.toChecksumAddress('###')  # первый кошелёк фермы

    balance = web3.eth.getBalance(wallet)
    fees = web3.toWei('25', 'gwei') * 30000
    nonce = web3.eth.getTransactionCount(wallet)

    tx = {
        'nonce': 0,
        'chainId': 5,
        'to': wallet,
        'value': 0,
        'gas': 30000,
        'gasPrice': web3.toWei('25', 'gwei')
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print("https://goerli.etherscan.io/tx/" + web3.toHex(tx_hash))


if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    p = Pool(processes=process_count)
    p.map(transfer, addresa)
    print("Sucsex")
