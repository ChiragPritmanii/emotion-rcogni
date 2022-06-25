from flask import Flask, render_template, request
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after', methods=['GET', 'POST'])
def after():
    img = request.files['file1']

    img.save('static/file.jpg')

    ####################################
    img = cv2.imread('static/file.jpg')
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = cascade.detectMultiScale(img, 1.32, 5)

    for x,y,w,h in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

        cropped = img[y:y+w, x:x+h, : ]

    cv2.imwrite('static/after.jpg', img)

    try:
        cv2.imwrite('static/cropped.jpg', cropped)

    except:
        pass

    #####################################

    try:
        img = cv2.imread('static/cropped.jpg', 0)
    except:
        img = cv2.imread('static/file.jpg', 0)

    
    img = cv2.resize(img, (48,48))

    img_pixels = image.img_to_array(img)
    img_pixels = np.dstack([img_pixels,img_pixels,img_pixels])
    img_pixels = np.expand_dims(img_pixels, axis = 0)
        

    model = load_model('fer_model.hdf5')

    prediction = model.predict(img_pixels)

    label_map = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral','Sad', 'Surprise'] 

    prediction = np.argmax(prediction[0])

    final_prediction = label_map[prediction]

    return render_template('after.html', data=final_prediction)

if __name__ == "__main__":
    app.run(debug=True)