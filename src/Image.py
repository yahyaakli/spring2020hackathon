import cv2
import io
import os


from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".." #put your google API credintials here 

# Instantiates a client
client = vision.ImageAnnotatorClient()

#folder = "/uploads/"
class Image():
    def __init__(self):
        self.labels = []
        self.image = None

    def capture(self):
        # chi 7aja
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Camera")
        img_counter = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()
        self.image = img_name


    def capture_bis(self):
        # chi 7aja

        # initialize the camera
        cam = cv2.VideoCapture(0)  # 0 -> index of camera
        s, img = cam.read()
        img_counter = 0
        if s:  # frame captured without any errors
            #namedWindow("cam-test", CV_WINDOW_AUTOSIZE)
            #imshow("cam-test", img)
            cv2.waitKey(0)
            #destroyWindow("cam-test")
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, img)  # save image
        self.image = img_name

    def findLabels(self):
        # The name of the image file to annotate
        file_name = self.image

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        #self.labels = labels
        print('Labels:')
        for label in labels:
            print(label.description+', score: '+str(label.score))
            self.labels.append(label)



