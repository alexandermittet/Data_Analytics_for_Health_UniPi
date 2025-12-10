#!/bin/bash
# Script to create conda environment "DAD" with all required packages

# Create conda environment with Python 3.9
conda create -n DAD python=3.9 -y

# Activate the environment
source $(conda info --base)/etc/profile.d/conda.sh
conda activate DAD

# Install packages via conda (faster and more reliable for scientific packages)
conda install -y \
    numpy=1.24.4 \
    pandas=2.2.3 \
    matplotlib=3.8.3 \
    seaborn=0.13.2 \
    scipy \
    scikit-learn \
    jupyter \
    ipykernel

# Install packages via pip (for packages not available in conda)
pip install pdfplumber==0.11.0

# Install jupyter kernel for the environment
python -m ipykernel install --user --name DAD --display-name "Python (DAD)"

echo "✓ Conda environment 'DAD' created successfully!"
echo "To activate: conda activate DAD"
echo "To use in Jupyter: Select kernel 'Python (DAD)'"


