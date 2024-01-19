pirates = input("How many pirates:")
totalUnits = input("How many units:")

tax = (3 * (int(pirates) - 2))
yonduShare = (round((int(totalUnits) - tax) * .13, 2))
quillShare = (round((int(totalUnits) - (float(yonduShare) + tax)) * .11, 2))
crewShare = (round((int(totalUnits) - int(tax) - float(yonduShare) - float(quillShare)) / int(pirates), 2))

yonduString = f"Yondu's share: {yonduShare + crewShare: .2f}"
quillString = f"Peter's  share: {quillShare + crewShare: .2f}"
crewString = f"Crew's share: {3 + crewShare: .2f}"

print(yonduString)
print(quillString)
print(crewString)