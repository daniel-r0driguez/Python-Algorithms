# This algorithm compresses a message by making more redundant characters cost less bits to store.
# So in a compressed file using this algorithm, the custom binary codes created by us as well as the Huffman Tree used to decode the bits
# will be stored in the file.
# In short, this algorithm needs is something to store the frequency of characters, and a Huffman Tree to assign and decode binary codes.
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffmanCodeTree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, binString + '0'))
    d.update(huffmanCodeTree(r, False, binString + '1'))
    return d

def main():
    string = 'ABBEEEEERRRRRRR'
    print("Original String: " + string)
    sizeOfMsg = len(string) * 8
    print("Using ASCII, the size is: " + str(sizeOfMsg) + " bits.")
    # Dictionary holding the count of each character from the string (msg). 
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=False)
    nodes = freq
    while len(nodes) > 1:
        key1, c1 = nodes[0]
        key2, c2 = nodes[1]
        nodes = nodes[2:]
        node = Node(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=False)
    huffmanCode = huffmanCodeTree(nodes[0][0])
    print(' Char | Frequency | Huffman code ')
    print('--------------------------------')
    for (char, frequency) in freq:
        print(' %4r | %4s | %12s' % (char, frequency, huffmanCode[char]))
    sizeOfMsg = 0
    # Find out the size of the compressed msg by multipying the frequency of each char with its bit code length.
    for (char, frequency) in freq:
        sizeOfMsg += frequency * len(huffmanCode[char])
    print("Compressed Message Size is now: " + str(sizeOfMsg) + " bits.")
    # Decode a binary string using the Huffman Tree from before.
    binString = '011111101010100001011001111010110110000001111'
    decoded = ''
    cur = nodes[0][0]
    for i in binString:
        if i == '0':
            cur = cur.left
        elif i == '1':
            cur = cur.right
        # If a char is found, add it to the string decoded and make cur start at the root of the tree.
        if type(cur) == str:
            decoded += cur
            cur = nodes[0][0]
    print("Binary String = " + binString)
    print("When decoded, it spells out: " + decoded)
main()