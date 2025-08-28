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
            titlefont=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            titlefont=dict(size=16),
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
            titlefont=dict(size=14)
        ),
        yaxis=dict(
            tickfont=dict(size=12),
            titlefont=dict(size=14)
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
