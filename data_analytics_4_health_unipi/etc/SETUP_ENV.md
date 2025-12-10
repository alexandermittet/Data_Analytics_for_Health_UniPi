# Setting up Conda Environment "DAD"

This guide explains how to create and use the conda environment for the Data Analytics for Digital Health project.

## Method 1: Using environment.yml (Recommended)

```bash
cd data_analytics_4_health_unipi
conda env create -f environment.yml
conda activate DAD
```

## Method 2: Using the setup script

```bash
cd data_analytics_4_health_unipi
bash setup_conda_env.sh
conda activate DAD
```

## Method 3: Manual setup

```bash
# Create environment
conda create -n DAD python=3.9 -y

# Activate environment
conda activate DAD

# Install packages
conda install -y numpy=1.24.4 pandas=2.2.3 matplotlib=3.8.3 seaborn=0.13.2 scipy scikit-learn jupyter ipykernel
pip install pdfplumber==0.11.0

# Install Jupyter kernel
python -m ipykernel install --user --name DAD --display-name "Python (DAD)"
```

## Using the environment

### Activate the environment:
```bash
conda activate DAD
```

### Use in Jupyter Notebook:
1. Start Jupyter: `jupyter notebook` or `jupyter lab`
2. In your notebook, go to Kernel → Change Kernel → Select "Python (DAD)"

### Deactivate when done:
```bash
conda deactivate
```

## Installed Packages

- **numpy** (1.24.4): Numerical computing
- **pandas** (2.2.3): Data manipulation and analysis
- **matplotlib** (3.8.3): Plotting and visualization
- **seaborn** (0.13.2): Statistical data visualization
- **scipy**: Scientific computing (for time series analysis)
- **scikit-learn**: Machine learning tools
- **jupyter**: Jupyter notebook environment
- **ipykernel**: Jupyter kernel for Python
- **pdfplumber** (0.11.0): PDF text extraction

## Troubleshooting

If conda is not found:
1. Make sure conda/miniconda/anaconda is installed
2. Initialize conda: `conda init bash` (or `conda init zsh` for zsh)
3. Restart your terminal
4. Or source conda: `source ~/miniconda3/etc/profile.d/conda.sh` (adjust path as needed)


