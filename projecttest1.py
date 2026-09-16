import numpy as np
from PIL import Image
import keras

MODEL_PATH = "skin_lesion_cnn_model.h5"
IMAGE_SIZE = (32, 32)


_model = None


def _load_model():
    """Load the trained CNN model once and reuse it."""
    global _model

    if _model is None:
        _model = keras.models.load_model(MODEL_PATH)

    return _model


def detect(file):
    """
    Classify an uploaded skin-lesion image.

    Parameters
    ----------
    file:
        Uploaded image file accepted by PIL.Image.open().

    Returns
    -------
    int
        Predicted class index from 0 to 6.
    """
    image = Image.open(file).convert("RGB")
    image = image.resize(IMAGE_SIZE)

    image_array = np.asarray(image, dtype=np.float32)
    image_array /= 255.0

    model = _load_model()
    predictions = model.predict(
        np.expand_dims(image_array, axis=0),
        verbose=0
    )

    predicted_class = int(np.argmax(predictions, axis=1)[0])

    return predicted_class
