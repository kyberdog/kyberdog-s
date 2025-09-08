def count_nucleotides(s):
    assert isinstance(s, str), "input parametre is string"
    #checking if s is string
    total = [s.count("A"), s.count("C"), s.count("G"), s.count("T")]
    #counting nucleotides
    return total
    


s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
counted = count_nucleotides(s)
print(*counted)
# * is operator that unpacks iterable objects