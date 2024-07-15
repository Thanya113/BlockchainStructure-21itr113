import hashlib
import datetime

class Block:
    """
    A class representing a block in the blockchain.
    """

    def __init__(self, index, previous_block_hash, data, timestamp):
        """
        Initialize a new block.
        :param index: Index of the block in the blockchain.
        :param previous_block_hash: Hash of the previous block.
        :param data: Data to be stored in the block.
        :param timestamp: Timestamp of block creation.
        """
        self.index = index
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()

    @staticmethod
    def create_origin_block():
        """
        Create the origin (genesis) block.
        :return: Origin block.
        """
        return Block(0, "0", "Origin Block", datetime.datetime.now())

    def get_hash(self):
        """
        Calculate the hash of the block.
        :return: Hash of the block.
        """
        header_bin = (
            str(self.index) + str(self.previous_block_hash) + str(self.data) + str(self.timestamp)
        ).encode()
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    def __str__(self):
        """
        Return a string representation of the block.
        :return: String representation.
        """
        return (f"Block #{self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_block_hash}\n"
                f"Hash: {self.hash}\n")


if __name__ == "__main__":
    # Test block creation
    genesis_block = Block.create_origin_block()
    print(genesis_block)
