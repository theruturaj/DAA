import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merge = Node(None, left.freq + right.freq)
        merge.left = left
        merge.right = right

        heapq.heappush(priority_queue, merge)

    return priority_queue[0]

def build_huffman_codes(root):
    def generate_codes(node, current_code):
        if node:
            if node.char:
                codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    codes = {}
    generate_codes(root, "")
    return codes

def encode_text(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def decode_text(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char:
            decoded_text += current.char
            current = root

    return decoded_text

def huffman_encoding(text):
    frequency_dict = defaultdict(int)
    for char in text:
        frequency_dict[char] += 1

    huffman_tree = build_huffman_tree(frequency_dict)
    huffman_codes = build_huffman_codes(huffman_tree)
    encoded_text = encode_text(text, huffman_codes)

    return encoded_text, huffman_tree

def huffman_decoding(encoded_text, root):
    decoded_text = decode_text(encoded_text, root)
    return decoded_text


text_to_encode = input("Enter text to encode -\n")
encoded_text, tree = huffman_encoding(text_to_encode)
decoded_text = huffman_decoding(encoded_text, tree)

print("Original text:", text_to_encode)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
