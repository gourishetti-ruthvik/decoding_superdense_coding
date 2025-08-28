#!/usr/bin/env python3
"""Test script for enhanced text analysis"""
#Import the main protocol logic and utility functions
from utils import text_to_bits

print("🧪 Testing Enhanced Text Analysis")
print("=" * 50)

# Define a list of sample test texts to analyze
test_texts = [
    "Hello World",
    "Quantum Computing", 
    "AI",
    "SuperdenseCoding123",
    "The quick brown fox",
    "a",
    "🚀 Quantum!"
]
# Loop through each test string and analyze it
for text in test_texts:
    print(f"\n📝 Text: \"{text}\"")
    bit0, bit1, analysis = text_to_bits(text)
    print(f"   Final Bits: {bit0}{bit1}")
    print(f"   Length: {analysis['text_length']} chars")
    print(f"   Unique: {analysis['unique_chars']} chars")
    print(f"   Methods:")
    for method, bits in analysis['methods'].items():
        print(f"     {method}: {bits}")

print("\n✅ Text analysis test completed!")
