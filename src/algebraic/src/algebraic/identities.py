"""
Core Algebraic Identities - Theorem 2.6 Implementation
======================================================

Implements the fundamental identity:
    φ_{L_{2k-1}} = φ^{2k-1}

Where:
    - L_{2k-1} are odd-index Lucas numbers
    - φ = (1 + √5)/2 is the golden mean
    - φ_n = (n + √(n²+4))/2 are metallic means
"""

import numpy as np
from decimal import Decimal, getcontext
from typing import List, Tuple, Union
from fractions import Fraction

# High precision for algebraic verification
getcontext().prec = 50


def lucas_number(m: int) -> int:
    """
    Compute the m-th Lucas number L_m.

    Definition: L_0 = 2, L_1 = 1, L_{m+1} = L_m + L_{m-1}

    Args:
        m: Index (non-negative integer)

    Returns:
        L_m: The m-th Lucas number

    Examples:
        >>> lucas_number(0)
        2
        >>> lucas_number(1)
        1
        >>> lucas_number(5)
        11
        >>> [lucas_number(2*k-1) for k in range(1, 6)]
        [1, 4, 11, 29, 76]  # Exceptional family
    """
    if m < 0:
        raise ValueError("Lucas numbers defined for non-negative indices")
    if m == 0:
        return 2
    if m == 1:
        return 1

    # Iterative computation for efficiency
    L_prev, L_curr = 2, 1
    for _ in range(2, m + 1):
        L_prev, L_curr = L_curr, L_prev + L_curr
    return L_curr


def fibonacci_number(m: int) -> int:
    """
    Compute the m-th Fibonacci number F_m.

    Definition: F_0 = 0, F_1 = 1, F_{m+1} = F_m + F_{m-1}

    Args:
        m: Index (non-negative integer)

    Returns:
        F_m: The m-th Fibonacci number

    Examples:
        >>> fibonacci_number(0)
        0
        >>> fibonacci_number(5)
        5
        >>> [fibonacci_number(2*k-1) for k in range(1, 6)]
        [1, 2, 5, 13, 34]
    """
    if m < 0:
        raise ValueError("Fibonacci numbers defined for non-negative indices")
    if m == 0:
        return 0
    if m == 1:
        return 1

    F_prev, F_curr = 0, 1
    for _ in range(2, m + 1):
        F_prev, F_curr = F_curr, F_prev + F_curr
    return F_curr


def golden_mean(precision: int = 50) -> Decimal:
    """
    Compute the golden mean φ = (1 + √5)/2 to specified precision.

    Args:
        precision: Decimal precision (default 50)

    Returns:
        φ to specified precision

    Examples:
        >>> phi = golden_mean(20)
        >>> float(phi)
        1.6180339887498948482...
    """
    getcontext().prec = precision + 5
    sqrt5 = Decimal(5).sqrt()
    phi = (Decimal(1) + sqrt5) / Decimal(2)
    return +phi  # + removes extra precision


def metallic_mean(n: Union[int, float], precision: int = 50) -> Decimal:
    """
    Compute the n-th metallic mean φ_n = (n + √(n²+4))/2.

    Args:
        n: Index (positive integer for standard metallic means)
        precision: Decimal precision

    Returns:
        φ_n to specified precision

    Examples:
        >>> phi1 = metallic_mean(1)  # Golden mean
        >>> phi2 = metallic_mean(2)  # Silver mean
        >>> float(phi2)
        2.414213562373095...
    """
    getcontext().prec = precision + 5
    n_dec = Decimal(n)
    sqrt_term = (n_dec**2 + Decimal(4)).sqrt()
    phi_n = (n_dec + sqrt_term) / Decimal(2)
    return +phi_n


def exceptional_family(k_max: int = 10) -> List[Tuple[int, int, int, Decimal]]:
    """
    Generate the exceptional family n = L_{2k-1}.

    Returns list of tuples: (k, 2k-1, n=L_{2k-1}, φ^{2k-1})

    This implements Corollary 2.7: Classification in Quadratic Fields.

    Args:
        k_max: Maximum k value (default 10)

    Returns:
        List of tuples with family parameters

    Examples:
        >>> family = exceptional_family(5)
        >>> [n for _, _, n, _ in family]
        [1, 4, 11, 29, 76]
    """
    family = []
    phi = golden_mean(precision=100)

    for k in range(1, k_max + 1):
        index = 2*k - 1
        n = lucas_number(index)
        phi_power = phi ** index
        family.append((k, index, n, phi_power))

    return family


