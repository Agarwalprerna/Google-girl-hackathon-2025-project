# Combinational Depth Prediction from RTL using Machine Learning

This repository contains the code and data for a project focused on predicting the combinational depth of digital circuits directly from Register-Transfer Level (RTL) Verilog code using a Decision Tree Regressor. The goal is to provide an early estimation of circuit timing characteristics, aiding in the identification of potential timing violations before the time-consuming process of synthesis and static timing analysis (STA).

**Key Features:**

* **Verilog Feature Extraction:** Python scripts utilizing the `pyverilog` library to parse Verilog RTL and extract relevant features, including:
    * Module and instance counts
    * Gate counts (AND, OR, XOR, NOT)
    * Fan-in and fan-out
    * Wire counts
* **Machine Learning Model:** Implementation of a Decision Tree Regressor to predict combinational depth based on the extracted features.
* **Data Generation:** A dataset of circuit features and combinational depth labels, generated through a combination of:
    * Automated feature extraction from Verilog files.
    * Manual analysis of gate-level netlists and diagrams produced by Yosys on EDA Playground.
* **Validation:** Methods for validating the predicted combinational depth, including:
    * Comparison with manually determined values.
    * Error metric calculations (MAE, RMSE, R-squared).
  
* **EDA Playground Integration:** Demonstration of using EDA Playground for:
    * RTL simulation and functional verification.
    * Basic synthesis with Yosys.
    * Netlist and diagram generation for manual analysis.


**Goal:**

This project aims to demonstrate the feasibility of using machine learning to predict combinational depth from RTL, offering a valuable tool for early-stage design analysis.

**Data Generation and Manual Analysis:**

The dataset includes manually labeled combinational depth values, as direct extraction from RTL is currently limited. The synthesis results obtained from EDA Playground are based on generic libraries and may not reflect the precise timing of real-world technologies. Manual analysis involved:

* Synthesizing Verilog designs using Yosys on EDA Playground.
* Analyzing the generated gate-level netlist diagrams and netlist files to determine the combinational depth.
* Manually counting gates and wires from the generated netlists.

**Feature Explanation:**

The following features were extracted from the Verilog designs to train the machine learning model:

* **Number of Gates (AND, OR, XOR, NOT):** These features represent the complexity of the circuit's logic implementation. The number and type of gates directly influence the combinational depth.
* **Number of Wires:** The number of wires reflects the connectivity and routing complexity of the circuit. More wires generally indicate more complex interconnections and potentially longer paths.
* **Maximum Fan-in:** The maximum fan-in indicates the maximum number of inputs to any logic gate in the circuit. Higher fan-in can lead to increased gate delays.
* **Maximum Fan-out:** The maximum fan-out indicates the maximum number of gates or modules driven by a single output. Higher fan-out can also lead to increased delays.

**Machine Learning Approach (Decision Tree Regressor):**

A Decision Tree Regressor was chosen for this project due to its simplicity, interpretability, and effectiveness on small datasets.

* **Small Dataset:** The dataset used in this project is relatively small, making complex models like deep neural networks or GNNs less suitable. Decision trees perform well with limited data.
* **Interpretability:** Decision trees provide a clear and understandable representation of the decision-making process. This allows us to analyze the importance of different features in predicting combinational depth.
* **Feature Importance:** Decision trees can provide feature importance scores, which help identify the most influential features.
* **GNN Comparison:** Graph Neural Networks (GNNs) are powerful for graph-structured data and could potentially model the circuit's connectivity. However, GNNs require larger datasets for effective training and are more complex to implement and interpret. Given the small dataset and the need for interpretability, a decision tree was a more practical choice.

**Limitations:**

* The dataset includes manually labeled combinational depth values, as direct extraction from RTL is currently limited.
* The synthesis results obtained from EDA Playground are based on generic libraries and may not reflect the precise timing of real-world technologies.
* The model's accuracy is limited by the size and quality of the training data.

**Future Work:**

* Develop a method for automated combinational depth extraction from RTL.
* Expand the dataset with more diverse circuits and real-world technology libraries.
* Explore other machine learning models, including ensemble methods and neural networks, as the dataset grows.
* Investigate the use of GNNs for modeling circuit connectivity.
