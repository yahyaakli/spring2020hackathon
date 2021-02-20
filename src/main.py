import io
import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Yahya/Downloads/hackathon-d17c6f5e9534.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate

file_name = 'C:/Users/Yahya/Documents/git/spring2020hackathon/uploads/1564684055231.jpeg'

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)
