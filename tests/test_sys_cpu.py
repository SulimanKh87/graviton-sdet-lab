import pytest
from src.sysprobe.cpu import cpu_info, has_flag

@pytest.mark.sanity
def test_cpu_model_present():
    info = cpu_info()
    assert any("Model" in k or "model" in k for k in info.keys())

@pytest.mark.regression
@pytest.mark.parametrize("flag", ["sse2", "avx", "neon"])
def test_cpu_flags_boolean(flag):
    assert isinstance(has_flag(flag), bool)
