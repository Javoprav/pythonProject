# -*- coding: utf-8 -*-
"""Урок 6 – Демонстрация - 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uvVCs3s42E8CgE1JSgHvJeXbGQMzhY07

# Урок 6

## Интро к уроку

## Эпизод 1 – Командная строка

### Команды

Чтобы посмотреть содержимое директории нужно выполнить команду ls (dir). Для навигации по каталогам есть команда cd. cd и имя папки чтобы перейти в нее. 
cd.. и две точки чтобы вернуться назад.

Мы можем создать файл или удалить файл. Для этого вводим команду touch (NUL>) и имя файла. Посмотрим создался ли файл, выполним команду ls (dir). Ага вот он. 
Теперь давайте удалим файл. Вводим rm (del) и имя файла. Проверим удалился ли файл, выполним ls (dir). Да файл был удален.

Давайте узнаем какая версия python у нас установлена. Вводим команду python -V или python3 -V

### Задача эпизода 2

Создать папки week5 и week6 в домашней директории.
В папке week5 создать файл text.txt
В папке week6 создать папку home_work и файл expl.txt
Вернитесь в папку week5 и удалте файл text.txt.
Очистите консоль и выйдите из нее.

## Эпизод 2 – Локальный python

### Python Windows

Чтобы установить интерпретатор python нужно перейти на сайт https://python.org В разделе download выбрать версию python под вашу операционную систему.
Если у вас Windows, выбираете Windows затем download. 

После скачивания запускаете установщик программы. Также нужно поставить галочку Add Python to PATH. И следуете инструкции на экране.

### Python в системе Linux

Системы семейства Linux ориентированы на программистов, поэтому поддержка Python уже установлена на большинстве компьютеров с Linux. 

Проверка версии Python

Откройте терминальное окно, запустив приложение Terminal в вашей системе (в Ubuntu нажмите клавиши Ctrl+Alt+T). Чтобы проверить, установлена ли поддержка Python в вашей системе, введите команду python 3. Если вы видите Python 3. и версия питона, то в системе установлена версия Python 3.

Если python3 не установлен, то его можно установить.

Установка Python 3.9 из исходного кода

Компиляция Python из исходного кода позволяет установить последнюю версию Python и настроить параметры сборки. Однако вы не сможете поддерживать установку Python через диспетчер пакетов apt.

Следующие шаги объясняют, как скомпилировать Python 3.9 из исходного кода:

Установите зависимости, необходимые для сборки Python:

> sudo apt update

> sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

Загрузите исходный код последней версии со страницы загрузки Python с помощью wget:

> wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz

После завершения загрузки распакуйте сжатый архив:

> tar -xf Python-3.9.6.tgz

Переключитесь в исходный каталог Python и запустите сценарий configure, который выполняет ряд проверок, чтобы убедиться, что все зависимости в вашей системе присутствуют:

> cd Python-3.9.6

> ./configure --enable-optimizations

Эта опция –enable-optimizations оптимизирует двоичный файл Python путем выполнения нескольких тестов. Это замедляет процесс сборки.

Запустите процесс сборки Python 3.9:

> make -j 2

Для ускорения сборки измените значение -j, чтобы оно соответствовало количеству ядер в вашем процессоре. Вы можете узнать номер, набрав nproc.

Когда процесс сборки будет завершен, установите двоичные файлы Python, набрав:

> sudo make altinstall

Мы используем altinstall вместо install, потому что позже будет перезаписан системный двоичный файл python3 по умолчанию.

Вот и все. Python 3.9 установлен и готов к использованию. Чтобы проверить это, введите:

> python3.9 --version

> The output should show the Python version:
Python 3.9.0+

### Python в системе OS X

В большинстве систем OS X поддержка Python уже установлена. 

Проверка наличия Python 

Откройте терминальное окно (команда Applications Utilities Terminal). Также можно нажать Command+пробел, ввести terminal и нажать Enter. Чтобы проверить, установлена ли поддержка Python в вашей системе, введите команду python. На экране появится информация о том, какая версия Python у вас установлена. На экране может появиться сообщение об ошибке, или покажет какая версия Python 3 в вашей системе установлена, вы сможете использовать ее без необходимости установки.

## Эпизод 3 – IDE

### Установка pycharm

Pycharm IDE для профессиональной разработки на Python.
Давайте установим pycharm. 
Перейдите по ссылке https://www.jetbrains.com/ru-ru/pycharm/
Нажмите “скачать”. Далее выберите вашу операционную систему и кликните скачать под “Community” это бесплатная версия pycharm.

После загрузки программы на ваш компьютер, запустите установщик, кликнув по нему 2 раза.

Далее следуя инструкции выберите папку куда хотите установить pycharm. Затем вы ставите все галочки, это позволит вам открывать файлы с расширением .py в pycharm. Нажемайте install и дождитесь завершение установки.
Далее запускаем pycharm ставим галочку что согласны с лицензией (можете ее прочесть, но кто это читает).

В открывшемся окне нужно выбрать “New project”. 
В поле location выбираете директорию в которой будет создан ваш проект. И нажимаете “Create”. 
Теперь pycharm создаст ваш проект и первый файл main.py. 
После того как открылся редактор в маленьком окошке нажимаете “Close”.

### Обзор редактора

В центре вы видете область редактирования файла, там где вы будете писать код. Сейчас там заготовка созданная pycharm.
Слева располагается дерево ваших папок проекта и файлы. На папку venv пока не обращайте внимание. Вверху находится меню.

### Создать папку

Для того чтобы создать новую папку, наведите мышку на область слева где располагаются папки и кликните правой кнопкой мыши. В появившемся меню выберите “new” далее “Directory”. В появившемся окошке в центре экрана введите название папки, название лучше давать латинскими буквами. К примеру введите my_dir. Теперь слева у вас появилась еще одна папка.

### Файлы: создание, переименование и удаление

Давайте теперь создадим файл с расширением .py. Наводим мышку на область с нашим проектом слева и нажимаем ПКМ. В появившемся меню выберите “new” далее “Python File”. В появившемся окошке в центре экрана введите название файла, его тоже лучше указывать латинскими буквами.
После того как вы его создали он сразу открывается на редактирование. Чтобы закрыть файл кликните на иконку крестика которая располагается справа от названия файла выше редактора кода. Чтобы открыть файл на редактирование кликните на него два раза слева в каталоге.
 
Давайте попробуем переименовать наш файл, кликаем на нем правой клавишей мыши и выбираем Refactor -> Rename или нажимаем shift + F6. И в появившемся окне вводим новое имя файла.
 
Чтобы удалить файл или папку, можно на нем кликнуть 1 раз и нажать del на клавиатуре или кликнуть ПКМ и выбрать пункт меню Delete, в появившемся окошке нажать “Delete”. После чего ваша файл или папка удалиться.

### Работа с кодом

Теперь давайте поработаем с кодом. Для этого создадим еще один файл и назовем его less_5.py. В редакторе введите print(“Hello pycharm”).

Теперь давайте запустим наш файл на исполнение. Кликните ПКМ в окне редактора кода и выберите “Run less 5” или Ctrl + Shift + F10 если вы в windows или linux и Ctrl + Shift + R в macos. В низу в терминале мы видим “Hello pycharm” это значит что наш код был выполнен интерпретатором python.

Как вы заметили pycharm выделяет разным цветом код. Ключевые слова языка и ваш код.

Чтобы сделать автоформатирование кода, т.е. pycharm нажмите Ctrl + Alt + L. Авто формат позволяет сделать ваш код более читабельным и приводит его к стандартам написания кода в python.

### Pycharm показывает ошибки

Теперь давайте воспользуемся самой крутой функцией ide это подсказка где у нас ошибка в коде. Давайте введем prnt(Error). Видим что наш код начал подчеркиваться красной валнистой линией. Это значит что здесь у нас ошибка. 
Запустим наш код на исполнение. В терминале снизу мы видим красный текст это ошибка, на которую указывает python.

Давайте исправим prnt на print. Красное подчеркивание под функцией print исчезло, но осталось под Error. Кликните два раза по Error или просто выделите это слово и нажмем Shift + “ и наш выделенный код будет обернут в кавычки. Все ошибки исчезли запустим код на исполнение и в терминал вывелось “Error”.

## Эпизод 4 – Файлы

### Чтение из файла

Давайте создадим файл text.txt и напишим в него “Hello World”. Кликаем ПКМ слева в каталоге и выбираем new -> File и пишем text.txt

Прежде, чем работать с файлом в python, его надо открыть. С этим замечательно справится встроенная функция open:

> f = open('text.txt', 'r')

У функции open много параметров, нам важны 2 аргумента: первый, это имя файла. Путь к файлу может быть относительным или абсолютным. Второй аргумент, это режим, в котором мы будем открывать файл. Режимы могут быть объединены, то есть, к примеру, 'rb' - чтение в двоичном режиме. По умолчанию режим равен 'rt'.


Открыли мы файл, а теперь мы хотим прочитать из него информацию. 
Первый - метод read, читающий весь файл целиком, если был вызван без аргументов, и n символов, если был вызван с аргументом (целым числом n).
"""

