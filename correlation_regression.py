import statsmodels.api as sm

# Correlation
df[['ad_spend', 'revenue']].corr()

# Regression
X = sm.add_constant(df['ad_spend'])
model = sm.OLS(df['revenue'], X).fit()
print(model.summary())
