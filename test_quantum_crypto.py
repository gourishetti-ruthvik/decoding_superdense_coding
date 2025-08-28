#!/usr/bin/env python3
"""Test script for quantum cryptography implementation"""

from quantum_protocol import SuperdenseCodingProtocol, QuantumRandomGenerator, QuantumCryptographyEngine

print("🧪 Testing Quantum Cryptography Implementation")
print("=" * 60)

# Test 1: Quantum Random Number Generator
print("\n🎲 Testing Quantum Random Number Generator...")
qrng = QuantumRandomGenerator()

try:
    # Generate random bits and analyze entropy
    random_bits = qrng.generate_quantum_random_bits(16)
    print(f"   ✅ Generated {len(random_bits)} random bits: {random_bits}")
    
    # Calculate entropy
    entropy = qrng.quantum_entropy_analysis(random_bits)
    print(f"   📊 Entropy: {entropy:.3f} bits")
    
    # Generate quantum key
    quantum_key = qrng.generate_quantum_key(32)
    print(f"   🔑 Generated quantum key: {len(quantum_key)} bytes")
    
    # Generate nonce
    nonce = qrng.generate_quantum_nonce(8)
    print(f"   🎯 Generated nonce: {len(nonce)} bytes")
    
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 2: Quantum Cryptography Engine
print("\n🔐 Testing Quantum Cryptography Engine...")
crypto_engine = QuantumCryptographyEngine()

try:
    # Test message
    test_bits = [1, 0]
    print(f"   📝 Original message: {test_bits}")
    
    # Encrypt message
    encrypted_package = crypto_engine.quantum_encrypt_message(test_bits, "alice")
    print(f"   🔒 Encryption successful")
    print(f"   📊 Key entropy: {encrypted_package['metadata']['key_entropy']:.3f}")
    
    # Decrypt message
    decrypted_bits = crypto_engine.quantum_decrypt_message(encrypted_package)
    print(f"   🔓 Decrypted message: {decrypted_bits[:2]}")
    
    # Verify
    success = test_bits == decrypted_bits[:2]
    print(f"   ✅ Encryption/Decryption: {'Success' if success else 'Failed'}")
    
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 3: Enhanced Superdense Coding Protocol
print("\n⚛️ Testing Enhanced Superdense Coding Protocol...")

try:
    # Create protocol with quantum crypto
    protocol = SuperdenseCodingProtocol(enable_quantum_crypto=True)
    print("   ✅ Protocol initialized with quantum cryptography")
    
    # Test protocol execution
    result = protocol.run_protocol_with_quantum_crypto(1, 0, noise_level=0.1)
    print("   ✅ Protocol execution completed")
    
    # Check results
    crypto_enabled = result.get('quantum_crypto_enabled', False)
    encryption_success = result.get('quantum_encryption_success', False)
    decryption_success = result.get('quantum_decryption_success', False)
    
    print(f"   🔐 Quantum crypto enabled: {crypto_enabled}")
    print(f"   🔒 Encryption success: {encryption_success}")
    print(f"   🔓 Decryption success: {decryption_success}")
    
    if 'quantum_key_entropy' in result:
        print(f"   📊 Key entropy: {result['quantum_key_entropy']:.3f}")
    
    if 'quantum_security_level' in result:
        print(f"   🛡️ Security level: {result['quantum_security_level']}")
    
    # Test entropy statistics
    entropy_stats = protocol.get_quantum_entropy_stats()
    if entropy_stats:
        print(f"   📈 Average key entropy: {entropy_stats['avg_key_entropy']:.3f}")
        print(f"   🎯 Quantum quality: {entropy_stats['quantum_quality']}")
    
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n✅ Quantum Cryptography Test Completed!")
print("\n🌟 Features Implemented:")
print("   • Quantum Random Number Generator (QRNG)")
print("   • Quantum Key Generation and Management") 
print("   • Quantum Message Encryption/Decryption")
print("   • Quantum Authentication and Integrity")
print("   • Enhanced Superdense Coding with Crypto")
print("   • Entropy Analysis and Security Metrics")
