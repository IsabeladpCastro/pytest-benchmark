import subprocess
import sys

def test_main_module_execution():
    """
    Testa se a chamada do modulo via linha de comando funciona corretamente.
    Isso aumenta a cobertura do arquivo src/pytest_benchmark/__main__.py
    """
    result = subprocess.run(
        [sys.executable, "-m", "pytest_benchmark", "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    assert result.returncode == 0
    assert "usage" in result.stdout.lower() or "pytest-benchmark" in result.stdout
