from brownie import FundMe, network, config, MockV3Aggregator, accounts
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN
from web3 import Web3 


if network.show_active() not in LOCAL_BLOCKCHAIN:
   price_feed_address = config[network][network.show_active()]["price_feed_address"]
else:
    deploy_mocks()
 
def deploy_FundMe():
    account = get_account()
    newFundme = FundMe.deploy(price_feed_address,{"from": account}) #, publish_source=config[network][network.show_active()].get("verify"))
    print(f"Contract deployed to {newFundme.address}")



def main(): 
    deploy_FundMe()