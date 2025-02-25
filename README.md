# Data Generation

The dataset used for training and evaluating the machine learning model was generated using a combination of methods:

1.  **Automated Feature Extraction:**
    * The Python script `extract_features.py` was used to automatically extract features (modules, instances, gates, fan-in, fan-out, gate counts) from a set of Verilog files.
    * This script utilizes the `pyverilog` library for Verilog parsing.
    * The generated CSV file `circuit_features.csv` contains the extracted features.

2.  **Manual Analysis:**
    * Due to the limitations of extracting combinational depth directly from RTL using `pyverilog` in the current implementation, a portion of the dataset was generated manually.
    * This manual generation involved:
        * **Synthesizing Verilog designs** using Yosys on EDA Playground.
        * **Analyzing the generated gate-level netlist diagrams and netlist files** to determine the combinational depth.
        * **Manually counting gates and wires** from the generated netlists.
        * This manual analysis was performed for a subset of the circuits to provide accurate combinational depth labels for training the machine learning model.

**Important Considerations:**

* The manual analysis was performed with the understanding that EDA Playground's synthesis uses generic libraries, and the results might not perfectly match those from a specific ASIC or FPGA technology.
* The manual process is time-consuming and might not be feasible for very large or complex circuits.
* The manual data generation was necessary to provide reliable labels for the target variable (combinational depth) in the absence of a fully automated method.

This combination of automated and manual methods was used to create a dataset suitable for training the machine learning model to predict combinational depth and a very small datasets has been generated due to limitation of TOOLS.
