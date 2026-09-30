import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Control vs variant, N=1000 each
# Conversion 5% vs 5.8%
count = np.array([58, 50])
nobs = np.array([1000, 1000])
z, p = proportions_ztest(count, nobs)
print(f"p-value: {p:.4f}")  # -> 0.42 -> NOT significant
