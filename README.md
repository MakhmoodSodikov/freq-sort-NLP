#README

-----------------------------------------------------------------------------------
#RU:
Эта программа создана для генерации предложений на основе вероятностного случайного выбора слов из заданного текста. 

Данная программа состоит из двух модулей. 
Запуская модуль train.py, укажите в нем путь к директории, в котором хранятся файлы для парсинга.
Укажите (опционально) булев аргумент -lc, если хотите, чтобы все символы хранились в нижнем регистре. 
Укажите путь к файлу, в который необходимо вывести модель.

Запуская модуль generate, укажите в нем путь к директории, в котором хранится файл модели. 
Укажите (опционально) значение аргумента -seed, начиная с которого вы хотите начать генерируемое предложение. 
Укажите путь к файлу, в который необходимо вывести ответ (опционально).

Каждый из модулей имеет также аргумент -help, при вызове которого вы можете получить более подробную помощь.

##Что нового в версии 2.0?

- Исправлены мелкие ошибки, модуль train стал работать более корректно;
- Код стал более читабельным, добавлены новые комментарии;
- Полностью поменялся контейнер, хранящий пары слов и частот, за счет чего программа работает еще быстрее;
- Теперь за транспортировку контейнера между модулями отвечает мощный и невероятно быстрый алгоритм сериализации и десериализации объектов Pickle.


##Что нового в версии 2.0.5?

- Улучшена генерация;
- Добавлен модуль __init__.py, теперь наши технологии искуственного интеллекта стали полноценной библиотекой!

-----------------------------------------------------------------------------------
#EN:
This program is designed to generate proposals based on probabilistic random selection of words from a given text.

This program consists of two modules.
When launching the train.py module, specify the path to the directory where the files for parsing are stored. 
Specify (optional) boolean argument -lc, if you want all characters to be stored in lower case. 
Specify the path to the file to which you want to display the model.

Running the generate module, specify the path to the directory in which the model file is stored. 
Specify (optional) the value of the argument -seed, from which you want to start the generated proposal. 
Specify the path to the file to which you want to display the response (optional).

Each of the modules also has a -help argument, when you call it you can get more help.

##What's new in version 2.0?

- Fixed minor bugs, module train began to work more correctly;
- The code has become more readable, new comments have been added;
- Completely changed the container, which stores words and frequencies, due to what the program works faster;
- Now, for transporting the container between the modules, a powerful and incredibly fast algorithm Pickle responds.


##What's new in version 2.0.5?

- Improved generation;
- __init__.py module was added, and now our technologies of artificial intelligence have become a full-fledged library!

(c) Sodikov Makhmood, 2018, DIHT MIPT.