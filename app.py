# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np


app = Flask(__name__)

# Open and redirect to default upload webpage
@app.route('/')
def load_form():
    return render_template('upload.html')

# Function to upload image and redirect to new webpage
@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    
    fileData = make_grayscale(file.read())
    with open(os.path.join('static/',filename),
        'wb') as f:
        f.write(fileData)


        # ends here

    display_message = 'Image successfully uploaded and displayed below'
    return render_template('upload.html', filename=filename, message = display_message)


def make_grayscale(input_image):
    imageArray = np.fromstring(input_image, dtype='uint8')
    print("Image Array:",imageArray)

    decodeArrayToImg = cv2.imdecode(imageArray, cv2.IMREAD_UNCHANGED)
    print(decodeArrayToImg)

    convertedImage = cv2.cvtColor(decodeArrayToImg,cv2.COLOR_RGB2GRAY)
    status, outputImage = cv2.imencode('.PNG',convertedImage)
    print("Status:",status)

    return outputImage

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))



if __name__ == "__main__":
    app.run()


