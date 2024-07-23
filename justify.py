import argparse

def justify_text(paragraph, width):
    words = paragraph.split()
    lines = []
    current_line = []

    for word in words:
        if len(' '.join(current_line + [word])) <= width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))

    justified_lines = []
    for line in lines[:-1]:
        spaces_to_add = width - len(line)
        words_in_line = line.split()
        if len(words_in_line) == 1:
            justified_lines.append(words_in_line[0] + ' ' * spaces_to_add)
        else:
            spaces = [' '] * (len(words_in_line) - 1)
            while spaces_to_add > 0:
                for i in range(len(spaces)):
                    if spaces_to_add > 0:
                        spaces[i] += ' '
                        spaces_to_add -= 1
            justified_lines.append(''.join(word + space for word, space in zip(words_in_line, spaces)) + words_in_line[-1])

    last_line = lines[-1].split()
    if len(last_line) == 1:
        justified_lines.append(lines[-1].ljust(width))
    else:
        spaces_to_add = width - len(lines[-1])
        words_in_line = last_line
        spaces = [' '] * (len(words_in_line) - 1)
        while spaces_to_add > 0:
            for i in range(len(spaces)):
                if spaces_to_add > 0:
                    spaces[i] += ' '
                    spaces_to_add -= 1
        justified_lines.append(''.join(word + space for word, space in zip(words_in_line, spaces)) + words_in_line[-1])

    return justified_lines

def main():
    parser = argparse.ArgumentParser(description='justify paragrap')
    parser.add_argument('--paragraph-string', type=str, required=True, help='paragraph')
    parser.add_argument('--paragraph-width', type=int, required=True, help='paragraph width')

    args = parser.parse_args()

    justified_text = justify_text(args.paragraph_string, args.paragraph_width)
    for i, line in enumerate(justified_text):
        print(f"Array [{i+1}] = \"{line}\"")
if __name__ == '__main__':
    main()
