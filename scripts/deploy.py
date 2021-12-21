from brownie import accounts, config, SimpleStorage, network

# earlier as we know for using any smart contract we have to first open that contract and read through it and that's how we were able to interact with it after we deploy it
# but using "brownie" we can directly "import" that smart contract into our script
# here we import this "network" keyword from brownie allows us to interact with differnt netwoks

# import os

# here using this "accounts" keyword we can add accounts in 3 differnt ways


def deploy_simple_storage():
    account = get_account()
    # here we want to use very 1st account that "brownie" makes for us by using "ganache-cli" and it can only be used when brownie works wih ganache-cli
    # print(account)
    # account = accounts.load("freecodecamp-account")
    # print(account)
    # we can also add brownie directly from terminal by using "brownie accounts new freecodecamp-account"
    # Also we can check our accounts list using "brownie accounts list"
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # when we use "config" we don't need to "import os" i.e no need to use "os.___()" as it grab information from "brownie-config.yaml" file
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    # using this we can directly deploy this contract to a chain
    # and it will automatically detect that it's a Transaction or Call so here we don't have to explicity tell that it's a Transact.. or a Call..
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    # Always remember that when we are going to do a transaction brownie requires the "account" from where we want to do the transaction
    transaction.wait(1)  # similar to that we had did in "web3_py_simple_storage"
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    # this function natively checks if we're working on a "Development Network" in this case we'll use "account[0]" and if not we'll use the method that pulls from our "brownie-config.yaml" file
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()


# After doing all things, now we actually want to Deploy to a Testnet which we did in the last "web3_py_simple_storage" file...
# ...where we just needed to add our http web3 provider which was our "infura account" and along with it we added our "Account Address" and "Private Key"...
# ...but in Brownie we get a pre-packaged list of network that it's alraedy compatible with and we can see all of that by running "brownie networks list"
# After running code we can see there is a difference between the "Develpoment Networks"(i.e Temporary Networks) and "Ethereum Networks"(i.e Persistent Networks)...
# ...So whenever we deploy to a network we default to this "Development Networks" as this is temporary so everything on these blockchains are deleted after our script completes it's deployment
# but however when we deploy to a "Ethereum Networks" which is persistent, so anything under this category of network, brownie is actcually going to keep track of our deployments and everythings in there...
# Now in our "web3_py_simple_storage" we used an "RPC url" or an "http provider" from "infura" to connect to a testnet we're going to use that exact same methodology...
# here in our brownie smart contract using an environment varibale same we did earlier in ".env" file so that brownie actually knows that infura is thing and can look natively for infura web3 project id...
# ...so that brownnie can use networks which are compatible with "Infura" by using this command "brownie run scripts/deploy.py --network rinkeby"
# Now if we watch our folders gets change watch in this specific order "build"-->"deployments"-->"4"(i.e our Chain_ID/ Network_ID of Rinkeby)-->"{}0x....." So everytime when we deploy to a blockchain brownie will actually save that deployment...
# ...so we can always go back and watch our past deployments...
# REMEMBER: we can only able to watch the deployment which were done on the "Ethereum Networks"(as it was saved) and not anything done on the "Development Networks"(as it was deleted)

# One of the most powerful feature of brownie, as typically we write scripts when we want something to be reproducible and we want to do something over and over again such as deploying simple storage or reading of value...
# However maybe we want to work with some of these contracts a little bit adhocc and get into a shell where we can actually interact with these contracts this is where the "brownie console" is actually going to come into play by writing these in the console that we get
# >>> SimpleStorage
# []
# >>> account = accounts[0]
# >>> account
# <Account '0x66aB6D9362d4F35596279692F0251Db635165871'>
# >>> simple_storage = SimpleStorage.deploy({"from": account})
# Transaction sent: 0x056b67af2d220b0341734bb5bde3cfa8560fad420c0b24c6a40593b1119dcbd4
#  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
#  SimpleStorage.constructor confirmed   Block: 1   Gas used: 334828 (2.79%)
#  SimpleStorage deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

# >>> simple_storage
# <SimpleStorage Contract '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87'>
# >>> SimpleStorage
# [<SimpleStorage Contract '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87'>]
# >>> len(SimpleStorage)
# 1
# >>> simple_storage = SimpleStorage.deploy({"from": account})
# Transaction sent: 0xdabbf7239d77c57222223d54a0d397bb8c8fcee22b02116ae3e49d0adfe85ad1
#  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 1
#  SimpleStorage.constructor confirmed   Block: 2   Gas used: 334828 (2.79%)
#  SimpleStorage deployed at: 0x602C71e4DAC47a042Ee7f46E0aee17F94A3bA0B6

# >>> len(SimpleStorage)
# 2
# So here everything that we had imported in our scripts is automatically already imported into this little shell here...
# >>> simple_storage.retrieve()
# 0
# >>> simple_storage.store(15, {"from": account})
# Transaction sent: 0x8e15adad8f35d811132d3034ee089c2f8b991df5be1125f80fe3e3df51baaec4
#  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 2
#  SimpleStorage.store confirmed   Block: 3   Gas used: 41393 (0.34%)

# <Transaction '0x8e15adad8f35d811132d3034ee089c2f8b991df5be1125f80fe3e3df51baaec4'>
# >>> simple_storage.retrieve()
# 15

# We can also run python commands as brownie is written in python
# >>> print("Hello!")
# Hello!
# >>> cat = 1 + 2
# >>> cat
# 3

# and we can quit using "quit()" command
