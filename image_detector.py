import cv2
import tensorflow as tf

# Loading the model
model = tf.keras.applications.MobileNetV2()

#opening pc webcamera
picture = cv2.VideoCapture(0)

#looping the frames in webcamera
while True:
    # Capture a frame from the webcam
    ret, frame = picture.read()

    # resizing the frame to match the input size to model
    resized_frame = cv2.resize(frame, (224, 224))

    # changing the frame to an array to be possessed by model
    input_frame = tf.keras.preprocessing.image.img_to_array(resized_frame)
    input_frame = tf.keras.applications.mobilenet_v2.preprocess_input(input_frame)

    # detecting the objects by using model
    predictions = model.predict(tf.expand_dims(input_frame, axis=0))
    detected_objects = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]

    # Print the name of the detected object
    print(detected_objects[0][1])

    # Display the detected object with name
    cv2.putText(frame, detected_objects[0][1], (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Object Detection', frame)

    # quit hte window by pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# closing all the windows
picture.release()
cv2.destroyAllWindows()
