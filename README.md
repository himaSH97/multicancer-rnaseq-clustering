# multicancer-rnaseq-clustering

Exploratory PCA and *k*-means on pan-cancer platelet RNA-seq (GSE68086). Labels are used only after clustering for comparison.

## Report

**[Full project write-up → index.md](index.md)**

## How to run

1. Python 3.x, install deps: `pip install -r requirements.txt`
2. Put the raw matrix at the path in `config/config.json` (see `data_path`).
3. Run: `python train_pipeline.py`

Outputs go under `results/` (CSVs, plots, `pca_3d.html`).
