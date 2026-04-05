'''Lab 11 Programming Assignment
Darian Marie Bruce
This program tests the provided module
is working as intended
04/05/2026'''

import pytest

from rotation_utils import adjust_rotation

def test_adjust_rotation_100() -> None:
    '''verifies that a valid angle is returned unchanged'''
    assert adjust_rotation(100) == 100

def test_adjust_rotation_460() -> None:
    '''verifies that large positive angles are read correctly'''
    assert adjust_rotation(460) == 100

def test_adjust_rotation_820() -> None:
    '''verifies that large positive angles are read correctly'''
    assert adjust_rotation(820) == 100

def test_adjust_rotation_negative_100() -> None:
    '''verifies that negative angles are converted to the positive equivalent'''
    assert adjust_rotation(-100) == 260

def test_adjust_rotation_negative_460() -> None:
    '''verifies that large negative angles are correct'''
    assert adjust_rotation(-460) == 260

def test_adjust_rotation_negative_820() -> None:
    '''Verify that large negative angles are correct'''
    assert adjust_rotation(-820) == 260

def test_adjust_rotation_invalid_input() -> None:
    '''Verify that non float input raises a type error'''
    with pytest.raises(TypeError):
        adjust_rotation("string")

