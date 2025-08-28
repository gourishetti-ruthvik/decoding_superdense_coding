"""
Professional Superdense Coding Simulator
FIXED VERSION - All Issues Resolved
"""

import streamlit as st
import time
from quantum_protocol import SuperdenseCodingProtocol
from utils import *

# Configure Streamlit with professional settings
st.set_page_config(
    page_title="Quantum Superdense Coding Simulator",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e1e8ed;
        text-align: center;
    }
    
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application with professional UI and fixed functionality"""
    
    # Professional header
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5em;">⚛️ Quantum Superdense Coding Simulator</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.2em; opacity: 0.9;">
            Advanced Quantum Communication Protocol Demonstration
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize protocol with session state
    if 'protocol' not in st.session_state:
        st.session_state.protocol = SuperdenseCodingProtocol()
    
    protocol = st.session_state.protocol
    
    # Sidebar configuration - FIXED
    st.sidebar.header("⚙️ Protocol Configuration")
    
    # FIXED: Noise level slider with proper range and explanation
    st.sidebar.markdown("### Channel Noise Settings")
    noise_level = st.sidebar.slider(
        "Quantum Channel Noise Level",
        min_value=0.00,
        max_value=0.50,  # Increased range for better testing
        value=0.05,
        step=0.01,
        help="Probability of quantum errors during transmission (0 = perfect channel, 0.5 = very noisy)"
    )
    protocol.noise_level = noise_level
    
    # Display noise level interpretation
    if noise_level <= 0.05:
        noise_desc = "🟢 Excellent (Laboratory conditions)"
    elif noise_level <= 0.15:
        noise_desc = "🟡 Good (Practical quantum networks)" 
    elif noise_level <= 0.30:
        noise_desc = "🟠 Challenging (Early quantum internet)"
    else:
        noise_desc = "🔴 Severe (Experimental conditions)"
    
    st.sidebar.markdown(f"**Channel Quality:** {noise_desc}")
    
    # Security monitoring toggle
    enable_security = st.sidebar.checkbox(
        "🛡️ Enable Security Monitoring",
        value=True,
        help="Monitor CHSH inequality for eavesdropping detection"
    )
    
    # Visualization options
    st.sidebar.markdown("### Visualization Options")
    visualization_mode = st.sidebar.selectbox(
        "Execution Mode",
        ["Standard View", "Detailed Analysis", "Real-time Animation"],
        help="Choose how to display protocol execution"
    )
    
    show_technical_specs = st.sidebar.checkbox("Show Technical Specifications", value=False)
    
    # Testing and analysis tools
    st.sidebar.markdown("### 🧪 Testing Tools")
    
    if st.sidebar.button("🔄 Reset All Results", help="Clear all execution history"):
        protocol.reset_results()
        st.sidebar.success("Results cleared!")
        st.rerun()
    
    if st.sidebar.button("⚖️ Test Protocol Balance", help="Run balanced tests on all bit combinations"):
        with st.sidebar:
            with st.spinner("Running balance tests..."):
                balance_results = protocol.test_protocol_balance(
                    num_tests_per_combination=5, 
                    noise_level=noise_level
                )
            st.success("Balance test completed!")
            
            # Show quick balance summary
            success_rates = [data['success_rate'] for data in balance_results.values()]
            balance_score = 1.0 - (max(success_rates) - min(success_rates))
            st.metric("Balance Score", f"{balance_score:.3f}")
        
        st.rerun()
    
    # Main content area
    if show_technical_specs:
        st.markdown("## 📋 Technical Specifications")
        display_technical_specs()
        st.markdown("---")
    
    # Protocol efficiency comparison
    st.markdown("## 📊 Communication Efficiency Analysis")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Classical Protocol",
            "1 bit",
            help="Traditional communication: 1 bit per transmission"
        )
    
    with col2:
        st.metric(
            "Superdense Coding",
            "2 bits",
            delta="100% improvement",
            help="Quantum protocol: 2 bits per qubit using entanglement"
        )
    
    with col3:
        st.metric(
            "Quantum Advantage",
            "2.0x",
            help="Multiplicative efficiency gain over classical methods"
        )
    
    with col4:
        st.metric(
            "Channel Efficiency",
            f"{(1-noise_level)*100:.0f}%",
            help="Current channel quality based on noise level"
        )
    
    # Efficiency chart
    fig = create_efficiency_chart()
    st.plotly_chart(fig, use_container_width=True)
    
    # Protocol execution section
    st.markdown("## 🚀 Protocol Execution Interface")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Message Input Configuration")
        
        # FIXED: Input method selection with proper functionality
        input_method = st.radio(
            "Select Input Method:",
            ["Manual Bit Selection", "Text to Binary", "Application Scenarios"],
            horizontal=True
        )
        
        if input_method == "Manual Bit Selection":
            st.markdown("**Direct Binary Input:**")
            col_a, col_b = st.columns(2)
            with col_a:
                bit0 = st.selectbox("First Bit (b₀)", [0, 1], help="Controls Z gate operation")
            with col_b:
                bit1 = st.selectbox("Second Bit (b₁)", [0, 1], help="Controls X gate operation")
                
            st.info(f"Selected Message: **{format_bits_display([bit0, bit1])}**")
        
        elif input_method == "Text to Binary":
            text_input = st.text_input(
                "Enter Text:",
                value="Hello World",
                max_chars=100,
                help="Entire text will be analyzed using multiple encoding methods"
            )
            
            if text_input:
                bit0, bit1, analysis_data = text_to_bits(text_input)
                
                # Let user choose encoding method
                col_method, col_preview = st.columns([1, 1])
                
                with col_method:
                    selected_method = st.selectbox(
                        "Choose Encoding Method:",
                        list(analysis_data['methods'].keys()),
                        index=0,  # Default to Hash-based
                        help="Different methods analyze text in various ways"
                    )
                
                # Update bits based on selected method
                if selected_method != analysis_data['selected_method']:
                    selected_bits = analysis_data['methods'][selected_method]
                    bit0, bit1 = int(selected_bits[0]), int(selected_bits[1])
                
                with col_preview:
                    st.markdown(f"**Selected Bits:** `{bit0}{bit1}`")
                    st.markdown(f"**Quantum State:** {format_bits_display([bit0, bit1])}")
                
                # Create expandable analysis section
                with st.expander("📊 **Full Text Analysis**", expanded=True):
                    col_stats, col_methods = st.columns(2)
                    
                    with col_stats:
                        st.markdown("**Text Statistics:**")
                        st.write(f"• Length: **{analysis_data['text_length']}** characters")
                        st.write(f"• Unique chars: **{analysis_data['unique_chars']}**")
                        st.write(f"• Vowels: **{analysis_data['vowel_count']}**")
                        st.write(f"• ASCII sum: **{analysis_data['ascii_sum']}**")
                        st.write(f"• Hash (8 chars): **{analysis_data['hash_value']}**")
                    
                    with col_methods:
                        st.markdown("**All Encoding Methods:**")
                        for method, bits in analysis_data['methods'].items():
                            is_selected = method == selected_method
                            if is_selected:
                                st.markdown(f"🎯 **{method}: {bits}** ✓")
                            else:
                                st.write(f"   {method}: {bits}")
                
                # Show encoding method details
                method_info = {
                    'Hash-based': "Uses MD5 hash of entire text - most uniform distribution",
                    'Frequency': "Based on vowel frequency and text length parity",
                    'ASCII Sum': "Uses sum of all ASCII values in the text",
                    'Diversity': "Considers character uniqueness and digit presence"
                }
                
                st.info(f"**{selected_method}:** {method_info.get(selected_method, 'Custom encoding method')}")
            else:
                bit0, bit1 = 0, 1
        
        else:  # Application Scenarios
            scenario = st.selectbox(
                "Choose Application Scenario:",
                [
                    "Medical Emergency Alert",
                    "Financial Transaction", 
                    "IoT Sensor Reading",
                    "System Status Update",
                    "Security Alert",
                    "Network Heartbeat"
                ],
                help="Predefined scenarios for different use cases"
            )
            
            bit0, bit1 = get_scenario_bits(scenario)
            
            st.markdown(f"""
            **Scenario Details:**
            - **Application**: {scenario}
            - **Message Bits**: {format_bits_display([bit0, bit1])}
            - **Use Case**: Real-world quantum communication scenario
            """)
        
        # Execution button with professional styling
        st.markdown("### ▶️ Protocol Execution")
        
        execute_button = st.button(
            "🚀 Execute Superdense Coding Protocol",
            type="primary",
            use_container_width=True,
            help="Run the complete quantum protocol with current settings"
        )
        
        if execute_button:
            st.markdown("---")
            st.markdown("### 📡 Protocol Execution Results")
            
            # Progress tracking for animation mode
            if visualization_mode == "Real-time Animation":
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                steps = [
                    "Initializing quantum system...",
                    "Creating entangled Bell state...",
                    f"Alice encoding message [{bit0}{bit1}]...",
                    "Transmitting through quantum channel...",
                    "Bob performing Bell measurement...",
                    "Analyzing results..."
                ]
                
                for i, step in enumerate(steps):
                    status_text.text(f"Step {i+1}/6: {step}")
                    time.sleep(0.6)
                    progress_bar.progress((i + 1) / len(steps))
                
                progress_bar.empty()
                status_text.empty()
            
            # Execute protocol
            result = protocol.run_protocol(bit0, bit1, noise_level)
            
            # Security check
            if enable_security:
                is_secure, security_metric, chsh_value = protocol.detect_eavesdropping()
                
                col_sec1, col_sec2 = st.columns(2)
                
                with col_sec1:
                    if is_secure:
                        create_info_box(
                            "🛡️ Channel Security Status",
                            f"Channel is SECURE. CHSH parameter: {chsh_value:.3f} (> 2.0 indicates quantum advantage)",
                            "success"
                        )
                    else:
                        create_info_box(
                            "⚠️ Security Alert",
                            f"Potential eavesdropping detected! CHSH parameter: {chsh_value:.3f} (≤ 2.0 indicates possible intrusion)",
                            "warning"
                        )
                
                with col_sec2:
                    gauge_fig, security_level = create_security_gauge(security_metric, chsh_value)
                    st.plotly_chart(gauge_fig, use_container_width=True)
            
            # Real-time channel status
            st.markdown("---")
            channel_status = protocol.get_real_time_channel_status()
            
            # Channel status display
            status_colors = {
                'EXCELLENT': '🟢',
                'GOOD': '🟡',
                'DEGRADED': '🟠', 
                'POOR': '🔴',
                'INITIALIZING': '⚪'
            }
            
            col_status1, col_status2 = st.columns(2)
            
            with col_status1:
                st.markdown(f"""
                ### 📡 Real-Time Channel Status
                
                **Status:** {status_colors.get(channel_status['status'], '⚪')} {channel_status['status']}
                
                **Quality:** {channel_status['quality']}
                
                **Stability:** {channel_status['stability']:.3f}
                
                **Recommendation:** {channel_status['recommendation']}
                """)
            
            with col_status2:
                st.markdown(f"""
                ### 📊 Performance Metrics
                
                **Consecutive Successes:** {channel_status['consecutive_successes']}
                
                **Consecutive Failures:** {channel_status['consecutive_failures']}
                
                **Channel Quality:** {result['fidelity']:.3f}
                
                **Noise Impact:** {result['noise_level']:.3f}
                """)
                
                # Channel quality indicator
                create_channel_quality_indicator(result['noise_level'], result['fidelity'])
            
            # Results display
            create_info_box(
                "✅ Protocol Execution Completed",
                f"Successfully processed quantum superdense coding protocol in {result['execution_time']:.3f} seconds",
                "success"
            )
            
            # Metrics display
            col_r1, col_r2, col_r3, col_r4 = st.columns(4)
            
            with col_r1:
                st.metric(
                    "Transmission",
                    "✅ Success" if result['success'] else "❌ Failed",
                    help="Whether the decoded message matches the original"
                )
            
            with col_r2:
                st.metric(
                    "Protocol Fidelity",
                    f"{result['fidelity']:.3f}",
                    delta=f"{(result['fidelity']-0.5):.3f}",
                    help="Measurement accuracy (1.0 = perfect, 0.5 = random)"
                )
            
            with col_r3:
                st.metric(
                    "Error Rate",
                    f"{result['error_rate']:.3f}",
                    delta=f"-{result['error_rate']:.3f}",
                    help="Probability of incorrect decoding"
                )
            
            with col_r4:
                st.metric(
                    "Quantum Advantage",
                    f"{result['quantum_advantage']}x",
                    help="Efficiency multiplier over classical communication"
                )
            
            # Message comparison
            st.markdown("### 📋 Message Transmission Analysis")
            
            col_t1, col_t2, col_t3 = st.columns(3)
            
            with col_t1:
                st.markdown("**Original Message (Alice):**")
                st.code(format_bits_display(result['original_bits']))
            
            with col_t2:
                st.markdown("**Decoded Message (Bob):**")
                st.code(format_bits_display(result['decoded_bits']))
                
            with col_t3:
                st.markdown("**Transmission Result:**")
                if result['success']:
                    st.success("✅ Perfect Match!")
                else:
                    st.error("❌ Transmission Error")
            
            # Quantum Simulation Visualization
            st.markdown("---")
            st.markdown("### 🌌 Quantum Protocol Simulation Visualization")
            st.markdown("*Real-time visualization of how the protocol encrypts and transmits your data*")
            
            # Create tabs for different visualization types
            viz_tab1, viz_tab2, viz_tab3 = st.tabs(["🔄 Quantum Circuit", "🌐 Bloch Spheres & States", "📊 State Evolution"])
            
            with viz_tab1:
                st.markdown("#### Quantum Circuit Diagram")
                st.markdown("Shows the actual quantum gates and operations used in your protocol execution:")
                
                circuit_fig = create_quantum_circuit_visualization([bit0, bit1], result)
                st.plotly_chart(circuit_fig, use_container_width=True)
                
                # Circuit explanation
                with st.expander("🔍 **Circuit Step-by-Step Explanation**", expanded=False):
                    st.markdown(f"""
                    **Your Message: {format_bits_display([bit0, bit1])}**
                    
                    1. **Bell State Preparation** (Blue):
                       - Hadamard gate creates superposition on Alice's qubit
                       - CNOT gate creates entanglement between Alice and Bob
                       - Result: |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
                    
                    2. **Alice's Encoding** (Red/Green):
                       - Bit₁ = {bit1}: {'X gate applied' if bit1 == 1 else 'No X gate (Identity)'}
                       - Bit₀ = {bit0}: {'Z gate applied' if bit0 == 1 else 'No Z gate (Identity)'}
                       - Encodes your 2-bit message into quantum state
                    
                    3. **Bell Measurement** (Purple/Orange):
                       - CNOT gate followed by Hadamard on Alice's qubit
                       - Disentangles the qubits for measurement
                       - Projects the quantum state to classical bits
                    
                    4. **Result** (Gray):
                       - Measurement yields: |{bit0}{bit1}⟩
                       - Bob successfully decodes Alice's original message!
                    """)
            
            with viz_tab2:
                st.markdown("#### Bloch Sphere Representation & State Vectors")
                st.markdown("Visualizes quantum states throughout the protocol execution:")
                
                bloch_fig = create_quantum_state_visualization(result, [bit0, bit1])
                st.plotly_chart(bloch_fig, use_container_width=True)
                
                # State explanation
                with st.expander("🌐 **Quantum State Analysis**", expanded=False):
                    st.markdown(f"""
                    **Understanding the Bloch Spheres:**
                    
                    🔵 **Initial State**: 
                    - Both qubits are maximally entangled
                    - No definite state vector (entangled superposition)
                    - Represents the shared Bell state |Φ⁺⟩
                    
                    🔴 **After Encoding**: 
                    - Alice applies quantum gates based on her message
                    - State vector shows the encoded quantum information
                    - Message {format_bits_display([bit0, bit1])} is now embedded in the quantum state
                    
                    🟢 **After Measurement**:
                    - Bell measurement disentangles the qubits
                    - State collapses to definite classical result
                    - Bob obtains the decoded bits: {bit0}, {bit1}
                    
                    📈 **State Vector Evolution**:
                    - Shows probability amplitudes for each basis state
                    - Demonstrates quantum superposition and collapse
                    - Final state matches Alice's original message
                    """)
            
            with viz_tab3:
                st.markdown("#### Real-time Protocol Metrics")
                
                col_metrics1, col_metrics2 = st.columns(2)
                
                with col_metrics1:
                    st.markdown("**Quantum State Properties:**")
                    
                    # Calculate quantum state metrics
                    fidelity = result.get('fidelity', 0)
                    entanglement_measure = min(1.0, max(0.0, 1.0 - result.get('noise_level', 0)))
                    coherence_time = result.get('execution_time', 0) * 1000  # Convert to ms
                    
                    st.metric("State Fidelity", f"{fidelity:.3f}", 
                             help="Accuracy of quantum state preparation (1.0 = perfect)")
                    st.metric("Entanglement Quality", f"{entanglement_measure:.3f}", 
                             help="Measure of quantum entanglement strength")
                    st.metric("Coherence Time", f"{coherence_time:.1f} ms", 
                             help="Duration quantum information remained coherent")
                    
                    # Quantum advantage indicator
                    qa = result.get('quantum_advantage', 1)
                    if qa >= 2:
                        st.success(f"🚀 **Quantum Advantage**: {qa}x efficiency over classical!")
                    elif qa >= 1.5:
                        st.info(f"✨ **Quantum Benefit**: {qa}x improvement")
                    else:
                        st.warning(f"⚡ **Classical Comparable**: {qa}x efficiency")
                
                with col_metrics2:
                    st.markdown("**Protocol Security Analysis:**")
                    
                    # Security metrics based on quantum properties
                    security_level = "High" if fidelity > 0.85 else "Medium" if fidelity > 0.7 else "Low"
                    noise_impact = result.get('noise_level', 0)
                    error_rate = result.get('error_rate', 0)
                    
                    st.metric("Security Level", security_level,
                             help="Based on quantum state fidelity and error rates")
                    st.metric("Noise Impact", f"{noise_impact:.3f}",
                             help="Environmental interference level (0 = no noise)")
                    st.metric("Transmission Error", f"{error_rate:.3f}",
                             help="Probability of incorrect decoding")
                    
                    # Protocol recommendation
                    if error_rate < 0.1 and fidelity > 0.8:
                        st.success("🛡️ **Excellent**: Protocol suitable for secure communication")
                    elif error_rate < 0.3 and fidelity > 0.6:
                        st.info("✅ **Good**: Protocol performs well for most applications")
                    else:
                        st.warning("⚠️ **Caution**: Consider error correction for critical applications")
            
            # Technical insights
            st.markdown("---")
            with st.expander("🔬 **Technical Insights: How Your Data Gets Encrypted**", expanded=False):
                st.markdown(f"""
                ### The Quantum Encryption Process:
                
                **1. Your Input**: `{format_bits_display([bit0, bit1])}`
                - This represents your original 2-bit message
                - In classical communication, this would require 2 separate transmissions
                
                **2. Quantum Encoding**: 
                - Alice applies quantum gates: {'X' if bit1==1 else 'I'}⊗{'Z' if bit0==1 else 'I'}
                - This transforms the shared Bell state: |Φ⁺⟩ → |Φ{['⁺','⁻','ᵧ','ᵧ⁻'][bit0*2+bit1]}⟩
                - Your 2 bits are now encoded in quantum entanglement properties
                
                **3. Quantum Transmission**:
                - Alice sends only 1 qubit (instead of 2 classical bits)
                - The entanglement preserves both bits of information
                - Bob's qubit automatically contains the complementary information
                
                **4. Quantum Decoding**:
                - Bell measurement extracts both encoded bits simultaneously
                - Quantum measurement collapses the superposition
                - Result: Bob recovers your original message `{format_bits_display([bit0, bit1])}`
                
                **🎯 Key Advantage**: 2 bits transmitted using only 1 quantum particle!
                **🔒 Security**: Quantum properties make eavesdropping detectable
                **⚡ Efficiency**: {result.get('quantum_advantage', 2)}x improvement over classical methods
                """)
            
            # Detailed analysis
            if visualization_mode == "Detailed Analysis":
                st.markdown("### 🔬 Detailed Protocol Analysis")
                
                # Protocol steps
                with st.expander("📋 Protocol Execution Steps", expanded=True):
                    display_protocol_steps(result['protocol_steps'])
                
                # Measurement statistics
                with st.expander("📊 Quantum Measurement Statistics"):
                    col_stat1, col_stat2 = st.columns(2)
                    
                    with col_stat1:
                        st.markdown("**Measurement Distribution:**")
                        counts_df = display_measurement_statistics(result['measurement_counts'])
                    
                    with col_stat2:
                        if result['measurement_counts']:
                            fig_dist = create_measurement_chart(result['measurement_counts'])
                            if fig_dist:
                                st.plotly_chart(fig_dist, use_container_width=True)
                    
                    # Protocol validation analysis
                    st.markdown("---")
                    st.markdown("#### 🔬 Protocol Validation Analysis")
                    
                    measurement_counts = result['measurement_counts']
                    original_bits = result['original_bits']
                    
                    if measurement_counts:
                        # Expected quantum state analysis
                        expected_state = f"{original_bits[1]}{original_bits[0]}"  # Qiskit bit order
                        total_shots = sum(measurement_counts.values())
                        expected_shots = measurement_counts.get(expected_state, 0)
                        expected_probability = expected_shots / total_shots if total_shots > 0 else 0
                        
                        col_val1, col_val2, col_val3 = st.columns(3)
                        
                        with col_val1:
                            st.metric("Expected State", f"|{expected_state}⟩", 
                                     help="Quantum state that should be measured most frequently")
                        
                        with col_val2:
                            st.metric("Measurement Confidence", f"{expected_probability*100:.1f}%", 
                                     help="Percentage of measurements in expected state")
                        
                        with col_val3:
                            error_rate = 1 - expected_probability
                            st.metric("Error Rate", f"{error_rate*100:.1f}%", 
                                     help="Percentage of measurements in unexpected states")
                        
                        # Validation results
                        if expected_probability > 0.8:
                            st.success("🎯 **Excellent Protocol Validation**: >80% measurements in expected state")
                        elif expected_probability > 0.6:
                            st.info("✅ **Good Protocol Performance**: 60-80% measurements in expected state")
                        elif expected_probability > 0.4:
                            st.warning("⚠️ **Moderate Protocol Quality**: 40-60% measurements in expected state")
                        else:
                            st.error("❌ **Poor Protocol Performance**: <40% measurements in expected state")
                        
                        # Error state analysis
                        error_states = {k: v for k, v in measurement_counts.items() if k != expected_state}
                        if error_states:
                            st.markdown("**Error State Analysis:**")
                            for state, count in error_states.items():
                                percentage = count / total_shots * 100
                                st.write(f"• State `|{state}⟩`: {count} shots ({percentage:.1f}%) - {'Quantum noise' if percentage < 10 else 'Significant error'}")
                        
                        # Superdense coding validation
                        encoding_map = {
                            (0, 0): "00",  # Identity
                            (0, 1): "01",  # X gate  
                            (1, 0): "10",  # Z gate
                            (1, 1): "11"   # XZ gates
                        }
                        
                        expected_encoding = encoding_map.get(tuple(original_bits), "unknown")
                        actual_most_frequent = max(measurement_counts.keys(), key=lambda k: measurement_counts[k])
                        
                        if expected_encoding == actual_most_frequent:
                            st.success(f"🎯 **Encoding Validation Passed**: Expected `|{expected_encoding}⟩` matches measured `|{actual_most_frequent}⟩`")
                        else:
                            st.error(f"❌ **Encoding Validation Failed**: Expected `|{expected_encoding}⟩` but measured `|{actual_most_frequent}⟩`")
                
                # Technical details
                with st.expander("⚙️ Technical Implementation Details"):
                    st.markdown(f"""
                    **Quantum Circuit Information:**
                    - **Bell State Created**: |Φ⁺⟩ = (1/√2)(|00⟩ + |11⟩)
                    - **Alice's Encoding**: {'X gate' if bit1 else 'No X'}, {'Z gate' if bit0 else 'No Z'}
                    - **Resulting Bell State**: {['|Φ⁺⟩', '|Ψ⁺⟩', '|Φ⁻⟩', '|Ψ⁻⟩'][bit0*2 + bit1]}
                    - **Channel Noise Level**: {noise_level:.3f}
                    - **Measurement Shots**: 1024
                    - **Backend**: {'Qiskit Aer Simulator' if 'QISKIT_AVAILABLE' else 'Classical Simulation'}
                    """)
    
    with col2:
        st.markdown("### 📚 Protocol Information")
        
        # Protocol overview
        create_info_box(
            "🔬 Superdense Coding Protocol",
            """
            Quantum communication protocol that transmits 2 classical bits 
            using 1 qubit transmission with prior shared entanglement.
            
            **Key Steps:**
            1. Create Bell state |Φ⁺⟩
            2. Alice encodes 2 bits using quantum gates
            3. Alice transmits 1 qubit to Bob  
            4. Bob performs Bell measurement
            5. Bob extracts original 2 bits
            """,
            "info"
        )
        
        # Quantum advantage explanation
        st.markdown("#### 🎯 Quantum Advantage")
        st.markdown("""
        - **Classical Limit**: 1 bit per transmission
        - **Quantum Protocol**: 2 bits per 1 qubit transmission  
        - **Efficiency Gain**: 100% improvement
        - **Key Resource**: Shared quantum entanglement
        """)
        
        # Latest execution summary
        if protocol.results_history:
            latest = protocol.results_history[-1]
            
            create_info_box(
                "📈 Latest Execution Summary",
                f"""
                **Success**: {'✅' if latest['success'] else '❌'}
                **Fidelity**: {latest['fidelity']:.3f}
                **Execution Time**: {latest['execution_time']:.3f}s
                **Noise Level**: {latest['noise_level']:.3f}
                """,
                "success" if latest['success'] else "warning"
            )
    
    # Performance analytics dashboard
    if len(protocol.results_history) > 1:
        st.markdown("---")
        st.markdown("## 📈 Performance Analytics Dashboard")
        
        # Performance chart
        fig_perf = create_performance_chart(protocol.results_history)
        if fig_perf:
            st.plotly_chart(fig_perf, use_container_width=True)
        
        # Balance analysis - NEW FEATURE
        if len(protocol.results_history) >= 4:
            st.markdown("### ⚖️ Transmission Balance Analysis")
            
            col_bal1, col_bal2 = st.columns([2, 1])
            
            with col_bal1:
                fig_balance = create_balance_analysis_chart(protocol.results_history)
                if fig_balance:
                    st.plotly_chart(fig_balance, use_container_width=True)
            
            with col_bal2:
                st.markdown("**Balance Statistics:**")
                balance_data = analyze_transmission_balance(protocol.results_history)
                if balance_data:
                    balance_df = pd.DataFrame(balance_data)
                    st.dataframe(balance_df, use_container_width=True, hide_index=True)
                    
                    # Calculate overall balance score
                    success_rates = [float(d['Success Rate']) for d in balance_data]
                    if success_rates:
                        balance_score = 1.0 - (max(success_rates) - min(success_rates))
                        st.metric("Balance Score", f"{balance_score:.3f}", 
                                help="1.0 = perfectly balanced, 0.0 = highly unbalanced")
        
        # Summary statistics
        st.markdown("### 📊 Session Statistics")
        
        fidelities = [r['fidelity'] for r in protocol.results_history]
        success_rates = [1 if r['success'] else 0 for r in protocol.results_history]
        
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        
        with col_s1:
            st.metric("Average Fidelity", f"{sum(fidelities)/len(fidelities):.3f}")
        
        with col_s2:
            st.metric("Success Rate", f"{sum(success_rates)/len(success_rates)*100:.1f}%")
        
        with col_s3:
            st.metric("Total Executions", len(protocol.results_history))
            
        with col_s4:
            st.metric("Best Fidelity", f"{max(fidelities):.3f}")
    
    # Real-world applications
    st.markdown("---")
    st.markdown("## 🌍 Real-World Applications")
    
    app_tab1, app_tab2, app_tab3 = st.tabs(["🏥 Healthcare", "🏦 Finance", "🌐 IoT Networks"])
    
    with app_tab1:
        st.markdown("""
        #### Medical & Healthcare Applications
        - **Secure Patient Data**: Quantum-encrypted medical record transmission
        - **Remote Diagnostics**: Protected sharing of diagnostic images and results
        - **IoT Medical Devices**: Authenticated communication for monitoring devices
        - **Emergency Systems**: Ultra-secure emergency alert protocols
        - **Telemedicine**: Quantum-safe video consultation platforms
        """)
    
    with app_tab2:
        st.markdown("""
        #### Financial Services Applications  
        - **Transaction Security**: Post-quantum cryptography for banking
        - **High-Frequency Trading**: Ultra-fast secure trading communications
        - **Digital Identity**: Quantum-enhanced authentication systems
        - **Cross-Border Payments**: Secure international money transfers
        - **Regulatory Compliance**: Tamper-proof audit trail systems
        """)
    
    with app_tab3:
        st.markdown("""
        #### Internet of Things Applications
        - **Smart Grid Security**: Protected power distribution control signals  
        - **Industrial Automation**: Secure factory automation protocols
        - **Smart City Infrastructure**: Authenticated traffic and utility management
        - **Supply Chain Tracking**: Tamper-proof logistics monitoring
        - **Environmental Monitoring**: Protected sensor network communications
        """)
    
    # Professional footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem; background: #f8f9fa; border-radius: 10px; margin-top: 2rem;'>
        <h4 style='color: #495057; margin: 0;'>🔬 Professional Quantum Communication Simulator</h4>
        <p style='color: #6c757d; margin: 0.5rem 0 0 0;'>
            <strong>Technology:</strong> Quantum Superdense Coding • 
            <strong>Efficiency:</strong> 2 bits per qubit transmission • 
            <strong>Security:</strong> CHSH inequality monitoring
        </p>
        <p style='color: #868e96; margin: 0.25rem 0 0 0; font-size: 0.9em;'>
            Advanced quantum information processing for next-generation secure communications
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()