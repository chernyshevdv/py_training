import sys

vocab = "".join(chr(i) for i in range(int(0x1F600), int(0x1F64F+1)))

shift = int(input().strip())
text = input().strip().lower()
result = ""
for char in text:
    old_pos = vocab.find(char)
    if old_pos < 0:
        print(f"Wrong symbol: {char}")
        sys.exit(1)
    new_pos = (old_pos + shift) % len(vocab)
    result += vocab[new_pos]
print(f"Result: \"{result}\"")