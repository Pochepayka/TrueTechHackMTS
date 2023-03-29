import cv2 as cv
import numpy as np
from google.cloud import storage
import os

videoPathName = 'file.mp4'
videoPath1 = 'static/video/film1.mp4'
videoPath2 = 'static/video/film2.mp4'
videoPath3 = 'static/video/film3.mp4'
videoPath4 = 'static/video/film4.mp4'
videoPath5 = 'static/video/film5.mp4'

threshold = 20000000 #максимальнодопустимая "тряска"
maxCountColor = 100 #максимальнодопустимое изменение цвета
maxCountArea = 2 #максимальнодопустимое изменение площади

# Функция определения смещения изображения между кадрами
def get_frame_diff(prev_frame, cur_frame, next_frame):
    # Convert frames to grayscale
    prev_frame_blur = createGray(prev_frame)
    cur_frame_blur = createGray(cur_frame)
    next_frame_blur = createGray(next_frame)

    # находим смещение
    diff_frames_1 = cv.absdiff(next_frame_blur, cur_frame_blur)
    diff_frames_2 = cv.absdiff(cur_frame_blur, prev_frame_blur)

    # накладываем два смещения друг не друга
    diff_frames = cv.addWeighted(diff_frames_1, 0.5, diff_frames_2, 0.5, 0)
    return diff_frames


def createGray(frame):
    #определяем границы цвета
    hsvMin = np.array((2, 2, 5), np.uint8)
    hsvMax = np.array((255, 255, 255), np.uint8)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    returnFrameHsv = cv.inRange(hsv, hsvMin, hsvMax)  # применяем цветовой фильтр"""
    returnFrameBlurHsv = cv.GaussianBlur(returnFrameHsv, (3, 3), 0)
    return returnFrameHsv


