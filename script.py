import cv2
import numpy as np
import easyocr

def adjust_contrast_brightness(img, contrast:float=1.0, brightness:int=0):
    brightness += int(round(255*(1-contrast)/2))
    return cv2.addWeighted(img, contrast, img, 0, brightness)

def image_preprocessing(image):
    image = adjust_contrast_brightness(image, 50)
    image = cv2.bitwise_not(image)
    return image

def split_by_strings(rects):
    rects = sorted(rects, key=lambda x: (x[0][1], x[0][0]))
    strings = []
    y_min = -1
    y_max = -1
    el = []
    for i in range(len(rects)):
        print(rects[i])
        if (rects[i][0][1] + rects[i][1][1]) / 2 >= y_min and (rects[i][0][1] + rects[i][1][1]) / 2 <= y_max:
            el.append(rects[i])
        else:
            if len(el) > 0:
                el = sorted(el, key=lambda x: x[0][0])
                strings.append(el[:])
                print(el)
                el = [rects[i]]
                y_min = rects[i][0][1]
                y_max = rects[i][1][1]
            else:
                el = [rects[i]]
                y_min = rects[i][0][1]
                y_max = rects[i][1][1]

    if len(el) > 0:
        el = sorted(el, key=lambda x: x[0][0])
        strings.append(el[:])
    return strings

def ocr_detector(image_path):
    reader = easyocr.Reader(['en', 'ru'])
    result = reader.readtext(image_path)
    font = cv2.FONT_HERSHEY_SIMPLEX
    rects = []
    for el in result:
        rects.append(((int(el[0][0][0]), int(el[0][0][1])), (int(el[0][2][0]), int(el[0][2][1]))))
    return split_by_strings(rects)

def split_image(strings, image_path, directory_path):
    my_file = open(directory_path + "requirements.txt", "w+")
    img = cv2.imread(image_path)
    y = 1
    x = 1
    my_file.write(str(len(strings)) + "\n")
    for row in strings:
        for col in row:
            top_left = col[0]
            bottom_right = col[1]
            crop_img = img[int(top_left[1]):int(bottom_right[1]), int(top_left[0]):int(bottom_right[0])]
            if not (crop_img is None):
                cv2.imwrite(directory_path + 'im' + str(y) + '_' + str(x) + '.jpg', crop_img)
                x += 1
        my_file.write(str(x - 1) + "\n")
        x = 1
        y += 1
    my_file.close()

def detect_strings(image_path, directory_path, preprocess=False):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if preprocess:
        image = image_preprocessing(image)
    cv2.imwrite(directory_path + 'im.jpg', image)
    strings = ocr_detector(directory_path + 'im.jpg')
    split_image(strings, image_path, directory_path)
    return 0
