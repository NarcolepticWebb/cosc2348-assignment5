import subprocess

def run_test(args, expected):
    result = subprocess.run(
        ["../calculator"] + args,
        capture_output=True,
        text=True
    )
    print("TEST RUN:", " ".join(args))
    assert expected in result.stdout

run_test(["2", "+", "3"], "5")
run_test(["10", "-", "4"], "6")
