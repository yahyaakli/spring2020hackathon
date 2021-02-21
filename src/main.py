import io
import os

from google.cloud import vision
from PIL import Image
import glob
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../uploads/hackathon-d17c6f5e9534.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate

file_name = os.path.abspath(r"C:\Users\Nabil Berjaoui\Documents\spring2020hackathon\uploads\istockphoto-1163967091-1024x1024.jpg")

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description+str(label.score))
