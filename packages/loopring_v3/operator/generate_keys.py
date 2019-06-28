from create_block import *
import subprocess

class Struct(object): pass

def generate_keys(blockType, numElements, onchainDataAvailability):
    block = Struct()
    block.onchainDataAvailability = onchainDataAvailability
    block.blockType = blockType
    block.numElements = numElements

    blockJson = json.dumps(block, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print("blockJson:", blockJson)

    inputFile = "./blocks/block_meta_" + str(blockType) + "_" + str(numElements) + ".json"
    f = open(inputFile, "w+")
    f.write(blockJson)
    f.close()
    subprocess.check_call(["build/circuit/dex_circuit", "-createkeys", inputFile])


if __name__ == "__main__":
    # generate keys for blocks with length: [1-16, 32, 64, 96, 128]
    size_arr = [4, 8, 16, 32, 64, 96, 128]

    for size in size_arr:
        generate_keys(0, size, False)
        generate_keys(0, size, True)
