import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 75000, 100000]
}

# Convert to DataFrame
df = pd.DataFrame(data)
print("Dataset:\n", df)

# Plot the data
plt.plot(df['Age'], df['Salary'], marker='o')
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
