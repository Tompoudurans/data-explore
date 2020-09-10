import dataexplorer
import os.path
import pathlib
from randomdatagen import generate_random_testing_data


def test_make_log_file():
    if not os.path.isfile("flight.db"):
        generate_random_testing_data(20)
    set = dataexplorer.load_sql("flight", "readings")
    stats = dataexplorer.get_stats(set)
    dataexplorer.make_log_file(stats, "testing")
    assert os.path.isfile("testing.log")
