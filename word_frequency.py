STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as praise:
        poem = praise.read()

    fileWords = poem.lower().replace('-', " ").replace(":", '').replace(",", " ").replace(".", " ").replace("/n", " ").replace('"', " ").split()

# for line in text:
#     line = line.strip()
#     line = line.lower()
#     words = line.split(" ")

    counted = []

    for word in fileWords:
        if word not in STOP_WORDS:
            counted.append(word)

    d = {}

    for word in counted:
            if word not in d.keys():
                d[word] = 1
            else:
                d[word] += 1

    d_filtered = sorted(d, key=d.get, reverse=True)
    for num in d_filtered:
        print(num, '|', d[num], '*' * d[num])


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
