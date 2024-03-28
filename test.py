import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, remitente, destinatario, cantidad):
        self.current_transactions.append({
            'remitente': remitente,
            'destinatario': destinatario,
            'cantidad': cantidad,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

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
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]


            if block['previous_hash'] != self.hash(last_block):
                return False

            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def mine(self):
        last_block = self.last_block
        last_proof = last_block['proof']
        proof = self.proof_of_work(last_proof)

      
        self.new_transaction(
            remitente="0",  
            destinatario=node_identifier,
            cantidad=1,
        )

       
        previous_hash = self.hash(last_block)
        block = self.new_block(proof, previous_hash)

        return block

blockchain = Blockchain()
node_identifier = "miner1"

# Añadir transacciones
blockchain.new_transaction("Juan", "Pedro", 10)
blockchain.new_transaction("Pedro", "Mario", 5)

# Minería de un nuevo bloque
new_block = blockchain.mine()

print("Chain:", blockchain.chain)
