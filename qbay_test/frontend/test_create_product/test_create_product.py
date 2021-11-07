from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


def test_create_product_1():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_create_product_1.in'))
    expected_out = open(current_folder.joinpath(
        'test_create_product_1.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')
    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_create_product_2():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_create_product_2.in'))
    expected_out = open(current_folder.joinpath(
        'test_create_product_2.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')
    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_create_product_3():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_create_product_3.in'))
    expected_out = open(current_folder.joinpath(
        'test_create_product_3.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')
    print('outputs', output)
    assert output.strip() == expected_out.strip()
