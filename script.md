# VIDEO 4: Quantitative Techniques — FULL SCRIPT (8 min)

## [0:00–0:45] HOOK
"Averages lie. Medians hide. And p-values fool even senior analysts. Today I'm showing you the quantitative techniques that actually drive decisions — from descriptive stats to A/B testing."

## [0:45–2:30] DESCRIPTIVE STATS
"Mean, median, mode — but also variance, standard deviation, and percentiles." See `descriptive_stats.py`.

"Why percentiles matter — P95 tells you the experience of your top users. The mean hides that."

## [2:30–4:00] DISTRIBUTIONS & TESTING
"Always visualize first." Then test: T-test for means, chi-square for categories. See `distributions_testing.py`.

## [4:00–5:30] CORRELATION & REGRESSION
"Correlation is not causation. But it's a starting point." See `correlation_regression.py`.

## [5:30–7:00] A/B TEST WALKTHROUGH
Real example. Control vs variant. N=1000 each. Conversion 5% vs 5.8%. Is it significant?
See `ab_test.py` — "This is the trap. It looks like a lift, but p = 0.42. Don't ship it."

## [7:00–8:00] RECAP
"Visualize. Test. Check effect size. Never trust a single number. Full notebooks in the repo."
