from kreisaufgaben import *

radiusliste = list(map(float, input(
    "Geben sie einen oder mehere Radien ein (mit leerzeichen getrennt):").split()))
radius = 0
print(radiusliste)


if len(radiusliste) == 1:
    radius = radiusliste[0]
    flaecheKreis(radius)
    umfangKreis(radius)
else:
    summeUmfangKreis(radiusliste)
    summeFlaecheKreis(radiusliste)
