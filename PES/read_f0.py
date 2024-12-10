import matplotlib.pyplot as plt

def extract_binary_data(log_file_path):
    with open(log_file_path, 'rb') as file:
        content = file.read()

    start = content.find(b'[[[')
    end = content.find(b']]]')
    
    if start != -1 and end != -1:
        return content[start+3:end]
    return None

def parse_pes_values(binary_content):
    """parse 16-bit PES values"""
    pes_values = []
    for i in range(0, len(binary_content), 2):
        if i + 1 < len(binary_content):
            pes_value = int.from_bytes(binary_content[i:i+2], byteorder='little')
            pes_values.append(pes_value)
    return pes_values

def write_pes_values(pes_values, filename="./pes/data/pes_values.txt"):
    with open(filename, "w") as file:
        for item in pes_values:
            file.write(str(item) + "\n")

def plot_pes_values(pes_values):
    plt.figure(figsize=(12, 6))
    plt.plot(pes_values, marker='o', linestyle='-', color='b', label='PES Values')
    plt.title('Plot of PES Values')
    plt.xlabel('Index')
    plt.ylabel('PES Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main(log_file_path):
    binary_content = extract_binary_data(log_file_path)
    
    if binary_content:
        pes_values = parse_pes_values(binary_content)
        
        print("\nParsed PES Values:")
        for i, pes in enumerate(pes_values, 1):
            print(f"PES {i}: {pes} (0x{pes:04X})")
        
        print("\nPES Analysis:")
        print(f"Total PES values: {len(pes_values)}")
        print(f"Min PES value: {min(pes_values)}")
        print(f"Max PES value: {max(pes_values)}")
        
        print("\nHex Dump:")
        hex_dump = ' '.join(f'{byte:02X}' for byte in binary_content)
        print(hex_dump)

        write_pes_values(pes_values)
        plot_pes_values(pes_values)
    else:
        print("No binary data found in the log file.")

log_file_path = './pes/data/f0-silent-1.log'
main(log_file_path)