f = open('text.txt')
print(f.read(10))
f.close()

"""Ещё один способ сделать это - прочитать файл построчно, воспользовавшись циклом for:

"""

f = open('text.txt')
for line in f:
  line

f.close()

"""После открытия файла и работы с ним, нужно обязательно закрыть файл. Сделать это можно с помощью метода close().

Открыть файл и не думать о том что бы его закрывать, об этом может позаботиться python. Нужно использовать оператор with as
"""

with open('text.txt', 'r') as f:
    print(f.read())

"""### Задача эпизода 4

Написать программу, которая считает гостей из файла и посчитает их количество.
"""

# Содержимое файла guests.txt

# Драт Калмин	
# Кисани Белден	
# Джасмаль Лид	
# Кхемед Рейн	
# Мехмен Пашар	
# Мен Кхалид

# Содержимое файла main.py


print(f"Гостей: {guests_count}")
for guests in guests:
  print(guests)



"""## Эпизод 5 – запись данных

### Запись в файл

Откроем файл на запись и запишем туда имя пользователя которое он введет.
Чтобы открыть файл на запись, нужно указать в каком режиме мы его открываем. Для этого вторым параметром передаем “w”. 

Вызывая метод write, мы передаем текст или переменную которую хотим записать.
"""

with open('newfile.txt', 'w') as f:
    f.write("Данные записаны")

