import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

from lib.utils import note_name, note_number


def test_note_name():
    assert 'C4' == note_name(60)
    assert 'Db4' == note_name(61)
    assert 'D4' == note_name(62)
    assert 'Eb4' == note_name(63)
    assert 'E4' == note_name(64)
    assert 'F4' == note_name(65)
    assert 'Gb4' == note_name(66)
    assert 'G4' == note_name(67)
    assert 'Ab4' == note_name(68)
    assert 'A4' == note_name(69)
    assert 'Bb4' == note_name(70)
    assert 'B4' == note_name(71)


def test_note_number():
    assert 60 == note_number('C4')
    assert 60 == note_number('c4')
    assert 61 == note_number('Db4')
    assert 61 == note_number('db4')
    assert 62 == note_number('D4')
    assert 62 == note_number('d4')
    assert 63 == note_number('Eb4')
    assert 63 == note_number('eb4')
    assert 64 == note_number('E4')
    assert 64 == note_number('e4')
    assert 65 == note_number('F4')
    assert 65 == note_number('f4')
    assert 66 == note_number('Gb4')
    assert 66 == note_number('gb4')
    assert 67 == note_number('G4')
    assert 67 == note_number('g4')
    assert 68 == note_number('Ab4')
    assert 68 == note_number('ab4')
    assert 69 == note_number('A4')
    assert 69 == note_number('a4')
    assert 70 == note_number('Bb4')
    assert 70 == note_number('bb4')
    assert 71 == note_number('B4')
    assert 71 == note_number('b4')
