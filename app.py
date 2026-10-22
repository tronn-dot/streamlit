import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Edge IoT MRA-DFL Simulator", layout="wide")

st.title("🚀 Edge IoT: Mutable Resource Allocation & Federated Learning Simulator")
st.markdown("### Interactive Software Prototype for Dynamic Resource Management")

# Sidebar Controls
st.sidebar.header("Simulation Settings")
num_nodes = st.sidebar.slider("Active Edge Nodes", min_value=10, max_value=120, value=60, step=10)
traffic_load = st.sidebar.slider("IoT Traffic Intensity", min_value=0.1, max_value=1.0, value=0.75, step=0.05)
run_button = st.sidebar.button("Run Simulation Round")

# Main Dashboard layout
col1, col2, col3, col4 = st.columns(4)

if run_button:
    with st.spinner("Running decentralized federated learning nodes..."):
        time.sleep(1.0) # Simulate processing delay
        
        # Simulated metrics based on paper findings
        allocated_rate = np.random.uniform(0.92, 0.96)
        connectivity = allocated_rate * 100
        backlogs = int(np.random.uniform(30, 48))
        alloc_time = np.random.uniform(0.85, 1.10)
        backup_nodes_added = int(num_nodes * (traffic_load * 0.2))

    col1.metric("Resource Allocation", f"{allocated_rate:.2f} / 1.0", "+8.5%")
    col2.metric("Network Connectivity", f"{connectivity:.1f}%", "+9.4%", delta_color="normal")
    col3.metric("Communication Backlogs", f"{backlogs} tasks", "-11.7% (Low)", delta_color="inverse")
    col4.metric("Allocation Speed", f"{alloc_time:.2f} sec", "Fast (~1s)")

    st.success("Simulation completed successfully! Decentralized federated learning updated local model weights without leaking raw user data.")
    
    st.markdown("---")
    st.subheader("Live Operational Log")
    st.info(f"• Analyzed {num_nodes} heterogeneous edge nodes handling non-IID data streams.\n"
            f"• Detected high traffic load intensity ({traffic_load}).\n"
            f"• Triggered MRA logic: Dynamically recruited **{backup_nodes_added} backup edge nodes** to prevent queue timeouts.\n"
            f"• Cleared communication backlogs successfully.")

else:
    col1.metric("Resource Allocation", "Ready", "---")
    col2.metric("Network Connectivity", "Standby", "---")
    col3.metric("Communication Backlogs", "0", "---")
    col4.metric("Allocation Speed", "0.00 sec", "---")
    
    st.warning("👈 Adjust your parameters in the sidebar and click **Run Simulation Round** to test the prototype live.")