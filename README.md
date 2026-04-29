# When the Counter-Insurgent Becomes the Killer
### Wagner, the AES Coup Belt, and the State-Led Civilian-Targeting Turn in the Sahel, 2018–2025

**POLI3148 Assignment 1 — Si Woo Kim — (HKU)**

**Live interactive report:** [siwookim1114.github.io/POLI3148-Assignment1](https://siwookim1114.github.io/POLI3148-Assignment1/)

Across Mali, Burkina Faso, and Niger — the three states that in 2024 formalized their breakaway as the *Alliance des États du Sahel* — the perpetrators of mass civilian killing have changed faster than the fighting itself. This project asks how, and how confidently, that turn can be read in the ACLED (Armed Conflict Location & Event Data) record between 2018 and 2025, using a breakdown of civilian-targeted fatalities by perpetrator type, a negative-binomial regression with three robustness specifications, a placebo on non-AES West Africa, V-Dem regime trajectories, and a three-method text analysis (TF-IDF, LDA topic modeling, VADER sentiment) of ACLED's event notes.

## Findings summary

- In Mali, civilian-targeted fatalities by **state forces rose 7.77× (95% CI 4.71–14.24)** and by **external forces rose 6.00× (1.95–30.07)** after Wagner's December 2021 deployment, while non-state armed groups rose only 1.19× (CI includes 1).
- The pooled negative-binomial estimate (country fixed effects, event-volume control, linear time trend) returns an **incidence-rate ratio (IRR) of 1.74 (95% CI 1.11–2.74, p = 0.017)** on 264 country-month observations. The result survives two robustness checks (NegativeBinomialP MLE that estimates α from the data, and cluster-robust standard errors at country level). The placebo on 13 non-AES West African countries returns IRR = 1.15 (p = 0.36, CI contains 1).
- The Russian-arrival breakpoint (IRR = 1.74) outperforms the French-exit breakpoint (IRR = 1.48, p = 0.097), and 75% of the variance in monthly civilian-fatality counts lies *within* countries across time rather than between countries — confirming the change is regime-driven, not cross-country drift.
- An admin1-level decomposition of Mali's events shows a southward shift: Mopti's share of civilian-targeted events drops from 0.54 to 0.31, while Ségou rises from 0.10 to 0.16 — independently corroborated by an unsupervised LDA topic model whose 'mopti-fulani' theme more than halves and 'fama-wagner-village' theme more than doubles post-Wagner.
- Three independent text-analysis methods on ACLED's event notes (TF-IDF distinguishing words, VADER sentiment, LDA topics) converge on the same shift: post-Wagner notes name Wagner-era actors (wagner, fama, mercenaries, patrol) rather than the jihadist-faction names that distinguished pre-Wagner reporting, while sentiment stays flat (Δ = 0.02) — ruling out a reporting-volume artifact.
- A Random Forest classifier trained on note text alone reaches **94% accuracy** distinguishing pre- vs post-Wagner notes (Logistic Regression baseline: 93%; majority-class baseline: 66%) — confirming the textual signal is robust enough to be machine-detectable, not a cherry-picked artefact of any single text-analysis method.

## Folder structure

| Path | Description |
|---|---|
| `code/01_data_cleaning.ipynb` | ACLED export integrity checks, type cleaning, derived columns, country-year merge with Powell-Thyne and V-Dem |
| `code/02_exploration.ipynb` | EDA: distributions, missingness, actor-coding sanity checks |
| `code/03_analysis.ipynb` | Bootstrap CIs, negative-binomial GLM, placebo, variance decomposition; writes `data/final_stats.json` and 5 figures (`fig_01_monthly_events`, `fig_02_civilian_fatalities_by_role`, `fig_03_pre_post_wagner_ratio`, `fig_04_vdem_regime`, `fig_05_mali_geographic`) |
| `code/04_text_analysis.ipynb` | TF-IDF distinctive-word extraction, LDA topic modeling, VADER sentiment scoring with Welch t-test, Random Forest + Logistic Regression classifiers on ACLED `notes`; appends text keys to `data/final_stats.json` and writes 4 figures (`fig_06_wordfreq`, `fig_07_sentiment`, `fig_08_topics`, `pyldavis_mali`) |
| `code/05_dashboard_figures.py` | Generates 3 dashboard/animated figures (`fig_01b_monthly_animated`, `fig_05b_mali_animated`, `fig_09_treemap`); writes self-contained HTML to `docs/figs/` |
| `code/Z_generate_report.py` | Single-file assembler: stitches the prose blocks and 11 Plotly figures into `docs/index.html` |
| `code/report_content/*.md` | Prose blocks (Lane 1 = data-scientist; Lane 2 = politics-expert) |
| `data/acled_raw.csv` | ACLED Data Export Tool download (Western Africa, 2018-01-01 → 2025-04-25) — **NOT bundled in repo (license + size); download your own per Step 2 below** |
| `data/acled_clean.parquet` | AES-core cleaned panel |
| `data/acled_clean_west_africa.parquet` | Full Western-Africa cleaned panel for placebo |
| `data/final_stats.json` | Single source of truth for all numbers in the report |
| `docs/figs/fig_01..05_*.html` | Core static Plotly figures from `03_analysis.ipynb` (Findings 1–5) |
| `docs/figs/fig_06..08_*.html` + `pyldavis_mali.html` | Text-analysis figures from `04_text_analysis.ipynb` (Finding 6) |
| `docs/figs/fig_01b_monthly_animated.html`, `fig_05b_mali_animated.html`, `fig_09_treemap.html` | Animated/dashboard figures from `05_dashboard_figures.py` |
| `docs/index.html` | Final analytical report |
| `plan/CITATION_VERIFICATION_LOG.md` | Per-citation tier-1 source verification |

## How to reproduce

1. `pip install pandas numpy plotly statsmodels scipy pyarrow scikit-learn nltk vaderSentiment jupyter`
2. Place ACLED export at `data/acled_raw.csv` (Western Africa, 2018-01-01 → 2025-04-25, all event types).
3. Run core notebooks: `jupyter nbconvert --to notebook --execute --inplace code/01_data_cleaning.ipynb code/02_exploration.ipynb code/03_analysis.ipynb`
4. Run text-analysis notebook: `jupyter nbconvert --to notebook --execute --inplace code/04_text_analysis.ipynb` (appends text keys to `data/final_stats.json`).
5. Generate animated and supplementary figures: `python code/05_dashboard_figures.py` (writes the 3 animated/treemap figures to `docs/figs/`).
6. Generate the report: `python code/Z_generate_report.py` — writes `docs/index.html`.

## Data sources

The dependent variable and all perpetrator-role coding come from the **Armed Conflict Location & Event Data project (ACLED)**, an event-level political-violence database that records each incident's date, location (latitude, longitude, and admin1 region), perpetrators (actor1 and actor2), event-type, sub-event-type, and reported fatalities. We pulled the Western Africa region from 2018-01-01 to 2025-04-25 (all event types) via the [ACLED Data Export Tool](https://acleddata.com/data-export-tool/) on 2026-04-25, which yielded 26,977 events across the AES core, of which 9,300 are flagged as civilian-targeted.

Coup-event timing comes from the **Powell-Thyne global coup dataset** (v2026.01.13), a registry of every coup attempt worldwide since 1950 that codes each as `successful` or `failed` with a `coup_date`. We use it to fix the first-coup breakpoints — Mali on 2020-08-18, Burkina Faso on 2022-01-23, and Niger on 2023-07-26 — that anchor the political-context layer of the analysis. Source: [Powell-Thyne dataset](http://www.jonathanmpowell.com/coup-detat-dataset.html).

The political-context layer in Figure 4 draws on **V-Dem v16** (March 2026 release), the expert-coded democracy-indicators dataset that provides the polyarchy index (`v2x_polyarchy`, an electoral-democracy 0–1 scale) and a six-category regime-of-the-world classification per country-year. We use these to document the AES core's post-coup regime trajectories alongside the violence series. Source: [V-Dem dataset](https://v-dem.net/data/the-v-dem-dataset/), accessed via the `vdemdata` R package.

## Methodology overview

The analysis builds country-month panels of civilian-targeted fatalities by perpetrator role (state / non-state armed group / external force), computes pre/post-Russian-arrival monthly-rate ratios with a bootstrap that resamples whole months at a time (2,000 replications, `np.random.seed(42)`), and fits a negative-binomial regression with country fixed effects, an event-volume control, and a linear time trend on the AES core. The headline IRR is reported under three specifications — fixed-α NB GLM, NegativeBinomialP MLE that estimates α from the data, and cluster-robust standard errors at country level — to confirm the result survives across reasonable specifications. The same regression is replicated on 13 non-AES Western African countries as a placebo. V-Dem regime indicators provide the political-context layer; an admin1-level geographic decomposition documents the post-Wagner de-concentration of Mali's civilian-targeted events out of Mopti and toward Ségou; a three-method text analysis (TF-IDF distinguishing words, VADER sentiment, LDA K=8 topic model) plus Random Forest + Logistic Regression classifiers triangulate the perpetrator-shift finding through ACLED's event notes.

## Limitations

- **ACLED is media-sourced and under-covers remote rural areas;** Eck (2012) documents the bias formally. The unchanged sentiment finding (Δ = 0.02) partially mitigates by ruling out a *change* in coverage tone, but a pre-existing level of under-reporting in junta-controlled rural Mopti and Ségou cannot be ruled out.
- **Short post-Wagner windows for Burkina Faso (15-month) and Niger (12-month)** make their CIs wide and their per-country IRRs imprecise. Mali's 41-month post-window does the heavy lifting in the pooled estimate. Re-running the analysis once Burkina Faso and Niger accumulate 30+ post-deployment months will be the most informative robustness test.
- **Observational design — endogenous selection.** Even with the placebo's silence, association is not causation. Wagner deployment may itself be partly a *symptom* of juntas selecting permissive partners (the "juntas choose Wagner because Wagner asks no questions" path), making Wagner a marker of regime intent rather than its independent cause.
- **Small-N panel for cluster-robust standard errors.** With only 3 country clusters in the AES core, the cluster-robust standard errors should be read as a sensitivity check rather than a definitive correction; small-cluster asymptotic theory does not strictly apply.
- **Text-analysis language coverage.** ACLED's `notes` field is English-only; French- and Arabic-language local reporting is excluded. The TF-IDF / VADER / LDA findings reflect the English-language source pool ACLED draws from, which may differentially over- or under-represent certain perpetrators.
- **Generalizability beyond the Sahel.** The state-led civilian-targeting turn we document is specific to the AES core's particular configuration of jihadist insurgency + military junta + Russian PMC partnership; whether it generalizes to other PMC-deployment contexts (Central African Republic, Libya, Syria) is an open question this dataset does not adjudicate.
- **Reported fatalities understate true death tolls.** ACLED's conservative-source-estimate convention records the lower number when sources disagree, so all fatality counts are floors, not point estimates.

## Author

This project is the work of **Si Woo Kim**, a student at The University of Hong Kong (HKU) submitting it for POLI3148 — *Data Science in Politics* (Spring 2026). The full source code lives at [github.com/siwookim1114/POLI3148-Assignment1](https://github.com/siwookim1114/POLI3148-Assignment1), the rendered interactive report is published at [siwookim1114.github.io/POLI3148-Assignment1](https://siwookim1114.github.io/POLI3148-Assignment1/), and the author can be reached on GitHub at [@siwookim1114](https://github.com/siwookim1114).
