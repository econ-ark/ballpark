# 'In the ballpark' of the Econ-ARK ...

means papers or models that are closely related enough to be of interest to the kinds of people who are interested in the Econ-ARK.

These are papers that an ambitious graduate student might be able to turn into a course project in an advanced class in structural microeconomics, heterogeneous agent macroeconomics, or computational economics. 

The papers mentioned here are of two kinds: Papers that
1. Have serious structural models that produce interesting results
   * In the "models" directory
   * The objective: Replicate (or improve!) the quantitative theory
1. Have strong empirical evidence that begs for a model
   * In the "empirical" directory
   * The objective: Construct a model that speaks to the results

We will be delighted to post any such contributions, under the name of the contributor, in:
   * The [REMARK](https://github.com/econ-ark/REMARK) repo 
      * if it is substantially complete replication of the paper's results
   * The [DemARK](https://github.com/econ-ark/DemARK) repo
      * if it demonstrates some of the ideas or content of the paper 

As an example of the kinds of things we are looking for, see the [paper](https://pdfs.semanticscholar.org/6052/a3eff6257db799e5e54ee0e99a358b11bccf.pdf)  by Iskhakov et al cited below, which is instantiated in the Econ-ARK ecosystem in four ways, in increasing order of importance, in the Econ-ARK:

1. As an entry in [our public Zotero bibliographical database](https://www.zotero.org/groups/2314611/ballpark)
1. As a DemARK at 
1. As a REMARK at 
1. As a collection of tools under the name `DCEGM`
    * `from HARK.DCEGM import *`

The papers listed herein are a small subset of the ones that we would welcome into the Econ-ARK. If you want to work on a paper that is not listed here, post an "issue" on the repo asking (and providing a link and bibliographical reference for the paper in question). If it is likely to prove interesting to our audience, we are very likely to encourage you to replicate it.

## Environment Setup

This repo uses [uv](https://docs.astral.sh/uv/) for dependency management and keeps per-platform environments in directories named `.venv-<os>-<arch>` (matching the pattern used in `HAFiscal-Latest`). Install uv first (`brew install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`).

**Local setup:**
```bash
# 1. Create / update the platform + architecture specific environment
bash scripts/setup_env.sh

# 2. Activate the environment that was created (example shown for macOS arm64)
source .venv-darwin-arm64/bin/activate

# 3. Work inside the environment
uv run jupyter lab
```

Run `scripts/setup_env.sh` again whenever dependencies change; it is idempotent and will reuse the existing `.venv-<os>-<arch>/` directory.

**Binder:** Launch from [mybinder.org](https://mybinder.org) using this repo; the build installs uv and uses it to install dependencies.

## Citation Management in Notebooks

Some notebooks use the legacy `cite2c` format (`<cite data-cite="..."></cite>`) for Zotero citations. The environment includes **jupyterlab-citation-manager**, which supports cite2c migration: when you open such a notebook in JupyterLab, the extension will detect the old format and offer to migrate it. After migration, citations and bibliographies render using your Zotero library. To use Zotero integration, add your [Zotero API key](https://www.zotero.org/settings/keys/new) in the extension settings (Settings → Advanced Settings → Citation Manager).

References:

Iskhakov, F., Jørgensen, T.H., Rust, J., Schjerning, B., others, 2017. The endogenous grid method for discrete-continuous dynamic choice models with (or without) taste shocks. Quantitative Economics 8, 317–365.

