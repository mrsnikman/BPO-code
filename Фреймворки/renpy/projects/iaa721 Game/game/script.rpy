﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Internet_Chan = Character('Internet_Chan', color="#c8ffc8")
image Internet_Chan stand = "Internet_Chan.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene tusur

    show Internet_Chan stand

    Internet_Chan "Hello world! iaa721"

    Internet_Chan "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
