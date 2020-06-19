## Results

Executed with

```python cartpole_difficulty.py > RESULTS_RAW.md```

at commit #a671e01 and cleaned up.

### Random Policy

```
Results for 2000 random trials
	Max reward: 104.0
	Median reward: 19.0
	Mean reward: 22.22
	Stddev reward: 11.88
	Min reward: 8.0

	Nets that do better than 5: 2000 (100.00%)
	Nets that do better than 10: 1886 (94.30%)
	Nets that do better than 15: 1282 (64.10%)
	Nets that do better than 20: 851 (42.55%)
	Nets that do better than 25: 576 (28.80%)
	Nets that do better than 30: 369 (18.45%)
	Nets that do better than 50: 68 (3.40%)
	Nets that do better than 100: 1 (0.05%)
	Nets that do better than 150: 0 (0.00%)
	Perfect nets (200 reward): 0 (0.00%)
```

See also `random-results.png` and `random-results-gt-15.png`.

### Randomly Initialized NN

```
Results for 2000 nn trials
	Max reward: 200.0
	Median reward: 10.0
	Mean reward: 28.50
	Stddev reward: 41.41
	Min reward: 8.0

	Nets that do better than 5: 2000 (100.00%)
	Nets that do better than 10: 731 (36.55%)
	Nets that do better than 15: 605 (30.25%)
	Nets that do better than 20: 541 (27.05%)
	Nets that do better than 25: 505 (25.25%)
	Nets that do better than 30: 462 (23.10%)
	Nets that do better than 50: 328 (16.40%)
	Nets that do better than 100: 130 (6.50%)
	Nets that do better than 150: 75 (3.75%)
	Perfect nets (200 reward): 50 (2.50%)
```

See also `nn-results.png` and `nn-results-gt-15.png`.
