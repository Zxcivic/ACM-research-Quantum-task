from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
def add_three_numbers(num1, num2, num3):
    circuit = QuantumCircuit(9, 3)
    for qubit in range(9):
        circuit.h(qubit)
    circuit.cx(0, 3)
    circuit.cx(1, 3)
    circuit.ccx(0, 1, 4)
    circuit.cx(2, 5)
    circuit.ccx(3, 5, 6)
    circuit.cx(3, 5)
    circuit.ccx(4, 6, 7)
    circuit.cx(4, 6)
    circuit.cx(5, 7)
    for i in range(3):
        circuit.measure(6+i, i)
    return circuit
num1 = '00' 
num2 = '01' 
num3 = '10' 
qc = add_three_numbers(num1, num2, num3)
simulator = AerSimulator()
transpiled_circuit = transpile(qc, simulator)
job = simulator.run(transpiled_circuit, shots=1)
result = job.result()
counts = result.get_counts(qc)
print(counts)