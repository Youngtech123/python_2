# Importing the libraries we need
# pandas is for handling the dataset (loading, cleaning, analyzing)
# matplotlib is for drawing the graphs
import pandas as pd
import matplotlib.pyplot as plt


# Task 1: Load and Explore Dataset

try:
    df = pd.read_csv("iris.csv")
except FileNotFoundError:
    print("The file was not found. Please check the filename or path.")
    raise

# Look at the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Check the structure of the dataset: column names, data types, missing values
print("\nInfo about the dataset:")
print(df.info())

# Check if there are missing values in the dataset
print("\nMissing values in each column:")
print(df.isnull().sum())

df = df.dropna()


# Task 2: Basic Data Analysis

# Get summary statistics of all numeric columns
print("\nSummary statistics of numeric columns:")
print(df.describe())

# Group data by species and calculate mean of numeric columns
print("\nAverage values for each species:")
print(df.groupby("species").mean())

# Task 3: Data Visualization

# 1. Line chart
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="blue")
plt.title("Sepal Length Trend (Row Index as Time)")
plt.xlabel("Index (row number)")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart: average petal length per species
species_means = df.groupby("species")["petal_length"].mean()
plt.figure(figsize=(6, 5))
species_means.plot(kind="bar", color=["red", "green", "blue"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: distribution of sepal width
plt.figure(figsize=(6, 5))
plt.hist(df["sepal_width"], bins=15, color="purple", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: sepal length vs petal length
plt.figure(figsize=(6, 5))
plt.scatter(df["sepal_length"], df["petal_length"], color="orange")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
