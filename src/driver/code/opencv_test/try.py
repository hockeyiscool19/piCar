import cv2

# GStreamer pipeline to capture video from /dev/video0
pipeline = "v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,format=BGR ! appsink"

cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error opening video stream or file")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame as needed here
        # For example, you can display it using cv2.imshow

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

