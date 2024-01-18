import cv2
import cvlib
from cvlib.object_detection import draw_bbox

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    bbox, level, conf = cvlib.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, level, conf)
    cv2.imshow("Object detected", output_image)
    print(level)
    is_found = 0
    for item in level:
        if item == "person":
            is_found = 1
    if is_found == 1:
        print("Person Detected")
    is_found = 0
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
