# file_compression.py

def compress(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tokenize: split into words, preserve newlines as tokens
    lines = content.splitlines()
    tokens = []
    for i, line in enumerate(lines):
        tokens.extend(line.split())
        if i < len(lines) - 1:
            tokens.append('\n')  # newline as special token

    # Build vocabulary (unique words → index)
    vocab = {}
    for token in tokens:
        if token not in vocab:
            vocab[token] = len(vocab)

    # Write compressed file
    with open(output_path, 'w', encoding='utf-8') as f:
        # Section 1: vocabulary  (one word per line)
        f.write(f"{len(vocab)}\n")
        for word in vocab:
            f.write(word + '\n')

        # Section 2: index sequence
        indices = [str(vocab[t]) for t in tokens]
        f.write(' '.join(indices) + '\n')

    original_size = len(content.encode('utf-8'))
    compressed_size = os.path.getsize(output_path)
    print(f"[Compress] {original_size} bytes → {compressed_size} bytes "
          f"({100 - compressed_size / original_size * 100:.1f}% saved)")


def decompress(compressed_path, output_path):
    with open(compressed_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    vocab_size = int(lines[0].strip())

    # Rebuild index → word mapping
    index_to_word = {}
    for i in range(1, vocab_size + 1):
        index_to_word[i - 1] = lines[i].rstrip('\n')

    # Rebuild token list from index sequence
    indices = list(map(int, lines[vocab_size + 1].split()))
    tokens = [index_to_word[i] for i in indices]

    # Reconstruct original text
    result = []
    for token in tokens:
        if token == '\n':
            result.append('\n')
        else:
            # Add space before word if previous char isn't newline
            if result and result[-1] != '\n':
                result.append(' ')
            result.append(token)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(result))

    print(f"[Decompress] Done → {output_path}")


# ── Main ──────────────────────────────────────────────
import os

compress('F:\\pycharm\\test.txt', 'fileName_compressed.txt')
decompress('F:\\pycharm\\test_restored.txt', 'fileName_restored.txt')

# Verify: so sánh nội dung (content comparison)
with open('F:\\pycharm\\test.txt', 'r', encoding='utf-8') as f:
    original = f.read()
with open('F:\\pycharm\\test_restored.txt', 'r', encoding='utf-8') as f:
    restored = f.read()

print("Identical:", original.strip() == restored.strip())