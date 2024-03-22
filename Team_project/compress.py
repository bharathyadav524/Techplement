import os
import gzip
import shutil
import argparse

class FileCompress:
    def compress(self, filein, fileout):
        with open(filein, 'rb') as f_in:
            with gzip.open(fileout, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def decompress(self, filein, fileout):
        with gzip.open(filein, 'rb') as f_in:
            with open(fileout, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def reverse_text(self, filein, fileout):
        with open(filein, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
            reversed_content = content[::-1]
        with open(fileout, 'w', encoding='utf-8') as f_out:
            f_out.write(reversed_content)

    def capitalize_text(self, filein, fileout):
        with open(filein, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
            capitalized_content = content.upper()
        with open(fileout, 'w', encoding='utf-8') as f_out:
            f_out.write(capitalized_content)

    def count_lines(self, filein):
        with open(filein, 'r', encoding='utf-8') as f_in:
            line_count = sum(1 for line in f_in)
        return line_count

    def count_words(self, filein):
        with open(filein, 'r', encoding='utf-8') as f_in:
            word_count = len(f_in.read().split())
        return word_count

def main():
    parser = argparse.ArgumentParser(description="File compression, decompression, and text manipulation utility")
    parser.add_argument('file', help="Input file path")
    parser.add_argument('-c', '--compress', action='store_true', help="Compress the file")
    parser.add_argument('-d', '--decompress', action='store_true', help="Decompress the file")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the content of the file")
    parser.add_argument('-C', '--capitalize', action='store_true', help="Convert the content to uppercase")
    parser.add_argument('-l', '--count-lines', action='store_true', help="Count the number of lines in the file")
    parser.add_argument('-w', '--count-words', action='store_true', help="Count the number of words in the file")
    parser.add_argument('-o', '--output', help="Output file name for compression or manipulation")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("Error: File does not exist")
        return

    file_compressor = FileCompress()

    if args.compress:
        output_file = args.output if args.output else args.file + ".gz"
        try:
            file_compressor.compress(args.file, output_file)
            print(f"File compressed successfully and saved as {output_file}")
        except Exception as e:
            print(f"Compression failed: {e}")

    if args.decompress:
        if not args.output:
            print("Error: Output file name required for decompression")
            return
        try:
            file_compressor.decompress(args.file, args.output)
            print(f"File decompressed successfully and saved as {args.output}")
        except Exception as e:
            print(f"Decompression failed: {e}")

    if args.reverse:
        output_file = args.output if args.output else args.file + "_reversed.txt"
        try:
            file_compressor.reverse_text(args.file, output_file)
            print(f"File content reversed successfully and saved as {output_file}")
        except Exception as e:
            print(f"Reversing content failed: {e}")

    if args.capitalize:
        output_file = args.output if args.output else args.file + "_capitalized.txt"
        try:
            file_compressor.capitalize_text(args.file, output_file)
            print(f"File content capitalized successfully and saved as {output_file}")
        except Exception as e:
            print(f"Capitalizing content failed: {e}")

    if args.count_lines:
        try:
            lines = file_compressor.count_lines(args.file)
            print(f"Number of lines in the file: {lines}")
        except Exception as e:
            print(f"Counting lines failed: {e}")

    if args.count_words:
        try:
            words = file_compressor.count_words(args.file)
            print(f"Number of words in the file: {words}")
        except Exception as e:
            print(f"Counting words failed: {e}")

if __name__ == "__main__":
    main()