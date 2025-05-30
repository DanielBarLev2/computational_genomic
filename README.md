# computational_genomic# Cancer Subtype Classification 🧬

This project builds a mutation-based classifier to predict cancer subtypes (HNSC vs LUSC) from genomic variant data.
## 🔧 Project Structure
```bash
project_root/
# ├── data/
# │   ├── train_muts_data.csv
# │   ├── test_muts_data.csv
# │   ├── train_meth_data.csv
# │   ├── test_meth_data.csv
# │   ├── train_feats.csv
# │   ├── test_feats.csv
# │   ├── 100_genes.csv
# │   ├── E_cool_ORF.csv
# ├── plots/
# │   ├──mutation_types_ordered.png
# ├── predictions/
# │   ├── results_muts.csv
# │   ├── results_meth.csv
# ├── Challenge_comp_geno.ipynb
```

## 📦 Requirements
Python 3.8+
pandas, scikit-learn, numpy, etc.

Set up the environment using Conda:

```bash
conda env create -f environment.yml
conda activate genomic-classifier
```

## 📁 Input Files
**train_muts_data.csv**: raw mutation records with case IDs and labels<br>
**test_muts_data.csv**: mutation records for inference<br>
**train_feats.csv**: numeric precomputed gene features<br>
**test_feats.csv**: numeric precomputed gene features<br>

## 📤 Output Files
**predictions.csv**: contains final case-level predictions for the test set of task 1
**predictions2.csv**: contains final case-level predictions for the test set of task 2