""" А вот ‘\n’ означает что следующая запись будет начинаться с новой строки."""

with open('newfile.txt', 'w') as f:
    name = input('Ваш пароль' )
    f.write(name + '\n')

"""### Задача эпизода 5

Написать программу которая будет сохранять ответы пользователя.
```
Программа: Какой язык вы учите?
Пользователь: Python
Программа: Как давно?
Пользователь: 3 недели
Программа: Где?
Пользователь: В Sky.pro
Программа: ответы записаны!
```
"""

user_language = input("Какой язык вы учите?")
user_time = input("Как давно?")
user_institution = input("Где?")

"""### Эпизод 6 – Придумываем свой формат хранения данных

Мы уже знаем, что из одной строки можно сделать несколько с помощью split, а из нескольких одну с помощью join. Теперь пора применить знания при работе с файлами ведь текстовый файл – это как одна стока, а данные может понадобиться разделять.

Итак давайте придумаем формат данных, в котором будем хранить информацию, кто какой язык учит. Например:

```
Драт Калмин:python 
Кисани Белден:java
Джасмаль Лид:go
```

И программа будет выводить в понятном виде:

``` 
Драт Калмин учит язык python 
```
"""

# main.py

with open('students.txt', 'r') as f:

    for line in f:
        student_data = line.strip().split(":")
        name = student_data[0]
        language = student_data[1]
        print(f"{name} учит язык {language}")

"""### Задача эпизода 6

Написать программу которая будет вести учет покупок и расходов.

Программа при запуске выводит список расходов и общую сумму по ним.

Программа: В списке 7 позиций. Сумма 2600 Р
"""

# list.txt

Спички:1:10
Лимон шт:1:50
Фасоль уп:1:100
Мешки мусор большие:1:50
Яблоки кг:1:100
Бананы кг:1:100
Овсянка уп:2:100
Пленка пищевая:1:50
Апельсины кг:1:100
Фольга уп:1:100
Груши кг:1:200
Мука ржаная кг:1:100
Шоколад шт:1:100

# main.py

# main.py

with open('list.txt', 'r') as f:

    groceries_summ = 0
    groceries_count = 0

    for line in f:

      ...

    print(groceries_count)
    print(groceries_summ)

"""## Эпизод 7 – Вредный код

Когда мы получаем данные из файла, мы получаем строки. 

С этими строками работают обычные строковые методы. И нам может показаться, что файлы программ на питоне – это какие то волшебные файлы, но это точно такие же текстовые файлы, которые интерпретатор Python выполняет построчно (ну почти построчно) . А если это текстовый файл, то его можно открыть, отредактировать, сохранить и как - нибудь испортить. Так и работаю вирусы – они проникают в тело файла и добавляют туда свой код. Особенность вирусов, что инфицированная программа сама начинает заражать другие программы, но у нас такого не будет. 


Прежде чем мы начнем, на всякий случай скажу: мы не одобряем написание вредоносного кода и делаем это только во имя науки.

Давайте возьмем два файла на питоне и откроем один с помощью другого как текст.
"""

#students.txt
# Драт Калмин:python 
# Кисани Белден:java
# Джасмаль Лид:go