def verify_errante_identity(k: int, precision: int = 50) -> Tuple[bool, Decimal, Decimal, Decimal]:
    """
    Verify Theorem 2.6: φ_{L_{2k-1}} = φ^{2k-1}

    Computes both sides and checks equality to specified precision.

    Args:
        k: Index in exceptional family
        precision: Verification precision

    Returns:
        (is_valid, phi_left, phi_right, difference)

    Examples:
        >>> valid, left, right, diff = verify_errante_identity(3)  # k=3, n=11
        >>> valid
        True
        >>> diff < Decimal('1e-45')
        True
    """
    getcontext().prec = precision + 10

    # Left side: φ_n where n = L_{2k-1}
    n = lucas_number(2*k - 1)
    phi_left = metallic_mean(n, precision=precision+5)

    # Right side: φ^{2k-1}
    phi = golden_mean(precision=precision+5)
    phi_right = phi ** (2*k - 1)

    # Check equality
    diff = abs(phi_left - phi_right)
    tolerance = Decimal(10) ** (-precision)
    is_valid = diff < tolerance

    return is_valid, phi_left, phi_right, diff


def verify_quadratic_field_classification(n: int) -> Tuple[bool, str]:
    """
    Verify Corollary 2.7: Check if φ_n ∈ ℚ(√5).

    This checks if √(n²+4) = m√5 for some integer m.

    Args:
        n: Integer to test

    Returns:
        (is_in_field, explanation)

    Examples:
        >>> verify_quadratic_field_classification(4)  # L_3
        (True, 'n=4=L_3, sqrt(20)=2*sqrt(5), F_3=2')
        >>> verify_quadratic_field_classification(2)  # Not exceptional
        (False, 'sqrt(8) not in Q(sqrt(5))')
    """
    import math

    val = n**2 + 4
    sqrt_val = math.sqrt(val)

    # Check if sqrt(n²+4) = m*sqrt(5)
    ratio_squared = val / 5
    ratio = math.sqrt(ratio_squared)

    if abs(ratio - round(ratio)) < 1e-10:
        m = round(ratio)
        # Verify it's F_{2k-1}
        for k in range(1, 20):
            if fibonacci_number(2*k - 1) == m:
                return (True, f'n={n}=L_{2*k-1}, sqrt({n**2+4})={m}*sqrt(5), F_{2*k-1}={m}')
        return (True, f'sqrt({n**2+4})={m}*sqrt(5), m={m}')
    else:
        return (False, f'sqrt({val}) not in Q(sqrt(5))')


def binet_formula_fibonacci(m: int, precision: int = 50) -> Decimal:
    """
    Compute F_m using Binet formula: F_m = (φ^m - (-φ)^{-m})/√5

    Theorem 2.3 implementation.
    """
    getcontext().prec = precision + 5
    phi = golden_mean(precision=precision+5)
    sqrt5 = Decimal(5).sqrt()

    term1 = phi ** m
    term2 = (-phi) ** (-m)
    F_m = (term1 - term2) / sqrt5
    return +F_m


def binet_formula_lucas(m: int, precision: int = 50) -> Decimal:
    """
    Compute L_m using Binet formula: L_m = φ^m + (-φ)^{-m}

    Theorem 2.3 implementation.
    """
    getcontext().prec = precision + 5
    phi = golden_mean(precision=precision+5)

    term1 = phi ** m
    term2 = (-phi) ** (-m)
    L_m = term1 + term2
    return +L_m


if __name__ == "__main__":
    # Run verification tests
    print("=" * 60)
    print("THEOREM 2.6 VERIFICATION: φ_{L_{2k-1}} = φ^{2k-1}")
    print("=" * 60)

    for k in range(1, 8):
        valid, left, right, diff = verify_errante_identity(k, precision=40)
        n = lucas_number(2*k - 1)
        status = "✓ VERIFIED" if valid else "✗ FAILED"
        print(f"k={k}: n=L_{2*k-1}={n}")
        print(f"  φ_n = {float(left):.15f}")
        print(f"  φ^{2*k-1} = {float(right):.15f}")
        print(f"  |diff| = {float(diff):.2e} {status}")
        print()

    print("=" * 60)
    print("COROLLARY 2.7: QUADRATIC FIELD CLASSIFICATION")
    print("=" * 60)

    test_values = [1, 2, 3, 4, 5, 11, 12, 29, 30, 76]
    for n in test_values:
        in_field, explanation = verify_quadratic_field_classification(n)
        symbol = "∈" if in_field else "∉"
        print(f"φ_{n} {symbol} ℚ(√5): {explanation}")
