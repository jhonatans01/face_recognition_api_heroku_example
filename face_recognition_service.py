import cv2
import dlib
import base64
from imutils import resize, face_utils
from urllib.parse import quote
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
def get_image_with_landmarks(file_path: str):
    rects = None
    gray = None
    clone = None

    try:
        image = cv2.imread(file_path, 1)
        image = resize(image, height=400)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clone = image.copy()
        rects = detector(gray, 1)

    except Exception:
        return {'error': 'Error while reading the image'}

    any_face_was_found = len(rects) > 0
    if any_face_was_found:
        for (i, rect) in enumerate(rects):
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            for point in range(1, 68):
                coords = shape.tolist()[point]
                cv2.circle(clone, (coords[0], coords[1]), 1, (0, 0, 255), thickness=2)
    else:
        return {'error': 'No face was detected in the image provided'}

    retval, buffer = cv2.imencode('.jpg', clone)
    image_as_text = base64.b64encode(buffer)

    return {'image_with_landmarks': 'data:image/png;base64,{}'.format(quote(image_as_text))}