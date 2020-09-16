import subprocess
import dataexplorer
import os
import pathlib
from randomdatagen import generate_random_testing_data


def test_help():
    exp_output = b"""Usage: __main__.py [OPTIONS]

  reads data and saves basic stats for the dataset into a log file

Options:
  --target TEXT  Insert here the name of the database file that you want to
                 import it needs to be in .db format

  --table TEXT   Insert here the table within the database that need to be
                 analysed

  --output TEXT  Insert here the name of the output file, this name needs to
                 end with .log

  --help         Show this message and exit.
"""
    current_output = subprocess.run(
        ["python", "-m", "dataexplorer", "--help"], capture_output=True
    )
    if os.name == "nt":
        exp_output = exp_output.replace(b"\n", b"\r\n")
    assert current_output.stdout == exp_output


def test_main_func():
    if os.path.isfile("testing.log"):
        log_file = pathlib.Path("testing.log")
        log_file.unlink()
    if not os.path.isfile("flight.db"):
        generate_random_testing_data(20)
    out = subprocess.run(
        [
            "python",
            "-m",
            "dataexplorer",
            "--target=flight.db",
            "--table=readings",
            "--output=testing.log",
        ]
    )
    assert out.returncode == 0
    assert os.path.isfile("testing.log")
    assert os.stat("testing.log").st_size > 0
