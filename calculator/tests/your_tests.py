import subprocess

def test_addition():
    result = subprocess.run(["./calculator", "2", "+", "3"], capture_output=True, text=True)
    assert "5" in result.stdout

def test_multiplication():
    result = subprocess.run(["./calculator", "4", "*", "5"], capture_output=True, text=True)
    assert "20" in result.stdout
