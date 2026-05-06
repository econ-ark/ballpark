# Opus 4.7 review prompt (exact text sent)

> Reviewer model: **Claude Opus 4.7** (Cursor, high thinking).
> Thread context: Cursor chat on `armonetarypolicyhabc-formalize-finalize` branch of `econ-ark/ballpark`.
> Matsya session pin: `--session topics2026-armonetarypolicyhabc` (reused, not new).
> Deliverable: [Ask AI help to formalize and finalize your ballpark item](https://llorracc.github.io/workspace-course-topics/assignments/ask-ai-help-to-formalize-and-finalize-ballpark.html).

```text
For all matsya interactions in this thread, use `--session topics2026-armonetarypolicyhabc` — do not open a new session.

Please review my ballpark entry for Algan, Y. and Ragot, X. (2009), "Monetary Policy with Heterogeneous Agents and Borrowing Constraints," at:

  https://github.com/econ-ark/ballpark/tree/master/models/We-Would-Like-In-Econ-ARK/ARMonetaryPolicyHABC

against the quality criteria articulated in:

  https://github.com/econ-ark/ballpark/blob/master/CONTRIBUTING.md

The entry currently sits between Draft and Primer on the exposition side, but already contains a formalization-layer scaffold (`docs/bellman-excerpt.md`, `docs/dolo-plus-draft.yaml`, `docs/verification.md`, `docs/matsya-session.txt`, `AGENTS.md`). I want a prioritized list of substantive changes that would push the item toward — and be finalized within — the Formalized tier.

Focus on the economics, the model statement, literature coverage, the dolo-plus / DDSL formalization, and the AGENTS.md file. Ignore cosmetic changes (formatting, typos, citation style).

Specifically, please address:

1. "The Model" layer. The recursive formulation currently lives in `ToramanSY_AlganRagot2009_Summary.ipynb` (ballpark summary) and in `docs/bellman-excerpt.md` (modular DDSL statement with symbol table and perches).
   - Is the recursive formulation explicit enough that Matsya can build the Formalized-tier layer on top of it without reinterpretation?
   - Does it admit an unambiguous periods / stages / perches decomposition (arrival, decision, continuation), or does it carry ambiguities?
   - Flag specifically whether the CES-over-(c,m)-with-leisure utility in the summary excerpt is reconciled with the separable CRRA + labor-disutility placeholder currently in `docs/dolo-plus-draft.yaml`.

2. Literature coverage.
   - Are the prior-literature and subsequent-literature notebooks present and well-scoped? If absent, list the 3-6 foundational papers you would expect (Bewley / Huggett / Aiyagari / Lucas / Imrohoroglu / Kehoe-Levine / Algan-Challe-Ragot etc.).
   - For subsequent literature, list influential follow-ups on monetary HA models with borrowing constraints through today.

3. Distinguishing features.
   - What makes Algan-Ragot (2009) distinctive relative to the foundational HA-monetary literature? Is this surfaced clearly in the summary / intro, or is it buried?
   - Specifically: the role of binding-vs-non-binding constraints, money-as-asset choice, inflation-tax redistribution channel.

4. AGENTS.md.
   - Are the "Known model features requiring attention" complete (utility mismatch, q_next law of motion, a_min placeholder, Pi calibration)? What's missing?
   - Are the "Common next tasks" well-scoped (grounded in actual gaps in the current files, not aspirational)?

5. Dolo-plus draft YAML.
   - Evaluate `docs/dolo-plus-draft.yaml` structurally: are the two stages (decision + shock) correctly wired? Are the `# unresolved:` / `# workaround:` flags pointing at the right things?
   - Identify the single most-important change needed to make the YAML paper-faithful rather than just structurally coherent.

6. Anything else a thoughtful graduate student would want clarified before attempting to promote this item to Formalized tier.

Output format: a numbered list of 6-10 proposed changes. For each give:
  (a) the problem in one sentence,
  (b) the proposed substantive change,
  (c) where in the item the change goes (file, section/line),
  (d) severity: Must-fix for Formalized or Nice-to-have.

End with: "Top 5 changes to implement now" ordered by impact, and explicitly flag any suggestions where you are unsure — I will verify against the paper PDF before accepting.

Omit cosmetic items. Do not rewrite files; give me a change list.
```
