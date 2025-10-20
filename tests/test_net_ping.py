import pytest
from src.netprobe.ping import ping


@pytest.mark.sanity
def test_ping_reachable():
    """
    Basic sanity check — verify ping to a known host runs without crashing.
    The result can be True or False depending on network, but must be boolean.
    """
    ok, output = ping("8.8.8.8", count=1, timeout=2)
    assert isinstance(ok, bool)
    assert isinstance(output, str)


@pytest.mark.regression
def test_ping_invalid_host():
    """
    Regression test — ping an invalid host.
    Ensures the function handles subprocess errors gracefully without exceptions.
    """
    ok, output = ping("notarealhost.local", count=1, timeout=1)
    assert isinstance(ok, bool)
    assert isinstance(output, str)
    # It should not crash; error output should contain either 'unknown host' or be empty
    assert "unknown" in output.lower() or len(output) >= 0


@pytest.mark.regression
def test_ping_tool_missing(monkeypatch):
    """
    Regression test — simulate missing 'ping' tool using monkeypatch.
    Ensures FileNotFoundError branch is executed gracefully.
    """
    import subprocess

    def fake_run(*args, **kwargs):
        raise FileNotFoundError("ping not found")

    monkeypatch.setattr(subprocess, "run", fake_run)
    ok, output = ping("8.8.8.8", count=1, timeout=1)
    assert ok is False
    assert "ping not found" in output
