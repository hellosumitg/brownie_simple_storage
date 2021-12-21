# this file will help us read directly from the "Rinkeby" blockchain and it's going to read feom a contract that we've already deployed...
# ...REMEMBER: we did something similar in "web3_py_simple_storage" file by using the "address" and the "abi" in this below command:-
# "simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)"

from brownie import SimpleStorage, accounts, config


def read_contract():
    # print(SimpleStorage[0]) # here by using [0] we would get the frist deployment that we had made and we would find the "contract address" that we deployed on "https://rinkeby.etherscan.io"
    simple_storage = SimpleStorage[-1]
    # here by using [-1] we would get the last or most recent deployment
    # As we know whenever we work with a smart contract we need to know its:-
    # ABI
    # Address
    # and for this brownie already knows its ABI from folders "build-->contracts-->{}SimpleStorage.json" and Address as it gets it saved in the folders "build-->deployments-->4-->{}0x..."
    print(simple_storage.retrieve())


def main():
    read_contract()


# and we can run this above codes written in this "read_value.py" by usiing this command "brownie run scripts/read_value.py --network rinkeby" and finally we get "15" as output
