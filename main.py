from KeyManagment import KeyManager
from networks.bitcoin import BitcoinWallet

manager = KeyManager.from_mnemonic(
    'race romance science affair sad just seminar lens diary relief glimpse horror')

key = manager.get_private_key_from_path("m/1/1", 'hex')
print(f'Key: {key}')

address = BitcoinWallet.get_address(key, testnet=True)
print(f'Address: {address}')
