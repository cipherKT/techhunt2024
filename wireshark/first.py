from scapy.all import *
import random

def create_packet(size):
    return IP()/UDP()/Raw(load="X" * size)  # Use UDP/IP with a dummy payload

def bit_to_packet_size(bit):
    if bit == '0':
        return 30    
    elif bit == '1':
        return 90

def encode_character(character):
    binary = f"{ord(character):08b}"  # Get 8-bit binary of character
    return [bit_to_packet_size(bit) for bit in binary] + [0,0,0,0,0]  # Add separator

# String to encode
flag = "HxvZ1xZMpJ"
packet_sizes = []

for char in flag:
    packet_sizes.extend(encode_character(char))
    print(f"Character: {char} -> Sizes: {encode_character(char)}")

# print(packet_sizes)
# Create packets and save to pcap
packets = [create_packet(size) for size in packet_sizes]
# print(packet_sizes[0])
# packet = create_packet(packet_sizes[0])
# print(len(packet))
# packets = create_packet(size for size in packet_sizes)
# print(len(s) for s in packets)
wrpcap("ctf_challenge.pcap", packets)

