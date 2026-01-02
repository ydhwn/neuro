# Neuromorphic Deployment Report

**Report Generated:** 2025-11-06 15:39:27
**Model:** SimpleSNN

## Model Specifications
- **Total Neurons:** 139
- **Total Synapses:** 9611

## Target Hardware Comparison
### Target: Intel Loihi
- **Neuron Capacity:** 131072
- **Synapse Capacity:** 131072000
- **Bit Precision:** 9 bits
- **Cores:** 128
- **Neurons per Core:** 1024
- **Neuron Utilization:** 0.11%
- **Synapse Utilization:** 0.01%
- **Estimated Energy per Inference:** 240.28 nJ (Bit-precision adjusted)
- **Estimated Inter-core Latency:** 0.00 ns
- **Cores Used:** 1 (of 128)
- **Cross-core Synapses:** 0
- **Core Allocation Map:**
  - Core 0: 139 neurons (fc1, fc2)
- **Warnings:** None

### Target: BrainChip Akida
- **Neuron Capacity:** 1200000
- **Synapse Capacity:** 10000000000
- **Bit Precision:** 4 bits
- **Cores:** 384
- **Neurons per Core:** 4096
- **Neuron Utilization:** 0.01%
- **Synapse Utilization:** 0.00%
- **Estimated Energy per Inference:** 14.42 nJ (Bit-precision adjusted)
- **Estimated Inter-core Latency:** 0.00 ns
- **Cores Used:** 1 (of 384)
- **Cross-core Synapses:** 0
- **Core Allocation Map:**
  - Core 0: 139 neurons (fc1, fc2)
- **Warnings:** None

### Target: SpiNNaker
- **Neuron Capacity:** 5000000
- **Synapse Capacity:** 200000000
- **Bit Precision:** 16 bits
- **Cores:** 864
- **Neurons per Core:** 1024
- **Neuron Utilization:** 0.00%
- **Synapse Utilization:** 0.00%
- **Estimated Energy per Inference:** 115.33 nJ (Bit-precision adjusted)
- **Estimated Inter-core Latency:** 0.00 ns
- **Cores Used:** 1 (of 864)
- **Cross-core Synapses:** 0
- **Core Allocation Map:**
  - Core 0: 139 neurons (fc1, fc2)
- **Warnings:** None