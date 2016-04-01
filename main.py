import csv

from bigchaindb import Bigchain


b = Bigchain()

# read all data from the csv as a dictionary
# e.g. [{
# "ACCOUNT":  "ABC128" ,
# "ASSET":  "ORCL" ,
# "COMM":  "1000" ,
# "COMM_RATE":  "0.02" ,
# "CPTY1":  "MARQUIS" ,
# "CPTY2":  "BONY" ,
# "GROSS PRICE":  "2499000" ,
# "NET PRICE":  "25" ,
# "PRICE":  "50" ,
# "QUANTITY":  "50000" ,
# "SIDE":  "S" ,
# "TYPE":  "EQ"
# },
# ...]
data = []
with open('data.csv', 'r') as fid:
    reader = csv.DictReader(fid)
    for row in reader:
        data.append(row)

# generate distinct users from the CPTY1 column and assign keys
users = []
for user_name in set([d['CPTY1'] for d in data]):
    sk, vk = b.generate_keys()
    user = users.append(
        {
            'name': user_name,
            'signing_key': sk,
            'verifying_key': vk
        }
    )

# create assets on the blockchain with the payload and assign to the user
for asset in data:
    user = [u for u in users if u['name'] == asset['CPTY1']][0]
    tx = b.create_transaction(b.me, user['verifying_key'], None, 'CREATE', payload=asset)
    tx_signed = b.sign_transaction(tx, b.me_private)
    b.write_transaction(tx_signed)