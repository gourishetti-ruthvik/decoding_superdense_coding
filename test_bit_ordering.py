#!/usr/bin/env python3
"""Test script to verify bit ordering in quantum protocol"""

from quantum_protocol import SuperdenseCodingProtocol

print("🧪 Testing Bit Ordering in Quantum Protocol")
print("=" * 50)

# Test all possible bit combinations
test_cases = [
    (0, 0),
    (0, 1), 
    (1, 0),
    (1, 1)
]

protocol = SuperdenseCodingProtocol(enable_quantum_crypto=False)

for bit0, bit1 in test_cases:
    print(f"\n📝 Testing input: bit0={bit0}, bit1={bit1}")
    
    # Run protocol with no noise for clean test
    # noise_level=0.0 ensures no interference
    # This allows us to isolate and test the bit ordering functionality
    result = protocol.run_protocol(bit0, bit1, noise_level=0.0)
    
    original = result['original_bits']
    decoded = result['decoded_bits']
    success = result['success']
    
    print(f"   Original: {original}")
    print(f"   Decoded:  {decoded}")
    print(f"   Success:  {success}")
    print(f"   Match:    {original == decoded}")
    
    if original != decoded:
        print(f"   ❌ MISMATCH! Expected {original}, got {decoded}")
    else:
        print(f"   ✅ PERFECT MATCH!")

print("\n" + "=" * 50)
print("Bit ordering analysis complete!")
