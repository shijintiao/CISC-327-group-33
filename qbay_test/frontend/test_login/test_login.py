from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

'''
There are three test parts in the login test which are the
input test, output test and function test.
test_login_1 represents the test of input, test all possibilities
of input(one test case for each category)
test_login_2 represents the test of output, test all possibilities
of out(one test case for each category)
test_login_3 represents the test of function, to test the function,
we need to make sure that the user can login.
'''


def test_login_1():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_login_1.in'))
    expected_out = open(current_folder.joinpath(
        'test_login_1.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_login_2():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_login_2.in'))
    expected_out = open(current_folder.joinpath(
        'test_login_2.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_login_3():
    """capsys -- object created by pytest to
    capture stdout and stderr
    This is the error guese test
    Will input some unexcepeted input
    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_login_3.in'))
    expected_out = open(current_folder.joinpath(
        'test_login_3.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')

    print('outputs', output)
    assert output.strip() == expected_out.strip()
    