#!/bin/bash
# Script to run the time series notebook with conda environment DAD

cd "$(dirname "$0")"

echo "Setting up and running notebook with DAD environment..."
echo ""

# Try to find and initialize conda
if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
    source "$HOME/miniconda3/etc/profile.d/conda.sh"
elif [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
    source "$HOME/anaconda3/etc/profile.d/conda.sh"
elif [ -f "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh" ]; then
    source "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh"
else
    echo "Warning: Could not find conda initialization script"
    echo "Please initialize conda manually or install it"
    exit 1
fi

# Create environment if it doesn't exist
if ! conda env list | grep -q "^DAD "; then
    echo "Creating DAD environment..."
    conda env create -f environment.yml
fi

# Activate environment
echo "Activating DAD environment..."
conda activate DAD

# Check if jupyter is available
if ! command -v jupyter &> /dev/null; then
    echo "Installing jupyter in DAD environment..."
    conda install -y jupyter ipykernel
fi

# Run the notebook
echo "Running notebook: 3.1 timeseries alex.ipynb"
echo ""
jupyter nbconvert --to notebook --execute "code/3.1 timeseries alex.ipynb" --output "3.1 timeseries alex_executed.ipynb"

echo ""
echo "✓ Notebook execution complete!"
echo "Output saved to: code/3.1 timeseries alex_executed.ipynb"


