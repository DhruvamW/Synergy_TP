# Correlation Analysis: Findings and Limitations

## Does signal increase or decrease with input value?

It depends on the domain and physical mechanism, not on a single universal rule:

- **Biochem** (signal vs concentration): signal **increases** with input value (slope ≈ 0.98, Pearson r = 0.999). This tracks a standard absorbance-vs-concentration calibration.
- **Electronics** (signal vs load): signal **decreases** as load (resistance) increases (slope ≈ -0.023, r = -0.985) — consistent with voltage drop under increasing load.
- **Electronics** (signal vs temperature): signal also **decreases** as temperature rises (slope ≈ -0.052, r = -0.992).
- **Mechanical** (signal vs load): signal (deflection) **increases** with load (slope ≈ 0.014, r = 0.984).
- **Mechanical** (stress vs load): stress **increases** with load (slope ≈ 1.64, r = 0.984), as expected from basic load-stress mechanics.

## Which domain shows the strongest signal-input relationship?

**Biochem** (signal vs concentration): Pearson r = 0.999, R² = 0.999, with the smallest fit errors of any relationship tested (MAE ≈ 0.011, RMSE ≈ 0.013 absorbance units). The three concentration levels produce tightly clustered replicates, giving a near-perfect linear fit.

## Which domain shows the weakest or noisiest relationship?

**Mechanical** is the noisiest, on both measures:

- Signal vs Load: R² = 0.968 (lowest R² in the set), MAE ≈ 0.078 mm, RMSE ≈ 0.101 mm — errors that are large relative to the signal's own range (0.50–2.10 mm).
- Stress vs Load: RMSE ≈ 12.0 MPa, the largest absolute error of any relationship.

This traces to a single replicate at the high-load condition (record M009: 2.10 mm / 270 MPa), which sits noticeably above its two sibling replicates (1.75 mm/230 MPa and 1.80 mm/235 MPa). That one point pulls both the Mechanical fits away from the tight linearity seen in Biochem.

## Does high correlation prove causation?

No. A high Pearson or Spearman value only shows that two variables move together in a consistent (linear or monotonic) way — it says nothing about *why*. In this dataset, the Electronics signal-vs-temperature correlation (r = -0.992) is a good caution: temperature was not varied independently of load — both increase together across the three Electronics conditions (35–36 °C at low load, up to 48–50 °C at high load). The strong temperature correlation could just as easily be a byproduct of load changing, not a direct temperature effect. Correlation identifies association; establishing causation requires controlled variation of one variable at a time (or independent physical justification).

## Can correlation be trusted with small sample size?

Not fully. Each relationship here is based on only **9 samples** (3 input levels × 3 replicates). With so few points, a single unusual measurement can swing the correlation coefficient substantially — the Mechanical results above are a direct example, where one replicate visibly worsened the fit. Small samples also make it hard to distinguish "the relationship is genuinely a bit noisy" from "the relationship is strong but one measurement was off." Wider replication (more repeats per condition, more input levels) would make the reported correlations more trustworthy.

## Can correlation miss nonlinear relationships?

Yes. Pearson correlation specifically measures *linear* association, and Spearman measures monotonic association — neither captures curvature such as saturation, thresholds, or peaks. All three Biochem points fall within a narrow concentration range (0.1–1.0 mM) where the assay may behave linearly, but many biochemical assays saturate at higher concentrations; a Pearson r near 1.0 inside this tested range would not guarantee linearity outside it. The same caution applies to Electronics and Mechanical: the fits look strongly linear across the tested range, but nothing in the correlation value itself rules out nonlinear behavior beyond it.

## How can outliers affect correlation?

A single extreme point can noticeably shift the slope, intercept, and error metrics, especially with only 9 samples per relationship. The clearest case here is Mechanical replicate M009 (high load): its signal and stress values run well above its paired replicates, which is why Mechanical shows the lowest R² and the highest RMSE in the whole summary, despite the underlying load-signal relationship being physically linear. Outliers don't just add random noise — they can pull a fitted line toward themselves, distorting the calibration for every other point.

## How can temperature, load, material type, or experimental condition act as confounding variables?

A confounder is a variable that changes alongside the one you're studying, making it impossible to tell which one is actually driving the response. In this dataset:

- **Temperature and load are confounded in Electronics**: temperature rises in step with load across all three conditions, so the strong signal-vs-temperature correlation could partly (or entirely) reflect the load effect instead.
- **Material type** would confound a Mechanical stress-vs-load relationship if different specimens (different alloys, batches) were mixed into the same load levels — stiffness differences would look like load effects.
- **Experimental condition/replicate-level factors** (e.g., calibration drift, ambient conditions on a given day) could explain outliers like M009 without any real physical change in the load-signal relationship.

Confounders are dangerous specifically because they produce correlations that look meaningful but reflect a shared cause rather than a direct relationship.

## Why should mixed-domain correlation be avoided?

Biochem, Electronics, and Mechanical measure fundamentally different physical quantities with different units, sensors, and expected magnitudes (absorbance ~0.1–1.0, voltage ~4–5 V, displacement ~0.5–2.1 mm). Pooling them into a single signal-vs-input_value correlation would mix unrelated scales and mechanisms — any correlation computed across domains would reflect the fact that different domains happen to occupy different numeric ranges, not a real underlying physical relationship. Each domain must be analyzed separately, exactly as done here, for the correlation and calibration numbers to mean anything.