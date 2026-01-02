import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Paths
base_path = Path(__file__).parent.parent
data_path = base_path / 'Data'
code_path = base_path / 'code'
plots_path = base_path / 'plots'

# Load features
features_df = pd.read_csv(data_path / '3.1_time_series_features.csv', index_col=0)

# Feature names with better descriptions
feature_cols = ['mean', 'variance', 'std', 'min', 'max', 'range', 'trend_slope', 'autocov_lag1', 'iqr']
feature_labels = {
    'mean': 'Mean',
    'variance': 'Variance',
    'std': 'Standard Deviation',
    'min': 'Minimum',
    'max': 'Maximum',
    'range': 'Range',
    'trend_slope': 'Trend Slope',
    'autocov_lag1': 'Autocovariance (lag-1)',
    'iqr': 'Interquartile Range'
}

# Create figure with larger titles
fig, axes = plt.subplots(3, 3, figsize=(18, 12))
fig.suptitle('Time Series Feature Distributions', fontsize=18, fontweight='bold', y=0.995)

for idx, col in enumerate(feature_cols):
    row = idx // 3
    col_idx = idx % 3
    ax = axes[row, col_idx]
    
    # Plot histogram
    ax.hist(features_df[col].dropna(), bins=30, edgecolor='black', alpha=0.7, color='steelblue')
    
    # Set title with larger font
    ax.set_title(feature_labels[col], fontsize=14, fontweight='bold', pad=10)
    # X-axis label clarifies these are feature values from ECG signals
    ax.set_xlabel('Feature Value', fontsize=11)
    ax.set_ylabel('Number of Patients', fontsize=11)
    ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.99])
plt.savefig(plots_path / '3.1_features_distribution.jpg', dpi=300, bbox_inches='tight')
print(f"Regenerated plot with clearer labels: {plots_path / '3.1_features_distribution.jpg'}")

