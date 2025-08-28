#!/usr/bin/env python3
"""
Bit Ordering Test - Quantum Protocol Verification

This test script systematically verifies the bit ordering in the quantum
superdense coding protocol to ensure proper encoding and decoding.

PURPOSE:
- Test all possible 2-bit combinations (00, 01, 10, 11)
- Verify that quantum gates correctly encode information
- Ensure Bell state measurements decode bits accurately
- Validate that bit ordering is consistent throughout the protocol

QUANTUM ENCODING SCHEME:
- 00 → Identity operation → |Φ+⟩ = (|00⟩ + |11⟩)/√2
- 01 → X gate operation → |Ψ+⟩ = (|01⟩ + |10⟩)/√2  
- 10 → Z gate operation → |Φ-⟩ = (|00⟩ - |11⟩)/√2
- 11 → XZ operation → |Ψ-⟩ = (|01⟩ - |10⟩)/√2

This systematic testing ensures the quantum protocol maintains
perfect fidelity under ideal conditions (no noise).
"""

# Import the quantum protocol class to be tested
from quantum_protocol import SuperdenseCodingProtocol

print("🧪 Testing Bit Ordering in Quantum Protocol")
print("=" * 50)

# Define all possible combinations of two bits to comprehensively test the protocol
# This covers the complete truth table for 2-bit quantum superdense coding
test_cases = [
    (0, 0),  # No quantum operations (Identity)
    (0, 1),  # X gate only (bit flip)
    (1, 0),  # Z gate only (phase flip)
    (1, 1)   # Both X and Z gates (bit flip + phase flip)
]

# Initialize protocol without quantum cryptography for clean testing
# This focuses the test on core superdense coding functionality
protocol = SuperdenseCodingProtocol(enable_quantum_crypto=False)

# Loop through each test case and verify correct encoding/decoding
print("\n🔍 Systematic Testing of All Bit Combinations:")
for bit0, bit1 in test_cases:
    print(f"\n📝 Testing input: bit0={bit0}, bit1={bit1}")
    
    # Run protocol with no noise for clean test conditions
    # noise_level=0.0 ensures no quantum decoherence or interference
    # This allows us to isolate and test the pure bit ordering functionality
    result = protocol.run_protocol(bit0, bit1, noise_level=0.0)
    
    # Extract results for validation
    original = result['original_bits']    # Input bits
    decoded = result['decoded_bits']      # Output bits after quantum protocol
    success = result['success']           # Protocol success flag
    
    # Display test results with clear formatting
    print(f"   Original: {original}")
    print(f"   Decoded:  {decoded}")
    print(f"   Success:  {success}")
    print(f"   Match:    {original == decoded}")
    
    # Provide clear pass/fail indication for each test case
    if original != decoded:
        print(f"   ❌ MISMATCH! Expected {original}, got {decoded}")
        print(f"      → This indicates a problem with quantum gate encoding or measurement")
    else:
        print(f"   ✅ PERFECT MATCH!")
        print(f"      → Quantum encoding and decoding working correctly")

print("\n" + "=" * 50)
print("🎯 Bit ordering analysis complete!")
print("\nSUMMARY:")
print("- All test cases should show PERFECT MATCH under ideal conditions")
print("- Any mismatches indicate issues with quantum gate implementation")
print("- This test validates the core superdense coding protocol functionality")
