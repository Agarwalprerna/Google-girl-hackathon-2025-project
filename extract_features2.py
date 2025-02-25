import os
import csv
from pyverilog.vparser.parser import parse
from pyverilog.vparser.ast import InstanceList, Instance, Decl, Input, Output

# List of Verilog files to analyze
verilog_files = [
    "encoder4to2.v",
    "full_adder.v",
    "mux4to1.v",
    "half_adder.v"
]

def extract_features(verilog_file):
    try:
        ast, _ = parse([verilog_file])  # Parse the Verilog file

        num_modules = 0
        num_instances = 0
        num_gates = 0
        max_fan_in = 0
        max_fan_out = 0
        gate_counts =  {"AND": 0, "OR": 0,  "XOR": 0, "NOT": 0}

        
        for mod in ast.description.definitions:
            num_modules += 1  # Counting modules

            local_fan_in = 0
            local_fan_out = 0

            for item in mod.items:
                if isinstance(item, InstanceList):  # Counting instances
                    num_instances += len(item.instances)

                if isinstance(item, Decl):  # Checking for inputs & outputs
                    for decl in item.list:
                        if isinstance(decl, Input):
                            local_fan_in += 1
                        elif isinstance(decl, Output):
                            local_fan_out += 1

                if isinstance(item, Instance):  # Checking for gate usage
                    for gate in ["AND", "OR", "XOR","NOT"]:
                        if gate.lower() in item.module.lower():
                            num_gates += 1
                            gate_counts.add(gate)

            max_fan_in = max(max_fan_in, local_fan_in)
            max_fan_out = max(max_fan_out, local_fan_out)

        return {
            "Circuit": os.path.basename(verilog_file),
            "Modules": num_modules,
            "Instances": num_instances,
            "Number of Gates": num_gates,
            "Max Fan-in": max_fan_in,
            "Max Fan-out": max_fan_out,
            **gate_counts  # Adds each gate type as a separate column
        }
    
    except Exception as e:
        print(f"Error processing {verilog_file}: {e}")
        return None

def main():
    csv_file = "circuit_features.csv"
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Circuit", "Modules", "Instances", "Number of Gates", "Max Fan-in", "Max Fan-out", "AND","OR","XOR","NOT"])
        writer.writeheader()

        for verilog_file in verilog_files:
            features = extract_features(verilog_file)
            if features:
                writer.writerow(features)

    print(f"Feature extraction completed! Results saved in {csv_file}")

if __name__ == "__main__":
    main()
