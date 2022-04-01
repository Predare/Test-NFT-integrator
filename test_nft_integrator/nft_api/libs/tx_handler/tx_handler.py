from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import inspect
from ..env_vars_extractor.variables_list import private_key,wallet_address,contract_address,contract_abi,project_id

w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/{}'.format(project_id)))  
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract_instance = w3.eth.contract(address=contract_address, abi=contract_abi)
def tx_create(data):
    
    transaction = contract_instance.functions.mint(data['owner'],data['unique_hash'],data['media_url']).buildTransaction({
        'chainId': 4,
        'gas': 10000000,
        'maxFeePerGas': w3.toWei('2', 'gwei'),
        'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
        'nonce': w3.eth.get_transaction_count(wallet_address),
    })
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)

    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_hash

def tx_total_supply():
    totalSupply = contract_instance.functions.totalSupply().call()
    return totalSupply