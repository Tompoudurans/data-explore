import sqlalchemy as sa
import pandas as pd
import click
import logging


@click.command()
@click.option(
    "--target",
    help="Insert here the name of the database file that you want to import it needs to be in .db format",
)
@click.option(
    "--table", help="Insert here the table within the database that need to be analysed"
)
@click.option(
    "--output",
    help="Insert here the name of the output file, this name needs to end with .log",
)
def main(target, table, output):
    """
    reads data and saves basic stats for the dataset into a log file
    """
    data = load_sql(target, table)
    stats = get_stats(data)
    make_log_file(stats, output)


def load_sql(file, table):
    """
    loads an SQL table and saves on a pandas dataframe
    """
    engine = sa.create_engine("sqlite:///" + file)
    connection = engine.connect()
    database = pd.read_sql(table, connection)
    return database


def get_stats(data):
    """
    provides the basic stats for the dataset
    """
    return data.describe()


def make_log_file(data, filename):
    """
    makes a log file
    """
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s: \n%(message)s",
    )
    logging.info(data)


if __name__ == "__main__":
    main()
