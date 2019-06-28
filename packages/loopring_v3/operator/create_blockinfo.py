from create_block import *
import subprocess

class Struct(object): pass

def create_fee_account(blockSize, blockIdx):
    depositBlock = Struct()
    depositBlock.onchainDataAvailability = False
    depositBlock.startHash = "0"
    depositBlock.deposits = []
    depositBlock.startIndex = 0
    depositBlock.realmID = 0
    depositBlock.count = blockSize
    for i in range(blockSize):
        deposit = Struct()

        deposit.depositIdx = blockIdx
        deposit.accountID = blockIdx
        deposit.publicKeyX = "1"
        deposit.publicKeyY = "1"
        deposit.secretKey = "1"
        deposit.tokenID = 0
        deposit.amount = "0"
        depositBlock.deposits.append(deposit)

    blockJson = json.dumps(depositBlock, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    # print("blockJson:", blockJson)

    inputFile = "./blocks/block_deposit_info_" + str(blockIdx) + ".json"
    f = open(inputFile, "w+")
    f.write(blockJson)
    f.close()

    blockOutputFile = "./blocks/block_deposit_" + str(blockIdx) + ".json"

    subprocess.check_call([
        "python3",
        "operator/create_block.py",
        "0",
        str(blockIdx),
        "1",
        inputFile,
        blockOutputFile
    ])

    # subprocess.check_call(["build/circuit/dex_circuit", "-createkeys", blockOutputFile])


def create_plain_account(blockSize, blockIdx, tokenId, amount):
    depositBlock = Struct()
    depositBlock.onchainDataAvailability = False
    depositBlock.startHash = "0"
    depositBlock.deposits = []
    depositBlock.startIndex = 0
    depositBlock.realmID = 0
    depositBlock.count = blockSize
    for i in range(blockSize):
        deposit = Struct()
        deposit.depositIdx = blockIdx
        deposit.accountID = blockIdx
        deposit.publicKeyX = "11030389387772387062227238280672938173043468496770435708172848962377071639233"
        deposit.publicKeyY = "12128623127897886109337982198088180333164139385137832250790949664234584942119"
        deposit.secretKey = "853715573630349932064082740595054554633366995671439896121322947697126391831"
        deposit.tokenID = tokenId
        deposit.amount = amount
        depositBlock.deposits.append(deposit)

    blockJson = json.dumps(depositBlock, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    # print("blockJson:", blockJson)

    inputFile = "./blocks/block_deposit_info_" + str(blockIdx) + ".json"
    f = open(inputFile, "w+")
    f.write(blockJson)
    f.close()

    blockOutputFile = "./blocks/block_deposit_" + str(blockIdx) + ".json"

    subprocess.check_call([
        "python3",
        "operator/create_block.py",
        "0",
        str(blockIdx),
        "1",
        inputFile,
        blockOutputFile
    ])

    # subprocess.check_call(["build/circuit/dex_circuit", "-createkeys", blockOutputFile])


def generateRingSettlementBlock(size, onchainDataAvailability, blockIdx):
    rsBlock = Struct()
    rsBlock.onchainDataAvailability = onchainDataAvailability
    rsBlock.timestamp = 0
    rsBlock.realmID = 0
    rsBlock.operatorAccountID = 4
    rsBlock.rings = []
    rsBlock.numElements = size

    for i in range(size):
        ring = Struct()
        ring.minerAccountID = 0
        ring.feeRecipientAccountID = 3
        ring.tokenID = 0
        ring.fee = "0"
        ring.orderA = Struct()
        ring.orderA.realmID = 0
        ring.orderA.orderID = 2 * i
        ring.orderA.accountID = 1
        ring.orderA.walletAccountID = 3
        ring.orderA.dualAuthPublicKeyX = "10915536126060110775271552343906722483233009925409955569530232730101353234195"
        ring.orderA.dualAuthPublicKeyY = "9623628720435786361448780991705015657264158715345955965017234940731292058464"
        ring.orderA.dualAuthSecretKey = "2694468128951809936118766415099067862597033929137076083229886097340106731740"

        ring.orderA.tokenIdS = 1
        ring.orderA.tokenIdB = 2
        ring.orderA.tokenIdF = 1

        ring.orderA.allOrNone = False
        ring.orderA.validSince = 0
        ring.orderA.validUntil = 0
        ring.orderA.walletSplitPercentage = 50
        ring.orderA.waiveFeePercentage = 50

        ring.orderA.amountS = str(int(1e17))
        ring.orderA.amountB = str(int(1e17))
        ring.orderA.amountF = str(int(1e16))

        ring.orderB = Struct()
        ring.orderB.realmID = 0
        ring.orderB.orderID = 2 * i + 1
        ring.orderB.accountID = 2
        ring.orderB.walletAccountID = 3

        ring.orderB.dualAuthPublicKeyX = "10915536126060110775271552343906722483233009925409955569530232730101353234195"
        ring.orderB.dualAuthPublicKeyY = "9623628720435786361448780991705015657264158715345955965017234940731292058464"
        ring.orderB.dualAuthSecretKey = "2694468128951809936118766415099067862597033929137076083229886097340106731740"

        ring.orderB.tokenIdS = 2
        ring.orderB.tokenIdB = 1
        ring.orderB.tokenIdF = 2

        ring.orderB.allOrNone = False
        ring.orderB.validSince = 0
        ring.orderB.validUntil = 0
        ring.orderB.walletSplitPercentage = 50
        ring.orderB.waiveFeePercentage = 50

        ring.orderB.amountS = str(int(1e17))
        ring.orderB.amountB = str(int(1e17))
        ring.orderB.amountF = str(int(1e16))

        rsBlock.rings.append(ring)

    blockJson = json.dumps(rsBlock, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    inputFile = "./blocks/block_trade_info_" + str(blockIdx) + ".json"
    f = open(inputFile, "w+")
    f.write(blockJson)
    f.close()

    blockOutputFile = "./blocks/block_trade_" + str(blockIdx) + ".json"
    blockType = "0"

    subprocess.check_call([
        "python3",
        "operator/create_block.py",
        "0",
        str(blockIdx),
        blockType,
        inputFile,
        blockOutputFile
    ])

    # subprocess.check_call(["build/circuit/dex_circuit", "-createkeys", blockOutputFile])

def generateRingSettlementKeysWithDA(size, blockIdx):
    generateRingSettlementBlock(size, True, blockIdx)

def generateRingSettlementKeysWithoutDA(size, blockIdx):
    generateRingSettlementBlock(size, False, blockIdx)

if __name__ == "__main__":
    # generate keys for blocks with length: [1-16, 32, 64, 96, 128]
    # size_arr = [*range(1, 17), 32, 64, 96, 128]
    # size_arr = [1, 4, 8, 16] # simple test
    size_arr = [8, 16, 32, 64, 128]
    blockIdx = 0

    create_plain_account(1, blockIdx, 0, str(int(1e18)))
    blockIdx += 1
    create_plain_account(1, blockIdx, 1, str(int(1e18)))
    blockIdx += 1
    create_plain_account(1, blockIdx, 2, str(int(1e18)))
    blockIdx += 1

    create_fee_account(1, blockIdx)
    blockIdx += 1
    create_fee_account(1, blockIdx)
    blockIdx += 1
    for size in size_arr:
        generateRingSettlementKeysWithDA(size, blockIdx)
        blockIdx += 1
