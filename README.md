# Face Emotion Recognition

Deployed Web App:  https://emotion-recogni.herokuapp.com/



Instructions to run the emotion recognition app on local server: 

Directory Structure:
- env: Virtual Environment containing all the dependencies
- templates: Folder containing HTML files
- static: Folder used to save initial image, cropped image and final image
- app.py: File containing code for web app 
- FER_CNN_Model.ipynb: Notebook containing CNN implementation
- fer_model.hdf5: saved model architecture and weights (best model achieved from FER_CNN_Model.ipynb)
- requirements.txt: List of dependencies to be installed
- haarcascade_frontalface_default.xml: File to detect faces

1. Open command line and type the following commands to create and activate virtual environment: 
  - virtualenv env
  - call env/Scripts/activate
2. Install required libraries using requirements file: 
  - pip install -r requirements.txt
3. Run the application on local host:
  - python app.py
4. Enter the local host in the browser
