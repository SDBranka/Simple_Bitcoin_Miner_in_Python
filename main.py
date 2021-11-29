import hashlib

# prints the hash of 'Hello World'
# sha256 is the algorithm for bitcoin   
# print(hashlib.sha256('Hello World'.encode()).hexdigest())


NONCE_LIMIT = 100000000000
zeros = 6


def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)

        hash_try = hashlib.sha256(base_text.encode()).hexdigest()

        if hash_try.startswith('0' * zeros):
            print(f"Found Hash With Nonce: {nonce}")
            return hash_try
    return -1


block_number = 24
transactions = " 76123fcc2142"
previous_hash = "876de8756b967c87"


# for testing purposes the number at the end of combined_text should be the reurned nonce. If entered and run the hash displyed should have the appropriate number pf leading zeros
# combined_text = str(block_number) + transactions + previous_hash + str(11025864)
# print(hashlib.sha256(combined_text.encode()).hexdigest())


# mine(block_number, transactions, previous_hash)