def epilepsion(Path):
    # загружаем видеофайл
    video = cv.VideoCapture(Path)

    # устанавливаем количество кадров в секунду
    fps = int(video.get(cv.CAP_PROP_FPS))

    # создаем объект VideoWriter
    output_filename = Path[:13] + 'Epilepsion/' + Path[13:]
    writer = cv.VideoWriter(output_filename, cv.VideoWriter_fourcc(*'mp4v'), fps,
                             (int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT))))

    #первый кадр
    ret, prev_frame = video.read()
    #второй кадр
    ret, cur_frame = video.read()
    countCadrs =2
    while True:
        # считываем кадр из видео
        ret, next_frame = video.read()

        # если кадры закончились, завершаем цикл
        if not ret:
            break
        # понимание с кем имеем дело
        print("Файл:",Path)

        # обновление примерного количества кадров
        countCadrs += 1
        print("Время:",countCadrs/20)

        # определение параметров кадра
        x, y, w, h = 0, 0, int(video.get(cv.CAP_PROP_FRAME_WIDTH)), \
                     int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

        # ищем контуры и отображаем
        thresh = createGray(prev_frame)
        prev_contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #cv.drawContours(cur_frame, prev_contours, -1, (255, 0, 0), 1)

        thresh = createGray(cur_frame)
        cur_contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(cur_frame, cur_contours, -1, (0, 255, 0), 2)

        thresh = createGray(next_frame)
        next_contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #cv.drawContours(cur_frame, next_contours, -1, (0, 0, 255), 1)




        """!!!!!!!!!!!!!!!!FILTER-FIRST!!!!!!!!!!!!!!!!!!"""
        # определение среднего цветового значения кадра
        prev_mean_color = cv.mean(prev_frame)
        prev_mean_color =(max(prev_mean_color[0], 1), max(prev_mean_color[1], 1), max(prev_mean_color[2], 1))

        cur_mean_color = cv.mean(cur_frame)
        cur_mean_color = (max(cur_mean_color[0], 1), max(cur_mean_color[1], 1), max(cur_mean_color[2], 1))

        next_mean_color = cv.mean(next_frame)
        next_mean_color = (max(next_mean_color[0], 1), max(next_mean_color[1], 1), max(next_mean_color[2], 1))

        # проверка на резкое изменение цвета
        print("Цвета:",prev_mean_color, cur_mean_color)
        if ((int(max(prev_mean_color[0], cur_mean_color[0])) / min(prev_mean_color[0],
                                                                      cur_mean_color[0]) > maxCountColor or \
        (int((max(prev_mean_color[1], cur_mean_color[1]) ) / min(prev_mean_color[1],
                                                                      cur_mean_color[1])) > maxCountColor) or \
        (int((max(prev_mean_color[2], cur_mean_color[2]) ) / min(prev_mean_color[2],
                                                                      cur_mean_color[2])) > maxCountColor)) or \
        (cur_mean_color[0] + cur_mean_color[1] + cur_mean_color[2]) / 3 > 250) or \
        (cur_mean_color[0] + cur_mean_color[1] + cur_mean_color[2]) / 3 < 1:

            flag = False
            cv.rectangle(cur_frame, (x, y), (x + int(w / 2), y + h), (0, 255, 0), -1)
        else:
            flag = True
        """_______________________________________________"""


        """!!!!!!!!!!!!!!!!FILTER-SECOND!!!!!!!!!!!!!!!!!!"""
        # определение сумарной площади контуров
        prev_sum = 1
        for prev_contour in prev_contours:
            prev_sum += cv.contourArea(prev_contour)

        cur_sum = 1
        for cur_contour in cur_contours:
            cur_sum += cv.contourArea(cur_contour)

        next_sum = 1
        for next_contour in next_contours:
            next_sum += cv.contourArea(next_contour)

        # проверка на резкое изменение контура в размерах
        print("Площадь:",cur_sum, prev_sum)
        if (int((max(cur_sum,prev_sum))/min(cur_sum,prev_sum)) >maxCountArea) and cur_sum!=1 and prev_sum!=1 :
            flag1 = False
            cv.rectangle(cur_frame, (x + int(w/2), y), (x + w, y + h), (255, 0, 0), -1)
        else:
            flag1 = True
        """_______________________________________________"""


        """!!!!!!!!!!!!!!!!FILTER-TREES!!!!!!!!!!!!!!!!!!"""
        # проверка на тряску и быстрое перемещение
        diff_frame = get_frame_diff(prev_frame, cur_frame, next_frame)
        print("Тряска:",diff_frame.sum())
        if diff_frame.sum() > threshold:
            flag2 = False
            cv.rectangle(cur_frame, (x , y+ int(h / 2)), (x + w, y + h), (255, 0, 0), -1)
        else:
            flag2 = True
        """_______________________________________________"""




        # записываем измененный кадр в файл
        """_______________________________________________"""
        print("Флаги:",flag,flag1,flag2)
        print()
        if flag1 and flag and flag2:
            writer.write(cur_frame)
        #
        # обновляем кадры
        prev_frame = cur_frame
        cur_frame = next_frame
        """_______________________________________________"""


    # освобождаем ресурсы
    video.release()
    writer.release()
    cv.destroyAllWindows()


def InportVideoFromCloud(bucket_name,source_blob_name):
    # Подключение к Google Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Загрузка файла с Google Cloud Storage
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(source_blob_name)
    return bucket


def ImportVideoInCloud(bucket,destination_blob_name):

    # Загрузка измененного файла на Google Cloud Storage
    upload_blob = bucket.blob(destination_blob_name)
    upload_blob.upload_from_filename(destination_blob_name)


def ReformatFileForEpilepsion(videoPathName):
    # Параметры Google Cloud Storage
    bucket_name = 'https://drive.google.com/drive'#'/HackatonServerForVideo/'+filename
    source_blob_name = 'static/video/'+videoPathName
    destination_blob_name = 'static/video/Epilepsion/'+videoPathName

    bucket = InportVideoFromCloud(bucket_name,source_blob_name)

    epilepsion(source_blob_name)

    ImportVideoInCloud(bucket,destination_blob_name)


"""---------------Вызыв-Главных-Функций-----------------------"""
#ReformatFileForEpilepsion(videoPathName)
epilepsion(videoPath1)
epilepsion(videoPath2)
epilepsion(videoPath3)
epilepsion(videoPath4)
epilepsion(videoPath5)
"""-----------------------------------------------------------"""

