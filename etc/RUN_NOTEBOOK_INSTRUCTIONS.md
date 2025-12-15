# Running the Time Series Notebook

Your conda installation seems to have some issues. Here are several ways to run the notebook:

## Option 1: Fix Conda and Use Environment (Recommended)

1. **Fix conda installation** (if needed):
   ```bash
   # Reinstall conda or fix the installation
   # Or use mamba instead: brew install mambaforge
   ```

2. **Create the environment**:
   ```bash
   cd data_analytics_4_health_unipi
   conda env create -f environment.yml
   ```

3. **Activate and run**:
   ```bash
   conda activate DAD
   jupyter notebook
   # Then open: code/3.1 timeseries alex.ipynb
   ```

## Option 2: Use pip with Current Python

If conda is not working, install packages with pip:

```bash
cd data_analytics_4_health_unipi
pip3 install numpy==1.24.4 pandas==2.2.3 matplotlib==3.8.3 seaborn==0.13.2 scipy scikit-learn jupyter pdfplumber==0.11.0
jupyter notebook
```

## Option 3: Run as Python Script

I've created a Python script version that you can run directly:

```bash
cd data_analytics_4_health_unipi
python3 code/run_timeseries_analysis.py
```

## Option 4: Use the Run Script

Try the automated script:

```bash
cd data_analytics_4_health_unipi
bash run_notebook.sh
```

---

**Note**: If you're using VS Code or another IDE, you can:
1. Open the notebook file
2. Select the Python interpreter/kernel
3. Run cells individually


