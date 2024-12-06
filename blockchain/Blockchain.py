import datetime
import hashlib
import json
import copy


# Define the Blockchain class
class Blockchain:
    def __init__(self):
        # Initialize the blockchain with an empty chain, difficulty, transactions, balances, and a copy of the chain
        # for peer comparison

        # stores the chain of blocks
        self.chain = []

        # the condition specifies that the block's hash must start with '00000'
        self.difficulty = '00000'

        # will contain the pending transactions awaiting mining confirmation
        self.transactions = []

        # dictionary(Map) that tracks users balances within the blockchain
        # Each key-value pair represents a user’s public key and their corresponding balance
        self.balances = dict()

        # the very first block and it s hardcoded because there are no previous blocks
        self.genesis_block()

        # This is an order to make a copy of a chain
        # A deep copy means that all elements of self.chain are duplicated,
        # including nested objects (if any).
        # This ensures that the copied object (self.peer_b) is completely independent of the original (self.chain),
        # so changes to self.chain won’t affect self.peer_b and vice versa.
        # A shallow copy, on the other hand, would only copy the references to objects,
        # meaning changes in nested objects could still affect the copy.
        self.peer_b = copy.deepcopy(self.chain)
