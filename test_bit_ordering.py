#!/usr/bin/env python3
"""Test script to verify bit ordering in quantum protocol"""
#Import the protocal class to be tested
from quantum_protocol import SuperdenseCodingProtocol

print("🧪 Testing Bit Ordering in Quantum Protocol")
print("=" * 50)

# Define all possible combinations of two bits to test the protocol
test_cases = [
    (0, 0),
    (0, 1), 
    (1, 0),
    (1, 1)
]

#Initialize protocol without quantum cryptography for simplicity
protocol = SuperdenseCodingProtocol(enable_quantum_crypto=False)

#Loop through each test case and check if the decoded bits match the original bits
for bit0, bit1 in test_cases:
    print(f"\n📝 Testing input: bit0={bit0}, bit1={bit1}")
    
    # Run protocol with no noise for clean test
    result = protocol.run_protocol(bit0, bit1, noise_level=0.0)
    
    original = result['original_bits']
    decoded = result['decoded_bits']
    success = result['success']
    
    print(f"   Original: {original}")
    print(f"   Decoded:  {decoded}")
    print(f"   Success:  {success}")
    print(f"   Match:    {original == decoded}")
    
    #Print outcome based on match
    if original != decoded:
        print(f"   ❌ MISMATCH! Expected {original}, got {decoded}")
    else:
        print(f"   ✅ PERFECT MATCH!")

print("\n" + "=" * 50)
print("Bit ordering analysis complete!")
