# 🌌 Quantum Superdense Coding Simulator

![Quantum Computing](https://img.shields.io/badge/Quantum-Computing-blueviolet?style=for-the-badge&logo=atom&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Qiskit](https://img.shields.io/badge/Qiskit-6929C4?style=for-the-badge&logo=qiskit&logoColor=white)
![Academic](https://img.shields.io/badge/Purpose-Academic%20%26%20Educational-orange?style=for-the-badge)

## 📋 Team Members

| 👤 **Team Member** | 🎯 **Role** | 💫 **Contribution** |
|--------------------|-------------|---------------------|
| **Gourishetti Ruthvik** | 🚀 Lead Developer | Core Development & Implementation Leadership |
| **G. Sai Pradhun** | 🏗️ Project Architect | System Architecture & Technical Design |
| **Sri Vyshnavi Chepuri** | 🎨 UX Research & Testing | User Experience & Visual Appeal Assessment |  
| **Beshwanth Sai Katari** | 🧠 Research Specialist | Research & Analysis |
| **Sahithi Pasam** | 🧪 Quality Assurance | System Testing & Vulnerability Detection |
| **Harshitha Koppuravuri** | ⚡ Test Engineer | Comprehensive Testing & Quality Validation |

## 🔬 Project Overview

A comprehensive quantum computing simulator that demonstrates the **Superdense Coding Protocol** - a fascinating quantum communication technique that allows transmission of 2 classical bits using just 1 qubit through quantum entanglement and Bell states.

## ✨ Key Features

- **🎯 Interactive Quantum Simulation**: Real-time visualization of quantum states and operations
- **📊 Educational Dashboard**: Step-by-step protocol breakdown with visual explanations
- **🔐 Quantum Cryptography**: Secure message transmission using quantum properties
- **📈 Performance Analytics**: Detailed metrics and success rate tracking
- **🎨 Modern UI/UX**: Streamlit-powered interface with cosmic theme
- **🧪 Comprehensive Testing**: Full test suite for protocol validation

## 🛠️ Technology Stack

- **Quantum Computing**: Qiskit Framework
- **Backend**: Python 3.8+
- **Frontend**: Streamlit
- **Visualization**: Matplotlib, Plotly
- **Testing**: Pytest
- **Version Control**: Git

## 🚀 Quick Start

### Prerequisites
```bash
python >= 3.8
pip >= 21.0
```

### Installation
```bash
# Clone the repository
git clone https://github.com/gourishetti-ruthvik/decoding_superdense_coding.git
cd decoding_superdense_coding

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📖 How It Works

### Superdense Coding Protocol

1. **🔗 Entanglement Creation**: Generate Bell state pairs
2. **📤 Encoding**: Apply quantum gates based on message bits
3. **📡 Transmission**: Send encoded qubit through quantum channel
4. **🔓 Decoding**: Perform Bell measurement to extract 2 bits
5. **✅ Verification**: Validate message integrity and success rate

### Quantum States Used

| **Message** | **Quantum Gate** | **Bell State** | **Measurement** |
|-------------|------------------|----------------|-----------------|
| 00          | I (Identity)     | \|Φ⁺⟩          | 00              |
| 01          | X (Pauli-X)      | \|Ψ⁺⟩          | 01              |
| 10          | Z (Pauli-Z)      | \|Φ⁻⟩          | 10              |
| 11          | Y (Pauli-Y)      | \|Ψ⁻⟩          | 11              |

## 🔬 Scientific Background

### Theoretical Foundation

This project implements concepts from several groundbreaking quantum information papers:

- **[Quantum Cryptography: Public Key Distribution and Coin Tossing](https://doi.org/10.1016/j.tcs.2014.05.025)** - Bennett & Brassard (1984)
- **[Communication via One- and Two-Particle Operators on Einstein-Podolsky-Rosen States](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.69.2881)** - Bennett & Wiesner (1992)
- **[Quantum Information and Computation](https://doi.org/10.1017/CBO9780511976667)** - Nielsen & Chuang (2010)
- **[Entanglement and Quantum Superposition](https://doi.org/10.1038/nature13171)** - Modern Quantum Mechanics Review (2014)

### Protocol Efficiency

- **Classical Communication**: 2 bits require 2 transmissions
- **Quantum Superdense Coding**: 2 bits require 1 qubit transmission + shared entanglement
- **Efficiency Gain**: 50% reduction in quantum channel usage

## 📊 Testing & Validation

### Test Coverage

- ✅ **Quantum Protocol Tests**: Bell state generation and measurement accuracy
- ✅ **Bit Ordering Tests**: Message encoding/decoding consistency  
- ✅ **Cryptographic Tests**: Security and integrity validation
- ✅ **Visualization Tests**: UI component and display verification
- ✅ **Text Analysis Tests**: Message processing and validation
- ✅ **Integration Tests**: End-to-end protocol validation

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test categories
python -m pytest test_quantum_protocol.py    # Protocol tests
python -m pytest test_bit_ordering.py        # Encoding tests
python -m pytest test_quantum_crypto.py      # Security tests
```

## 📁 Project Structure

```
decoding_superdense_coding/
├── app.py                          # Main Streamlit application
├── quantum_protocol.py             # Core quantum protocol implementation
├── utils.py                        # Utility functions and helpers
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── test_quantum_protocol.py        # Protocol unit tests
├── test_bit_ordering.py            # Encoding/decoding tests
├── test_quantum_crypto.py          # Cryptographic validation tests
├── test_quantum_viz.py             # Visualization tests
├── test_text_analysis.py           # Text processing tests
└── test_validation_final.py        # Integration tests
```

## 🎯 Usage Examples

### Basic Message Transmission
```python
from quantum_protocol import SuperdenseCoding

# Initialize protocol
sdc = SuperdenseCoding()

# Encode and transmit message
message = "01"  # 2-bit message
success = sdc.transmit_message(message)
print(f"Transmission success: {success}")
```

### Batch Processing
```python
# Test multiple messages
messages = ["00", "01", "10", "11"]
results = [sdc.transmit_message(msg) for msg in messages]
success_rate = sum(results) / len(results)
print(f"Success rate: {success_rate:.2%}")
```

## 🔐 Security Features

- **Quantum No-Cloning**: Information cannot be copied without detection
- **Bell State Security**: Entanglement provides cryptographic security
- **Measurement Protection**: Eavesdropping attempts collapse quantum states
- **Integrity Verification**: Built-in error detection and correction

## 🎨 User Interface

### Dashboard Features
- 🎛️ **Interactive Controls**: Message input and protocol parameters
- 📊 **Real-time Visualization**: Quantum circuit and state diagrams  
- 📈 **Analytics Panel**: Success rates and performance metrics
- 🎨 **Cosmic Theme**: Modern dark theme with quantum-inspired design
- 📱 **Responsive Design**: Works on desktop and mobile devices

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📄 License & Usage

**🎓 Academic & Educational Use Only**

This project is developed for **academic research and educational purposes only**. It serves as a quantum computing simulator and learning tool for understanding superdense coding protocols.

**📋 Usage Terms:**
- ✅ **Academic Research**: Permitted for educational institutions and research
- ✅ **Learning & Teaching**: Can be used in quantum computing courses and workshops  
- ✅ **Personal Study**: Individual learning and experimentation encouraged
- ❌ **Commercial Use**: Not licensed for commercial or production applications
- ❌ **Redistribution**: Please reference original repository for updates

**📚 Citation:**
If you use this simulator in academic work, please cite this repository and acknowledge the team members listed above.

## 🙏 Acknowledgments

- **Qiskit Team** for the excellent quantum computing framework
- **Streamlit Community** for the amazing web app framework
- **Quantum Computing Research Community** for foundational research
- **IBM Quantum Experience** for quantum hardware access and resources

## 📞 Contact

- **Lead Developer**: Gourishetti Ruthvik
- **Project Repository**: [GitHub - decoding_superdense_coding](https://github.com/gourishetti-ruthvik/decoding_superdense_coding)
- **Issues & Support**: [GitHub Issues](https://github.com/gourishetti-ruthvik/decoding_superdense_coding/issues)

---

**⚡ Powered by Quantum Computing | 🌟 Built with Python & Streamlit | 🔬 Research-Driven Innovation**
