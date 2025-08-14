import pytest
from panel_solver import solve_panel_cutting

def test_panel_cutting():
    result = solve_panel_cutting(
        stock_widths=[1000], stock_heights=[1000], 
        piece_widths=[300, 400], piece_heights=[300, 400], 
        quantities=[2, 2], kerf=2, trims=5
    )
    assert result['panels_used'] >= 1
    assert result['total_waste'] >= 0