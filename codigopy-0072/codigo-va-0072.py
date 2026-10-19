# catherine eileen huerta rascon NC = 0072
# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os 
ruta_imagen = os.path.join(
    "img-original-0072",
    "hyundai.jpg"
)

hyundai = cv2.imread(ruta_imagen)
hyundai = cv2.cvtColor(hyundai, cv2.COLOR_BGR2RGB)
print(hyundai)
cv2.imshow("hyundai original 0072", hyundai)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("catherine eileen huerta rascon NC = 0072")