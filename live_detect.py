# Importa la biblioteca opencv
import cv2

# Define un objeto video capture
vid = cv2.VideoCapture(0)

while(True):
   
    # Captura el video cuadro por cuadro
    ret, frame = vid.read()

    # Muestra el cuadro de resultado
    cv2.imshow("Web cam", frame)
      
    # Cierra la ventana con la tecla espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, libera el objeto capturado
vid.release()

# Cierra todas las ventanas
cv2.destroyAllWindows()