#!/usr/bin/env python3
"""Test script for quantum visualization functions"""

from utils import create_quantum_state_visualization, create_quantum_circuit_visualization

print("🧪 Testing Quantum Visualization Functions")
print("=" * 50)

# Mock protocol result for testing
mock_result = {
    'success': True,
    'fidelity': 0.95,
    'error_rate': 0.05,
    'noise_level': 0.1,
    'execution_time': 0.123,
    'quantum_advantage': 2
}

test_cases = [
    ([0, 0], "Identity operation"),
    ([0, 1], "X gate only"),
    ([1, 0], "Z gate only"), 
    ([1, 1], "X and Z gates")
]

for bits, description in test_cases:
    print(f"\n📝 Testing: {bits} - {description}")
    
    try:
        # Test quantum state visualization
        state_fig = create_quantum_state_visualization(mock_result, bits)
        print(f"   ✅ Quantum state visualization created")
        print(f"   📊 Figure has {len(state_fig.data)} traces")
        
        # Test circuit visualization  
        circuit_fig = create_quantum_circuit_visualization(bits, mock_result)
        print(f"   ✅ Circuit visualization created")
        print(f"   🔄 Circuit shows gates for bits: {bits}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")

print("\n✅ Quantum visualization test completed!")
