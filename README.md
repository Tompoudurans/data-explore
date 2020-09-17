## A tool to capture information about the general structure of tables within an sql database

The tool computes:
the number of records in a table of a given database (count), the mean value of all records in the table (mean) as well as their standard deviation (std), and their (0%, 25%, 50%, 75%, 100%) quartile

### Required softwares

To be able to install the software, it is necessary first to have a version of git (any version)
as well as a version of python 3.7 or 3.8 (this software has not been tested for further versions).
Also its is important that pip is installed.

### Installation

#### Basic software requirements

To install, the following is assumed to be available:

- Python 3.7 or 3.8 (the software might work on other versions but it is only tested on 3.7 or 3.8).
- A recent version of git.

If those are not available please get in touch with the maintainer for alternative ways of installing.

#### Virtual environment

It is recommended to run the software using a Python virtual environment (this ensures that different dependencies are isolated).

To setup the environment, run the following in a command line tool:

    $ python -m venv data-explore

Once the virtual environment is created, it needs to be activated with the following commands:

On Windows, run:

    C:\> data-explore\Scripts\activate.bat

On unix (linux or OS X):

    source data-explore/bin/activate

#### Installation

The following commands will download and install the software

    $ git clone https://github.com/Tompoudurans/data-explore
    $ cd data-explore
    $ python setup.py develop


To confirm installation was successful run the following:

    $ python -m dataexplorer --help

### Utilisation

After installation,
For any `<table>` within a `<database>` sql file, the tool can be run entering the following command:

    $ python -m dataexplorer --target=<database> --table=<table> --output=<log>

The `<log>` file  produced by this command will contain all the information about the general structure of the `<table>` held in <`database`>.

### Test

The tool is tested using the Python testing framework pyrest. To install pytest:

    $ python -m pip install pytest
    
To run the tests:    

    $  python -m pytest -p no:logging
