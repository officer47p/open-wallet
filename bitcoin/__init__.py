from bip32 import BIP32
from mnemonic import Mnemonic
from bitcoinaddress import Address
from bitcoinaddress.key.key import Key


class BitcoinWallet(object):
    def __init__(self, seed: str):
        self.seed = seed

    @classmethod
    def from_mnemonic(cls, words: str):
        mnemo = Mnemonic('english')
        seed = mnemo.to_seed(words, passphrase="")
        return cls(seed)

    def get_address_by_path(self, path, type='P2WPKH', compressed=True):
        bip32 = BIP32.from_seed(self.seed)
        privkey = bip32.get_privkey_from_path(path)
        key = Key.of(privkey.hex())
        if(type == 'P2WPKH'):
            address = Address.of(key).mainnet.pubaddrbc1_P2WPKH
        elif(type == 'P2PKH'):
            if(compressed):
                address = Address.of(key).mainnet.pubaddr1c
        else:
            address = Address.of(key).mainnet.pubaddr1
        return address
