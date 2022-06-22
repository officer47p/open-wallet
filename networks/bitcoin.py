from bitcoinaddress import Address
from bitcoinaddress.key.key import Key


class BitcoinWallet(object):

    @classmethod
    def get_address(cls, private_key, testnet=False):
        key = None
        if type(private_key) == bytes:
            key = Key.of(private_key.hex())
        elif type(private_key) == str:
            key = Key.of(private_key)

        return Address.of(key).testnet.pubaddrtb1_P2WPKH if testnet else Address.of(key).mainnet.pubaddrbc1_P2WPKH
