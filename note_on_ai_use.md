# Note on AI Use

**Author:** Si Woo Kim · **Course:** POLI3148 · **Assignment 1**

This note documents how AI was used in producing this assignment.

## Tool

I used **Claude Code** (Anthropic) with a multi-agent specialist setup spanning idea brainstorming, data retrieval, data cleaning, data visualization, data analysis, report generation, copy-editing, and other tasks.

## Phase-by-phase

I used AI for research and ideation, brainstorming, data cleaning, data visualization, statistical analysis, report generation, citation retrieval, copy-editing, and other related tasks across the project. Throughout every phase, I exercised my own critical thinking and analytical judgment to direct the work and to ensure the final submission reflects my own reasoning.

I proposed the research question myself — distinguishing whether the post-coup violence in the AES core (Mali, Burkina Faso, Niger) reflects an autonomous jihadist resurgence or a state-led civilian-targeting turn — and I used the figures and statistical results throughout the analysis to draw the valuable insights that anchor each finding in the report. I made every editorial decision about which alternative explanations to engage, which mechanisms to spell out, which findings to emphasize, and which limitations to flag honestly.

When AI-generated outputs were unclear, abstract, or factually wrong, I challenged them and required revision. For example, I caught factual issues such as the Figure 8 topic-prevalence statement that needed to be stated as "more than doubles" rather than "roughly doubles," the Figure 5 Mali map that initially rendered at a world-view zoom rather than a Mali-centred zoom, and the FAMa-Wagner-Ségou topic label that did not match the figure's actual top-three words. I also caught a more substantive misdescription in which both the README and the Finding 6 prose claimed the Random Forest classifier distinguished "pre- vs post-Wagner notes," when inspection of the training cell showed the actual target was `civilian_targeted` — a genuine analytical misframing that I corrected in both places before submission. I rejected interpretations that overstated what the figures actually showed and required figure-prose alignment for every cited number, including iterating the Figure 1, Figure 2, Figure 5, and Figure 7 mean-line and textbox layouts until each value cited in the prose was directly visible in the figure that displayed it.

For citations, AI helped me retrieve and format candidate peer-reviewed sources, and I performed an additional manual verification step before any citation entered the report. The audit trail of this verification is documented in `plan/CITATION_VERIFICATION_LOG.md`.

For drafting, I directed and reviewed every paragraph iteratively. I supplied the ideas, framing, and analytical emphasis, and I used AI as a drafting and rephrasing tool to render those ideas efficiently. The result is a report in which every analytical choice, every figure-to-claim mapping, every alternative explanation, and every limitation reflects my own judgment, with AI working as the drafting and revision instrument under my direction.

I verified all AI-generated code and figures by reviewing the outputs, double-checking values against the underlying data, and confirming that the analysis pipeline ran end-to-end and produced consistent results from the cleaned data through to the rendered report.

