import sys

def file_to_binary(file_path):
    with open(file_path, 'rb') as file:
        binary_data = ''.join(format(byte, '08b') for byte in file.read())
    return binary_data

if __name__ == "__main__":
    input_file_path = sys.argv[1]  # Get input file path from command-line argument
    binary_data = file_to_binary(input_file_path)
    print(binary_data)  # Print the binary data
