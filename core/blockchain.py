import datetime
from block import Block

# Create the genesis block
blockchain = [Block.create_origin_block()]
print("Genesis block created!")
print(blockchain[-1])
print("=" * 50)

# Create 10 more blocks
for i in range(1, 11):
    new_block = Block(
        i,
        blockchain[-1].hash,
        f"Block {i} data",
        datetime.datetime.now()
    )
    blockchain.append(new_block)
    print(f"Block #{i} created!")
    print(new_block)
    print("=" * 50)


