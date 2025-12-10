# Time Series Analysis Methods - Course Recommendations

This document summarizes the time series analysis methods and approaches recommended in the course slides for Task 3.

## Overview

Based on the course slides (`8_time_series_similarity_2024.pdf` and `5-data-understanding_ts.pdf`), the following methods and workflow are recommended for time series analysis.

## Recommended Workflow

### 1. Preprocessing (MANDATORY)

Before any time series analysis, the following preprocessing steps should be applied:

#### a) Offset Translation Removal
- **Objective**: Remove mean offset to compare shapes, not absolute values
- **Method**: `Q = Q - mean(Q)`
- **When to use**: Always as first step

#### b) Amplitude Scaling
- **Objective**: Normalize amplitude to compare inherent patterns independently of magnitude
- **Method**: `Q = (Q - mean(Q)) / std(Q)`
- **When to use**: When comparing time series with different scales/magnitudes

#### c) Linear Trend Removal
- **Objective**: Remove linear trends that can distort similarity measures
- **Method**: Fit best-fitting straight line, then subtract it from the time series
- **When to use**: When time series show clear upward or downward trends

#### d) Noise Filtering
- **Objective**: Remove noise to reveal underlying patterns
- **Method**: Moving Average (MA) smoothing
  - Formula: `t_i = (1/w) * Σ(t_j)` for j from i-w/2 to i+w/2
  - Window size `w` should be chosen based on data characteristics
- **When to use**: When time series contain significant noise

### 2. Time Series Approximation Methods

The course emphasizes several approximation techniques for dimensionality reduction:

#### a) Piecewise Aggregate Approximation (PAA)
- **Purpose**: Represent time series as sequence of box basis functions
- **Method**: 
  - Divide time series T of length n into w equal-sized segments
  - Replace values in each segment with their average
  - Results in w coefficients representing the original series
- **Use case**: Compression and dimensionality reduction before similarity computation

#### b) Symbolic Aggregate Approximation (SAX)
- **Purpose**: Convert time series to discrete symbolic representation
- **Method**:
  - First apply PAA to get w coefficients
  - Determine breakpoints that divide distribution into α equiprobable regions (α = alphabet size)
  - Map PAA coefficients to symbols based on which region they fall into
  - Result: String representation (e.g., "baabccbc")
- **Use case**: Discrete representation for pattern matching and clustering

#### c) Discrete Fourier Transform (DFT)
- **Purpose**: Spectral decomposition to extract frequency components
- **Method**: Decompose time-dependent functions into frequency components
- **Use case**: 
  - Detect seasonality patterns
  - Extract different frequency components from single time series
  - Example: Detect day/night and seasonal variations in hourly temperature data
- **Advantage**: Fast algorithms exist (O(n log n))

### 3. Similarity Measures

#### a) Euclidean Distance
- **Formula**: `D(Q,C) = sqrt(Σ(q_i - c_i)²)`
- **Limitation**: Very sensitive to distortions (offset, scaling, trends, noise)
- **When to use**: Only after applying all necessary preprocessing transformations
- **Note**: Course emphasizes that preprocessing is essential before using Euclidean distance

#### b) Dynamic Time Warping (DTW)
- **Purpose**: Handle time series that evolve at different speeds or have misalignments
- **Method**: 
  - Uses dynamic programming approach
  - Allows non-linear alignments between time series
  - Creates matrix of size |Q| × |C| with distances between all point pairs
- **Advantage**: Can correct misalignments that Euclidean distance cannot handle
- **Use case**: When time series have similar shapes but different timing/phase shifts

### 4. Feature Extraction

Statistical features that can be extracted from time series:

- **Mean**: Expected value of the time series
- **Variance**: Variance of the time series
- **Standard Deviation**: Used in normalization
- **Min/Max**: Extreme values
- **Trend**: Slope of linear model fitting the time series
- **Seasonality**: Repeating short-term cycles
- **Auto-covariance**: Correlation between components at different time lags
- **Rolling statistics**: Rolling mean, rolling std within a window

## Recommended Approach for Task 3

Based on the project requirements and course materials:

### Step 1: Create Univariate Time Series per Patient
- Create one time series for each `subject_id`
- Each series should represent one specific type of information at a time
- Use `charttime` as the timestamp
- Suggested data sources:
  - Laboratory values (e.g., glucose, troponin) over time
  - Diagnostic codes (ICD codes) over time from heart_diagnoses
  - Microbiology events over time

### Step 2: Preprocessing
Apply the following preprocessing steps in order:
1. **Offset Translation**: Remove mean (`Q = Q - mean(Q)`)
2. **Amplitude Scaling**: Normalize by standard deviation (`Q = (Q - mean(Q)) / std(Q)`)
3. **Linear Trend Removal**: If trends are present, remove them
4. **Noise Filtering**: Apply moving average if noise is significant

### Step 3: Choose Analysis Approach

#### Option A: Approximation Approach
- Apply **PAA** or **SAX** to compress/approximate the time series
- Use the approximated representation for further analysis
- Benefits: Dimensionality reduction, faster computation

#### Option B: Feature Extraction Approach
- Extract statistical features (mean, variance, std, min, max, trend, seasonality)
- Use features as representation of the time series
- Benefits: Fixed-size representation, interpretable features

#### Option C: Hybrid Approach
- Apply approximation (PAA/SAX) first
- Then extract features from the approximated series
- Combine with statistical features from original series

### Step 4: Similarity Analysis (if needed)
- Use **Euclidean distance** after preprocessing for shape-based similarity
- Use **DTW** if time series have phase shifts or different speeds
- Consider fast approximations to DTW using compressed representations

## Key Points from Course Materials

1. **Preprocessing is essential**: Euclidean distance is very sensitive to distortions and requires proper preprocessing
2. **Univariate focus**: Course emphasizes working with univariate time series (one variable at a time)
3. **Short series are OK**: The project notes that series can be short - focus on consistency rather than length
4. **Multiple approaches**: Course presents both approximation and feature extraction as valid approaches
5. **Stationarity**: Before applying statistical models, time series should be preprocessed to achieve stationarity (consistent means, variance, and covariance over time)

## Implementation Recommendations

For the project implementation:

1. **Start simple**: Begin with basic preprocessing (offset removal, scaling)
2. **Visualize**: Plot time series before and after preprocessing to verify transformations
3. **Choose one method**: Either use approximation (PAA/SAX) OR feature extraction, not necessarily both
4. **Document decisions**: Explain why you chose specific preprocessing steps and methods
5. **Link to tabular data**: Use diagnostic codes and other tabular information to enrich time series analysis

## Libraries to Consider

- **tslearn**: For DTW, time series clustering
- **pyts**: For SAX, PAA, and other transformations
- **scipy**: For DFT (fft functions)
- **pandas**: For time series manipulation and rolling statistics
- **numpy**: For basic operations and transformations


