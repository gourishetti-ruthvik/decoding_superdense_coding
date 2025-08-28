# Quantum Superdense Coding Simulator

A professional, interactive Streamlit application for simulating, visualizing, and analyzing the quantum superdense coding protocol. This simulator is designed for researchers, educators, and students to explore the principles and practicalities of quantum communication, including efficiency, noise effects, and security monitoring.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Real-World Applications](#real-world-applications)
- [Requirements](#requirements)
- [License](#license)
- [Authors](#authors)
- [References](#references)

---

## Overview

**Superdense coding** is a quantum communication protocol that enables the transmission of two classical bits of information by sending only one qubit, provided that the sender and receiver share an entangled pair. This simulator provides a hands-on, visual environment to understand and experiment with the protocol, including the effects of quantum noise and security considerations.

---

## Features

- **Full Protocol Simulation:**  
  Step-by-step execution of the superdense coding protocol, including Bell state creation, message encoding, quantum channel transmission, and decoding.

- **Interactive User Interface:**  
  - Choose message input: manual bit selection, text-to-binary conversion, or real-world scenario presets.
  - Adjust quantum channel noise and security monitoring options.
  - Select visualization modes: standard, detailed, or real-time animation.

- **Real-Time Analytics & Visualization:**  
  - Track protocol fidelity, error rates, and success rates.
  - Visualize communication efficiency, measurement distributions, and performance over time.
  - Analyze protocol balance across all possible bit combinations.

- **Security Monitoring:**  
  - Simulate eavesdropping detection using the CHSH inequality.
  - Visual channel security indicators and recommendations.

- **Professional Visualizations:**  
  - Efficiency comparison charts (classical vs. quantum).
  - Performance dashboards and technical specification displays.
  - Channel quality and security gauges.

- **Application Scenarios:**  
  - Explore use cases in healthcare, finance, and IoT with scenario-based message presets.

- **Testing Tools:**  
  - Protocol balance testing across all bit combinations.
  - Session reset and analytics dashboard.

---

## How It Works

1. **Entanglement:**  
   Alice and Bob share a maximally entangled Bell state.

2. **Encoding:**  
   Alice encodes her 2-bit message using quantum gates (I, X, Z, XZ) on her qubit.

3. **Transmission:**  
   Alice sends her qubit to Bob through a quantum channel, which may introduce noise.

4. **Decoding:**  
   Bob performs a Bell measurement to recover the original 2 bits.

5. **Analysis:**  
   The simulator compares the sent and received bits, calculates fidelity, and updates analytics.

6. **Security:**  
   Optionally, the protocol monitors for eavesdropping using the CHSH inequality.

---

## Project Structure

```
decoding_superdense_coding/
│
├── app.py                # Main Streamlit application (UI and workflow)
├── quantum_protocol.py   # Superdense coding protocol logic and simulation
├── utils.py              # Visualization, analytics, and utility functions
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (this file)
└── __pycache__/          # Python cache files
```

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/gourishetti-ruthvik/decoding_superdense_coding.git
   cd decoding_superdense_coding
   ```

2. **(Recommended) Create and activate a virtual environment:**

   On **Windows**:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

   On **macOS/Linux**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

5. **Open your browser:**  
   Visit the local URL provided by Streamlit (typically http://localhost:8501).
   
---

## Usage

1. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

2. **Open your browser:**  
   Visit the local URL provided by Streamlit (typically http://localhost:8501).

3. **Explore the simulator:**  
   - Configure protocol parameters in the sidebar.
   - Input messages manually, via text, or select from application scenarios.
   - Execute the protocol and analyze results with interactive charts and metrics.
   - Use testing tools for protocol balance and reset session data as needed.

---

## Technical Details

- **Quantum Protocol Implementation:**  
  - Uses Qiskit for quantum circuit simulation (if available), with a realistic classical fallback.
  - Supports adaptive noise modeling and error mitigation.
  - Tracks protocol steps and execution time for each run.

- **Noise Modeling:**  
  - Simulates quantum channel noise using balanced Pauli errors and depolarizing noise models.
  - Allows real-time adjustment of noise level to observe its effect on protocol fidelity.

- **Security Monitoring:**  
  - Implements CHSH inequality checks to simulate eavesdropping detection.
  - Visualizes channel security status and provides recommendations.

- **Visualization:**  
  - Uses Plotly for interactive charts and Streamlit for UI components.
  - Includes efficiency, performance, measurement, and balance analysis charts.

- **Extensibility:**  
  - Modular code structure allows for easy extension to other quantum protocols or additional analytics.

---

## Real-World Applications

- **Healthcare:**  
  - Secure patient data transmission
  - IoT medical device authentication
  - Emergency alert protocols

- **Finance:**  
  - Quantum-safe financial transactions
  - Digital identity verification
  - Secure high-frequency trading

- **IoT:**  
  - Smart grid and industrial automation security
  - Authenticated sensor networks
  - Tamper-proof supply chain tracking

---

## Requirements

See [requirements.txt](requirements.txt) for the full list.  
Key dependencies:
- streamlit
- qiskit
- qiskit-aer
- plotly
- pandas
- numpy

---

## License

This project is for educational and demonstration purposes only.  
Feel free to use, modify, and share for non-commercial and academic purposes.

---

## Authors

Quantum Superdense Coding Simulator  
Developed by Gourishetti Ruthvik, G.Sai Pradhun, Sri Vyshnavi Chepuri, Beshwanth Sai Katari, Sahithi Pasam, Harshitha Koppuravuri.
For questions or contributions, please open an issue or submit a pull request.

---

## References

- [Superdense Coding - Wikipedia](https://en.wikipedia.org/wiki/Superdense_coding)
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Streamlit Documentation](https://docs.streamlit.io/)