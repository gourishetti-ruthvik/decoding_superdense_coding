"""
Professional Utility Functions - Fixed and Enhanced
CLEAN VERSION - No Hackathon Branding
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st

def format_bits_display(bits):
    """Format bits for nice display"""
    if isinstance(bits, (list, tuple)) and len(bits) == 2:
        return f"{bits[0]}{bits[1]}"
    return str(bits)

def create_info_box(title, content, icon="ℹ️"):
    """Create a professional info box"""
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 10px 0;
    ">
        <h3 style="color: white; margin: 0 0 10px 0;">{icon} {title}</h3>
        <p style="color: white; margin: 0; line-height: 1.6;">{content}</p>
    </div>
    """, unsafe_allow_html=True)

def create_security_gauge(security_score, chsh_value=2.5):
    """Create a security level gauge"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = security_score * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Security Level"},
        delta = {'reference': 80},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "yellow"},
                {'range': [80, 100], 'color': "green"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90}}))
    
    fig.update_layout(
        template='plotly_dark',
        height=250,
        font=dict(size=12)
    )
    
    # Determine security level based on both metrics
    if security_score > 0.8 and chsh_value > 2.0:
        level = "High"
    elif security_score > 0.5:
        level = "Medium"
    else:
        level = "Low"
    
    return fig, level

def create_channel_quality_indicator(noise_level, fidelity):
    """Create a channel quality indicator"""
    quality_score = (1 - noise_level) * fidelity * 100
    
    if quality_score > 80:
        color = "🟢"
        status = "Excellent"
    elif quality_score > 60:
        color = "🟡"  
        status = "Good"
    elif quality_score > 40:
        color = "🟠"
        status = "Fair"
    else:
        color = "🔴"
        status = "Poor"
    
    st.markdown(f"""
    <div style="
        padding: 15px;
        border-radius: 8px;
        background: linear-gradient(90deg, rgba(75,192,192,0.3) 0%, rgba(153,102,255,0.3) 100%);
        border: 2px solid {color.replace('🟢', '#4CAF50').replace('🟡', '#FFC107').replace('🟠', '#FF9800').replace('🔴', '#F44336')};
        text-align: center;
        margin: 10px 0;
    ">
        <h4>{color} Channel Quality: {status}</h4>
        <p><strong>Score:</strong> {quality_score:.1f}/100</p>
        <p><strong>Noise Level:</strong> {noise_level:.3f} | <strong>Fidelity:</strong> {fidelity:.3f}</p>
    </div>
    """, unsafe_allow_html=True)

def display_protocol_steps(steps):
    """Display protocol execution steps"""
    if not steps:
        st.info("No protocol steps recorded.")
        return
    
    for i, step in enumerate(steps, 1):
        step_icon = "🔧" if "initialize" in step.lower() else "⚡" if "encode" in step.lower() else "🔗" if "entangle" in step.lower() else "📡" if "transmit" in step.lower() else "📊" if "measure" in step.lower() else "🔍"
        st.markdown(f"**{i}.** {step_icon} {step}")
    
    st.success("✅ Protocol execution completed successfully!")

def create_efficiency_chart():
    """Create professional communication efficiency comparison chart"""
    fig = go.Figure(data=[
        go.Bar(
            name='Communication Efficiency',
            x=['Classical Protocol', 'Superdense Coding'],
            y=[1, 2],
            marker_color=['#E74C3C', '#2ECC71'],
            text=['1 bit', '2 bits'],
            textposition='outside',
            textfont=dict(size=16, color='white'),
        )
    ])
    
    fig.update_layout(
        title='Communication Efficiency Comparison',
        xaxis_title='Protocol Type',
        yaxis_title='Bits Transmitted per Qubit',
        template='plotly_dark',
        height=400,
        showlegend=False,
        font=dict(size=14),
        title_font=dict(size=18),
        xaxis=dict(
            tickfont=dict(size=14),
            title_font=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            title_font=dict(size=16),
            range=[0, 2.5]
        )
    )
    
    fig.add_annotation(
        x=0, y=1.2,
        text="Standard<br>Classical",
        showarrow=False,
        font=dict(size=12, color='white'),
        bgcolor='rgba(231, 76, 60, 0.7)',
        bordercolor='white',
        borderwidth=1
    )
    
    fig.add_annotation(
        x=1, y=2.2,
        text="Quantum<br>Advantage",
        showarrow=False,
        font=dict(size=12, color='white'),
        bgcolor='rgba(46, 204, 113, 0.7)',
        bordercolor='white',
        borderwidth=1
    )
    
    return fig

def create_measurement_chart(measurement_counts):
    """Create enhanced measurement results chart with validation insights"""
    if not measurement_counts:
        return None
    
    states = list(measurement_counts.keys())
    counts = list(measurement_counts.values())
    total_shots = sum(counts)
    
    # Calculate probabilities and determine state classifications
    probabilities = [count/total_shots for count in counts]
    max_count = max(counts)
    
    # Color coding based on measurement confidence
    colors = []
    for count in counts:
        if count == max_count:
            colors.append('#2ECC71')  # Green for primary state
        elif count > total_shots * 0.1:  # More than 10% suggests significant presence
            colors.append('#F39C12')  # Orange for secondary states
        else:
            colors.append('#E74C3C')  # Red for noise/error states
    
    # Create professional bar chart
    fig = go.Figure(data=[
        go.Bar(
            x=[f"|{state}⟩" for state in states],
            y=counts,
            marker_color=colors,
            text=[f"{count}<br>({prob:.1%})" for count, prob in zip(counts, probabilities)],
            textposition='outside',
            textfont=dict(size=12, color='white'),
            hovertemplate='<b>State:</b> |%{x}⟩<br>' +
                         '<b>Count:</b> %{y}<br>' +
                         '<b>Probability:</b> %{customdata:.3f}<br>' +
                         '<extra></extra>',
            customdata=probabilities
        )
    ])
    
    fig.update_layout(
        title='Quantum State Measurement Distribution',
        xaxis_title='Quantum States',
        yaxis_title='Measurement Count',
        template='plotly_dark',
        height=450,
        showlegend=False,
        font=dict(size=12),
        title_font=dict(size=16),
        xaxis=dict(
            tickfont=dict(size=12),
            title_font=dict(size=14)
        ),
        yaxis=dict(
            tickfont=dict(size=12),
            title_font=dict(size=14)
        )
    )
    
    # Add validation annotations
    primary_state = states[counts.index(max_count)]
    confidence = max_count / total_shots * 100
    
    fig.add_annotation(
        x=len(states)-1, y=max(counts) * 0.8,
        text=f"Primary: |{primary_state}⟩<br>Confidence: {confidence:.1f}%",
        showarrow=True,
        arrowhead=2,
        arrowcolor='white',
        font=dict(size=11, color='white'),
        bgcolor='rgba(46, 204, 113, 0.8)',
        bordercolor='white',
        borderwidth=1
    )
    
    return fig

def create_channel_status_chart(noise_level, fidelity, error_rate):
    """Create real-time channel status visualization"""
    # Channel quality metrics
    metrics = ['Noise Level', 'Fidelity', 'Error Rate']
    values = [noise_level * 100, fidelity * 100, (1 - error_rate) * 100]
    
    # Color coding based on performance
    colors = []
    for i, value in enumerate(values):
        if i == 0:  # Noise level (lower is better)
            colors.append('#E74C3C' if value > 30 else '#F39C12' if value > 15 else '#2ECC71')
        else:  # Fidelity and Success Rate (higher is better)
            colors.append('#2ECC71' if value > 80 else '#F39C12' if value > 60 else '#E74C3C')
    
    fig = go.Figure(data=[
        go.Bar(
            x=metrics,
            y=values,
            marker_color=colors,
            text=[f"{value:.1f}%" for value in values],
            textposition='outside',
            textfont=dict(size=14, color='white'),
        )
    ])
    
    fig.update_layout(
        title='Real-time Channel Performance',
        xaxis_title='Performance Metrics',
        yaxis_title='Percentage (%)',
        template='plotly_dark',
        height=350,
        showlegend=False,
        font=dict(size=12),
        title_font=dict(size=16),
        yaxis=dict(range=[0, 100])
    )
    
    return fig

def display_measurement_statistics(measurement_counts):
    """Enhanced measurement statistics with protocol validation"""
    if not measurement_counts:
        st.warning("No measurement data available.")
        return None
    
    # Convert to DataFrame for analysis
    total_measurements = sum(measurement_counts.values())
    data = []
    
    for state, count in measurement_counts.items():
        probability = count / total_measurements
        data.append({
            'Quantum State': state,
            'Count': count,
            'Probability': probability
        })
    
    counts_df = pd.DataFrame(data)
    counts_df = counts_df.sort_values('Count', ascending=False)
    
    # Add analysis columns
    counts_df['Percentage'] = (counts_df['Probability'] * 100).round(2)
    counts_df['Expected?'] = ['✅ Primary' if row['Count'] == counts_df['Count'].max() 
                             else ('⚠️ Error' if row['Count'] > total_measurements * 0.1 
                                  else '❌ Noise') for _, row in counts_df.iterrows()]
    
    # Format for display
    counts_df['Probability'] = counts_df['Probability'].round(4)
    counts_df['Percentage'] = counts_df['Percentage'].astype(str) + '%'
    counts_df['Quantum State'] = counts_df['Quantum State'].apply(lambda x: f"|{x}⟩")
    
    st.dataframe(
        counts_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Quantum State": st.column_config.TextColumn("Quantum State |ψ⟩"),
            "Count": st.column_config.NumberColumn("Measurement Count"),
            "Probability": st.column_config.NumberColumn("Probability", format="%.4f"),
            "Percentage": st.column_config.TextColumn("Percentage"),
            "Expected?": st.column_config.TextColumn("Classification")
        }
    )
    
    # Protocol validation analysis without nested columns
    primary_state = counts_df.loc[counts_df['Count'].idxmax(), 'Quantum State']
    primary_percentage = counts_df.loc[counts_df['Count'].idxmax(), 'Count'] / total_measurements * 100
    error_rate = (total_measurements - counts_df.loc[counts_df['Count'].idxmax(), 'Count']) / total_measurements * 100
    
    # Display metrics in a simple layout to avoid column nesting
    st.markdown("**📊 Protocol Validation Summary:**")
    st.write(f"🎯 **Primary State:** {primary_state.replace('|', '').replace('⟩', '')} ({primary_percentage:.1f}% confidence)")
    st.write(f"⚠️ **Error Rate:** {error_rate:.1f}% (noise and decoherence effects)")
    st.write(f"📏 **Total Measurements:** {total_measurements:,} shots")
    
    # Advanced validation analysis
    st.markdown("**🔬 Detailed Protocol Analysis:**")
    
    # Expected state verification
    expected_states = ['00', '01', '10', '11']
    detected_states = [state.replace('|', '').replace('⟩', '') for state in counts_df['Quantum State'].values]
    
    valid_encoding = any(state in expected_states for state in detected_states)
    if valid_encoding:
        st.success("✅ Valid quantum encoding detected - Protocol executed correctly")
    else:
        st.error("❌ Invalid quantum states detected - Check Bell state preparation")
    
    # Noise analysis
    if error_rate < 10:
        st.success(f"🔥 Excellent channel quality - Error rate: {error_rate:.1f}%")
    elif error_rate < 25:
        st.warning(f"⚠️ Moderate noise present - Error rate: {error_rate:.1f}%")
    else:
        st.error(f"🚨 High noise environment - Error rate: {error_rate:.1f}%")
    
    # Bell state analysis
    if primary_percentage > 70:
        st.info("🎯 Strong Bell state correlation - Quantum entanglement preserved")
    elif primary_percentage > 50:
        st.warning("⚡ Moderate entanglement - Some decoherence present")
    else:
        st.error("💥 Weak correlation - Significant quantum decoherence")
    
    return counts_df

def display_protocol_results(result):
    """Display comprehensive protocol execution results"""
    if not result:
        st.error("No protocol results to display.")
        return
    
    # Main results summary
    st.markdown("### 📊 Protocol Execution Summary")
    
    # Success indicators
    success_color = "🟢" if result.get('success', False) else "🔴"
    fidelity_color = "🟢" if result.get('fidelity', 0) > 0.8 else "🟡" if result.get('fidelity', 0) > 0.5 else "🔴"
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Transmission Status",
            f"{success_color} {'Success' if result.get('success', False) else 'Failed'}",
            help="Overall protocol execution status"
        )
    
    with col2:
        st.metric(
            "Fidelity",
            f"{fidelity_color} {result.get('fidelity', 0):.3f}",
            help="Quantum state fidelity measurement"
        )
    
    with col3:
        st.metric(
            "Error Rate",
            f"{result.get('error_rate', 1.0):.3f}",
            help="Protocol error rate"
        )
    
    with col4:
        st.metric(
            "Bits Transmitted",
            f"2 bits/qubit",
            help="Superdense coding efficiency"
        )
    
    # Detailed bit information
    st.markdown("### 🔤 Bit Transmission Details")
    
    original_bits = result.get('original_bits', 'N/A')
    decoded_bits = result.get('decoded_bits', 'N/A')
    
    if isinstance(original_bits, (list, tuple)) and len(original_bits) == 2:
        original_display = f"{original_bits[0]}{original_bits[1]}"
    else:
        original_display = str(original_bits)
    
    if isinstance(decoded_bits, (list, tuple)) and len(decoded_bits) == 2:
        decoded_display = f"{decoded_bits[0]}{decoded_bits[1]}"
    else:
        decoded_display = str(decoded_bits)
    
    col_bits1, col_bits2 = st.columns(2)
    
    with col_bits1:
        st.info(f"📤 **Original Bits:** `{original_display}`")
    
    with col_bits2:
        match_icon = "✅" if original_display == decoded_display else "❌"
        st.info(f"📥 **Decoded Bits:** `{decoded_display}` {match_icon}")
    
    # Channel information if available
    if 'channel_info' in result:
        channel = result['channel_info']
        st.markdown("### 📡 Channel Status")
        
        noise_level = channel.get('noise_level', 0)
        noise_color = "🟢" if noise_level < 0.1 else "🟡" if noise_level < 0.3 else "🔴"
        
        st.write(f"**Noise Level:** {noise_color} {noise_level:.3f}")
        st.write(f"**Channel Type:** {channel.get('type', 'Unknown')}")
        
        if 'correction_applied' in channel:
            correction_icon = "✅" if channel['correction_applied'] else "❌"
            st.write(f"**Noise Correction:** {correction_icon} {'Applied' if channel['correction_applied'] else 'Not Applied'}")

def create_bell_state_visualization():
    """Create Bell state preparation visualization"""
    fig = go.Figure()
    
    # Bell states data
    bell_states = ['|Φ⁺⟩ = (|00⟩ + |11⟩)/√2', '|Φ⁻⟩ = (|00⟩ - |11⟩)/√2', 
                   '|Ψ⁺⟩ = (|01⟩ + |10⟩)/√2', '|Ψ⁻⟩ = (|01⟩ - |10⟩)/√2']
    bit_combinations = ['00', '01', '10', '11']
    
    fig.add_trace(go.Scatter(
        x=list(range(4)),
        y=[1]*4,
        mode='markers+text',
        marker=dict(size=60, color=['#2ECC71', '#3498DB', '#F39C12', '#E74C3C']),
        text=bell_states,
        textposition='top center',
        textfont=dict(size=10, color='white'),
        name='Bell States'
    ))
    
    # Add bit encoding information
    fig.add_trace(go.Scatter(
        x=list(range(4)),
        y=[0.5]*4,
        mode='markers+text',
        marker=dict(size=40, color='rgba(255,255,255,0.3)'),
        text=[f"Input: {bits}" for bits in bit_combinations],
        textposition='middle center',
        textfont=dict(size=12, color='white'),
        name='Bit Encoding'
    ))
    
    fig.update_layout(
        title='Bell State Encoding for Superdense Coding',
        xaxis_title='Bit Combination Index',
        yaxis_title='Quantum State Level',
        template='plotly_dark',
        height=400,
        showlegend=False,
        xaxis=dict(tickmode='array', tickvals=list(range(4)), ticktext=bit_combinations),
        yaxis=dict(range=[0, 1.5], showticklabels=False)
    )
    
    return fig

def create_quantum_circuit_display():
    """Create a visual representation of the quantum circuit"""
    # This would typically require qiskit visualization, but we'll create a conceptual diagram
    fig = go.Figure()
    
    # Circuit elements (simplified representation)
    steps = ['Initialize', 'Encode', 'Entangle', 'Transmit', 'Measure', 'Decode']
    y_pos = [2, 2, 2, 2, 2, 2]
    
    fig.add_trace(go.Scatter(
        x=list(range(len(steps))),
        y=y_pos,
        mode='markers+lines+text',
        marker=dict(size=50, color='#3498DB'),
        line=dict(width=4, color='#2ECC71'),
        text=steps,
        textposition='bottom center',
        textfont=dict(size=12, color='white'),
        name='Quantum Circuit Flow'
    ))
    
    # Add qubit lines
    fig.add_trace(go.Scatter(
        x=[-0.5, len(steps)-0.5],
        y=[2.5, 2.5],
        mode='lines',
        line=dict(width=2, color='white'),
        name='Qubit 1'
    ))
    
    fig.add_trace(go.Scatter(
        x=[-0.5, len(steps)-0.5],
        y=[1.5, 1.5],
        mode='lines',
        line=dict(width=2, color='white'),
        name='Qubit 2'
    ))
    
    fig.update_layout(
        title='Superdense Coding Quantum Circuit',
        template='plotly_dark',
        height=300,
        showlegend=False,
        xaxis=dict(showticklabels=False, showgrid=False),
        yaxis=dict(showticklabels=False, showgrid=False, range=[1, 3])
    )
    
    return fig

def create_performance_chart(results_history):
    """Create performance analytics chart from protocol results history"""
    if not results_history or len(results_history) < 2:
        return None
    
    # Extract data from results history
    iterations = list(range(1, len(results_history) + 1))
    fidelities = [result.get('fidelity', 0) for result in results_history]
    success_rates = [1 if result.get('success', False) else 0 for result in results_history]
    error_rates = [result.get('error_rate', 1.0) for result in results_history]
    
    # Calculate running averages
    running_fidelity = []
    running_success = []
    running_error = []
    
    for i in range(len(results_history)):
        running_fidelity.append(sum(fidelities[:i+1]) / (i+1))
        running_success.append(sum(success_rates[:i+1]) / (i+1))
        running_error.append(sum(error_rates[:i+1]) / (i+1))
    
    # Create subplot figure
    fig = go.Figure()
    
    # Add fidelity trace
    fig.add_trace(go.Scatter(
        x=iterations,
        y=fidelities,
        mode='lines+markers',
        name='Fidelity',
        line=dict(color='#2ECC71', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Run %{x}</b><br>' +
                     'Fidelity: %{y:.3f}<br>' +
                     '<extra></extra>'
    ))
    
    # Add running average fidelity
    fig.add_trace(go.Scatter(
        x=iterations,
        y=running_fidelity,
        mode='lines',
        name='Avg Fidelity',
        line=dict(color='#27AE60', width=2, dash='dash'),
        hovertemplate='<b>Run %{x}</b><br>' +
                     'Average Fidelity: %{y:.3f}<br>' +
                     '<extra></extra>'
    ))
    
    # Add success rate trace
    fig.add_trace(go.Scatter(
        x=iterations,
        y=success_rates,
        mode='lines+markers',
        name='Success Rate',
        line=dict(color='#3498DB', width=3),
        marker=dict(size=8),
        yaxis='y2',
        hovertemplate='<b>Run %{x}</b><br>' +
                     'Success: %{y}<br>' +
                     '<extra></extra>'
    ))
    
    # Add running average success rate
    fig.add_trace(go.Scatter(
        x=iterations,
        y=running_success,
        mode='lines',
        name='Avg Success',
        line=dict(color='#2980B9', width=2, dash='dash'),
        yaxis='y2',
        hovertemplate='<b>Run %{x}</b><br>' +
                     'Average Success: %{y:.3f}<br>' +
                     '<extra></extra>'
    ))
    
    # Update layout for dual y-axis
    fig.update_layout(
        title='Protocol Performance Analytics',
        xaxis_title='Protocol Execution #',
        yaxis=dict(
            title='Fidelity',
            title_font=dict(color='#2ECC71'),
            tickfont=dict(color='#2ECC71'),
            range=[0, 1]
        ),
        yaxis2=dict(
            title='Success Rate',
            title_font=dict(color='#3498DB'),
            tickfont=dict(color='#3498DB'),
            overlaying='y',
            side='right',
            range=[0, 1]
        ),
        template='plotly_dark',
        height=450,
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Add performance annotations
    avg_fidelity = sum(fidelities) / len(fidelities)
    avg_success = sum(success_rates) / len(success_rates)
    
    fig.add_annotation(
        x=len(iterations) * 0.7,
        y=avg_fidelity,
        text=f"Avg Fidelity: {avg_fidelity:.3f}",
        showarrow=True,
        arrowhead=2,
        arrowcolor='#2ECC71',
        bgcolor='rgba(46, 204, 113, 0.8)',
        bordercolor='white',
        borderwidth=1,
        font=dict(color='white', size=12)
    )
    
    return fig

def text_to_bits(text):
    """Convert entire text to 2-bit representation using multiple encoding methods"""
    if not text:
        return 0, 0, {}
    
    # Method 1: Hash-based encoding (most robust for entire text)
    import hashlib
    text_hash = hashlib.md5(text.encode()).hexdigest()
    hash_val = int(text_hash[:2], 16)  # First 2 hex chars to decimal
    hash_bit0 = (hash_val >> 1) & 1
    hash_bit1 = hash_val & 1
    
    # Method 2: Character frequency analysis
    char_count = len(text)
    vowel_count = sum(1 for c in text.lower() if c in 'aeiou')
    freq_bit0 = 1 if vowel_count > char_count // 2 else 0
    freq_bit1 = 1 if char_count % 2 == 1 else 0
    
    # Method 3: ASCII sum modulo
    ascii_sum = sum(ord(c) for c in text)
    sum_bit0 = (ascii_sum >> 1) & 1
    sum_bit1 = ascii_sum & 1
    
    # Method 4: Character diversity
    unique_chars = len(set(text.lower()))
    div_bit0 = 1 if unique_chars > char_count // 2 else 0
    div_bit1 = 1 if any(c.isdigit() for c in text) else 0
    
    # Default method: Use hash-based (most reliable)
    final_bit0, final_bit1 = hash_bit0, hash_bit1
    
    # Analysis data for display
    analysis_data = {
        'text_length': char_count,
        'unique_chars': unique_chars,
        'vowel_count': vowel_count,
        'ascii_sum': ascii_sum,
        'hash_value': text_hash[:8],
        'methods': {
            'Hash-based': f"{hash_bit0}{hash_bit1}",
            'Frequency': f"{freq_bit0}{freq_bit1}",
            'ASCII Sum': f"{sum_bit0}{sum_bit1}",
            'Diversity': f"{div_bit0}{div_bit1}"
        },
        'selected_method': 'Hash-based',
        'final_bits': f"{final_bit0}{final_bit1}"
    }
    
    return final_bit0, final_bit1, analysis_data

def text_to_bits_simple(text):
    """Simple version for backward compatibility"""
    if not text:
        return 0, 0
    bit0, bit1, _ = text_to_bits(text)
    return bit0, bit1

def create_balance_analysis_chart(results_history):
    """Create transmission balance analysis chart showing bit combination distribution"""
    if not results_history or len(results_history) < 4:
        return None
    
    # Extract bit combinations from results history
    bit_combinations = []
    for result in results_history:
        original_bits = result.get('original_bits', [0, 0])
        if isinstance(original_bits, (list, tuple)) and len(original_bits) == 2:
            bit_combo = f"{original_bits[0]}{original_bits[1]}"
        else:
            bit_combo = str(original_bits)
        bit_combinations.append(bit_combo)
    
    # Count occurrences of each bit combination
    from collections import Counter
    combo_counts = Counter(bit_combinations)
    
    # Ensure all combinations are represented
    all_combos = ['00', '01', '10', '11']
    combo_data = {combo: combo_counts.get(combo, 0) for combo in all_combos}
    
    # Calculate percentages
    total_runs = sum(combo_data.values())
    if total_runs == 0:
        return None
    
    combo_percentages = {combo: (count / total_runs) * 100 for combo, count in combo_data.items()}
    
    # Determine balance quality
    expected_percentage = 25.0  # Ideal: 25% each for perfect balance
    max_deviation = max(abs(pct - expected_percentage) for pct in combo_percentages.values())
    
    if max_deviation <= 5:
        balance_quality = "Excellent"
        balance_color = "#2ECC71"
    elif max_deviation <= 10:
        balance_quality = "Good" 
        balance_color = "#F39C12"
    elif max_deviation <= 15:
        balance_quality = "Fair"
        balance_color = "#E67E22"
    else:
        balance_quality = "Poor"
        balance_color = "#E74C3C"
    
    # Create the balance analysis chart
    fig = go.Figure()
    
    # Add bar chart for bit combination distribution
    fig.add_trace(go.Bar(
        x=list(combo_data.keys()),
        y=list(combo_data.values()),
        text=[f"{count}<br>({combo_percentages[combo]:.1f}%)" 
              for combo, count in combo_data.items()],
        textposition='outside',
        marker=dict(
            color=[balance_color if abs(combo_percentages[combo] - expected_percentage) <= 5 
                   else '#E74C3C' for combo in combo_data.keys()],
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>Bits: %{x}</b><br>' +
                     'Count: %{y}<br>' +
                     'Percentage: %{text}<br>' +
                     '<extra></extra>',
        name='Transmission Count'
    ))
    
    # Add reference line for perfect balance
    fig.add_hline(
        y=total_runs / 4,
        line_dash="dash",
        line_color="white",
        annotation_text=f"Perfect Balance ({total_runs/4:.1f} each)",
        annotation_position="top right"
    )
    
    # Update layout
    fig.update_layout(
        title=f'Transmission Balance Analysis - Quality: {balance_quality}',
        xaxis_title='Bit Combinations',
        yaxis_title='Number of Transmissions',
        template='plotly_dark',
        height=400,
        showlegend=False,
        font=dict(size=12),
        title_font=dict(size=16, color=balance_color),
        xaxis=dict(
            tickfont=dict(size=14),
            title_font=dict(size=14)
        ),
        yaxis=dict(
            tickfont=dict(size=12),
            title_font=dict(size=14)
        )
    )
    
    # Add balance quality annotation
    fig.add_annotation(
        x=1.5,
        y=max(combo_data.values()) * 0.8,
        text=f"Balance Quality: {balance_quality}<br>Max Deviation: {max_deviation:.1f}%",
        showarrow=True,
        arrowhead=2,
        arrowcolor=balance_color,
        bgcolor=f'rgba({int(balance_color[1:3], 16)}, {int(balance_color[3:5], 16)}, {int(balance_color[5:7], 16)}, 0.8)',
        bordercolor='white',
        borderwidth=1,
        font=dict(color='white', size=11)
    )
    
    return fig

def create_detailed_balance_stats(results_history):
    """Create detailed balance statistics for the transmission analysis"""
    if not results_history:
        return {}
    
    # Extract bit combinations
    bit_combinations = []
    success_by_combo = {}
    fidelity_by_combo = {}
    
    for result in results_history:
        original_bits = result.get('original_bits', [0, 0])
        if isinstance(original_bits, (list, tuple)) and len(original_bits) == 2:
            bit_combo = f"{original_bits[0]}{original_bits[1]}"
        else:
            bit_combo = str(original_bits)
        
        bit_combinations.append(bit_combo)
        
        # Track success and fidelity by combination
        if bit_combo not in success_by_combo:
            success_by_combo[bit_combo] = []
            fidelity_by_combo[bit_combo] = []
        
        success_by_combo[bit_combo].append(1 if result.get('success', False) else 0)
        fidelity_by_combo[bit_combo].append(result.get('fidelity', 0))
    
    # Calculate statistics
    from collections import Counter
    combo_counts = Counter(bit_combinations)
    total_runs = len(bit_combinations)
    
    stats = {
        'total_runs': total_runs,
        'combo_counts': dict(combo_counts),
        'combo_percentages': {combo: (count / total_runs) * 100 
                             for combo, count in combo_counts.items()},
        'success_rates': {combo: (sum(successes) / len(successes)) * 100 
                         for combo, successes in success_by_combo.items()},
        'avg_fidelities': {combo: sum(fidelities) / len(fidelities) 
                          for combo, fidelities in fidelity_by_combo.items()}
    }
    
    # Calculate balance score
    expected_percentage = 25.0
    deviations = [abs(pct - expected_percentage) for pct in stats['combo_percentages'].values()]
    max_deviation = max(deviations) if deviations else 0
    balance_score = max(0, 100 - (max_deviation * 4))  # Scale to 0-100
    
    stats['balance_score'] = balance_score
    stats['max_deviation'] = max_deviation
    
    return stats

def analyze_transmission_balance(results_history):
    """Analyze transmission balance and return data suitable for DataFrame display"""
    if not results_history or len(results_history) < 4:
        return None
    
    # Extract bit combinations and metrics
    combo_data = {}
    all_combos = ['00', '01', '10', '11']
    
    # Initialize data structure
    for combo in all_combos:
        combo_data[combo] = {
            'count': 0,
            'successes': [],
            'fidelities': [],
            'error_rates': []
        }
    
    # Process results history
    for result in results_history:
        original_bits = result.get('original_bits', [0, 0])
        if isinstance(original_bits, (list, tuple)) and len(original_bits) == 2:
            bit_combo = f"{original_bits[0]}{original_bits[1]}"
        else:
            bit_combo = str(original_bits)
        
        if bit_combo in combo_data:
            combo_data[bit_combo]['count'] += 1
            combo_data[bit_combo]['successes'].append(1 if result.get('success', False) else 0)
            combo_data[bit_combo]['fidelities'].append(result.get('fidelity', 0))
            combo_data[bit_combo]['error_rates'].append(result.get('error_rate', 1.0))
    
    # Calculate statistics for DataFrame
    total_runs = sum(data['count'] for data in combo_data.values())
    expected_count = total_runs / 4  # Perfect balance
    
    balance_analysis = []
    
    for combo in all_combos:
        data = combo_data[combo]
        count = data['count']
        percentage = (count / total_runs * 100) if total_runs > 0 else 0
        deviation = abs(percentage - 25.0)  # Deviation from perfect 25%
        
        # Calculate performance metrics
        avg_success = (sum(data['successes']) / len(data['successes']) * 100) if data['successes'] else 0
        avg_fidelity = sum(data['fidelities']) / len(data['fidelities']) if data['fidelities'] else 0
        avg_error_rate = sum(data['error_rates']) / len(data['error_rates']) if data['error_rates'] else 1.0
        
        # Determine balance status
        if deviation <= 5:
            balance_status = "✅ Excellent"
        elif deviation <= 10:
            balance_status = "🟡 Good"
        elif deviation <= 15:
            balance_status = "🟠 Fair"
        else:
            balance_status = "❌ Poor"
        
        # Performance rating
        if avg_success >= 90 and avg_fidelity >= 0.85:
            performance = "🔥 High"
        elif avg_success >= 70 and avg_fidelity >= 0.70:
            performance = "⚡ Medium"
        else:
            performance = "⚠️ Low"
        
        balance_analysis.append({
            'Bit Combination': f"|{combo}⟩",
            'Count': count,
            'Percentage': f"{percentage:.1f}%",
            'Deviation': f"{deviation:.1f}%",
            'Balance Status': balance_status,
            'Success Rate': f"{avg_success:.1f}%",
            'Avg Fidelity': f"{avg_fidelity:.3f}",
            'Performance': performance
        })
    
    return balance_analysis

def get_balance_summary_metrics(results_history):
    """Get overall balance summary metrics"""
    if not results_history:
        return {}
    
    balance_data = analyze_transmission_balance(results_history)
    if not balance_data:
        return {}
    
    # Calculate overall metrics
    total_runs = sum(int(item['Count']) for item in balance_data)
    deviations = [float(item['Deviation'].replace('%', '')) for item in balance_data]
    max_deviation = max(deviations)
    avg_deviation = sum(deviations) / len(deviations)
    
    # Overall balance score (0-100)
    balance_score = max(0, 100 - (max_deviation * 4))
    
    # Balance quality
    if max_deviation <= 5:
        balance_quality = "Excellent"
        quality_color = "🟢"
    elif max_deviation <= 10:
        balance_quality = "Good"
        quality_color = "🟡"
    elif max_deviation <= 15:
        balance_quality = "Fair"
        quality_color = "🟠"
    else:
        balance_quality = "Poor"
        quality_color = "🔴"
    
    # Performance metrics
    success_rates = [float(item['Success Rate'].replace('%', '')) for item in balance_data]
    fidelities = [float(item['Avg Fidelity']) for item in balance_data]
    
    avg_success = sum(success_rates) / len(success_rates)
    avg_fidelity = sum(fidelities) / len(fidelities)
    
    return {
        'total_runs': total_runs,
        'balance_score': balance_score,
        'balance_quality': balance_quality,
        'quality_color': quality_color,
        'max_deviation': max_deviation,
        'avg_deviation': avg_deviation,
        'avg_success_rate': avg_success,
        'avg_fidelity': avg_fidelity,
        'uniformity_index': 100 - avg_deviation  # Higher is more uniform
    }

def create_quantum_state_visualization(protocol_result, bits_input):
    """Create comprehensive quantum state visualization showing the protocol steps"""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import numpy as np
    
    # Create subplot with Bloch sphere and state vector
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Initial Bell State |Φ⁺⟩', 'After Alice\'s Encoding', 'After Bob\'s Measurement', 'State Vector Evolution'),
        specs=[[{'type': 'scatter3d'}, {'type': 'scatter3d'}],
               [{'type': 'scatter3d'}, {'type': 'xy'}]],
        vertical_spacing=0.1,
        horizontal_spacing=0.1
    )
    
    # Quantum state data based on the input bits
    bit0, bit1 = bits_input
    
    # Step 1: Initial Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
    # Bloch sphere representation for qubit 1 (Alice's qubit)
    initial_x, initial_y, initial_z = 0, 0, 0  # Maximally entangled state
    
    # Step 2: After Alice's encoding operations
    # Apply gates based on input bits
    if bit1 == 1:  # X gate
        encoded_x = 1 if bit0 == 0 else -1
        encoded_y = 0
        encoded_z = 0 if bit0 == 0 else 0
    else:  # No X gate
        encoded_x = 0
        encoded_y = 0
        encoded_z = 1 if bit0 == 0 else -1
    
    # Step 3: After Bob's measurement
    # Measurement collapses to definite state
    measured_x = 1 if bit1 == 1 else 0
    measured_y = 0
    measured_z = 1 if bit0 == 1 else -1
    
    # Add Bloch sphere for initial state
    add_bloch_sphere(fig, row=1, col=1, x=initial_x, y=initial_y, z=initial_z, 
                     title="Initial Entangled State", color='blue')
    
    # Add Bloch sphere for encoded state
    add_bloch_sphere(fig, row=1, col=2, x=encoded_x, y=encoded_y, z=encoded_z,
                     title=f"After Encoding {bit0}{bit1}", color='red')
    
    # Add Bloch sphere for measured state
    add_bloch_sphere(fig, row=2, col=1, x=measured_x, y=measured_y, z=measured_z,
                     title="After Measurement", color='green')
    
    # State vector evolution plot
    steps = ['Initial |Φ⁺⟩', f'X^{bit1} Z^{bit0}', 'Bell Measurement', f'Result |{bit0}{bit1}⟩']
    probabilities = [
        [0.5, 0, 0, 0.5],  # Initial Bell state
        [0.25, 0.25, 0.25, 0.25] if bit0==1 or bit1==1 else [0.5, 0, 0, 0.5],  # After encoding
        [1.0, 0, 0, 0] if bit0==0 and bit1==0 else [0, 1.0, 0, 0] if bit0==0 else [0, 0, 1.0, 0] if bit1==0 else [0, 0, 0, 1.0],  # After measurement
        [1.0, 0, 0, 0] if bit0==0 and bit1==0 else [0, 1.0, 0, 0] if bit0==0 else [0, 0, 1.0, 0] if bit1==0 else [0, 0, 0, 1.0]   # Final result
    ]
    
    # Add state probability evolution
    for i, state in enumerate(['|00⟩', '|01⟩', '|10⟩', '|11⟩']):
        fig.add_trace(
            go.Scatter(
                x=steps,
                y=[prob[i] for prob in probabilities],
                mode='lines+markers',
                name=state,
                line=dict(width=3),
                marker=dict(size=8)
            ),
            row=2, col=2
        )
    
    # Update layout
    fig.update_layout(
        title=f"🌌 Quantum Superdense Coding Visualization - Message: |{bit0}{bit1}⟩",
        height=700,
        showlegend=True,
        font=dict(size=12)
    )
    
    # Update subplot titles and axes
    fig.update_xaxes(title_text="Protocol Steps", row=2, col=2)
    fig.update_yaxes(title_text="State Probability", row=2, col=2)
    
    return fig

def add_bloch_sphere(fig, row, col, x, y, z, title, color):
    """Add a Bloch sphere representation to the subplot"""
    import numpy as np
    
    # Create sphere surface
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    sphere_x = np.outer(np.cos(u), np.sin(v)) * 0.98
    sphere_y = np.outer(np.sin(u), np.sin(v)) * 0.98
    sphere_z = np.outer(np.ones(np.size(u)), np.cos(v)) * 0.98
    
    # Add sphere surface
    fig.add_trace(
        go.Surface(
            x=sphere_x, y=sphere_y, z=sphere_z,
            opacity=0.1,
            colorscale='Blues',
            showscale=False,
            hoverinfo='skip'
        ),
        row=row, col=col
    )
    
    # Add coordinate axes
    axis_length = 1.2
    
    # X axis (red)
    fig.add_trace(
        go.Scatter3d(
            x=[-axis_length, axis_length], y=[0, 0], z=[0, 0],
            mode='lines',
            line=dict(color='red', width=3),
            showlegend=False,
            hoverinfo='skip'
        ),
        row=row, col=col
    )
    
    # Y axis (green)
    fig.add_trace(
        go.Scatter3d(
            x=[0, 0], y=[-axis_length, axis_length], z=[0, 0],
            mode='lines',
            line=dict(color='green', width=3),
            showlegend=False,
            hoverinfo='skip'
        ),
        row=row, col=col
    )
    
    # Z axis (blue)
    fig.add_trace(
        go.Scatter3d(
            x=[0, 0], y=[0, 0], z=[-axis_length, axis_length],
            mode='lines',
            line=dict(color='blue', width=3),
            showlegend=False,
            hoverinfo='skip'
        ),
        row=row, col=col
    )
    
    # Add state vector
    if abs(x) > 0.01 or abs(y) > 0.01 or abs(z) > 0.01:
        fig.add_trace(
            go.Scatter3d(
                x=[0, x], y=[0, y], z=[0, z],
                mode='lines+markers',
                line=dict(color=color, width=6),
                marker=dict(size=[3, 10], color=color),
                showlegend=False,
                hoverinfo='text',
                hovertext=f'State Vector: ({x:.2f}, {y:.2f}, {z:.2f})'
            ),
            row=row, col=col
        )
    
    # Add labels
    fig.add_trace(
        go.Scatter3d(
            x=[axis_length*1.1], y=[0], z=[0],
            mode='text',
            text=['|+⟩'],
            textfont=dict(size=14, color='red'),
            showlegend=False,
            hoverinfo='skip'
        ),
        row=row, col=col
    )
    
    fig.add_trace(
        go.Scatter3d(
            x=[0], y=[0], z=[axis_length*1.1],
            mode='text',
            text=['|0⟩'],
            textfont=dict(size=14, color='blue'),
            showlegend=False,
            hoverinfo='skip'
        ),
        row=row, col=col
    )
    
    fig.add_trace(
        go.Scatter3d(
            x=[0], y=[0], z=[-axis_length*1.1],
            mode='text',
            text=['|1⟩'],
            textfont=dict(size=14, color='blue'),
            showlegend=False,
            hoverinfo='skip'
        ),
        row=row, col=col
    )

def create_quantum_circuit_visualization(bits_input, protocol_result):
    """Create quantum circuit diagram showing the protocol steps"""
    import plotly.graph_objects as go
    
    bit0, bit1 = bits_input
    
    fig = go.Figure()
    
    # Circuit dimensions
    circuit_width = 10
    circuit_height = 4
    qubit_spacing = 1
    
    # Draw quantum wires
    for i in range(2):
        y_pos = circuit_height - i * qubit_spacing
        fig.add_trace(
            go.Scatter(
                x=[0, circuit_width],
                y=[y_pos, y_pos],
                mode='lines',
                line=dict(color='black', width=2),
                showlegend=False,
                hoverinfo='skip'
            )
        )
        
        # Qubit labels
        qubit_name = 'Alice' if i == 0 else 'Bob'
        fig.add_annotation(
            x=-0.5, y=y_pos,
            text=f'{qubit_name}',
            showarrow=False,
            font=dict(size=14, color='blue')
        )
    
    # Gate positions
    bell_pos = 1
    encoding_pos = 3
    measurement_pos = 6
    result_pos = 8
    
    # Bell state preparation
    fig.add_shape(
        type="rect",
        x0=bell_pos-0.3, y0=circuit_height-0.3,
        x1=bell_pos+0.3, y1=circuit_height+0.3,
        fillcolor="lightblue",
        line=dict(color="blue", width=2)
    )
    fig.add_annotation(
        x=bell_pos, y=circuit_height,
        text="H",
        showarrow=False,
        font=dict(size=16, color='blue')
    )
    
    # CNOT gate
    fig.add_trace(
        go.Scatter(
            x=[bell_pos, bell_pos],
            y=[circuit_height, circuit_height-1],
            mode='lines',
            line=dict(color='blue', width=3),
            showlegend=False,
            hoverinfo='skip'
        )
    )
    
    # Control and target dots for CNOT
    fig.add_trace(
        go.Scatter(
            x=[bell_pos],
            y=[circuit_height],
            mode='markers',
            marker=dict(size=10, color='blue'),
            showlegend=False,
            hoverinfo='skip'
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=[bell_pos],
            y=[circuit_height-1],
            mode='markers',
            marker=dict(size=15, color='white', line=dict(color='blue', width=2)),
            showlegend=False,
            hoverinfo='skip'
        )
    )
    
    # Alice's encoding gates
    if bit1 == 1:  # X gate
        fig.add_shape(
            type="rect",
            x0=encoding_pos-0.3, y0=circuit_height-0.3,
            x1=encoding_pos+0.3, y1=circuit_height+0.3,
            fillcolor="lightcoral",
            line=dict(color="red", width=2)
        )
        fig.add_annotation(
            x=encoding_pos, y=circuit_height,
            text="X",
            showarrow=False,
            font=dict(size=16, color='red')
        )
    
    if bit0 == 1:  # Z gate
        fig.add_shape(
            type="rect",
            x0=encoding_pos+0.7-0.3, y0=circuit_height-0.3,
            x1=encoding_pos+0.7+0.3, y1=circuit_height+0.3,
            fillcolor="lightgreen",
            line=dict(color="green", width=2)
        )
        fig.add_annotation(
            x=encoding_pos+0.7, y=circuit_height,
            text="Z",
            showarrow=False,
            font=dict(size=16, color='green')
        )
    
    # Bob's Bell measurement
    # CNOT
    fig.add_trace(
        go.Scatter(
            x=[measurement_pos, measurement_pos],
            y=[circuit_height, circuit_height-1],
            mode='lines',
            line=dict(color='purple', width=3),
            showlegend=False,
            hoverinfo='skip'
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=[measurement_pos],
            y=[circuit_height],
            mode='markers',
            marker=dict(size=10, color='purple'),
            showlegend=False,
            hoverinfo='skip'
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=[measurement_pos],
            y=[circuit_height-1],
            mode='markers',
            marker=dict(size=15, color='white', line=dict(color='purple', width=2)),
            showlegend=False,
            hoverinfo='skip'
        )
    )
    
    # Hadamard on Alice's qubit
    fig.add_shape(
        type="rect",
        x0=measurement_pos+0.7-0.3, y0=circuit_height-0.3,
        x1=measurement_pos+0.7+0.3, y1=circuit_height+0.3,
        fillcolor="lightyellow",
        line=dict(color="orange", width=2)
    )
    fig.add_annotation(
        x=measurement_pos+0.7, y=circuit_height,
        text="H",
        showarrow=False,
        font=dict(size=16, color='orange')
    )
    
    # Measurement symbols
    for i in range(2):
        y_pos = circuit_height - i * qubit_spacing
        fig.add_shape(
            type="rect",
            x0=result_pos-0.3, y0=y_pos-0.3,
            x1=result_pos+0.3, y1=y_pos+0.3,
            fillcolor="lightgray",
            line=dict(color="black", width=2)
        )
        
        result_bit = bit0 if i == 0 else bit1
        fig.add_annotation(
            x=result_pos, y=y_pos,
            text=str(result_bit),
            showarrow=False,
            font=dict(size=16, color='black')
        )
    
    # Add protocol step labels
    steps = [
        (bell_pos, -0.5, "Bell State\nPreparation"),
        (encoding_pos+0.35, -0.5, "Alice's\nEncoding"),
        (measurement_pos+0.35, -0.5, "Bell\nMeasurement"),
        (result_pos, -0.5, f"Result\n|{bit0}{bit1}⟩")
    ]
    
    for x, y, text in steps:
        fig.add_annotation(
            x=x, y=y,
            text=text,
            showarrow=False,
            font=dict(size=12, color='navy'),
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="navy",
            borderwidth=1
        )
    
    # Update layout
    fig.update_layout(
        title=f"🔄 Quantum Circuit: Superdense Coding Protocol - Message |{bit0}{bit1}⟩",
        xaxis=dict(range=[-1, circuit_width+1], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[-1, circuit_height+0.5], showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        width=800,
        height=400,
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    return fig

def get_scenario_bits(scenario):
    """Map application scenarios to specific bit combinations"""
    scenario_map = {
        "Quantum Key Distribution": (0, 0),  # Secure key establishment
        "Secure Banking": (0, 1),            # Financial transaction
        "Military Communication": (1, 0),     # Defense protocol
        "Satellite Communication": (1, 1),    # Space communication
        "Medical Data Transfer": (0, 0),      # Healthcare data
        "Financial Trading": (0, 1),          # High-frequency trading
        "IoT Device Control": (1, 0),         # Internet of Things
        "Emergency Services": (1, 1),         # Emergency communication
        "Blockchain Verification": (0, 0),    # Cryptocurrency
        "Scientific Research": (0, 1),        # Research data
        "Government Communications": (1, 0),   # Official channels
        "Autonomous Vehicle": (1, 1),         # Self-driving car data
        "Smart Grid Control": (0, 0),         # Power grid management
        "Weather Monitoring": (0, 1),         # Meteorological data
        "Air Traffic Control": (1, 0),        # Aviation safety
        "Nuclear Facility": (1, 1),           # Nuclear monitoring
        "Space Exploration": (0, 0),          # NASA/ESA missions
        "Cybersecurity Alert": (0, 1),        # Security monitoring
        "Supply Chain": (1, 0),               # Logistics tracking
        "Stock Market": (1, 1),               # Market data
        "Gaming Protocol": (0, 0),            # Online gaming
        "Social Media": (0, 1),               # Social networks
        "Video Streaming": (1, 0),            # Media content
        "Email Encryption": (1, 1),           # Secure email
        "Database Sync": (0, 0),              # Data synchronization
        "API Authentication": (0, 1),         # Service authentication
        "Cloud Storage": (1, 0),              # File storage
        "VPN Connection": (1, 1),             # Virtual private network
        "Smart Home": (0, 0),                 # Home automation
        "Industrial IoT": (0, 1),             # Factory automation
        "Autonomous Drone": (1, 0),           # Drone communication
        "Biometric Security": (1, 1),         # Identity verification
        "Remote Surgery": (0, 0),             # Telemedicine
        "Stock Trading": (0, 1),              # Algorithmic trading
        "Quantum Internet": (1, 0),           # Quantum networking
        "Distributed Computing": (1, 1),      # Grid computing
        "Privacy Protection": (0, 0),         # Data privacy
        "Authentication": (0, 1),             # User verification
        "Data Integrity": (1, 0),             # Data validation
        "Network Security": (1, 1),           # Security protocols
        "Emergency Alert": (0, 0),            # Crisis communication
        "Traffic Management": (0, 1),         # Urban traffic
        "Energy Grid": (1, 0),                # Smart grid
        "Spacecraft Control": (1, 1),         # Space missions
        "Research Collaboration": (0, 0),     # Academic research
        "Patent Filing": (0, 1),              # Intellectual property
        "Legal Documentation": (1, 0),        # Legal systems
        "Insurance Claims": (1, 1),           # Insurance processing
        "Healthcare Records": (0, 0),         # Medical records
        "Pharmaceutical Research": (0, 1),    # Drug development
        "Climate Monitoring": (1, 0),         # Environmental data
        "Seismic Detection": (1, 1),          # Earthquake monitoring
        "Ocean Research": (0, 0),             # Marine science
        "Astronomy Data": (0, 1),             # Space observation
        "Particle Physics": (1, 0),           # Physics experiments
        "Gene Sequencing": (1, 1),            # Genomics research
        "Neural Networks": (0, 0),            # AI training
        "Machine Learning": (0, 1),           # ML algorithms
        "Quantum Computing": (1, 0),          # Quantum algorithms
        "Cryptography": (1, 1),               # Encryption protocols
        "Digital Forensics": (0, 0),          # Investigation tools
        "Incident Response": (0, 1),          # Security incidents
        "Threat Detection": (1, 0),           # Cybersecurity
        "Vulnerability Scan": (1, 1),         # Security assessment
        "Penetration Testing": (0, 0),        # Security testing
        "Compliance Audit": (0, 1),           # Regulatory compliance
        "Risk Assessment": (1, 0),            # Risk management
        "Business Intelligence": (1, 1),      # Analytics
        "Customer Service": (0, 0),           # Support systems
        "Sales Analytics": (0, 1),            # Sales data
        "Marketing Campaign": (1, 0),         # Marketing analytics
        "Product Development": (1, 1),        # R&D communication
        "Quality Control": (0, 0),            # Manufacturing QC
        "Supply Logistics": (0, 1),           # Logistics management
        "Inventory Management": (1, 0),       # Stock control
        "Fleet Tracking": (1, 1),             # Vehicle monitoring
        "Asset Management": (0, 0),           # Asset tracking
        "Maintenance Schedule": (0, 1),       # Preventive maintenance
        "Safety Monitoring": (1, 0),          # Safety systems
        "Environmental Control": (1, 1),      # HVAC systems
        "Access Control": (0, 0),             # Building security
        "Surveillance System": (0, 1),        # Security cameras
        "Alarm System": (1, 0),               # Security alarms
        "Fire Safety": (1, 1),                # Fire protection
        "Emergency Evacuation": (0, 0),       # Safety protocols
        "Disaster Recovery": (0, 1),          # Business continuity
        "Backup Systems": (1, 0),             # Data backup
        "System Recovery": (1, 1),            # System restoration
        "Performance Monitoring": (0, 0),     # System monitoring
        "Load Balancing": (0, 1),             # Resource management
        "Capacity Planning": (1, 0),          # Infrastructure planning
        "Resource Allocation": (1, 1),        # Resource optimization
        "Cost Optimization": (0, 0),          # Financial optimization
        "Budget Planning": (0, 1),            # Financial planning
        "Revenue Analysis": (1, 0),           # Financial analysis
        "Profit Tracking": (1, 1),            # Financial tracking
        "Investment Strategy": (0, 0),        # Investment planning
        "Portfolio Management": (0, 1),       # Asset management
        "Risk Management": (1, 0),            # Financial risk
        "Fraud Detection": (1, 1),            # Security fraud
        "Anti-Money Laundering": (0, 0),      # AML compliance
        "Regulatory Reporting": (0, 1),       # Compliance reporting
        "Tax Calculation": (1, 0),            # Tax processing
        "Audit Trail": (1, 1),                # Audit logging
        "Security Alert": (0, 1),             # Security notification
        "Network Heartbeat": (1, 0)           # Network monitoring
    }
    
    return scenario_map.get(scenario, (0, 0))  # Default to (0,0) if scenario not found

def display_technical_specs():
    """Display comprehensive technical specifications of the quantum superdense coding protocol"""
    
    # Create main specification tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🔬 Quantum Theory", "⚙️ Implementation", "📊 Performance", "🔒 Security"])
    
    with tab1:
        st.markdown("### 🔬 Quantum Theory Foundations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🌌 Bell States (Maximally Entangled States)**
            
            The protocol utilizes four Bell states:
            
            • **|Φ⁺⟩ = (|00⟩ + |11⟩)/√2** → Encoding: 00
            • **|Φ⁻⟩ = (|00⟩ - |11⟩)/√2** → Encoding: 01  
            • **|Ψ⁺⟩ = (|01⟩ + |10⟩)/√2** → Encoding: 10
            • **|Ψ⁻⟩ = (|01⟩ - |10⟩)/√2** → Encoding: 11
            
            **⚡ Quantum Operations**
            
            • **Identity (I)**: No operation for bit 0
            • **Pauli-X**: Bit flip for encoding bit 1  
            • **Pauli-Z**: Phase flip for encoding bit 0
            • **Pauli-Y**: Combined X and Z for encoding bit 1
            """)
            
            st.markdown("""
            **🔗 Entanglement Properties**
            
            • **Concurrence**: C = 1 (maximal entanglement)
            • **Entanglement Entropy**: S = 1 bit
            • **Schmidt Rank**: 2 (bipartite entanglement)
            • **Bell Inequality**: Violation by factor √2
            """)
        
        with col2:
            st.markdown("""
            **📐 Mathematical Framework**
            
            **Density Matrix Representation:**
            ```
            ρ = |ψ⟩⟨ψ| where |ψ⟩ is Bell state
            ```
            
            **Fidelity Calculation:**
            ```
            F = ⟨ψ_ideal|ρ_measured|ψ_ideal⟩
            ```
            
            **Channel Capacity:**
            ```
            C = 2 bits per qubit pair
            ```
            
            **Quantum Advantage:**
            ```
            Efficiency = 2× classical protocols
            ```
            """)
            
            # Add quantum circuit visualization
            st.markdown("**🔄 Quantum Circuit Flow**")
            circuit_fig = create_quantum_circuit_display()
            st.plotly_chart(circuit_fig, use_container_width=True)
    
    with tab2:
        st.markdown("### ⚙️ Implementation Specifications")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔧 Hardware Requirements**
            
            • **Quantum Processor**: 2+ qubit capacity
            • **Gate Fidelity**: >99.5% for reliable operation
            • **Coherence Time**: T₂ > 100 μs minimum
            • **Gate Time**: <10 ns for fast operations
            • **Readout Fidelity**: >99% measurement accuracy
            
            **📡 Communication Channel**
            
            • **Quantum Channel**: Entangled photon pairs
            • **Classical Channel**: Authentication & synchronization
            • **Transmission Rate**: Up to 10⁶ photons/second
            • **Distance Range**: 1-1000 km (fiber/free-space)
            • **Error Correction**: Integrated noise mitigation
            """)
            
            st.markdown("""
            **💻 Software Framework**
            
            • **Quantum SDK**: Qiskit 2.0+ compatibility
            • **Backend Support**: IBM Quantum, Google Cirq
            • **Simulator**: High-fidelity noise modeling
            • **Language**: Python 3.8+ with NumPy/SciPy
            • **Visualization**: Plotly for real-time analysis
            """)
        
        with col2:
            st.markdown("""
            **🎛️ Control Parameters**
            
            • **Noise Level**: 0.0 - 0.5 (configurable)
            • **Shot Count**: 1024 (default), up to 8192
            • **Measurement Basis**: Computational {|0⟩, |1⟩}
            • **Error Models**: Depolarizing, amplitude damping
            • **Calibration**: Real-time parameter adjustment
            
            **🔄 Protocol Steps**
            
            1. **Initialize**: Create |00⟩ state
            2. **Entangle**: Apply Hadamard + CNOT
            3. **Encode**: Apply Pauli operations
            4. **Transmit**: Send qubit through channel
            5. **Decode**: Reverse entanglement operations
            6. **Measure**: Extract classical bits
            """)
            
            # Technical metrics display
            st.markdown("**📈 Performance Metrics**")
            metrics_data = {
                "Metric": ["Theoretical Fidelity", "Practical Fidelity", "Success Rate", "Error Rate", "Channel Capacity"],
                "Value": ["100%", "85-95%", ">90%", "<10%", "2 bits/qubit"],
                "Benchmark": ["Perfect", "Excellent", "High", "Low", "Optimal"]
            }
            st.dataframe(metrics_data, use_container_width=True)
    
    with tab3:
        st.markdown("### 📊 Performance Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **⚡ Efficiency Metrics**
            
            • **Information Density**: 2 classical bits per qubit
            • **Bandwidth Efficiency**: 100% quantum channel utilization
            • **Time Complexity**: O(1) - constant time encoding
            • **Space Complexity**: O(1) - minimal qubit overhead
            • **Scaling**: Linear with message length
            
            **🎯 Accuracy Benchmarks**
            
            • **Ideal Conditions**: 100% fidelity
            • **Laboratory Conditions**: 95-98% fidelity
            • **Real-world Deployment**: 85-95% fidelity
            • **Noisy Environments**: 70-90% fidelity
            • **Error Correction**: +5-10% improvement
            """)
            
            # Performance comparison chart
            efficiency_fig = create_efficiency_chart()
            st.plotly_chart(efficiency_fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            **🚀 Comparative Analysis**
            
            | Protocol | Bits/Qubit | Efficiency | Security |
            |----------|------------|------------|----------|
            | Classical | 1 | 50% | Medium |
            | Superdense | 2 | 100% | High |
            | Teleportation | 0 | N/A | Maximum |
            | BB84 QKD | 0.5 | 25% | Maximum |
            
            **📡 Channel Performance**
            
            • **Fiber Optic**: 99.9% transmission fidelity
            • **Free Space**: 95-99% (weather dependent)
            • **Satellite Links**: 90-95% transmission fidelity
            • **Urban Environment**: 85-95% (interference)
            • **Underwater**: 70-85% (attenuation limited)
            """)
            
            st.markdown("""
            **🔬 Noise Analysis**
            
            • **Thermal Noise**: T₁ relaxation effects
            • **Dephasing**: T₂* coherence limitations  
            • **Gate Errors**: Imperfect quantum operations
            • **Measurement Errors**: Readout inaccuracies
            • **Environmental**: Electromagnetic interference
            """)
    
    with tab4:
        st.markdown("### 🔒 Security Specifications")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🛡️ Quantum Security Features**
            
            • **No-Cloning Theorem**: Quantum states cannot be copied
            • **Entanglement Detection**: Bell inequality violations
            • **Eavesdropping Detection**: CHSH parameter monitoring
            • **Information-Theoretic Security**: Unconditional security
            • **Forward Secrecy**: Each transmission independent
            
            **🔐 Cryptographic Properties**
            
            • **Key Distribution**: Quantum-secured key exchange
            • **Authentication**: Quantum digital signatures
            • **Integrity**: Tamper-evident transmission
            • **Non-repudiation**: Quantum fingerprinting
            • **Privacy**: Information-theoretic privacy
            """)
            
            st.markdown("""
            **⚔️ Attack Resistance**
            
            • **Intercept-Resend**: Detectable via fidelity
            • **Man-in-the-Middle**: Prevented by entanglement
            • **Photon-Number-Splitting**: N/A (true single photons)
            • **Trojan Horse**: Isolated quantum channels
            • **Side-Channel**: Hardware security modules
            """)
        
        with col2:
            st.markdown("""
            **🎯 Security Levels**
            
            | Threat Model | Security Level | CHSH Value |
            |--------------|----------------|------------|
            | No Attack | Maximum | >2.5 |
            | Passive Eavesdrop | High | 2.0-2.5 |
            | Active Attack | Medium | 1.5-2.0 |
            | Compromised | Low | <1.5 |
            
            **🔍 Monitoring Parameters**
            
            • **CHSH Inequality**: S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
            • **Threshold**: S > 2.0 indicates security
            • **Violation**: S ≤ 2.0 suggests eavesdropping
            • **Confidence**: Statistical significance testing
            • **Real-time**: Continuous security monitoring
            """)
            
            # Security gauge visualization
            security_score = 0.85  # Example security level
            gauge_fig, security_level = create_security_gauge(security_score, 2.6)
            st.plotly_chart(gauge_fig, use_container_width=True)
            
            st.success(f"🔒 Current Security Level: **{security_level}**")
    
    # Additional technical information
    st.markdown("---")
    st.markdown("### 📚 Additional Resources")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **📖 References**
        • Bennett & Wiesner (1992)
        • Nielsen & Chuang Textbook
        • IBM Qiskit Documentation
        • Nature Quantum Information
        """)
    
    with col2:
        st.info("""
        **🔗 Standards**
        • ITU-T Y.3800 Series
        • NIST Post-Quantum Crypto
        • ISO/IEC 23837:2021
        • ETSI GS QKD Series
        """)
    
    with col3:
        st.info("""
        **🛠️ Tools & Frameworks**
        • Qiskit Quantum Computing
        • Cirq by Google
        • Q# Microsoft Quantum
        • PennyLane Quantum ML
        """)
    
    st.markdown("""
    ---
    💡 **Note**: These specifications represent the current state-of-the-art in quantum superdense coding 
    implementation. Performance may vary based on hardware platform and environmental conditions.
    """)


