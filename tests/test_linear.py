import pytest
from linear_solver import solve_linear_cutting

def test_linear_cutting():
    result = solve_linear_cutting(
        stock_lengths=[1000], cut_lengths=[300, 400], quantities=[2, 2], kerf=2, trims=5
    )
    assert result['stocks_used'] >= 1
    assert result['total_waste'] >= 0