#!/usr/bin/env python3
"""
Test script to debug text transmission validation issues
"""
#Tests for superdense Coding Protocol implementation

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quantum_protocol import SuperdenseCodingProtocol
import hashlib

# Function to convert text to bits using various methods
def text_to_bits_hash_based(text, method="hash"):
    """Convert text to bits using hash-based method (same as in app.py)"""
    if method == "hash":
        hash_val = int(hashlib.md5(text.encode()).hexdigest(), 16)
        bit1 = (hash_val >> 0) & 1
        bit0 = (hash_val >> 1) & 1
        return [bit0, bit1]
    #Should return [1, 0] for input bits [1, 0]
    elif method == "frequency":
        char_freq = {}
        for char in text:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        total_chars = len(text)
        unique_chars = len(char_freq)
        
        # Use frequency metrics to determine bits
        bit0 = 1 if unique_chars > (total_chars / 2) else 0
        bit1 = 1 if any(freq > 1 for freq in char_freq.values()) else 0
        
        return [bit0, bit1]
    elif method == "ascii_sum":
        ascii_sum = sum(ord(char) for char in text)
        bit0 = ascii_sum % 2
        bit1 = (ascii_sum // 2) % 2
        return [bit0, bit1]
    elif method == "diversity":
        vowels = sum(1 for char in text.lower() if char in 'aeiou')
        consonants = sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiou')
        
        bit0 = 1 if vowels > consonants else 0
        bit1 = 1 if len(text) > 5 else 0
        
        return [bit0, bit1]
    else:
        # Default: first character ASCII
        if text:
            ascii_val = ord(text[0])
            return [ascii_val % 2, (ascii_val >> 1) % 2]
        return [0, 0]

def test_text_transmission():
    print("🧪 Testing Text Transmission Validation")
    print("=" * 50)
    
    # Test cases from user reports
    test_cases = [
        ("01", "hash"),
        ("10", "hash"),
        ("hello", "hash"),
        ("world", "hash"),
        ("test", "frequency"),
        ("example", "ascii_sum"),
        ("quantum", "diversity"),
    ]
    
    protocol = SuperdenseCodingProtocol()
    
    for text_input, method in test_cases:
        print(f"\n📝 Testing text: '{text_input}' with method: {method}")
        
        # Convert text to bits using the same method as app.py
        original_bits = text_to_bits_hash_based(text_input, method)
        print(f"   Original bits: {original_bits}")
        
        # Run the quantum protocol
        result = protocol.run_protocol(original_bits[0], original_bits[1])
        decoded_bits = result['decoded_bits']
        protocol_success = result['success']
        
        print(f"   Decoded bits:  {decoded_bits}")
        print(f"   Protocol says: {'SUCCESS' if protocol_success else 'FAILED'}")
        
        # Manual comparison (like in the updated app.py)
        manual_match = (original_bits == decoded_bits)
        print(f"   Manual match:  {manual_match}")
        
        if manual_match:
            print("   ✅ PERFECT MATCH!")
        else:
            print("   ❌ MISMATCH DETECTED!")
            print(f"   🔍 Original: {original_bits}")
            print(f"   🔍 Decoded:  {decoded_bits}")
            
        print(f"   Protocol success: {protocol_success}, Manual match: {manual_match}")

if __name__ == "__main__":
    test_text_transmission()
