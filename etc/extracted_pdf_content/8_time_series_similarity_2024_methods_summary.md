# Methods Summary: 8_time_series_similarity_2024.pdf

## Preprocessing

### scaling

```
• Most common distortions:
• Offset Translation
• Amplitude Scaling
• Linear Trend
• Noise
```

```
--- Page 13 ---

Transformation II: Amplitude Scaling
0 100 200 300 400 500 600 700 800 900 1000 0 100 200 300 400 500 600 700 800 900 1000
Q = (Q - mean(Q)) / std(Q)
```

```
Removed linear trend,
offset translation,
amplitude scaling

--- Page 15 ---
```

### filtering

```
• data compression
• length
• noise filtering
• left_height
• able to support some interesting non-Euclidean similarity measures (right_height can
```


## Approximation

### SAX

```
--- Page 71 ---

Symbolic Aggregate Approximation (SAX)
• Convert the data into a discrete format, with a small alphabet size.
• A time series T of length n is divided into w equal-sized segments;
```

```
--- Page 72 ---

Symbolic Aggregate Approximation (SAX)
• Once the breakpoints are determined,
baabccbc
```

```
• Dynamic Programming Algorithm Optimization for
Spoken Word Recognition. Hiroaki Sakode et al. 1978.
• Experiencing SAX: a Novel Symbolic Representation of
Time Series. Jessica Line et al. 2009
• Compression-based data mining of sequential data.
```

### Symbolic Aggregate Approximation

```
• Adaptive Piecewise Constant
Approximation Euclidean CDM
• Symbolic Aggregate Approximation

--- Page 62 ---
```

```
--- Page 71 ---

Symbolic Aggregate Approximation (SAX)
• Convert the data into a discrete format, with a small alphabet size.
• A time series T of length n is divided into w equal-sized segments;
```

```
--- Page 72 ---

Symbolic Aggregate Approximation (SAX)
• Once the breakpoints are determined,
baabccbc
```

### PAA

```
--- Page 69 ---

Piecewise Aggregate Approximation (PAA)
• Represent the time series as a sequence of box basis functions
with each box of the same size.
```

```
the values in each segment are then approximated and replaced by
a single coefficient, which is their average.
• Aggregating these w coefficients form the PAA representation of T.
• Next, we determine the breakpoints that divide the distribution
space into ɑ equiprobable regions, where ɑ is the alphabet size
```

```
baabccbc
each region is assigned a symbol.
• The PAA coefficients can then be easily
mapped to the symbols corresponding to
the regions in which they reside.
```

### Piecewise Aggregate Approximation

```
--- Page 69 ---

Piecewise Aggregate Approximation (PAA)
• Represent the time series as a sequence of box basis functions
with each box of the same size.
```

### DFT

```
--- Page 64 ---

Discrete Fourier Transform (DFT)
• Apply a spectral decomposition of a signal
• DTF is a method to decompose functions depending on time into functions
```

```
number of
complete cycles
• DFT extracts different seasonality patterns from a single time series variable
• Example: Given an hourly temperature data set, DFT can detect the presence
of day/night variations and summer/winter variations
```

```
complete cycles
• DFT extracts different seasonality patterns from a single time series variable
• Example: Given an hourly temperature data set, DFT can detect the presence
of day/night variations and summer/winter variations
• it will tell you that those two seasonality (frequencies) are present in
```

### Discrete Fourier Transform

```
--- Page 64 ---

Discrete Fourier Transform (DFT)
• Apply a spectral decomposition of a signal
• DTF is a method to decompose functions depending on time into functions
```

```
--- Page 65 ---

Discrete Fourier Transform (DFT)
• A peak value at 10 Hz with a
magnitude of one while all other
```

```
--- Page 66 ---

Discrete Fourier Transform (DFT)
• Data comprises of 3 different
elementary components with 3
```

### approximation

```
--- Page 54 ---

Fast Approximations to DTW
• Approximate the time series with some compressed or downsampled
representation, and do DTW on the new representation.
```

```
--- Page 55 ---

Fast Approximations to DTW
• There is strong visual evidence to suggests it works well
• In the literature there is good experimental evidence for the utility of
```

