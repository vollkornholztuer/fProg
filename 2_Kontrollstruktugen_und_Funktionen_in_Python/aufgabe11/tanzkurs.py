import math

damen = ['dame1', 'dame2', 'dame3', 'dame4']
herren = ['herr1', 'herr2', 'herr3', 'herr4']
tanzlehrer = ['tanzlehrer1']

damenLength = len(damen)
herrenLength = len(herren)
tanzlehrerLength = 1

menge1 = math.pow(damenLength, herrenLength)
menge2 = math.pow(herrenLength, damenLength)
menge3 = damenLength + herrenLength

menge = menge1 + menge2 + menge3
print(menge)
