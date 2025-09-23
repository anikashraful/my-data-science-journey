import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file
df = pd.read_csv('data.csv')  # Replace with your CSV filename

# Step 2: Display summary statistics for numeric columns
print("\nSummary Statistics:\n", df.describe())
for col in df.select_dtypes(include='number').columns:
    print(f"\nColumn: {col}")
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Min:", df[col].min())
    print("Max:", df[col].max())

# Step 3: Generate Histograms for each numeric column
for col in df.select_dtypes(include='number').columns:
    plt.figure()
    df[col].hist(bins=20)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# Step 4: Scatter plot of first two numeric columns (if more than one exists)
num_cols = df.select_dtypes(include='number').columns
if len(num_cols) > 1:
    plt.figure()
    plt.scatter(df[num_cols[0]], df[num_cols[1]])
    plt.xlabel(num_cols[0])
    plt.ylabel(num_cols[1])
    plt.title(f'Scatter Plot of {num_cols[0]} vs {num_cols[1]}')
    plt.show()
