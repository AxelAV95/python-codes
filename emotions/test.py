'''

Versión de Python necesaria: Python 3.9.0

Módulos necesarios:

pip install tensorflow (algo pesado)
pip install keras
pip install numpy
pip install opencv-python


'''

#En terminal escribir python test.py para ejecutar

from keras.models import load_model #Importa la función load_model para cargar un modelo de red neuronal
from time import sleep #Importa la función sleep para pausar el programa temporalmente
from keras.preprocessing.image import img_to_array # Importa funciones para procesar imágenes
from keras.preprocessing import image
import cv2 #Importa la biblioteca OpenCV para el procesamiento de imágenes y la detección de caras
import numpy as np #Importa la biblioteca NumPy para operaciones matriciales

#Carga un clasificador en cascada preentrenado para la detección de caras desde un archivo XML, 
#dado por OpenCV
face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

#Carga un modelo de red neuronal previamente entrenado para la detección de emociones desde un archivo
classifier =load_model('./emociones.h5') 

#Define una lista de etiquetas de clases de emociones
class_labels = ['Enojado','Feliz','Neutro','Triste','Sorprendido']

#Abre una conexión con la cámara web del sistema
cap = cv2.VideoCapture(0)

while True:
    # Obtener un frame del video
    ret, frame = cap.read() #se captura continuamente un solo fotograma de video desde la cámara web
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #La imagen capturada se convierte a escala de grises (gray) para facilitar el procesamiento
    faces = face_classifier.detectMultiScale(gray,1.3,5) #Se utiliza el clasificador en cascada de Haar para detectar caras en la imagen en escala de grises.


    # Se itera sobre las caras detectadas
    for (x,y,w,h) in faces:
        #Se dibuja un rectángulo alrededor de cada cara detectada en la imagen original
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w] #Se recorta la región de interés (ROI) de la cara en escala de grises
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA) #La ROI se redimensiona a 48x48 píxeles para que coincida con el tamaño de entrada esperado por el modelo de detección de emociones

    #Se normaliza la ROI y se prepara para la clasificación
        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

        # Se realiza una predicción de emociones en la ROI utilizando el modelo de red neuronal previamente cargado (classifier.predict(roi))

            preds = classifier.predict(roi)[0]
            print("\nprediction = ",preds)
            label=class_labels[preds.argmax()]
            print("\nprediction max = ",preds.argmax())
            print("\nlabel = ",label)
            label_position = (x,y) #La etiqueta de emoción predicha se muestra en la esquina superior izquierda del rectángulo que rodea la cara
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_DUPLEX ,0.7,(0,255,0),1)
        else:
            #Si no se detecta una cara en una región, se muestra el mensaje 
            cv2.putText(frame,'Ningún rostro detectado',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        print("\n\n")
         
    nombre_position = (10, 30)  # Coordenadas para la posición del texto
    cv2.putText(frame, "Axel A.V", nombre_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imshow('Detector de emociones',frame) #La imagen procesada con las etiquetas de emociones se muestra en una ventana 
    if cv2.waitKey(1) & 0xFF == ord('q'): #El bucle se ejecuta hasta que se presiona la tecla 'q'
        break

#Cuando se presiona 'q', se liberan los recursos de la cámara (cap.release()) y 
#se cierra la ventana de visualización (cv2.destroyAllWindows())
cap.release()
cv2.destroyAllWindows()


























