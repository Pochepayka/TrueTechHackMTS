import cv2 as cv
import numpy as np
import os

# Изменение яркости кадра
def brightness_processing(frame, brightness, frame_size=None):
    result = cv.addWeighted(frame, 1.0, frame, 0, brightness - 50)
    result = cv.resize(result, frame_size)
    return result

# Изменение контраста кадра
def contrast_processing(frame, contrast, frame_size=None):
    result = cv.addWeighted(frame, contrast, frame, 0, 0)
    result = cv.resize(result, frame_size)
    return result

# Изменение насыщенности кадра
def saturation_processing(frame, saturation, frame_size=None):
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv_frame[...,1] = np.clip(hsv_frame[...,1] * saturation, 0, 255)
    result = cv.cvtColor(hsv_frame, cv.COLOR_HSV2BGR)
    result = cv.resize(result, frame_size)
    return result

# Изменение резкости кадра
def sharpness_processing(frame, sharpness, frame_size=None):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    result = cv.filter2D(frame, -1, kernel*sharpness)
    result = cv.resize(result, frame_size)
    return result

def format(videoPath, brightness, contrast, saturation, sharpness):
    # Значения яркости, контраста, насыщенности и резкости по умолчанию
    DEFAULT_BRIGHTNESS = 50
    DEFAULT_CONTRAST = 50
    DEFAULT_SATURATION = 50
    DEFAULT_SHARPNESS = 50

    cap = cv.VideoCapture(videoPath)
    # Кол-во фпс
    fps = int(cap.get(cv.CAP_PROP_FPS))
    # Разрешение
    frame_size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

    # Формируем имя выходного файла
    output_filename = videoPath[:len(videoPath) - 4] + '_new.mp4'

    # Используем графический процессор для записи видео
    # fourcc = cv.VideoWriter_fourcc(*'H264')
    fourcc = cv.VideoWriter_fourcc(*'mp4v')

    out = cv.VideoWriter(output_filename, fourcc, fps, frame_size, True)

    # Цикл с обработкой видео
    while cap.isOpened():
        # ret - T - если прочитал кадр, F - если не прочитал
        # frame - кадр(массив пикселей)
        # Читаем текущий кадр
        ret, frame = cap.read()
        if ret:  # Если успешно прочёл кадр
            # Изменяем яркость входного кадра, если значение не равно стандартному
            if brightness != DEFAULT_BRIGHTNESS:
                frame = brightness_processing(frame, brightness, frame_size=frame_size)
            # Изменяем контраст входного кадра, если значение не равно стандартному
            if contrast != DEFAULT_CONTRAST:
                frame = contrast_processing(frame, contrast / 50, frame_size=frame_size)
            # Изменяем насыщенность входного кадра, если значение не равно стандартному
            if saturation != DEFAULT_SATURATION:
                frame = saturation_processing(frame, saturation / 50, frame_size=frame_size)
            # Изменяем резкось входного кадра, если значение не равно стандартному
            if sharpness != DEFAULT_SHARPNESS:
                frame = sharpness_processing(frame, sharpness / 50, frame_size=frame_size)
            out.write(frame)
        else:
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()

videoPath2 = 'static/video/example.mp4'
videoPath1 = 'static/video/mem.mp4'
videoPath0 = 'static/video/epil.mp4'
videoPath3 = 'static/video/primer1.mp4'
videoPath4 = 'static/video/primer2.mp4'

# Пользовательские значения яркости, контраста и насыщенности
brightness = int(input("Введите уровень яркости (от 0 до 100): "))
contrast = float(input("Введите уровень контраста (от 0 до 100): "))
saturation = float(input("Введите уровень насыщенности (от 0 до 100): "))
sharpness = float(input("Введите значение резкости (от 0 до 100): "))


