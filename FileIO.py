import sys
from itertools import islice, count


class FileHandler:
    def __init__(self, file_name):
        self._file_name = file_name

    def write_text_file(self, content):
        f = open(self._file_name, mode='wt', encoding='utf-8')
        f.write(content)
        f.close()
        return f

    def append_text_to_file(self, content):
        f = open(self._file_name, mode='at', encoding='utf-8')
        f.write(content)
        f.close()
        return f

    def read_text_file(self):
        f = open(self._file_name, mode='rt', encoding='utf-8')
        """Read all lines and display text"""
        lines = f.readlines()
        for line in lines:
            sys.stdout.write(line)

    def write_sequence(self, num):
        """
        write Recaman's sequence to a file
        :param file_name:
        :param num:
        :return:
        """
        try:
            f = open(self._file_name, mode='wt', encoding='utf')
            f.writelines(f"{r}\n" for r in islice(sequence(), num + 1))
        finally:
            f.close()

    def read_sequence(self):
        with open(self._file_name, mode='rt', encoding='utf-8') as f:
            return [int(line.strip()) for line in f]

    def print_sequence(self):
        print()
        n = 1
        for line in self.read_sequence():
            sys.stdout.write(str(line))
            sys.stdout.write(" ")
            if n % 10 == 0:
                print("\n")
            n += 1


def sequence():
    """
    generates Recaman's sequence
    :return:
    """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def main():
    fh = FileHandler("sample.txt")

    content = """This is really a very long text.
    This is the second line.
    This is the third line.
    """

    fh.write_text_file(content)
    fh.append_text_to_file("This fourth line was appended")
    fh.read_text_file()

    sw = FileHandler("sequence.txt")
    sw.write_sequence(100)
    sw.print_sequence()


if __name__ == '__main__':
    main()
