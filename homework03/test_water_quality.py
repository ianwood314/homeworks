from water_quality import calc_avg_turbidity, time_to_safe_threshold
import pytest

def test_calc_avg_turbidity():
    assert calc_avg_turbidity([{'a': 1, 'b': 1}, {'a': 1, 'b': 1}, {'a': 1, 'b': 1}], 'a', 'b') == 1.0
    assert calc_avg_turbidity([{'a': 1, 'b': 1}, {'a': 1, 'b': 1}, {'a': 2, 'b': 2}], 'a', 'b') == 2.0
    assert isinstance(calc_avg_turbidity([{'a': 1, 'b': 2}, {'a': 2, 'b': 4}], 'a', 'b'), float) == True 

def test_calc_avg_turbidity_exceptions():
    with pytest.raises(ZeroDivisionError):
        calc_avg_turbidity([], 'a', 'b') 
    with pytest.raises(KeyError):
        calc_avg_turbidity([{'a': 1, 'b': 2}, {'a': 2, 'b': 4}], 'a', 'c')

def test_time_to_safe_threshold():
    assert time_to_safe_threshold(0.7) == 0.
    assert time_to_safe_threshold(1.2) > 0.
    assert isinstance(time_to_safe_threshold(10), float) == True

def test_time_to_safe_threshold_exceptions():
    with pytest.raises(ValueError):
        time_to_safe_threshold(-10.)
    with pytest.raises(ValueError):
        time_to_safe_threshold(0)

