"""
Metallic Means and Universality: Algebraic Structure Module

This module implements the proven algebraic results from:
"Metallic Means and Universality: Algebraic Structure, Analytic Proof, and Geometric Unification"
by Beatriz Errante (2026)

Key Results Implemented:
- Theorem 2.6: Main Algebraic Identification φ_{L_{2k-1}} = φ^{2k-1}
- Corollary 2.7: Quadratic Field Classification
- Theorem 2.10-2.11: Asymptotic Expansions
- Theorem 2.4: Cyclotomic Identities
"""

from .identities import (
    lucas_number,
    fibonacci_number,
    metallic_mean,
    golden_mean,
    verify_errante_identity,
    exceptional_family,
    verify_quadratic_field_classification
)

from .asymptotic import (
    asymptotic_expansion_phi_n,
    asymptotic_expansion_ln_phi_n,
    catalan_coefficients,
    expansion_coefficients_b_k
)

from .cyclotomic import (
    cyclotomic_identities,
    verify_cyclotomic_identities,
    pentagonal_geometry
)

__version__ = "1.0.0"
__author__ = "Beatriz Errante"

__all__ = [
    'lucas_number',
    'fibonacci_number',
    'metallic_mean',
    'golden_mean',
    'verify_errante_identity',
    'exceptional_family',
    'asymptotic_expansion_phi_n',
    'asymptotic_expansion_ln_phi_n',
    'cyclotomic_identities'
]
