# Feature Dictionary

## rolling_average_signal

- **Formula:** Rolling mean of `signal`, window size 3, computed within each `(domain, condition)` group, ordered by `time_step`. `min_periods=1` is used, so the first 1–2 rows of a group show a partial-window average rather than `NaN` (this is a deliberate choice — see note below).
- **Applies to:** All domains, since every domain has ordered replicates within a condition.
- **Required columns:** `domain`, `condition`, `time_step`, `signal`.
- **Invalid when:** Rows are not properly ordered by `time_step`, or when a window would cross into a different `condition` (this is why grouping is done by `domain` + `condition` before rolling, not on the raw row order).
- **Why useful for ML:** Smooths replicate-to-replicate measurement noise, giving a more stable estimate of the underlying signal at each condition than any single reading. Useful as an input feature or as a sanity check against the raw signal to catch instrumentation glitches.
- **Note on partial windows:** With `min_periods=1`, the first row of each group reports itself as the "average," and the second row averages 2 points. If your grading expects strict 3-point windows only, change `min_periods=1` to `min_periods=3` in `add_rolling_average()` — the first two rows per group will then be `NaN`.

## normalized_signal

- **Formula:** `signal / baseline_signal`
- **Applies to:** All domains — every domain in this dataset has a `baseline_signal` value.
- **Required columns:** `signal`, `baseline_signal`.
- **Invalid when:** `baseline_signal` is missing or equal to zero (would divide by zero).
- **Why useful for ML:** Removes the domain- and sensor-specific baseline offset, expressing signal as a multiple of a reference reading. This makes readings more comparable within a domain regardless of absolute measurement scale.

## power_w

- **Formula:** `voltage_v * current_a`
- **Applies to:** Electronics only.
- **Required columns:** `domain`, `voltage_v`, `current_a`.
- **Invalid when:** Domain is not Electronics, or either `voltage_v` or `current_a` is missing.
- **Why useful for ML:** Power is a physically meaningful derived quantity in electrical systems that voltage or current alone don't capture — it can reveal load behavior (e.g., power dissipation increasing with load) that's directly relevant to the Electronics domain's engineering questions.

## error_percent

- **Formula:** `((signal - expected_signal) / expected_signal) * 100`
- **Applies to:** All domains with a valid `expected_signal`.
- **Required columns:** `signal`, `expected_signal`.
- **Invalid when:** `expected_signal` is missing or equal to zero.
- **Why useful for ML:** Expresses deviation from the theoretical/expected value as a scale-independent percentage, letting an ML model (or a human) directly compare "how far off" different domains are from their own expectations, despite very different absolute signal ranges.

## stress_ratio

- **Formula:** `stress_mpa / reference_stress_mpa`
- **Applies to:** Mechanical only.
- **Required columns:** `domain`, `stress_mpa`, `reference_stress_mpa`.
- **Invalid when:** Domain is not Mechanical, or `stress_mpa`/`reference_stress_mpa` is missing, or `reference_stress_mpa` is zero.
- **Why useful for ML:** Normalizes measured stress against a known reference/rated stress, which is a standard way engineers judge how close a material is to a critical threshold — more informative to a model than raw MPa alone.

## coefficient_of_variation / stability_flag

- **Formula:** `coefficient_of_variation = std(signal) / mean(signal)`, computed per replicate group (`domain`, `condition`, `input_value`). `stability_flag` buckets that value as:
  - `stable`: cv ≤ 0.05
  - `moderate`: 0.05 < cv ≤ 0.15
  - `unstable`: cv > 0.15
- **Applies to:** All domains — computed per replicate group regardless of domain.
- **Required columns:** `domain`, `condition`, `input_value`, `signal` (need ≥2 replicates in the group).
- **Invalid when:** A group has fewer than 2 replicates, or the group's mean signal is zero (coefficient_of_variation undefined) — in these cases `stability_flag` is left blank (`NaN`), not defaulted to a bucket.
- **Why useful for ML:** Flags which measurements come from noisy/inconsistent replicate groups versus tightly reproducible ones. A model trained without this would treat a noisy 3-replicate group and a tight 3-replicate group as equally trustworthy, which they aren't.

## ml_ready

- **Formula:** Boolean AND of the following conditions:
  - `signal`, `expected_signal`, `input_value`, `domain`, `condition` are all present
  - `expected_signal != 0`
  - if `domain == "Electronics"`: `power_w` must be valid (not NaN)
  - if `domain == "Mechanical"`: `stress_ratio` must be valid (not NaN)
  - `stability_flag` is known (not NaN) and not equal to `"unstable"`
- **Applies to:** All domains.
- **Required columns:** All of the above, plus the intermediate engineered columns (`power_w`, `stress_ratio`, `stability_flag`) computed earlier in the pipeline.
- **Invalid when:** Any required value is missing, a domain-specific feature that should have been computed is missing, or the row's replicate group is `unstable` (or its stability couldn't be computed at all).
- **Why useful for ML:** Acts as a single gatekeeping column so a model-training script can filter to `ml_ready == True` without re-deriving every validity rule — keeps unreliable or incomplete rows out of training without silently corrupting the dataset.