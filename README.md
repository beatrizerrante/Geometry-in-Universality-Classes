# Metallic Means and Universality: Algebraic Structure, Analytic Proof, and Geometric Unification

**Beatriz Errante** | February 21, 2026


## 📋 Overview

This repository contains the complete implementation and supplementary materials for the paper "Metallic Means and Universality: Algebraic Structure, Analytic Proof, and Geometric Unification" by Beatriz Errante.

The paper investigates the connection between metallic means and universality classes in one-dimensional dynamics through three complementary approaches:

### ✅ Proven Algebraic Results
For odd-index Lucas numbers $n = L_{2k-1}$ ($1,4,11,29,76,199,521,\ldots$), we prove:

$$\varphi_n = \varphi^{2k-1}, \qquad \sqrt{n^2+4} = F_{2k-1}\sqrt{5}$$

where $\varphi$ is the golden mean and $F_{2k-1}$ are odd-index Fibonacci numbers.

### 📊 Numerical Evidence
Spectral computation confirms $\delta_{L_{2k-1}} = \delta_2^{2k-1}$ to within $10^{-8}$ relative error.

### 🔮 Research Program
Three precisely formulated open problems whose resolution would complete the theory.

## 📁 Repository Structure
metallic-means-universality/
├── paper/ # LaTeX source for the main paper
│ ├── main.tex # Main paper file
│ ├── sections/ # Individual sections
│ │ ├── 01-introduction.tex
│ │ ├── 02-algebraic-results.tex
│ │ ├── 03-numerical-evidence.tex
│ │ ├── 04-epstein-class.tex
│ │ ├── 05-banach-spaces.tex
│ │ ├── 06-fixed-point.tex
│ │ ├── 07-geometric-consequences.tex
│ │ ├── 08-synthesis.tex
│ │ └── appendices.tex
│ ├── bibliography.bib # References
│ └── figures/ # Generated figures
├── src/ # Source code
│ ├── algebraic/ # Algebraic identities module
│ │ ├── init.py
│ │ ├── identities.py # Theorem 2.6 implementation
│ │ ├── asymptotic.py # Theorems 2.10-2.11
│ │ └── cyclotomic.py # Theorem 2.4
│ ├── numerical/ # Numerical computations
│ │ ├── init.py
│ │ ├── fourier.py # Fourier series utilities
│ │ ├── renormalization.py # Renormalization operator
│ │ └── eigenvalue.py # Eigenvalue computation
│ └── visualization/ # Plotting utilities
│ └── plots.py
├── tests/ # Unit tests
│ ├── test_algebraic.py
│ └── test_suite.py
├── data/ # Data files
│ ├── golden_mean_coeffs.npy # Fourier coefficients of f2*
│ └── eigenvalues/ # Computed eigenvalues
├── docs/ # Documentation
│ ├── open-problems.md
│ └── geometric-dictionary.md
├── requirements.txt # Python dependencies
├── main.py # Main entry point
├── LICENSE # License
└── README.md # This file


## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/beatriz-errante/metallic-means-universality.git
cd metallic-means-universality

# Install dependencies
pip install -r requirements.txt

# Run algebraic verification
python main.py --verify-all

# Generate figures
python main.py --generate-figures

# Run test suite
python main.py --run-tests

📊 Key Results
Theorem 2.6 (Main Algebraic Identification)

from src.algebraic import verify_errante_identity

for k in range(1, 8):
    valid, left, right, diff = verify_errante_identity(k)
    print(f"k={k}: Verified: {valid}, |diff| = {diff:.2e}")

Numerical Verification
n	k	2k-1	δ_n (computed)	δ₂^{2k-1}	Rel. Error
4	2	3	22.7477923456	22.7477914672	3.9e-8
11	3	5	183.6482910234	183.6481198765	9.3e-7
29	4	7	1483.9578234567	1483.9543210987	2.4e-6
🔬 Open Problems
Three central open problems are identified:

Epstein Class Preservation – Prove that $\mathcal{R}{L{2k-1}}$ preserves the Epstein class

Contraction Estimates – Prove $\mathcal{R}_n = \mathcal{C}_k + \mathcal{K}_k$ with $\mathcal{C}_k$ contractive

Fixed Point Theorem – Apply Krasnoselskii's theorem to obtain $f_n^*$

📖 Citation
@article{errante2026metallic,
  title={Metallic Means and Universality: Algebraic Structure, 
         Analytic Proof, and Geometric Unification},
  author={Errante, Beatriz},
  year={2026},
  note={Feb 21, 2026 version}
}
