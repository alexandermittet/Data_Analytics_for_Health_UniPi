# Methods Summary: 5-data-understanding_ts.pdf

## Preprocessing

### pre-process

```

Data Understanding
and pre-processing
Time Series
Anna Monreale and Francesca Naretto
```

```
Time series analysis
To analyze and compare different time series,
we first need to pre-process them such that
they have all the same format.
3
```

```
TS: why all of these statistics?
Before the application of any statistical model to TS, we need to
analyze and pre-process them so that we can have stationary
data.
Stationary: consistent means, variance and covariance over
```

### scaling

```
• Most common distortions:
• Offset Translation
• Amplitude Scaling
• Linear Trend
• Noise
```

```
--- Page 18 ---

Amplitude scaling
Objective: compare inherent patterns in different TS independently of their magnitudes.
Normalize the amplitude: divide by the standard deviation of the TS.
```

```
Removed linear trend,
offset translation,
amplitude scaling

--- Page 29 ---
```


## Approximation


## Similarity

### Euclidean

```

Time series analysis
• Often we need to employ Euclidean distance to
analyze/compare time series. Euclidean distance is
very sensitive to “distortions” in the data.
```

```
Time series analysis
• Often we need to employ Euclidean distance to
analyze/compare time series. Euclidean distance is
very sensitive to “distortions” in the data.
• These distortions are dangerous and should be
```

### similarity

```
Time series characteristics
• Large amount of data.
• Similarity is not easy to estimate.
• Different data formats.
• Different sampling rates.
```

### distance

```

Time series analysis
• Often we need to employ Euclidean distance to
analyze/compare time series. Euclidean distance is
very sensitive to “distortions” in the data.
```

```
Time series analysis
• Often we need to employ Euclidean distance to
analyze/compare time series. Euclidean distance is
very sensitive to “distortions” in the data.
• These distortions are dangerous and should be
```


## Feature Extraction

### mean

```

Time series statistics
• Mean: the expected value of the time series
• Variance: variance of the time series
• Trends: the slope of a linear model that models the
```

```
0 0
0 50 100 150 200 250 300 0 50 100 150 200 250 300
Q = Q - mean(Q)
C = C - mean(C)
D(Q,C)
```

```
0 50 100 150 200 250 300 0 50 100 150 200 250 300
Q = Q - mean(Q)
C = C - mean(C)
D(Q,C)
0 50 100 150 200 250 300
```

### variance

```
Time series statistics
• Mean: the expected value of the time series
• Variance: variance of the time series
• Trends: the slope of a linear model that models the
time series behavior
```

```
--- Page 23 ---

TS: sliding statistics – auto-covariance
How much does a component of a TS correlate with the
previous and future components?
```

```
How much does a component of a TS correlate with the
previous and future components?
How to: compute the covariance between two components of
the TS using the formula:
High auto-covariance may
```

### std

```
0 100 200 300 400 500 600 700 800 900 1000
0 100 200 300 400 500 600 700 800 900 1000
Q = (Q - mean(Q)) / std(Q)
C = (C - mean(C)) / std(C)
D(Q,C)
```

```
0 100 200 300 400 500 600 700 800 900 1000
Q = (Q - mean(Q)) / std(Q)
C = (C - mean(C)) / std(C)
D(Q,C)

```

```
called window.
Given a window, each locality can now be described.
Examples are: rolling mean, rolling std etc.

--- Page 20 ---
```

### min

```
Anna Monreale and Francesca Naretto
Computer Science Department
Introduction to Data Mining, 2nd Edition
Chapter 1 & Data Exploration (Additional Resources)

```

```

Also for time series: know your data
• For preparing data for data mining task it is essential
to have an overall understanding of your data
• Gain insight in your data
```

### trend

```

Time series understanding
1. Look for trends
2. Check for seasonality, cyclicity, irregularities
3. Look for noise
```

```
• Mean: the expected value of the time series
• Variance: variance of the time series
• Trends: the slope of a linear model that models the
time series behavior
• Interquartile ranges: check the distributions
```

```
--- Page 12 ---

Trend
It is a long-term movement of the time series. It is non repeating.
Technically, it is a slope 𝑑𝑒𝑙𝑡𝑎 of a linear model, modelling the time
```

### seasonality

```
Time series understanding
1. Look for trends
2. Check for seasonality, cyclicity, irregularities
3. Look for noise

```

```
--- Page 13 ---

Seasonality
It is a regular periodic occurrence within a time
interval, usually smaller than a year.
```

```
the TS using the formula:
High auto-covariance may
indicate seasonality

--- Page 24 ---
```


## Key Concepts

- Time Series
- Also for time series: know your data
- Time series
- A univariate series x is a sequence of values
- A multivariate time series x is a sequence that
- comprised of multiple time series, each representing a
- time series
- Time series characteristics
- Time series understanding
- Time series statistics
- • Mean: the expected value of the time series
- • Variance: variance of the time series
- time series behavior
- It is a long-term movement of the time series. It is non repeating.
- Time series analysis
- To analyze and compare different time series,
- Time series analysis
- analyze/compare time series. Euclidean distance is
- The time series may be huge. Analyzing it in its entirety may be
- time series, then subtract that line from the time series.

