from bitcoin import BitcoinWallet

words = 'race romance science affair sad just seminar lens diary relief glimpse horror'
wallet = BitcoinWallet.from_mnemonic(words)
address = wallet.get_address_by_path('m/1/0')

print(address)
