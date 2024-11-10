# Input data; Resistances and Temperatures should be equal in size.
Resistances = [7.575, 7.495, 7.377, 7.244, 7.09, 6.907, 6.685, 6.397, 5.991, 5.704]
Temperatures = [1/23, 1/25, 1/28, 1/31, 1/35, 1/40, 2/81, 1/53, 2/121, 1/74]

# Preparing for Summation Terms
ResistancesSquared = []
for i in Resistances:
    ResistancesSquared.append(i**2)

ResTemp = []
for i,j in zip(Resistances, Temperatures):
    ResTemp.append(i*j)

# Summation Terms
SumSxx = sum(ResistancesSquared)
SumSy = sum(Temperatures)
SumSx = sum(Resistances)
SumS = len(Resistances)
SumSxy = sum(ResTemp)

# Coefficient Terms
CoeffD = (SumS * SumSxx) - ((SumSx)**2)
CoeffA = ((SumS * SumSxy) - (SumSx * SumSy)) / CoeffD
CoeffB = ((SumSxx * SumSy) - (SumSxy * SumSx)) / CoeffD

print(f"Coefficient A: {CoeffA}")
print(f"Coefficient B: {CoeffB}")