# TrueTechHackMTS
Формулировка:
Необходимо разработать дополнительный функционал для плеера KION, который поможет пользователям с особыми потребностями комфортно смотреть любимые фильмы и сериалы. 

Возможные дополнения для плеера:
Настройка цветовой палитры (блокировка/изменение спектра цветов) изображения
Настройка яркости, контрастности, насыщенности, резкости изображения
Включение/выключение сцен, которые могут вызвать эпилептический припадок
Сохранение настроек для конкретного пользователя
Возможность выбора рекомендуемых пресетов
Примечание: выше представлены рекомендованные улучшения для плеера, вы также можете погрузиться глубже в проблематику и модифицировать его по своему усмотрению, охватив большую аудиторию.

Решение:

Презентация (загружать во второй вопрос)
Ссылка на открытый репозиторий 
Рабочий продукт
Ссылка на Readme (можно разместить на Github): 
- Инструкции по развертке и установки решения, а также данные для входа тестовых пользователей. 
- Визуальное описание бизнес-процесса, сервисов, сущности БД (могут быть приложены отдельной ссылкой на файл) 
- Схематическое описание архитектуры
- Скриншоты сервиса
- Предложения по масштабированию
 

Критерии оценки:
Техническое решение:

Описание архитектуры приложения
Техническая эффективность решения 
Креативность технического решения
Функционал: 

Массовость проблемы 
Точность решения проблемы (работоспособность алгоритма)
UX решения
Креативность решения



<br>
<hr>
<b>Описание решения:</b> <br>
Есть значит у нас веб плеер, у него есть доступ ко всем файлам из конкретной папке на облаке (films). Из нее они стримятся. При стриме соответственно настройкам к видео применяется CSS фильтр. Включение режима дальтоника увеличивает набор пресетов с базового до расширенного. Включение режима эпилептика, делает проверку на наличие особых, отредактированых под эпилепсию файлов  на облаке. Если их нет вызывает функцию их создания  из дефолтных файлов. И при выборе видео стримит уже отредактированный.<br>

Редактирование файла для эпилептиков происходит с помощью библиотеки Python OpenCV.

Отслеживаем по трем основным потернам:<br>
1)сильное изменение среднего цвета в соседних кадрах<br>
2)сильное изменение площади контуров в соседних кадрах<br>
3)сильное смещение контуров в соседних картах<br>
 Силу параметров можем менять с помощью констант для улучшения эффекта при калибровке

