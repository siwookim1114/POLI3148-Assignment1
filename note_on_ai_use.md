# Note on AI Use

**Author:** Si Woo Kim · **Course:** POLI3148 (Spring 2026, HKU) · **Assignment 1**

This note documents how AI was used in producing this assignment.

## Tool

**Claude Code** (Anthropic), model `claude-opus-4-7` (1M-context). Claude Code is an interactive command-line agent that reads and writes files, runs Python and shell, fetches web content, and orchestrates specialist sub-agents. The session ran 2026-04-25 to 2026-04-26.

## Multi-agent workflow

I configured Claude Code with a six-agent specialist team and a written coordination contract:

- **politics-expert** — political-science framing, theoretical interpretation, citation gatekeeping (custom-built for this project).
- **data-scientist** — data wrangling, statistical analysis, figure production, engineering.
- **academic-researcher** — peer-reviewed citation discovery and verification.
- **search-specialist** — open-source-event verification (e.g., Wagner deployment dates).
- **english-expert** — copy-editing for register, hedging, clarity, and word-count discipline.
- **research-orchestrator** — workflow sequencing.

The contract enforces a "two-lane" rule: every empirical finding carries both a descriptive paragraph (data-scientist) and a political-science interpretation paragraph (politics-expert). Neither agent crosses lanes.

## Phase-by-phase

| Phase | AI's role | My role |
|---|---|---|
| Topic | Three candidate topics with literature scaffolds proposed; ACLED data feasibility verified. | Chose the AES-Wagner topic; weighed plagiarism risk against analytical depth. |
| Data acquisition | Powell-Thyne and V-Dem v16 fetched. | I ran the ACLED export myself with my Research-tier account. |
| Cleaning + analysis | Notebooks `01_data_cleaning`, `02_exploration`, `03_analysis`, `04_text_analysis` authored to my brief: bootstrap CIs, negative-binomial regression with country dummy variables, placebo on non-AES West Africa, variance decomposition, TF-IDF + LDA + VADER + sklearn classifiers. | Specified every analytical decision; sanity-checked every output. |
| Citation verification | Each citation WebFetched against Cambridge / Oxford Academic / Sage / Taylor & Francis. Audit trail: `plan/CITATION_VERIFICATION_LOG.md`. | I required ≥18 verified citations before drafting could begin. |
| Drafting | politics-expert authored Lane 2 + Introduction + Discussion + Conclusion + bibliography; data-scientist authored Lane 1 + Methods + assembler. | I wrote the structural scaffold (`STRUCTURE.md`) — section budgets, figure mapping, citation mandates, banned-language rules — and reviewed every output. |
| Copy-editing | english-expert trimmed to 1,500-word target and humanised voice. | I checked diffs to confirm no factual content moved. |
| Audits | professor-grader, ml-engineer, web-verifier, code-reviewer ran final passes. | I posed mock instructor Q&A and required every answer in <60 seconds. |
| Submission | not done by AI. | Mine. |

## What AI did not do

- AI did not pick the topic.
- AI did not download the ACLED data; I did.
- AI did not invent any number — every numeric claim traces to `data/final_stats.json`, which is the deterministic output of `03_analysis.ipynb`.
- AI did not invent any citation — every citation passed an explicit WebFetch with URL/DOI logged.

## Responsibility

I take full responsibility for every claim. Where AI authored prose, I reviewed it and would have written something equivalent given the same evidence and time. Where AI computed a statistic, the computation is reproducible from the public ACLED, Powell-Thyne, and V-Dem datasets. AI's contribution was throughput and discipline (citation verification, banned-language checks, validation gates) — not analytical originality.
