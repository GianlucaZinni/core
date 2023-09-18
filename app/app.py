from hashlib import sha256
import json
from time import time
from typing import List, Dict
from fastapi import FastAPI

app = FastAPI()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Crear el genesis block
        self.new_block(previous_hash="1", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        return sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

blockchain = Blockchain()

@app.post("/vote/")
async def vote(candidate: str):
    sender = "Your Name"  # Replace with actual user authentication
    recipient = candidate
    amount = 1

    # Create a new transaction
    index = blockchain.new_transaction(sender, recipient, amount)

    # Perform proof of work and add a new block
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "Vote recorded successfully",
        'block_index': index,
        'candidate': candidate,
        'proof': proof,
        'previous_hash': previous_hash,
    }

    return response

@app.get("/chain/")
async def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return response
