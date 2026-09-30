import seaborn as sns
from scipy import stats

# Always visualize first
sns.histplot(df['revenue'], kde=True)

# T-test for means, chi-square for categories
t_stat, p_value = stats.ttest_ind(control, variant)
