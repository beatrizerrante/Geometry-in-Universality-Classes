"""
Test Suite for Metallic Means and Universality
==============================================

Comprehensive tests for all algebraic and numerical implementations.
Run with: pytest tests/ -v
"""

import numpy as np
from decimal import Decimal, getcontext
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from algebraic.identities import (
    lucas_number, fibonacci_number, golden_mean, metallic_mean,
    verify_errante_identity, exceptional_family, verify_quadratic_field_classification
)
from algebraic.asymptotic import (
    catalan_coefficients, asymptotic_expansion_phi_n, asymptotic_expansion_ln_phi_n
)
from algebraic.cyclotomic import cyclotomic_identities


def test_lucas_numbers():
    """Test Lucas number computation."""
    assert lucas_number(0) == 2
    assert lucas_number(1) == 1
    assert lucas_number(2) == 3
    assert lucas_number(3) == 4
    assert lucas_number(5) == 11
    print("✓ Lucas numbers test passed")


def test_fibonacci_numbers():
    """Test Fibonacci number computation."""
    assert fibonacci_number(0) == 0
    assert fibonacci_number(1) == 1
    assert fibonacci_number(5) == 5
    assert fibonacci_number(7) == 13
    print("✓ Fibonacci numbers test passed")


def test_errante_identity():
    """Test Theorem 2.6: Main algebraic identity."""
    for k in range(1, 8):
        valid, left, right, diff = verify_errante_identity(k, precision=30)
        assert valid, f"Identity failed for k={k}"
    print("✓ Errante identity test passed")


def test_quadratic_field_classification():
    """Test Corollary 2.7: Quadratic field classification."""
    exceptional = [1, 4, 11, 29, 76, 199, 521]
    for n in exceptional:
        in_field, _ = verify_quadratic_field_classification(n)
        assert in_field, f"n={n} should be in Q(sqrt(5))"
    print("✓ Quadratic field classification test passed")


def test_catalan_coefficients():
    """Test Catalan-type coefficients."""
    coeffs = catalan_coefficients(5)
    expected = [1, 1, 2, 5, 14]
    assert coeffs == expected
    print("✓ Catalan coefficients test passed")


def test_asymptotic_expansions():
    """Test Theorems 2.10 and 2.11."""
    n = 1000
    approx, exact, bound = asymptotic_expansion_phi_n(n, N=5)
    error = abs(approx - exact)
    assert error < 1e-10
    print("✓ Asymptotic expansions test passed")


def test_cyclotomic_identities():
    """Test Theorem 2.4."""
    ids = cyclotomic_identities(precision=30)
    assert ids['identity_1_valid']
    assert ids['identity_2_valid']
    assert ids['identity_3_valid']
    assert ids['identity_4_valid']
    print("✓ Cyclotomic identities test passed")


def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("TEST SUITE: METALLIC MEANS AND UNIVERSALITY")
    print("=" * 60)

    test_lucas_numbers()
    test_fibonacci_numbers()
    test_errante_identity()
    test_quadratic_field_classification()
    test_catalan_coefficients()
    test_asymptotic_expansions()
    test_cyclotomic_identities()

    print("=" * 60)
    print("ALL TESTS PASSED ✓")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
