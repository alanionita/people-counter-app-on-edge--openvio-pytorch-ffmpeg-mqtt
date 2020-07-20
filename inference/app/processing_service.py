from cv2 import rectangle, imread, resize


def preprocessing(input_image, input_shape):
    _, _, h, w = input_shape
    image = resize(input_image, (w, h))
    image = image.transpose((2, 0, 1))
    image = image.reshape(1, *image.shape)
    print('Preprocesing complete!')
    return image


def draw_boxes(frame, result, args, width, height):
    print('result ::: ', result)
    for box in result[0][0]:  # Output shape is 1x1x100x7
        print('box ::: ', box)
        conf = box[2]
        if conf >= 0.5:
            xmin = int(box[3] * width)
            ymin = int(box[4] * height)
            xmax = int(box[5] * width)
            ymax = int(box[6] * height)
            rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
    return frame
