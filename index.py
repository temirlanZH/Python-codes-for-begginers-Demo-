# Python for Begginers (This is my code)

# Python Math
# x = int (input("Сколько вам лет?: "))
# if x <= 5:
#     print("Привет малыш")
# if x > 5:
#     print("Привет друг")
# if x >= 18:
#     print("Здравствуйте")

# a = 10
# if (a > 5) and (a > 10) or (a < 15):
#     print(a < 15)

# Акинатор с помощью Python

# жёлтый, оранжевый, персиковый, коричневый.
# print('Выберите любой цвет который показан - Желтый, Оранжевый, Персиковый, Коричневый, Черный, Серый, Светло-Черный, Черно-Белый')

# question1 = input('Ваш цвет из семейства желтых?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет оранжевый или жёлтый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет жёлтый?')
#         if question3 == 'Да':
#             print('Ваш цвет жёлтый!')
#             quit()
#         else:
#             print('Ваш цвет оранжевый!')
#             quit()


# question1 = input('Ваш цвет из семейства темно-желтых?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет коричневый или персиковый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет коричневый?')
#         if question3 == 'Да':
#             print('Ваш цвет коричневый!')
#             quit()
#         else:
#             print('Ваш цвет персиковый!')
#             quit()

# question1 = input('Ваш цвет из семейства черных?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет черный или серый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет черный?')
#         if question3 == 'Да':
#             print('Ваш цвет черный!')
#             quit()
#         else:
#             print('Ваш цвет серый!')
#             quit()

# question1 = input('Ваш цвет из семейства Ярко-черных?')

# if question1 == 'Да':
#     question2 = input('Ваш цвет Светло-Черный или Черно-Белый?')
#     if question2 == 'Да':
#         question3 = input('Ваш цвет Светло-Черный?')
#         if question3 == 'Да':
#             print('Ваш цвет Светло-Черный!')
#             quit()
#         else:
#             print('Ваш цвет Черно-Белый!')
#             quit()

# a = 'love'
# b = 'you'
# c = a + b
# print(c)

# Stroka format 
# name = "Алексей"

# ice_place = "Медео"

# number = 8

# boolean = "Пока нету"

# no_int_nimber = 0.3145

# stroka = 'Привет, меня зовут {}, я увлекаюсь программированием. Я живу в Алмате и у нас есть каток {}. Вчера мы ездили на каток вместо с друзьями, нас было {} человек. Недавно на телефон скачал себе игру Brawl Stars, наличие легендарок - {}, шанс на легу - {}.' .format(name, ice_place, number, boolean, no_int_nimber)
# print(stroka)


# Brawlers modules
# brawlers = "Тик, Шелли, ЛИОН, Пэм, Барли, ЛЕАН, Биби, Фрэнк, Нита, Кольт, Бык, ЛЕОН, Ворон"

# brawlers = (brawlers).lower()
# print(brawlers[67:71])
# from autocorrect import Speller

# spell = Speller(lang="en")
# print(spell("Telegram is the mast multifunctional manager of all. Soooon I will alsa learn how to wgite telegram botc."))

# color = ["Красный", "Желтый", "Синий", "Коричневый", "Черный", "Белый"]

# array and stroka
# array = ["Яблоко", "Подсолнух", 3]

# if "Яблоко" in array:
#      print("Яблоко в картинке присутствует!")

# if "Подсолнух" in array:
#      print("Подсолнух в картинке присутствует!")

# if 3 in array: 
#     print("Число 3 присутствуют в массиве!")

# Операция и методы списка
# my_list1 = ["сок", "компот"]
# my_list2 = [ "молоко", "кофе", "чай"]
# my_list1.extend(my_list2)
# my_list1[0] = "kompot"
# my_list1.sort(reverse=True)
# print(my_list1)

# array = ["Дом 1", "Дом 2", "Дом 3", "Дом 4", "Дом 5", "Дом 6", "Дом 7", "Дом 8", "Дом 9", "Дом 10", "Дом 11", "Дом 12", "Дом 13", "Дом 14" ]
# for i in range(0,14,3):array[i] += " Доставлено"
# print(array)


# 2 Модуль окончен ура!!

# temirlanZH = ["шоколад Milka", "сыр Ементаль", "молоко Казахстанское", "мыло хозяйственное", "колбаса Докторская", "шоколад Nestle",
#          "молоко Домашнее", "сыр Чедер", "Салат Айсберг", "шоколад Казахстанский", "хлеб черный", "хлеб ржаной", "хлеб пшеничный",
#          "хлеб белый", "хлеб кирпичик", "хлеб батон"]

# count = 0

# for index in range(len(temirlanZH)):
#     if "молоко" in temirlanZH[index - count] or "сыр" in temirlanZH[index - count]:
#         temirlanZH.remove(temirlanZH[index - count])
#         count += 1

# count = 0
# xleb_count = 0

# for index in range(len(temirlanZH)):
#     if "хлеб" in temirlanZH[index - count]:
#         if xleb_count == 2:
#             print(temirlanZH[index - count])
#             xleb_count = 0
#         else:
#             temirlanZH.remove(temirlanZH[index - count])
#             xleb_count += 1
#             count += 1

# print(temirlanZH)



# Начинаем с 3 модуля)
# print("Начнем с 3 модуля!")
# Function DEV in phyton
# def summa(a, b):
#   return a + b

# number = summa(2, 3)
# number = number * 2
# print(number)

# def identification(name, age, work):
#     more_18, work_good = False, False

#     if work in ["Доктор", "Программист" , "Программный Инженер" , "Менеджер по продажам" , "Дизайнер" , "Веб-разработчик"]:
#         work_good = True  

#         output = 'Ваше имя {0}, ваша профессия {1}, вам больше 18 лет - {2}'.format(name, work_good, more_18)
#         return output

# print(identification("Mike", 20 , "Программный Инженер"))
# 15 lesson in phyton lang.
# word = input()
# chisla = list(range(1, 11)) #1,2,3,4,5,6,7,8,9,10

# def half(chisla, word):
#     if word == "половина":
#         print(chisla[0:5])
#     else:
#         print(chisla)

# half(chisla, word)

def decoration_function(func):
    def wrapper():
        print("Наша Функция {} - Прошла Функция)" .format(func))
        func()
    return wrapper

@decoration_function
def hello_world():
    print("Hello World!")
hello_world()