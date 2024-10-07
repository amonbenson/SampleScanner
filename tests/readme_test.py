import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

import pytest
import subprocess


def readme_contentsof(name):
    with open('README.md') as readme:
        return (
            readme.read()
                  .split('```contentsof<%s>' % name)[1]
                  .split('```')[0]
                  .strip()
        )


def command_line_output_in_readme():
    return readme_contentsof('samplescanner -h')


def license_output_in_readme():
    return readme_contentsof('cat LICENSE')


def expected_command_line_output():
    return subprocess.check_output(
        ['./samplescanner', '-h'],
        stderr=subprocess.STDOUT,
    ).strip()


def expected_license():
    with open('LICENSE') as license:
        return license.read().strip()


@pytest.mark.skipif(
    sys.platform == 'win32',
    reason='./samplescanner script does not work on Windows',
)
def test_readme_contains_proper_command_line_output():
    assert command_line_output_in_readme() == expected_command_line_output()


@pytest.mark.skipif(
    sys.platform == 'win32',
    reason='./samplescanner script does not work on Windows',
)
def test_readme_contains_content_of_license():
    assert license_output_in_readme() == expected_license()
