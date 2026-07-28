# Multidimensional Scaling (MDS) using Scikit-learn

## Overview

This project demonstrates **Multidimensional Scaling (MDS)**, a dimensionality reduction technique that projects high-dimensional data into a lower-dimensional space while preserving the pairwise distances between data points as much as possible.

The project contains **two examples**:
1. **MDS on the Scikit-learn Digits Dataset** (real-world dataset)
2. **MDS on a Synthetic Blob Dataset** generated using `make_blobs()`

Both examples reduce the original data to **2 dimensions** for visualization using Matplotlib.

---

## Features

- Demonstrates Multidimensional Scaling (MDS)
- Works with both real-world and synthetic datasets
- Reduces high-dimensional data to two dimensions
- Visualizes the transformed data using scatter plots
- Prints the original and reduced dataset dimensions

---

## Technologies Used

- Python 3.x
- NumPy
- Matplotlib
- Scikit-learn

---

## Installation

Install the required libraries:

```bash
pip install numpy matplotlib scikit-learn
```

---

## Project Structure

```
MDS-Dimensionality-Reduction/
│
├── mds_digits.py        # MDS on the Digits dataset
├── mds_blobs.py         # MDS on a synthetic dataset
├── README.md
└── requirements.txt
```

---

## Example 1: MDS on the Digits Dataset

### Dataset

The Digits dataset is a built-in Scikit-learn dataset containing handwritten digit images.

- Samples: **1797**
- Features: **64**
- Classes: **10 (Digits 0–9)**

### Workflow

1. Load the Digits dataset.
2. Extract feature matrix (`X`) and labels (`y`).
3. Apply MDS with `n_components = 2`.
4. Transform the data into two dimensions.
5. Visualize the reduced data using a coloured scatter plot.

### Expected Output

```
Original Dimension of X = (1797, 64)
Dimension of X after MDS = (1797, 2)
```

A coloured scatter plot is displayed where each colour represents a digit class (0–9).

---

## Example 2: MDS on a Synthetic Blob Dataset

### Dataset

The dataset is generated using Scikit-learn's `make_blobs()` function.

Parameters:
- Samples: **100**
- Features: **3**
- Cluster Centres: **2**
- Random State: **42**

### Workflow

1. Generate a synthetic dataset.
2. Apply MDS with `n_components = 2`.
3. Transform the data into two dimensions.
4. Visualize the transformed data using a scatter plot.

### Expected Output

```
Original Dimension of X = (100, 3)
Dimension of X after MDS = (100, 2)
```

A 2D scatter plot displays the reduced representation of the generated data.

---

## How MDS Works

1. Computes the pairwise distances between all data points.
2. Finds a lower-dimensional representation that preserves these distances as closely as possible.
3. Produces a lower-dimensional dataset suitable for visualization and exploratory analysis.

---

## Advantages of MDS

- Preserves pairwise distances between data points.
- Useful for visualizing high-dimensional datasets.
- Helps identify patterns and clusters.
- Applicable to both real-world and synthetic datasets.
- Easy to implement using Scikit-learn.

---

## Limitations

- Computationally expensive for large datasets.
- Slower than PCA for high-dimensional data.
- Results may vary depending on initialization.
- Primarily intended for visualization rather than feature extraction.

---

## Future Improvements

- Compare MDS with PCA, t-SNE, and UMAP.
- Visualize data in three dimensions (`n_components = 3`).
- Experiment with different distance metrics.
- Apply MDS to larger real-world datasets.
- Add cluster colouring to the synthetic dataset visualization.

---

## Conclusion

This project demonstrates the application of **Multidimensional Scaling (MDS)** on both a real-world dataset (Digits) and a synthetic dataset (Blobs). It illustrates how MDS effectively reduces data dimensionality while preserving the relationships between samples, making it a valuable technique for data visualization and exploratory data analysis.

---

## License

This project is intended for educational and learning purposes.