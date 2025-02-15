# Файл с разлиными определениями, создание переменных и тп

# Определение персонажей игры.
define mar = Character('Маринетт', color="#a51887", image='mar')
define adr = Character('Адриан', color="#e49901", image='adr')

define lady = Character('Леди Баг', color="#c21c1c", image='lady')
define cat = Character('Супер-Кот', color="#131b5b", image='cat')

define tik = Character('Тикки', color="#0b041c", image='tikki')
define plug = Character('Плагг', color="#4e0931", image='plug')

define alya = Character('Аля', color="#c95642", image='alya')
define gabr = Character('Габриэль Агрест', color="#435257", image='gabr')
define bad = Character('Злодейка', color="#31053e", image='badgirlie')

define persistent.Best_end = False # объявление постоянной переменной
define persistent.Good_Mar_end = False
define persistent.Good_Adr_end = False
define persistent.Bad_end = False

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    $ left2 = Position(xalign = 0.2, yalign = 1) # сокращение для удобства
    $ right2 = Position(xalign = 0.8, yalign = 1) # сокращение для удобства

# для галереи кнопки
init python:

    g = Gallery()

    g.locked_button = "images/gallery_posters/locked gallery.png"

    g.button("best_end")
    g.condition("persistent.Best_end") 
    g.image("images/gallery_posters/unlocked gallery4.png")

    
    g.button("good_mar_end")
    g.condition("persistent.Good_Mar_end") 
    g.image("images/gallery_posters/unlocked gallery2.png")

    g.button("good_adr_end")
    g.condition("persistent.Good_Adr_end") 
    g.image("images/gallery_posters/unlocked gallery1.png")
    

    g.button("bad_end")
    g.condition("persistent.Bad_end") 
    g.image("images/gallery_posters/unlocked gallery3.png")


# Список концовок с их статусом (разблокировано или нет)
# default gallery_images = [
#     {"title": "Концовка 1", "image": "images/gallery_posters/unlocked gallery.png"},
#     {"title": "Концовка 2", "image": "images/gallery_posters/unlocked gallery.png"},
#     {"title": "Концовка 3", "image": "images/gallery_posters/unlocked gallery.png"},
#     {"title": "Концовка 4", "image": "images/gallery_posters/unlocked gallery.png"},
# ]

# default current_index = 0  # Индекс текущей картинки
# default locked_image = "images/gallery_posters/locked gallery.png"  # Изображение для заблокированных концовок



# пример анимации моргания тип
image animation1:
    "mar normal"
    pause 2.0 # пауза
    "cat normal"
    pause 2.0
    repeat

# пример анимации вращение
image spin1:
    "mar normal"
    rotate 0 # начальный угол 0 
    linear 5.0 rotate 360 # линейно за 5 секунд поворот на 360 градусов
    repeat

# пример трансформации
transform zoomin1: 
    zoom 0 xpos 960 ypos 540 anchor(0.5, 0.5) 
    # координаты это левый верхний угол картинки, анкор это якорь, чтобы увеичение было посередине
    linear 3.0 zoom 1 alpha 0.7 # прозрачность
    repeat
