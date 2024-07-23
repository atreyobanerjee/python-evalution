import textwrap
import argparse

def justify_text(paragraph, width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            for i in range(width - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            lines.append(''.join(current_line))
            current_line, current_length = [], 0
        current_line.append(word)
        current_length += len(word)

    lines.append(' '.join(current_line).ljust(width))
    return lines

def main():
    parser = argparse.ArgumentParser(description='justify paragrap')
    parser.add_argument('--paragraph-string', type=str, required=True, help='paragraph')
    parser.add_argument('--paragraph-width', type=int, required=True, help='paragraph width')

    args = parser.parse_args()

    justified_text = justify_text(args.paragraph_string, args.paragraph_width)

    for i, line in enumerate(justified_text, 1):
        print(f"Array [{i}] = \"{line}\"")

if __name__ == '__main__':
    main()
