# Models We Would Like In Econ-ARK

In this directory are:

1. The [Jupyter notebook](./We-Would-Like-In-Econ-ARK.ipynb) — a collection of papers on housing and heterogeneity compiled by Shujaat Khan.
2. The [We-Would-Like-In-Econ-ARK](./We-Would-Like-In-Econ-ARK) directory — one subdirectory per paper (named by Zotero citekey).

## What goes in each paper subdirectory

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the canonical structure (exposition, formalization, and asset layers) and the pre-merge checklist.

The [Benhabib_et_al_2019](./We-Would-Like-In-Econ-ARK/Benhabib_et_al_2019/) subdirectory is the reference instance of the current structure:

- `index.md` assembling four content notebooks
- `<citekey>_intro.ipynb` (metadata + provenance)
- `<citekey>_prior-literature.ipynb`
- `<citekey>_summary.ipynb` (with an explicit "The Model" recursive formulation)
- `<citekey>_subsequent-literature.ipynb`
- Split bib files (`references.bib`, `self.bib`, `subsequent-literature.bib`)
- Paper as `.pdf` plus optionally `.mmd` for AI ingestion

Older items in this directory follow a legacy "slideware" pattern (a single summary notebook with figures scraped from the paper). Refactoring a legacy item to the canonical structure is an explicitly welcome PR.
