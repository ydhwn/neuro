import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import torch
import os

from snn_model.model import SimpleSNN
from utils.neuromorphic_profiler import NeuromorphicProfiler
from utils.virtual_chip import VirtualNeuromorphicChip
from utils.report_generator import generate_deployment_report

def load_model(checkpoint_path: str):
    if not os.path.isfile(checkpoint_path):
        return None, None, None
    ckpt = torch.load(checkpoint_path, map_location="cpu")
    input_dim = ckpt.get("input_dim", 63)
    num_classes = ckpt.get("num_classes", 10)
    model = SimpleSNN(input_dim=input_dim, hidden_dim=ckpt.get("hidden_dim", 128), num_classes=num_classes)
    model.load_state_dict(ckpt["model_state"]) 
    model.eval()
    label_to_idx = ckpt.get("label_to_idx", {})
    idx_to_label = {v: k for k, v in label_to_idx.items()} if label_to_idx else {i: str(i) for i in range(num_classes)}
    return model, idx_to_label, input_dim

def main():
    model, _, _ = load_model("models/snn_latest.pt")
    if model is None:
        print("Failed to load model. Make sure 'models/snn_latest.pt' exists.")
        return

    # Neuromorphic Profiler Setup
    virtual_chip = VirtualNeuromorphicChip(chip_type="loihi")
    profiler = NeuromorphicProfiler(chip=virtual_chip)
    model.register_profiler(profiler)

    # Generate Deployment Report
    target_chips = [
        VirtualNeuromorphicChip(chip_type="loihi"),
        VirtualNeuromorphicChip(chip_type="akida"),
        VirtualNeuromorphicChip(chip_type="spinnaker"),
    ]
    report = generate_deployment_report(profiler, target_chips)
    
    report_path = "deployment_report.md"
    with open(report_path, "w") as f:
        f.write(report)
        
    print(f"Deployment report saved to {report_path}")

if __name__ == "__main__":
    main()