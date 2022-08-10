import copy
import time


class Block:

    def __init__(self, transactions, lastHash, forger, blockCount):
        self.transactions = transactions
        self.lastHash = lastHash
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        data = {
            'lastHash': self.lastHash,
            'forger': self.forger,
            'blockCount': self.blockCount,
            'timestamp': self.timestamp,
            'signature': self.signature
        }
        jsonTransactions = []
        for transaction in self.transactions:
            jsonTransactions.append(transaction.toJson())
        data['transactions'] = jsonTransactions
        return data

    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    def sign(self, signature):
        self.signature = signature

