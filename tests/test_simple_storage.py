# Create in exact the same syntactical name using "test_" in first place as this the syntax that "pytest" is going to be lokking for...
# As this file is used for automatically testing contracts so as to check that they are doing that we want them to do or not.
# without doing it manually that we had did earlier to check whether 15 is updated appropriately or not.
# Also we can write tests directly in solidity as we did in "RemixIDE" and it's also a great way of testing smart contracts
# However a lot of professional developers code their tests in the smart contract development framework programing language like Python or Javascript.
# Doing in this way provide lots of flexibility and customization with what we're doing with our smart contracts and not being confined to whatever only solidity has..

from brownie import SimpleStorage, accounts


def test_deploy():
    # We should know that testing of anything can be separated into 3 categories:-
    # 1. Arrange Stage: in this we setup all the pieces
    account = accounts[0]
    # 2. Act Stage: we will deploy...SimpleStorage contract
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # expected = 15  # just for checking that this test gives an error or not...
    # 3. Assert Stage
    assert starting_value == expected


def test_updating_storage():
    # this function is nearly similar to the "deploy_simple_storage()" as we had written in "deploy.py" file
    # 1. Arrange Stage
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # 2. Act Stage
    expected = 15
    simple_storage.store(expected, {"from": account})
    # 3. Assert Stage
    assert expected == simple_storage.retrieve()
    # assert 5 == simple_storage.retrieve()
    # just for checking for various values we would run "brownie test --pdb"
    # And if we are wrong we would be put in a python shell to check for  differnt values so as to know why our test is failing...


# Some important tips:-
# If we want to test just one function we should use "brownie test -k test_updating_storage
# for getting more detailed output we should use this command "brownie test -s"
# here everything that we want to do to with "brownie test" actually come from "pytest documentation": "https://docs.pytest.org/en/6.2.x/contents.html"
# so if there any flag or some awesome debugger we want to use, we can use it with "brownie    " just by lookig at the "pytest documentation" all tools are exactly the same.
