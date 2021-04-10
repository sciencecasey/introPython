'''
Created on Mar 23, 2021

@author: CaseyJayne
'''


class LFSR(object):
    '''
    classdocs
    '''

    def __init__(self, seed: str, tap: int):
        '''
        Constructor
        '''
        # check correct types
        if isinstance(tap, int):
            self.tap = tap
        else:
            print("tap needs to be in integer index")
            return
        if isinstance(seed, str):
            self.seed = seed
        else:
            print("Seed needs to be a string")
            return
        if len(seed) < tap:
            print("tap needs to be a valid index of seed")
            return

    def __len__(self):
        return len(self.seed)

    def step(self):
        """
        return the new seed
        """
        # XOR the seed bit and the tap bit
        new = int(self.seed[0]) ^ int(self.seed[-self.tap])
        # shift all the bits down
        temp = self.seed[1:] + str(new)
        # calculate integer value
        return temp

    def __str__(self):
        return f"{self.seed}"


def main():
    seeds = {"0110100111": 2,
             "0100110010": 8,
             "1001011101": 5,
             "0001001100": 1,
             "1010011101": 7}
    for seed, tap in seeds.items():
        new = LFSR(seed, tap).step()
        print(f"{new} {new[-1]}")


if __name__ == "__main__":
    main()
