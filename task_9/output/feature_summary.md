# Feature Engineering Summary

## Which features are general across all domains?

- `rolling_average_signal` — computed within every `(domain, condition)` group.
- `normalized_signal` — every domain in this dataset has a valid `baseline_signal`.
- `error_percent` — every domain has a valid `expected_signal`.
- `coefficient_of_variation` / `stability_flag` — computed per replicate group regardless of domain.
- `ml_ready` — computed for every row, domain-agnostic gatekeeper column.

## Which features are domain-specific?

- `power_w` — Electronics only (requires `voltage_v`, `current_a`, which only Electronics rows have).
- `stress_ratio` — Mechanical only (requires `stress_mpa`, `reference_stress_mpa`, which only Mechanical rows have).

Biochem has no domain-exclusive engineered feature in this set — it relies entirely on the general features above.

## Which rows are not ML-ready and why?

In this dataset, **all 27 rows come out `ml_ready = True`**. This is a real result of running the pipeline, not an oversight — every replicate group has all required base values, Electronics rows all have valid `power_w`, Mechanical rows all have valid `stress_ratio`, and even the noisiest replicate group (Mechanical, high_load: coefficient_of_variation ≈ 0.101, driven by the M009 outlier) still falls in the `moderate` bucket rather than crossing the 0.15 `unstable` threshold.

That means this particular dataset is "too clean" to demonstrate a rejected row. To show what *would* disqualify a row under this pipeline:
- A row with `expected_signal` missing or 0 → fails the base-validity check.
- An Electronics row missing `current_a` → `power_w` is NaN → fails the domain-feature check even if everything else is fine.
- A replicate group whose coefficient_of_variation exceeds 0.15 (e.g., if M009's signal had been 2.5 mm instead of 2.10 mm, pushing the high-load Mechanical group's CV over 0.15) → `stability_flag = "unstable"` → all rows in that group fail, even the well-behaved replicates.

## Which engineered feature is most useful for Electronics?

**`power_w`.** Voltage or current alone under-describe an electrical load; power is the physically meaningful combined quantity, and it tracks load in this dataset (rising from ~0.99 W at low load to ~1.28–1.44 W at high load) in a way neither input column shows on its own.

## Which engineered feature is most useful for Mechanical?

**`stress_ratio`.** It expresses measured stress as a fraction of the rated/reference stress (e.g., ~0.80 at low load rising to ~0.90 at high load for the M009 outlier), which is the standard way to judge proximity to a material's structural limit — far more actionable for an ML model than raw MPa.

## Which engineered feature is most useful for Biochem?

**`normalized_signal`.** Since Biochem has no domain-exclusive feature, the most useful general one is the signal expressed as a multiple of baseline (fold-change over blank), which is a standard analytical-chemistry/assay metric and is directly interpretable — e.g., the high-concentration group reads roughly 10x baseline, consistent with the near-linear concentration/signal relationship found in Part 2.

## Why should invalid domain features be left blank instead of forcing a value?

Forcing a placeholder (like 0) into a column such as `power_w` for a Mechanical row or `stress_ratio` for a Biochem row would be indistinguishable from a genuine measured value of zero — a downstream model or analyst couldn't tell "this doesn't apply" from "this was actually measured as zero." Leaving it as `NaN`/blank makes the missingness explicit, so it can be deliberately filtered, imputed, or excluded — rather than silently treated as real data and corrupting any statistics or training that touches that column.

## How can feature engineering introduce misleading information?

A few concrete risks visible in this pipeline:
- **Partial rolling windows:** with `min_periods=1`, the first row of each group reports its own value as a "3-point rolling average," which can look like a smoothed/validated number when it's really just the raw first reading.
- **Small-sample coefficient_of_variation:** with only 3 replicates per group, a single outlier (like M009) swings the CV substantially — the derived `stability_flag` reflects that instability accurately, but with more replicates the same underlying process might land in a different bucket entirely, meaning the flag is sensitive to sample size, not just true variability.
- **Boundary-crossing rolling windows:** if grouping were done incorrectly (e.g., by domain alone, not domain+condition), the rolling average would blend signal from physically unrelated conditions (e.g., mixing low-load and high-load Electronics readings), producing a smoothed value that doesn't correspond to any real physical state.
- **Percent-based features on small denominators:** `error_percent` can look dramatic for small `expected_signal` values (e.g., an 8.3% swing in the low-concentration Biochem group from a 0.01-unit absolute difference), which could mislead a model or reviewer into treating it as a bigger deviation than the raw signal difference actually represents.