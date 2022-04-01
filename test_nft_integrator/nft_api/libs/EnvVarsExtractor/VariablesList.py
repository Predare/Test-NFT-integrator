from dotenv import dotenv_values

config = dotenv_values(".env")

private_key = config['SIGNER_PRIVATE_KEY']
wallet_address = config['WALLET_ADDRESS']
contract_address = config['CONTRACT_ADDRESS']
contract_abi = config['CONTRACT_ABI']
project_id = config['WEB3_INFURA_PROJECT_ID']