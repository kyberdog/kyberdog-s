def complementing(s):
    s = list(s)
    comp = []
    for i in range(0, len(s)):
        if s[i] == "A":
            comp.append("T")
        elif s[i] == "T":
            comp.append("A")
        elif s[i] == "G":
            comp.append("C")
        elif s[i] == "C":
            comp.append("G")
    comp = list(reversed(comp))
    return comp

s = "AAAACCCGGT"
complemented = complementing(s)
print(*complemented, sep="")
