import streamlit as st
import random

st.set_page_config(page_title="BB84 QKD Simulator with Eve", page_icon="🔐")

st.title("🔐 BB84 Quantum Key Distribution Simulator with Eve  by NEERAJ   THIS IS MY FIRST  PROJECT   ROAD TO GET JOB")
st.markdown("Simulate how Alice, Bob, and Eve communicate using quantum bits (qubits)")

# Input parameters
key_length = st.slider("Length of Key", 5, 50, 10)
show_details = st.checkbox("Show Simulation Steps", value=True)

# Randomly generate bits and bases
alice_bits = [random.randint(0, 1) for _ in range(key_length)]
alice_bases = [random.choice(['Z', 'X']) for _ in range(key_length)]
eve_bases = [random.choice(['Z', 'X']) for _ in range(key_length)]
bob_bases = [random.choice(['Z', 'X']) for _ in range(key_length)]

def measure(bit, basis_sent, basis_received):
    if basis_sent == basis_received:
        return bit
    else:
        return random.randint(0, 1)

# Eve intercepts
eve_bits = [measure(alice_bits[i], alice_bases[i], eve_bases[i]) for i in range(key_length)]
# Bob receives what Eve forwards
bob_bits = [measure(eve_bits[i], eve_bases[i], bob_bases[i]) for i in range(key_length)]

# Sifted keys
sifted_key_indices = [i for i in range(key_length) if alice_bases[i] == bob_bases[i]]
sifted_alice_key = [alice_bits[i] for i in sifted_key_indices]
sifted_bob_key = [bob_bits[i] for i in sifted_key_indices]

# Calculate error rate
mismatches = sum(1 for a, b in zip(sifted_alice_key, sifted_bob_key) if a != b)
error_rate = (mismatches / len(sifted_alice_key)) * 100 if sifted_alice_key else 0

# Display results
st.subheader("🧪 Results")
st.write(f"Sifted Alice Key: {sifted_alice_key}")
st.write(f"Sifted Bob Key: {sifted_bob_key}")
st.write(f"⚠️ Error Rate: `{error_rate:.2f}%`")

if show_details:
    st.subheader("📊 Full Transmission Details")
    st.write(f"Alice Bits:  {alice_bits}")
    st.write(f"Alice Bases: {alice_bases}")
    st.write(f"Eve Bases:   {eve_bases}")
    st.write(f"Eve Bits:    {eve_bits}")
    st.write(f"Bob Bases:   {bob_bases}")
    st.write(f"Bob Bits:    {bob_bits}")

st.markdown("---")

