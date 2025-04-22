# 🔐 BB84 Quantum Key Distribution Simulator

A web-based simulator that demonstrates the BB84 quantum key distribution protocol, including the presence of an eavesdropper (Eve). This project provides a visual and interactive way to understand quantum cryptography concepts.

## 🌟 Features

- Interactive simulation of the BB84 protocol
- Visualization of quantum key distribution between Alice and Bob
- Demonstration of eavesdropping by Eve
- Adjustable key length
- Detailed step-by-step visualization of the quantum transmission process
- Error rate calculation
- User-friendly interface built with Streamlit

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/bb84-simulator.git
cd bb84-simulator
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

To start the simulator, run:
```bash
streamlit run bb84_webapp.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📊 How to Use

1. Adjust the key length using the slider (5-50 bits)
2. Toggle "Show Simulation Steps" to view detailed transmission information
3. Observe how the quantum key distribution process works
4. See the impact of Eve's eavesdropping on the final key

## 🔬 Technical Details

The simulator implements the following aspects of the BB84 protocol:

- Random bit and basis generation for Alice
- Quantum state preparation and measurement
- Eavesdropping simulation by Eve
- Key sifting process
- Error rate calculation

## 📚 About BB84 Protocol

The BB84 protocol, developed by Bennett and Brassard in 1984, is a quantum key distribution scheme that allows two parties to produce a shared random secret key. The security of the protocol comes from the fundamental principles of quantum mechanics:

- Quantum states cannot be cloned (No-cloning theorem)
- Measurement of quantum states affects the system
- Any attempt at eavesdropping introduces errors that can be detected

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

- Neeraj

## 🙏 Acknowledgments

- Inspired by the original BB84 protocol paper
- Built using Streamlit for the web interface 