```
• Time series can be compressed using
various transformations:
• Piecewise Linear Approximation
• Adaptive Piecewise Constant
Approximation Euclidean CDM
```

### compression

```
--- Page 61 ---

Compression Based Dissimilarity
• Use as features whatever structure a
given compression algorithm finds.
```

```
Compression Based Dissimilarity
• Use as features whatever structure a
given compression algorithm finds.
𝐶(𝑥,𝑦)
• 𝑑 𝑥, 𝑦 = 𝐶𝐷𝑀 𝑥, 𝑦 =
```

```
• Approximation is a special form of Dimensionality
Reduction specifically designed for TSs.
• Approximation vs Compression:
• the approximated space is always understandable
• the compressed space is not necessarily understandable.
```


## Similarity

### DTW

```
--- Page 19 ---

How is DTW Calculated?
Q
• We create a matrix with size of |Q| by
```

```
--- Page 20 ---

How is DTW Calculated?
• The DTW distance can “freely” move
outside the diagonal of the matrix
```

```

How is DTW Calculated?
• The DTW distance can “freely” move
outside the diagonal of the matrix
C
```

### Dynamic Time Warping

```
--- Page 17 ---

Dynamic Time Warping
• Sometimes two time series that are
conceptually equivalent evolve at different
```

```
misalignments in data.
Euclidean.
Dynamic Time Warping.

--- Page 18 ---
```

```
--- Page 49 ---

Dynamic Time Warping – A Real Example
• A Real Example
• This example shows 2 one-
```

### Euclidean

```
--- Page 10 ---

Euclidean Distance
• Given two time series:
• Q = q … q C
```

```
--- Page 11 ---

Problems with Euclidean Distance
• Euclidean distance is very sensitive to “distortions” in the data.
• These distortions are dangerous and should be removed.
```

```

Problems with Euclidean Distance
• Euclidean distance is very sensitive to “distortions” in the data.
• These distortions are dangerous and should be removed.
• Most common distortions:
```

### similarity

```
--- Page 1 ---

Time Series - Similarity, Distances,
Transformations and Clustering

```

```
Problems in Working with Time Series
• Large amount of data.
• Similarity is not easy to estimate.
• Differing data formats.
• Differing sampling rates.
```

```
--- Page 7 ---

Similarity, Distances and
Transformations

```

### distance

```
--- Page 1 ---

Time Series - Similarity, Distances,
Transformations and Clustering

```

```
--- Page 7 ---

Similarity, Distances and
Transformations

```

```
--- Page 10 ---

Euclidean Distance
• Given two time series:
• Q = q … q C
```

### correlation

```
• 1st derivative mean, 1st derivative variance, … Min Value 3 2 5
• parameters of regression, forecasting, Markov model
Autocorrelation 0.2 0.3 0.5
… … … …

```

### alignment

```
Warped Time Axis. Nonlinear
aligned “one to one”. Greatly suffers
alignments are possible. Can correct
from the misalignment in data.
misalignments in data.
```

```
aligned “one to one”. Greatly suffers
alignments are possible. Can correct
from the misalignment in data.
misalignments in data.
Euclidean.
```

```
alignments are possible. Can correct
from the misalignment in data.
misalignments in data.
Euclidean.
Dynamic Time Warping.
```


## Feature Extraction

### mean

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

```
Transformation II: Amplitude Scaling
0 100 200 300 400 500 600 700 800 900 1000 0 100 200 300 400 500 600 700 800 900 1000
Q = (Q - mean(Q)) / std(Q)
C = (C - mean(C)) / std(C)
D(Q,C)
```

### variance

```
• Example of features:
Mean 5.3 6.4 4.8
• mean, variance, skewness, kurtosis,
• 1st derivative mean, 1st derivative variance, … Min Value 3 2 5
• parameters of regression, forecasting, Markov model
```

```
Mean 5.3 6.4 4.8
• mean, variance, skewness, kurtosis,
• 1st derivative mean, 1st derivative variance, … Min Value 3 2 5
• parameters of regression, forecasting, Markov model
Autocorrelation 0.2 0.3 0.5
```

### std

