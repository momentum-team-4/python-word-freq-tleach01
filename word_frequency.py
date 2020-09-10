STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

text = open('praise_song_for_the_day.txt', 'r')

d = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    


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
