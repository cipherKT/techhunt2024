import pyshark
import matplotlib.pyplot as plt

# Function to extract packet sizes from a pcap file
def extract_packet_sizes(pcap_file):
    packet_sizes = []
    
    # Open pcap file
    cap = pyshark.FileCapture(pcap_file, use_json=True, include_raw=True)

    # Loop through packets
    for packet in cap:
        try:
            # Extract the packet size (length)
            packet_size = int(packet.length)
            packet_sizes.append(packet_size)
        except AttributeError:
            continue  # If packet doesn't have a length attribute, skip it

    return packet_sizes

# Plot the packet sizes
def plot(packet_sizes):
    plt.plot(packet_sizes, marker = 'o', linestyle = '-', color = 'b', markersize = 4)
    plt.xlabel('Packets')
    plt.ylabel('Size')
    plt.show()
# Main function
def main(pcap_file):
    packet_sizes = extract_packet_sizes(pcap_file)
    print(packet_sizes)
    plot(packet_sizes)

# Example usage:
if __name__ == '__main__':
    pcap_file = 'ctf_challenge.pcap'
    main(pcap_file)

