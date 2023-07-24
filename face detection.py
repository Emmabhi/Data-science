import cv2
import numpy as np

# Load the YOLOv3 model
model = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load the input image
img = cv2.imread("image.jpg")

# Get the output layer names
layer_names = model.getLayerNames()
output_layer_names = [layer_names[i - 1] for i in model.getUnconnectedOutLayers()]

# Convert the image to a blob
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), (0, 0, 0), True, False)

# Set the input of the network
model.setInput(blob)

# Forward propagate the network
outs = model.forward(output_layer_names)

# Get the bounding boxes and confidence scores
boxes = []
confidences = []
class_ids = []

for out in outs:
    for detection in out:
        # Get the bounding box coordinates
        x, y, w, h = detection[0:4]
        confidence = detection[5]
        class_id = detection[6]

        # If the confidence is greater than the threshold,
        # draw the bounding box and add it to the list
        if confidence > 0.5:
            boxes.append([x, y, w, h])
            confidences.append(confidence)
            class_ids.append(class_id)

# Draw the bounding boxes on the image
for box in boxes:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()