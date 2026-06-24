# WTA Tennis Data: Python for Data Analysts

Three Jupyter notebooks taking you from raw WTA match data to a working regression model.

## Prerequisites

- [VS Code](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- Python 3.10+
- Git

## Setup

**1. Clone this repository**

```bash
git clone <this-repo-url>
cd tennis-notebooks
```

**2. Install dependencies**

Create a virtual environment first (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

Then install:
```bash
pip install -r requirements.txt
```

VS Code will detect `.venv` automatically when you open the project.

**3. Get the data**

```bash
git clone https://github.com/JeffSackmann/tennis_wta data
```

**4. Open in VS Code**

```bash
code .
```

Open any `.ipynb` file and select your Python interpreter when prompted.

## Notebooks

Work through them in order:

| Notebook | What you'll do |
|---|---|
| `EDA.ipynb` | Load a single season, explore the data, build your first visualisations |
| `JOIN_DATA.ipynb` | Consolidate 14 years of match data, clean it, engineer features |
| `REGRESSION.ipynb` | Build a linear model to understand what drives player ranking points |

Stuck? Complete reference versions live in `solutions/`.

## If something goes wrong

Each notebook has a "Stuck?" cell near the top. For `EDA.ipynb` and `REGRESSION.ipynb`,
that's a reset cell that reloads `df` from the source CSV. For `JOIN_DATA.ipynb`, restart
the kernel (`Kernel → Restart Kernel` in VS Code) and re-run from the top — there are too
many intermediate frames to reset piecemeal.

## Data

WTA Rankings, Results, and Stats by [Jeff Sackmann / Tennis Abstract](https://github.com/JeffSackmann/tennis_wta).
Licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
