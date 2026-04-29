# When the Counter-Insurgent Becomes the Killer
### Wagner, the AES Coup Belt, and the State-Led Civilian-Targeting Turn in the Sahel, 2018–2025

**POLI3148 Assignment 1 — Si Woo Kim — Spring 2026 (HKU)**

Across Mali, Burkina Faso, and Niger — the three states that in 2024 formalized their breakaway as the *Alliance des États du Sahel* — the perpetrators of mass civilian killing have changed faster than the fighting itself. This project asks how, and how confidently, that turn can be read in the ACLED (Armed Conflict Location & Event Data) record between 2018 and 2025, using a breakdown of civilian-targeted fatalities by perpetrator type, a negative-binomial regression, a placebo on non-AES West Africa, and V-Dem regime trajectories.

## Findings summary

- In Mali, civilian-targeted fatalities by **state forces rose 7.77× (95% CI 4.71–14.24)** and by **external forces rose 6.00× (1.95–30.07)** after Wagner's December 2021 deployment, while non-state armed groups rose only 1.19× (CI includes 1).
- The pooled negative-binomial estimate (country dummy variables, control for total monthly event volume, linear time trend) returns an **incidence-rate ratio (IRR) of 1.74 (95% CI 1.11–2.74, p = 0.017)** on 264 country-month observations. The placebo on 13 non-AES West African countries returns IRR = 1.15 (p = 0.36, CI contains 1).
- The Russian-arrival breakpoint (IRR = 1.74) outperforms the French-exit breakpoint (IRR = 1.48, p = 0.097), and 74.7% of the variance in monthly civilian-fatality counts lies *within* country across time rather than between countries.

## Folder structure

| Path | Description |
|---|---|
| `code/01_data_cleaning.ipynb` | ACLED export integrity checks, type cleaning, derived columns, country-year merge with Powell-Thyne and V-Dem |
| `code/02_exploration.ipynb` | EDA: distributions, missingness, actor-coding sanity checks |
| `code/03_analysis.ipynb` | Bootstrap CIs, negative-binomial GLM, placebo, variance decomposition; writes `data/final_stats.json` and 5 figures (`fig_01_monthly_events`, `fig_02_civilian_fatalities_by_role`, `fig_03_pre_post_wagner_ratio`, `fig_04_vdem_regime`, `fig_05_mali_geographic`) |
| `code/04_text_analysis.ipynb` | TF-IDF distinctive-word extraction, LDA topic modeling, VADER sentiment scoring with Welch t-test, Random Forest + Logistic Regression classifiers on ACLED `notes`; appends text keys to `data/final_stats.json` and writes 4 figures (`fig_06_wordfreq`, `fig_07_sentiment`, `fig_08_topics`, `pyldavis_mali`) |
| `code/05_dashboard_figures.py` | Generates 3 dashboard/animated figures (`fig_01b_monthly_animated`, `fig_05b_mali_animated`, `fig_09_treemap`); writes self-contained HTML to `docs/figs/` |
| `code/Z_generate_report.py` | Single-file assembler: stitches the prose blocks and 12 Plotly figures into `docs/index.html` |
| `code/report_content/*.md` | Prose blocks (Lane 1 = data-scientist; Lane 2 = politics-expert) |
| `data/acled_raw.csv` | ACLED Data Export Tool download (Western Africa, 2018-01-01 → 2025-04-25) |
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

- **ACLED** Data Export Tool, https://acleddata.com/data-export-tool/, retrieved 2026-04-25 (Western Africa region, 2018-01-01 to 2025-04-25, all event types).
- **Powell-Thyne global coup dataset**, v2026.01.13, http://www.jonathanmpowell.com/coup-detat-dataset.html.
- **V-Dem v16** (March 2026 release), https://v-dem.net/data/the-v-dem-dataset/, accessed via the `vdemdata` R package.

## Methodology overview

The analysis builds country-month panels of civilian-targeted fatalities by perpetrator role (state / non-state armed group / external force), computes pre/post-Russian-arrival monthly-rate ratios with a bootstrap that resamples whole months at a time (2,000 replications, `np.random.seed(42)`), fits a negative-binomial regression with country dummy variables and a control for total monthly event volume to the AES core, and replicates the same specification on 13 non-AES Western African countries as a placebo. V-Dem regime indicators provide the political-context layer, and an admin1-level geographic decomposition documents the post-Wagner de-concentration of Mali's civilian-targeted events out of Mopti and toward the Ségou–Niono corridor.

## Limitations

- ACLED is media-sourced and under-covers remote rural areas; Eck (2012) documents the bias formally.
- Burkina Faso (15-month) and Niger (12-month) post-Wagner windows are short; their CIs are wider and they should not be over-interpreted.
- The design is observational: even with the placebo's silence, association is not causation, and Wagner deployment may itself be partly a symptom of juntas selecting permissive partners.
- All fatality counts are *reported* fatalities under ACLED's conservative-source-estimate convention, so they understate.

## AI tools used

See `note_on_ai_use.md`.
