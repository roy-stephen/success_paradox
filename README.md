# The Luck Factor: How Much Does Chance Impact Success?

This project explores the role of luck in success through simulations of a selection process, inspired by a Veritasium video (link to video if available). We analyze how the impact of luck varies depending on the selection ratio (number of selected applicants relative to total applicants) and the weight given to luck in the selection process.

## Project Overview

We often attribute success solely to hard work, talent, and perseverance. However, this project demonstrates that luck plays a significant, often underestimated role, especially in highly competitive environments. We use a simplified model of a selection process, similar to astronaut selection, where both skill and luck contribute to the final outcome.

## Key Findings

*   **The Impact of Luck is Not Constant:** Luck's influence is significantly amplified in highly competitive scenarios with low selection ratios.
*   **Luck Weight Matters:** Increasing the weight given to luck directly increases its overall impact.
*   **The Success Paradox:** We must believe we are in control to strive for success, yet we must also acknowledge the significant role of luck.

## Project Structure

The project consists of the following components:

*   **`app.py`:** A Streamlit web application that allows users to interactively explore the simulation by varying parameters and visualizing the results.
*   **`analysis.ipynb`:** A Jupyter Notebook that provides a detailed walkthrough of the analysis, including code, explanations, and visualizations.
*   **`README.md`:** This file, providing an overview of the project.

## How to Run

### Web App (Streamlit)

1.  Make sure you have Python and pip installed.
2.  Install the required Python packages:

    ```bash
    pip install streamlit numpy pandas matplotlib seaborn scipy plotly
    ```

3.  Navigate to the project directory in your terminal.
4.  Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5.  Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

### Jupyter Notebook

1.  Make sure you have Jupyter Notebook or JupyterLab installed.
2.  Install the required Python packages (as listed above).
3.  Navigate to the project directory in your terminal.
4.  Launch Jupyter Notebook or JupyterLab:

    ```bash
    jupyter notebook  # or jupyter lab
    ```

5.  Open the `analysis.ipynb` notebook.

## Interactive Visualization

The Streamlit web app (`app.py`) provides an interactive interface to explore the simulation. You can adjust the following parameters:

*   **Number of Applicants:** The total number of applicants.
*   **Number Selected:** The number of applicants to be selected.
*   **Luck Weight:** The weight given to luck in the selection process.
*   **Number of Simulations:** The number of simulation runs.
*   **Distribution:** The distribution used to generate skill and luck scores (uniform or normal).
*   **Mean (loc):** The mean of the normal distribution (if selected).
*   **Standard Deviation (scale):** The standard deviation of the normal distribution (if selected).

The app displays key statistics and visualizations, allowing you to see how the impact of luck changes with different parameter values.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or improvements, please open an issue or submit a pull request.
