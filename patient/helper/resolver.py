import tensorflow.keras
import numpy as np
from PIL import Image, ImageOps


np.set_printoptions(suppress=True)
model1 = tensorflow.keras.models.load_model('keras_model1.h5') #Arterialnaya_gipertenziya
model2 = tensorflow.keras.models.load_model('keras_model2.h5') #ONMK
model3 = tensorflow.keras.models.load_model('keras_model3.h5') #Serdechnaya_nedostatochnost
model4 = tensorflow.keras.models.load_model('keras_model4.h5') #Stenokardiya_IBS_infarkt_miokarda
model5 = tensorflow.keras.models.load_model('keras_model5.h5') #Prochie_zabolevaniya_serdca
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def open_image(dta):
    image = Image.open(dta.file)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    return normalized_image_array


def predict(value):
    data[0] = open_image(value)

    result1 = str(model1.predict(data)[0][1])
    result2 = str(model2.predict(data)[0][1])
    result3 = str(model3.predict(data)[0][1])
    result4 = str(model4.predict(data)[0][1])
    result5 = str(model5.predict(data)[0][1])

    json = {"model1": result1,
            "model2": result2,
            "model3": result3,
            "model4": result4,
            "model5": result5,
            }

    return json
