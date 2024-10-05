import sys

def binary_to_file(binary_data, output_file_path):
    byte_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    with open(output_file_path, 'wb') as output_file:
        output_file.write(bytearray(int(b, 2) for b in byte_data))

if __name__ == "__main__":
    binary_data = sys.stdin.read()  # Read from standard input
    output_file_path = sys.argv[1]  # Get output file path from command-line argument
    binary_to_file(binary_data, output_file_path)
