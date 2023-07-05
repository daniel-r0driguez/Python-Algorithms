import random
import time
random.seed(time.time())
def generateArray(array: list[int], i: int):
    for j in range(0, i):
        array[j] = random.randint(0, 21)
    return array

def main():
    LEN = 100
    array = [0] * LEN
    array = generateArray(array, LEN)
    print(array)
main()