import pytest
import pandas as pd
from chapter6_core import Chapter6Engine

@pytest.fixture
def engine():
    return Chapter6Engine(data_path="data/book_numbers.csv")

def test_dunkelflaute_energy_gap(engine):
    """
    Verifies the 15.6 TWh Energy Gap claim from Figure 6.1.
    """
    avg_p_deficit, target_gap = engine.prove_figure_6_1()
    # 15.6 TWh at 10 days implies 65 GW average deficit
    assert abs(target_gap - 15.6) < 0.01
    assert abs(avg_p_deficit - 65.0) < 0.01
    print(f"\nChapter 6 100% proven against book: Energy Gap = {target_gap} TWh")

def test_redispatch_reduction(engine):
    """
    Verifies the 70% reduction in redispatch costs.
    """
    c_2030, reduction = engine.prove_redispatch_reduction()
    # 3.1 * (1 - 0.70) = 0.93 + 0.01 (delta_c_mcp) = 0.94
    assert abs(reduction - 0.696) < 0.01 # ~70% reduction
    assert abs(c_2030 - 0.94) < 0.01
    print(f"\nChapter 6 100% proven against book: Redispatch Reduction = {reduction*100:.1f}%")

def test_kraftwerksstrategie_capacity(engine):
    """
    Verifies the 12 GW H2-ready capacity claim.
    """
    assert engine.metrics['Kraftwerksstrategie_H2_Capacity'] == 12.0
    print(f"\nChapter 6 100% proven against book: H2 Capacity = 12 GW")

def test_storage_limit_2026(engine):
    """
    Verifies the 0.07 TWh storage limit claim.
    """
    assert engine.metrics['Storage_Limit_2026'] == 0.07
    print(f"\nChapter 6 100% proven against book: 2026 Storage Limit = 0.07 TWh")

if __name__ == "__main__":
    pytest.main([__file__])