```
Transformation II: Amplitude Scaling
0 100 200 300 400 500 600 700 800 900 1000 0 100 200 300 400 500 600 700 800 900 1000
Q = (Q - mean(Q)) / std(Q)
C = (C - mean(C)) / std(C)
D(Q,C)
```

```
0 100 200 300 400 500 600 700 800 900 1000 0 100 200 300 400 500 600 700 800 900 1000
Q = (Q - mean(Q)) / std(Q)
C = (C - mean(C)) / std(C)
D(Q,C)

```

### min

```
E Mountain Gorilla
S
https://izbicki.me/blog/converting-images-into-time-series-for-data-mining.html

--- Page 19 ---
```

```
(i,j) = cost of best path reaching cell (i,j)
(i-1,j-2) (i-1,j-1) (i-1,j)
= d(q ,c ) + min{ (i-1,j-1), (i-1,j ), (i,j-1) }
i j
(i-2,j-2) (i-2,j-1) (i-2,j)
```

```
--- Page 23 ---

Dynamic Programming Approach
C
Q
```

### max

```
Warping width that achieves
c 85
max Accuracy
a
r FACE 2%
```

```
Feature\Time Series A B C
2. create a feature vector, and
3. use it to measure similarity and/or classify Max Value 11 12 19
• Example of features:
Mean 5.3 6.4 4.8
```

### trend

```

What We Can Do With Time Series?
• Trends, Seasonality • Motif Discovery
10

```

```
Time Series Components
• A given TS consists of three systematic components including level,
trend, seasonality, and one non-systematic component called noise.
• Level: The average value in the series.
• Trend: The increasing or decreasing value in the series.
```

```
trend, seasonality, and one non-systematic component called noise.
• Level: The average value in the series.
• Trend: The increasing or decreasing value in the series.
• Seasonality: The repeating short-term cycle in the series.
• Noise: The random variation in the series.
```

### seasonality

```

What We Can Do With Time Series?
• Trends, Seasonality • Motif Discovery
10

```

```
Time Series Components
• A given TS consists of three systematic components including level,
trend, seasonality, and one non-systematic component called noise.
• Level: The average value in the series.
• Trend: The increasing or decreasing value in the series.
```

```
• Level: The average value in the series.
• Trend: The increasing or decreasing value in the series.
• Seasonality: The repeating short-term cycle in the series.
• Noise: The random variation in the series.
• A systematic component have consistency or recurrence and can be
```


## Key Concepts

- Time Series - Similarity, Distances,
- What is a Time Series? 25.1750
- • A time series is a collection of observations
- Time Series are Ubiquitous
- be seen as time series
- Problems in Working with Time Series
- What We Can Do With Time Series?
- Time Series Components
- • In time series analysis we recognize two
- • Given two time series:
- series, then subtract that line from the time series.
- • Sometimes two time series that are
- two similar time series
- time series.
- shifted points in the two time series
- time series, is a path through the matrix.
- Both time series move
- Only one time series moves
- Dynamic Programming Approach
- Dynamic Programming Approach
- Dynamic Programming Approach
- • Given the following input time series:
- power demand time series.
- • Approximate the time series with some compressed or downsampled
- the approach on clustering, classification, etc.
- • For long time series, shape-based similarity give
- 1. extract global features from the time series,
- Feature\Time Series A B C
- • Time series can be compressed using
- Time Series Approximation
- Time Series Approximation
- • DFT extracts different seasonality patterns from a single time series variable
- • Represent the time series as a sequence of straight lines.
- used to represent a particular time series.
- • Represent the time series as a sequence of box basis functions
- dividing the time series into M equi-sized ``frames’’.
- • A time series T of length n is divided into w equal-sized segments;
- Summary of Time Series Similarity
- • If you have short time series
- • If you have long time series
- Summary of Time Series Representation
- Clustering Time Series
- • It is based on the similarity between time series.
- • The two general methods of time series clustering are
- Types of Time Series Clustering
- objects. Given a set of individual time series data, the objective is to
- group similar time series into the same cluster.
- • Features-based clustering: extract features, or time series motifs (see
- next lectures) as the features and use them to cluster time series.
- • Compression-based clustering: compress time series and run

