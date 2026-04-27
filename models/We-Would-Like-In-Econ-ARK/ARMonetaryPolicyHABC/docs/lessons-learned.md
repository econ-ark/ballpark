# Lessons learned — ARMonetaryPolicyHABC formalize-and-finalize pass

Reusable patterns and course-corrections from the
`armonetarypolicyhabc-formalize-finalize` branch, for future contributors
working on related ballpark items. Modeled on the consolidated "Lessons
learned" section of the
[Benhabib worked example](https://llorracc.github.io/workspace-course-topics/worked-examples/benhabib-formalize-finalize/).

## Workflow and discipline

1. **Branch discipline up front.** Every commit for this assignment landed on
   a single item-scoped branch (`armonetarypolicyhabc-formalize-finalize`),
   branched from `origin/master` after the infrastructure PR merged. No
   `CONTRIBUTING.md` / infra edits on this branch.

2. **Commit scope ≈ one review item.** Each commit after the initial scaffold
   addresses one numbered item from the AI review (Opus) or one flagged item
   from the Matsya Evaluate turn. Small cleanups get their own small commits.
   This keeps the PR diff reviewable.

3. **Accept / edit / reject every AI-proposed change.** See
   `docs/accept-edit-reject.md`. One-line reasoning per item, targets listed,
   implementation status recorded. Nothing was merged blind.

4. **Record AI prompts and responses verbatim.** Prompts live in
   `docs/opus-prompt.md`; reviews in `docs/opus-review.md`; Matsya Evaluate
   responses in `docs/matsya-evaluate-turn.txt`. Reviewers can reproduce
   every step.

## Starting below Draft tier (the hardest case)

5. **When starting below Draft tier, scope aggressively.** The Benhabib
   worked example started at Primer (four notebooks, bib files, `.mmd`
   already present) and ended at Formalized in 10 rounds. This item started
   below Draft: no `index.md`, no four-notebook exposition layer, no paper
   in-repo. A realistic target for one pass is **Draft with
   partial-Formalized artifacts**, not Formalized. `docs/tier-assessment.md`
   records what did and did not land, and why.

6. **Separate scaffold from review.** The first commit on this branch was a
   pre-review formalization scaffold (bellman-excerpt draft + YAML draft +
   supporting docs). The Opus and Matsya reviews were then run against that
   scaffold. Splitting scaffold commits from review-artifact commits from
   implementation commits keeps the PR readable.

## Matsya interaction

7. **One stable `--session` per ballpark, reused across assignments.** We
   used `topics2026-armonetarypolicyhabc` through Class 10, Class 11, and
   Class 12 work. Server-side history accumulates into one reviewable thread.

8. **Single focused question, `--no-think`, small prompt.** The Matsya
   Evaluate turn (`docs/matsya-evaluate-turn.txt`) was ~2 KB of prompt with
   three numbered sub-questions plus structured verdict requests. It
   returned in ~52 seconds with a substantive response; no 120-second
   timeout. Pattern worth copying: compact decomposition pasted inline +
   CANONICAL / PROVISIONAL / UNRESOLVED verdict format requested.

9. **Matsya's critiques come in two flavors.** Dolo-plus-syntax gaps
   (PROVISIONAL / UNRESOLVED in the retrieved corpus) get inline
   `# workaround:` / `# unresolved:` comments in the YAML. Factual errors in
   our draft get corrected outright. Our Turn surfaced one of each:
   `@in StochasticMatrix` was a syntax gap (fixed by switching to `@in R+`
   plus the `@dist MarkovChain` annotation); the four-control budget was a
   draft error (fixed by pinning `a_next` via the budget identity).

## Writing bellman-excerpt.md

10. **Pre-empt Matsya's predictable critiques before the Evaluate turn.**
    The first-pass bellman-excerpt included a comprehensive symbol table
    (split into in-scope household block vs. out-of-scope aggregate-side
    deferred symbols), a numbered timing convention, and the two-stage
    perch decomposition. Matsya did not flag any missing economic
    structure — only two syntactic idioms.

11. **Name degenerate movers explicitly.** The identity movers
    (`g_{≺∘}` in Stage 1, `g_{∘≻}` in Stage 2) are labeled
    `# degenerate: identity` in both the YAML and the bellman-excerpt.
    Reviewers can distinguish "identity" from "omitted."

12. **Distinguish household scope from aggregate scope up front.** Putting
    `K`, `Y`, `G`, `Omega`, `tau^{tot}`, `Pi_inf` in a dedicated
    "Out of scope for this draft" table (with deferral reasons) stops a
    reader from thinking the formalization is incomplete. It is scoped to
    the household block on purpose.

## Writing dolo-plus-draft.yaml

13. **Flag workarounds, don't hide them.** `# unresolved:` (paper not in
    repo), `# workaround:` (deliberate placeholder), and
    `# degenerate: identity` (labeled no-op) are honest outputs. A YAML
    with flagged gaps is reviewable; a YAML with silently-fudged syntax
    is not.

14. **Don't conflate paper gaps with dolo-plus spec gaps.**
    `verification.md` (at the item root) partitions each open issue into one
    of these buckets. The `P_e` declaration was a spec gap (now closed). The
    utility kernel is a paper gap (deferred until the paper PDF / `.mmd` is
    in-repo). The distinction determines who can close each item.

16. **Item-root layout is non-optional for Formalized.**
    `CONTRIBUTING.md` §"Formalized" requires `bellman-excerpt.md`,
    `dolo-plus-draft.yaml`, `verification.md`, and `matsya-session.txt` at
    the **item root** (alongside `AGENTS.md`), not under `docs/`. The PR #72
    review surfaced this: an automated mechanical check looks for these four
    names exactly at the item root. AI iteration history (Opus prompt /
    review, Matsya turn transcripts, accept-edit-reject log,
    lessons-learned) belongs under `docs/`, but the four canonical
    deliverables themselves do not. Earlier drafts of the Bellman excerpt
    that pre-date the Matsya iteration belong under `docs/legacy-drafts/`,
    not at the item root — `CONTRIBUTING.md` line 52 explicitly forbids
    keeping multiple parallel Bellman files.

15. **Comment directly on the offending line.** Each `# unresolved:` /
    `# workaround:` sits immediately above the symbol or equation it
    qualifies, not in a separate "caveats" section. The reviewer sees the
    reason at the point of encounter.

## Symbol-collision hygiene

16. **Rename when two symbols would collide.** The household Markov kernel
    `Pi` was renamed `P_e` to avoid collision with the aggregate inflation
    series `Pi_inf`. The rename is documented in the bellman-excerpt
    symbol table, the YAML, the verification note, and `AGENTS.md`. Future
    contributors adding the aggregate monetary block will not accidentally
    shadow `Pi` between the two blocks.

## AI-review-plus-implementation rhythm

17. **One Opus pass for a full prioritized list; Matsya for focused
    syntactic questions.** Opus 4.7 returned a ten-item prioritized review
    (`docs/opus-review.md`). Matsya was used afterward for narrow
    dolo-plus-syntax verdicts. Mixing the two roles on one model is
    possible but less efficient: Opus reasons broadly about economics +
    criteria; Matsya retrieves from the canonical dolo-plus corpus.

18. **Record current tier after each pass.** `docs/tier-assessment.md`
    lists, item by item from `CONTRIBUTING.md`, what is Draft-tier
    compliant, what is Primer-tier blocked (four-notebook layout; paper
    in-repo), and what Formalized-tier artifacts are present but not yet
    paper-grounded. This is what a maintainer needs to decide what to
    merge and what to ask a follow-up contributor to extend.
