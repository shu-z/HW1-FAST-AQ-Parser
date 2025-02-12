# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    transcribed=transcribe('ATCGTCGATCG')

    assert transcribed == 'UAGCAGCUAGC', 'Transcribed sequence not as expected'

 


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """

    reverse_transcribed=reverse_transcribe('ATCGTCGATCG')

    assert reverse_transcribed == 'CGAUCGACGAU', 'Reverse transcribed sequence not as expected'



