# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """

    transcription_dict = {"A":"U", "C":"G", "G":"C", "T":"A"}

    if isinstance(seq, str) is False:
        raise ValueError('Seq must be type string')

    if len(seq)==0:
        raise ValueError('Seq cannot be empty string')

    
    seq=seq.upper()
    transcribed="".join(map(transcription_dict.get, seq))
    return(transcribed)
        

  


def reverse_transcribe(seq: str) -> str:

    """
    transcribes DNA to RNA then reverses
    the strand
    """

    transcribed=transcribe(seq)

    return(transcribed[::-1])
