def transcribing(t): #t is dna
    assert isinstance(t, str), "t is string"
    #checking if t is string
    rna = t.replace("T", "U")
    return rna

t = "GATGGAACTTGACTACGTAAATT"
print(transcribing(t))