import cv2

def preprocessing(input_image, input_shape):
    _, _, h, w = input_shape
    image = cv2.imread(input_image)
    image = cv2.resize(image, (w, h))
    image = image.transpose((2, 0, 1))
    image = image.reshape(1, 3, h, w)
    print('Preprocesing complete!')
    return image