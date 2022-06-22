from mnemonic import Mnemonic
from bip32 import BIP32


class KeyManager(object):
    def __init__(self, seed) -> None:
        self.seed = seed

    @classmethod
    def from_mnemonic(cls, words: str):
        mnemo = Mnemonic('english')
        seed = mnemo.to_seed(words, passphrase="")
        return cls(seed)

    def get_private_key_from_path(self, path, format='bytes'):
        bip32 = BIP32.from_seed(self.seed)
        private_key = bip32.get_privkey_from_path(path)

        if format == 'bytes':
            return private_key
        elif format == 'hex':
            return private_key.hex()

    def get_public_key_from_path(self, path, format='bytes'):
        bip32 = BIP32.from_seed(self.seed)
        public_key = bip32.get_pubkey_from_path(path)

        if format == 'bytes':
            return public_key
        elif format == 'hex':
            return public_key.hex()
