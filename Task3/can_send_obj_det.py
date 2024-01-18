import can
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
        with can.Bus(
            interface="socketcan", channel="can0", receive_own_messages=True
        ) as bus:
            # send a message
            message = can.Message(
                arbitration_id=291, is_extended_id=False, data=[0x1, 0x22, 0x33]
            )
            bus.send(message, timeout=0)
    else:
        with can.Bus(
            interface="socketcan", channel="can0", receive_own_messages=True
        ) as bus:
            # send a message
            message = can.Message(
                arbitration_id=291, is_extended_id=False, data=[0x00, 0x22, 0x33]
            )
            bus.send(message, timeout=0)
        print("Person not Detected")
    is_found = 0
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
