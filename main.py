from KeyManagment import KeyManager
from networks.bitcoin import BitcoinWallet

manager = KeyManager.from_mnemonic(
    'race romance science affair sad just seminar lens diary relief glimpse horror')

private_key = manager.get_private_key(path="m/1/1")
public_key = manager.get_public_key(path="m/1/1", compressed=False)

print(f'Private Key: {private_key.hex()}')
print(f'Public Key: {public_key.hex()}')

address = BitcoinWallet.get_address(private_key)
print(f'Address: {address}')

signature = KeyManager.sign(private_key, b"Hello there")
print(f'Signature: {signature.hex()}')
