# LIRA
Проект "LIRA - Latex Image Recognition Algorithm" - инновационное решение для студентов и учащихся, которым приходится тратить много времени на перевод рукописных записей в формат Latex. Проект основан на использовании глубоких нейронных сетей для автоматического распознавания рукописного текста и его преобразования в код Latex. 

# Проблема 
большое количество статей хранится либо в отсканированном виде, либо в формате pdf, что затрудняет их использование в других работах. Вместо ручного набора информации можно воспользоваться специальным инструментом, преобразующим математическое выражение с изображения в наиболее распространённый формат – LaTeX.

# Потребность
Часто возникает необходимость перевести в том числе рукописные выражения в печатный формат. Также это пригодиться студентам и преподавателям, для создания удобных конспектов. 

# Решение
В поисках наилучшего решения, мы начали с поисков похожих моделей и наткнулись на pix2text (https://github.com/breezedeus/Pix2Text/tree/main), у которого была неплохо обучена модель, поэтому мы ее взяли за основу.

# План действий
1) Обработать изображение. Нам хотелось не просто распознавать формулы, но еще и предоставлять готовый PDF-документ на русском. Поэтому требовалось создать отдельный скрипт для детекции отдельных частей картинки.
2) После распознавания, нужно было выбрать и применить модель
3) Выдать ответ пользователю



