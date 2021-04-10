def getBin(self, seed: str):
    """
    get binary number from string
    """
    num = 0
    for i in range(1, len(seed) + 1):
        # add the binary digit if applicable
        value = int(seed[-i])
        if value:
            num += 2 ** (i - 1)
    return num
