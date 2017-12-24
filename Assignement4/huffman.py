import heapq, sys


class Node:
    def __init__(self, key, frequency):
        self.frequency = frequency
        self.left = None
        self.right = None
        self.character = key

    def __cmp__(self, other):
        if isinstance(other, Node):
            return self.frequency > other.frequency
        return -1


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.frequency = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
        self.frequency[' ']=0
        self.frequency['.'] = 0
        self.frequency[',']=0
        self.frequency['?']=0
        self.frequency['!'] = 0
        self.frequency[chr(39)]=0

    def mapping_code(self):
        for code, value in self.frequency.iteritems():
            print code +  "\t" +self.codes[code]+"\t"+ str(value)

    def compress(self, text):
        self.create_frequency_dict(text)
        self.create_heap()
        self.build_tree()
        self.create_code()
        self.mapping_code()

    def build_tree(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            newNode = Node(None, node1.frequency + node2.frequency)
            newNode.left = node1
            newNode.right = node2
            heapq.heappush(self.heap, newNode)

    def create_frequency_dict(self, text):
        global valid_char
        for character in text:
            # if 0 <= ord(character) < 128:
            if character in self.frequency:
                valid_char += 1
                self.frequency[character] += 1

    def create_heap(self):
        for key in self.frequency:
            node = Node(key, self.frequency[key])
            heapq.heappush(self.heap, node)
        return

    def create_code(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.create_code_recursive(root, current_code)

    def create_code_recursive(self, root, current_code):
        if root is None:
            return
        if root.character is not None:
            self.codes[root.character] = current_code
            return
        self.create_code_recursive(root.left, current_code + "0")
        self.create_code_recursive(root.right, current_code + "1")

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            if character in self.codes:
                encoded_text += self.codes[character]
        return encoded_text


def main():
    h = HuffmanCoding()
    with open(sys.argv[1], "r") as f:
        text = f.read().strip().lower()
        text = ''.join(char for char in text if ord(char) < 128)
    h.compress(text)
    encoded_text = h.get_encoded_text(text)
    encoded_bits = len(encoded_text)
    text_bits = valid_char * 5
    bits_saved=text_bits - encoded_bits
    compression_percentage=(bits_saved*100)/text_bits
    print "The text was encoded using {0} bits".format(encoded_bits)
    print "The text had {0} valid characters".format(valid_char)
    print "Using 5 bit fixed length encoding, this would have been {0} bits long".format(text_bits)
    print "so we saved {0} bits".format(bits_saved)
    print "{0:2f} percent compressed".format(compression_percentage)


valid_char = 0

if __name__ == "__main__":
    main()