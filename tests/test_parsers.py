# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    #read in fasta test file
    fasta_obj=FastaParser('./data/test.fa')
    fasta_seqs=[x for x in fasta_obj]

    # see if first line of fasta is the same 
    first_line='TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    assert fasta_seqs[0][1]==first_line, 'First sequence is incorrect'
    assert fasta_seqs[0][0] == 'seq0', 'First sequence name is incorrect'
    assert len(fasta_seqs[0]) == 2, 'Does not have two elements in tuple'
    assert len(fasta_seqs) == 100, '# sequences read in does not match'






def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    #read in fastq test file
    fastq_obj=FastqParser('./data/test.fq')
    fastq_seqs=[x for x in fastq_obj]

    first_line='TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    first_qual='*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='
    # see if first line of fasta is the same 
    assert fastq_seqs[0][1]==first_line, 'First sequence is incorrect'
    assert fastq_seqs[0][0] == 'seq0', 'First sequence name is incorrect'
    assert fastq_seqs[0][2]==first_qual, 'First quality score is incorrect'
    assert len(fastq_seqs[0]) == 3, 'Does not have three elements in tuple'
    assert len(fastq_seqs) == 100, '# sequences read in does not match'



    #see if quality score is correct 