#main.py
with open('students.txt', 'r') as f:

    for line in f:
        student_data = line.strip().split(":")
        name = student_data[0]
        language = student_data[1]
        print(f"{name} учит язык {language}")

# Код файла 2
with open('main.py') as f:
  for line in f:
    print(line)

"""### Зловред

И так мы поработали с открытием файла, чтением из файла и записью.
Теперь давайте напишем вредный код на python. Что должен уметь делать наш код.
Он будет открывать другой файл python и записывать в конец файла вредоносный код, например 

> print(“Я вредный код).
"""

# Код программы main.py

with open('students.txt', 'r') as f:
    for line in f:
        student_data = line.strip().split(":")
        name = student_data[0]
        language = student_data[1]
        print(f"{name} учит язык {language}")


# Код программы infector.py

malcode = "print('я вредный код')"

with open('programm_1.py','a') as f:
  f.write("\n" + malcode)

"""### Антивирус

Прекрасно, мы написали свой первый зловредный код на языке python.
Настало время придумать антивирус. Который будет искать вредоносный код в других программах python и сообщать от этом.
"""

# Код программы detector.py


malcode = "я вредный код"

with open('programm_1.py','r') as f:
  content = f.read()
  if malcode in content:
    print("Обнаружен зловред!")
  else: 
    print("Все чисто!")

"""## Селфчек

Как установить локально Python?
"""

# Как открыть консоль?

Windows:
Нажмите Win+X на клавиатуре. 
Выберите: Командная строка, чтобы запустить командную строку. Командная строка (администратор), чтобы запустить командную строку от имени администратора

MacOS:
Если на панели меню у вас есть кнопка Поиска Spotlight, нажмите её. 
Если нет – используйте сочетание клавиш Command + Space.
Затем введите Terminal / Терминал

# Как перейти в папку и вернуться обратно?

Windows: cd foldername
Unix-подобные:cd foldername

# Как создать папку

Windows: mkdir foldername
Unix-подобные: mkdir foldername

# Как создать файл

Windows: NUL> file.txt
Unix-подобные: touch file.txt

# Как открыть файл для редактирования?

Windows: "filename.txt"
Unix-подобные: open filename.txt

# Как удалить папку?

Windows: rm foldername
Unix-подобные: rmdir foldername

# Как удалить файл?

Windows: del foldername
Unix-подобные: rm foldername

# Как очистить экран терминала

Windows: cls
Unix-подобные: clear

# Как запустить программу на python из командной строки?

Windows: python filename.py / python3 filename.py
Unix-подобные: python filename.py / python3 filename.py

# Как установить Python?

Чтобы установить интерпретатор python нужно перейти на сайт https://python.org В разделе download выбрать версию python под вашу операционную систему. Если у вас Windows, выбираете Windows затем download.
После скачивания запускаете установщик программы. Также нужно поставить галочку Add Python to PATH. И следуете инструкции на экране.

# Как установить IDE?

Pycharm IDE для профессиональной разработки на Python. Давайте установим pycharm. Перейдите по ссылке https://www.jetbrains.com/ru-ru/pycharm/ Нажмите “скачать”. Далее выберите вашу операционную систему и кликните скачать под “Community” это бесплатная версия pycharm.
После загрузки программы на ваш компьютер, запустите установщик, кликнув по нему 2 раза.

# Как запустить код внутри IDE?

Кликните ПКМ в окне редактора кода и выберите “Run main” или Ctrl + Shift + F10 если вы в windows или linux и Ctrl + Shift + R в macos. 
Внизу в терминале мы видим “Hello pycharm” это значит что наш код был выполнен интерпретатором python.

# Как открыть файл на чтение/запись?

f = open('text.txt',"r") # на чтение
f = open('text.txt',"w") # на запись

# Как получить все содержимое файла?

f = open('text.txt')
content = f.read()
print(content)
f.close()

# Как получить файл построчно

f = open('text.txt')
for line in f:
  print(line)

f.close()

# Как записать данные в файл (заменить содержимое файла)?

with open('newfile.txt', 'w') as f:
    name = input('Ваш пароль' )
    f.write(name + '\n')

# Как не закрывать файл вручную?

with open('text.txt', 'r') as f:
    print(f.read())

# Как дописать данные в файл?

with open('text.txt', 'a') as f:
    print(f.write("Эта строчка добавится в конец файла"))

# Как проверить, есть ли строка в файле?

with open("main.py", 'r') as f:
    contents = f.read()
    if "Я пришел и" in contents:
        print("Вредоносный код обнаружен!")
    else:
        print("Файл чист")