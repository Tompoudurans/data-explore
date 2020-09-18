import dataexplorer
import os.path
import pathlib
from randomdatagen import generate_random_testing_data


def test_make_log_file():
    """
    test to check that the function works and that a log file has been created
    """
    if os.path.isfile("secondtest.log"):
        log_file = pathlib.Path("secondtest.log")
        log_file.unlink()
    if not os.path.isfile("flight.db"):
        generate_random_testing_data(20)
    set = dataexplorer.load_sql("flight.db", "readings")
    stats = dataexplorer.get_stats(set)
    dataexplorer.make_log_file(stats, "secondtest.log")
    assert os.path.isfile("secondtest.log")
