"""
Professional Utility Functions - Fixed and Enhanced
CLEAN VERSION - No Hackathon Branding
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st

def create_efficiency_chart():
    """Create professional communication efficiency comparison chart"""
    fig = go.Figure(data=[
        go.Bar(
            name='Communication Efficiency',
            x=['Classical Protocol', 'Superdense Coding'],
            y=[1, 2],
            marker_color=['#E74C3C', '#2ECC71'],
            text=['1 bit', '2 bits'],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title={
            'text': "Communication Protocol Efficiency Comparison",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2C3E50'}
        },
        xaxis_title="Protocol Type",
        yaxis_title="Bits Transmitted per Channel Use",
        showlegend=False,
        height=400,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'color': '#2C3E50'}
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#ECF0F1')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#ECF0F1')
    
    return fig

def create_measurement_chart(measurement_counts):
    """Create measurement distribution chart with professional styling"""
    if not measurement_counts:
        return None
        
    states = list(measurement_counts.keys())
    counts = list(measurement_counts.values())
    
    # Calculate percentages
    total = sum(counts)
    percentages = [f"{(c/total)*100:.1f}%" for c in counts]
    
    fig = px.bar(
        x=states, 
        y=counts,
        title="Quantum Measurement Distribution",
        labels={'x': 'Quantum State', 'y': 'Measurement Count'},
        color=counts,
        color_continuous_scale='Viridis',
        text=percentages
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=False
    )
    
    return fig

def create_performance_chart(results_history):
    """Create comprehensive performance tracking chart"""
    if not results_history:
        return None
    
    timestamps = list(range(1, len(results_history) + 1))
    fidelities = [r['fidelity'] for r in results_history]
    success_rates = [1 if r['success'] else 0 for r in results_history]
    
    fig = go.Figure()
    
    # Add fidelity line
    fig.add_trace(go.Scatter(
        x=timestamps, 
        y=fidelities, 
        mode='lines+markers',
        name='Protocol Fidelity', 
        line=dict(color='#3498DB', width=3),
        marker=dict(size=8)
    ))
    
    # Add success rate line
    fig.add_trace(go.Scatter(
        x=timestamps, 
        y=success_rates, 
        mode='lines+markers',
        name='Success Rate', 
        line=dict(color='#27AE60', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title={
            'text': "Protocol Performance Analytics",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        xaxis_title="Execution Number",
        yaxis_title="Performance Metric",
        hovermode='x',
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    return fig

def display_protocol_steps(steps):
    """Display protocol execution steps in a clean format"""
    st.markdown("### 🔄 Protocol Execution Steps")
    
    for i, step in enumerate(steps, 1):
        st.markdown(f"**Step {i}:** {step}")

def display_measurement_statistics(measurement_counts):
    """Display detailed measurement statistics as professional table"""
    if measurement_counts:
        counts_df = pd.DataFrame(
            list(measurement_counts.items()), 
            columns=['Quantum State', 'Count']
        )
        total_measurements = counts_df['Count'].sum()
        counts_df['Probability'] = counts_df['Count'] / total_measurements
        counts_df['Percentage'] = (counts_df['Probability'] * 100).round(2)
        
        # Format for display
        counts_df['Probability'] = counts_df['Probability'].round(4)
        counts_df['Percentage'] = counts_df['Percentage'].astype(str) + '%'
        
        st.dataframe(
            counts_df,
            use_container_width=True,
            hide_index=True
        )
        return counts_df
    return None

def get_scenario_bits(scenario):
    """Get predefined message bits for different application scenarios"""
    scenario_mapping = {
        "Medical Emergency Alert": [1, 1],      # Critical priority
        "Financial Transaction": [1, 0],         # High security
        "IoT Sensor Reading": [0, 1],           # Data transmission
        "System Status Update": [0, 0],         # Normal operation
        "Security Alert": [1, 1],               # Maximum priority
        "Network Heartbeat": [0, 0]             # Keep-alive signal
    }
    return scenario_mapping.get(scenario, [0, 1])

def text_to_bits(text):
    """
    Convert text input to binary representation
    FIXED: Proper text to bits conversion
    """
    if not text or len(text) == 0:
        return [0, 1]
    
    # Get ASCII value of first character
    ascii_val = ord(text[0])
    # Convert to 8-bit binary string
    binary_str = format(ascii_val, '08b')
    # Take first 2 bits
    bit0 = int(binary_str[0])
    bit1 = int(binary_str[1])
    
    return [bit0, bit1]

def format_bits_display(bits):
    """Format bit array for clean display"""
    return f"[{bits[0]}, {bits[1]}] → Binary: '{bits[0]}{bits[1]}'"

def create_security_gauge(security_metric, chsh_value):
    """Create a security level gauge based on CHSH inequality"""
    
    # Determine security level and color
    if chsh_value > 2.4:
        security_level = "High Security"
        color = "#27AE60"  # Green
    elif chsh_value > 2.0:
        security_level = "Moderate Security" 
        color = "#F39C12"  # Orange
    else:
        security_level = "Potential Risk"
        color = "#E74C3C"  # Red
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = chsh_value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"Channel Security<br><span style='font-size:0.8em;color:gray'>CHSH Parameter</span>"},
        delta = {'reference': 2.0},
        gauge = {
            'axis': {'range': [None, 3.0]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 2.0], 'color': "#FADBD8"},
                {'range': [2.0, 2.4], 'color': "#FCF3CF"}, 
                {'range': [2.4, 3.0], 'color': "#D5DBDB"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 2.0
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    return fig, security_level

def display_technical_specs():
    """Display technical specifications in a professional format"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🔬 Quantum System Specifications
        - **Qubits Used**: 2 (Alice: 1, Bob: 1)
        - **Bell States**: 4 maximally entangled states
        - **Channel Capacity**: 2 classical bits per transmission
        - **Quantum Advantage**: 100% efficiency improvement
        - **Fidelity**: >95% (ideal conditions)
        """)
    
    with col2:
        st.markdown("""
        #### ⚙️ Implementation Features
        - **Protocol**: Standard Superdense Coding
        - **Security**: CHSH inequality monitoring
        - **Noise Modeling**: Realistic channel simulation
        - **Backend**: Qiskit quantum simulator
        - **Interface**: Real-time interactive dashboard
        """)

def create_info_box(title, content, box_type="info"):
    """Create styled information boxes"""
    
    colors = {
        "info": {"bg": "#EBF3FD", "border": "#3498DB", "icon": "ℹ️"},
        "success": {"bg": "#E8F5E8", "border": "#27AE60", "icon": "✅"},
        "warning": {"bg": "#FEF9E7", "border": "#F39C12", "icon": "⚠️"},
        "error": {"bg": "#FADBD8", "border": "#E74C3C", "icon": "❌"}
    }
    
    style = colors.get(box_type, colors["info"])
    
    st.markdown(f"""
    <div style="
        background-color: {style['bg']};
        border-left: 4px solid {style['border']};
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.25rem;
    ">
        <h4 style="margin: 0; color: #2C3E50;">
            {style['icon']} {title}
        </h4>
        <p style="margin: 0.5rem 0 0 0; color: #34495E;">
            {content}
        </p>
    </div>
    """, unsafe_allow_html=True)

def display_transmission_analysis(results_history):
    """Display comprehensive transmission analysis and recommendations"""
    if not results_history:
        return
    
    st.markdown("### 📊 Transmission Performance Analysis")
    
    # Calculate statistics
    fidelities = [r['fidelity'] for r in results_history]
    success_rates = [1 if r['success'] else 0 for r in results_history]
    error_rates = [r['error_rate'] for r in results_history]
    noise_levels = [r['noise_level'] for r in results_history]
    
    avg_fidelity = sum(fidelities) / len(fidelities)
    avg_success = sum(success_rates) / len(success_rates)
    avg_error = sum(error_rates) / len(error_rates)
    avg_noise = sum(noise_levels) / len(noise_levels)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Average Fidelity", f"{avg_fidelity:.3f}", 
                 help="Higher is better (closer to 1.0)")
    
    with col2:
        st.metric("Success Rate", f"{avg_success*100:.1f}%", 
                 help="Percentage of successful transmissions")
    
    with col3:
        st.metric("Average Error Rate", f"{avg_error:.3f}", 
                 help="Lower is better (closer to 0.0)")
    
    with col4:
        st.metric("Average Noise Level", f"{avg_noise:.3f}", 
                 help="Channel noise during tests")
    
    # Recommendations
    st.markdown("#### 🎯 Performance Recommendations")
    
    if avg_fidelity < 0.7:
        create_info_box(
            "⚠️ Low Fidelity Detected",
            "Consider reducing noise level or implementing error correction to improve transmission quality.",
            "warning"
        )
    elif avg_fidelity > 0.9:
        create_info_box(
            "✅ Excellent Performance",
            "Channel conditions are optimal for quantum communication protocols.",
            "success"
        )
    else:
        create_info_box(
            "ℹ️ Good Performance",
            "Channel performance is within acceptable range for practical quantum communication.",
            "info"
        )
    
    # Noise impact analysis
    if avg_noise > 0.2:
        st.markdown("""
        **High Noise Environment Detected:**
        - Consider implementing quantum error correction
        - Use adaptive protocols to adjust for channel conditions
        - Implement error mitigation techniques
        """)
    elif avg_noise < 0.05:
        st.markdown("""
        **Low Noise Environment:**
        - Ideal conditions for quantum communication
        - Consider testing higher complexity protocols
        - Explore advanced quantum algorithms
        """)

def create_channel_quality_indicator(noise_level, fidelity):
    """Create a visual indicator for channel quality"""
    
    # Determine quality based on both noise and fidelity
    if noise_level < 0.05 and fidelity > 0.9:
        quality = "Excellent"
        color = "#27AE60"
        icon = "🟢"
    elif noise_level < 0.15 and fidelity > 0.7:
        quality = "Good"
        color = "#F39C12"
        icon = "🟡"
    elif noise_level < 0.3 and fidelity > 0.5:
        quality = "Fair"
        color = "#E67E22"
        icon = "🟠"
    else:
        quality = "Poor"
        color = "#E74C3C"
        icon = "🔴"
    
    st.markdown(f"""
    <div style="
        background-color: {color}20;
        border: 2px solid {color};
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
    ">
        <h3 style="margin: 0; color: {color};">
            {icon} Channel Quality: {quality}
        </h3>
        <p style="margin: 0.5rem 0 0 0; color: #2C3E50;">
            Noise: {noise_level:.3f} | Fidelity: {fidelity:.3f}
        </p>
    </div>
    """, unsafe_allow_html=True)

def analyze_transmission_balance(results_history):
    """Analyze the balance of transmission results across different bit combinations"""
    if not results_history:
        return None
        
    # Count successes and failures for each bit combination
    combinations = {'00': {'success': 0, 'total': 0},
                   '01': {'success': 0, 'total': 0},
                   '10': {'success': 0, 'total': 0},
                   '11': {'success': 0, 'total': 0}}
    
    for result in results_history:
        orig_bits = result['original_bits']
        bit_combo = f"{orig_bits[0]}{orig_bits[1]}"
        combinations[bit_combo]['total'] += 1
        if result['success']:
            combinations[bit_combo]['success'] += 1
    
    # Calculate success rates
    balance_data = []
    for combo, data in combinations.items():
        if data['total'] > 0:
            success_rate = data['success'] / data['total']
            balance_data.append({
                'Bit Combination': combo,
                'Success Rate': f"{success_rate:.3f}",
                'Successes': data['success'],
                'Total Attempts': data['total'],
                'Success Percentage': f"{success_rate*100:.1f}%"
            })
    
    return balance_data

def create_balance_analysis_chart(results_history):
    """Create a chart showing transmission balance across different inputs"""
    if not results_history or len(results_history) < 4:
        return None
        
    balance_data = analyze_transmission_balance(results_history)
    if not balance_data:
        return None
    
    combinations = [d['Bit Combination'] for d in balance_data]
    success_rates = [float(d['Success Rate']) for d in balance_data]
    
    fig = go.Figure(data=[
        go.Bar(
            x=combinations,
            y=success_rates,
            marker_color=['#3498DB', '#2ECC71', '#F39C12', '#E74C3C'],
            text=[d['Success Percentage'] for d in balance_data],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title={
            'text': "Transmission Success Rate by Bit Combination",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2C3E50'}
        },
        xaxis_title="Bit Combination (b₀b₁)",
        yaxis_title="Success Rate",
        yaxis=dict(range=[0, 1.1]),
        showlegend=False,
        height=400,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'color': '#2C3E50'}
    )
    
    # Add horizontal line at 0.5 for reference
    fig.add_hline(y=0.5, line_dash="dash", line_color="red", 
                  annotation_text="Random Guess Level")
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#ECF0F1')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#ECF0F1')
    
    return fig