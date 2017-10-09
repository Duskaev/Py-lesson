#Частичный импорт
fron math import pi as Pi# 3.14

def calculate_square_area(a):
	"""Возврощает площадь квадрата"""
	return a**2


def calculate_rectangle_area(a, b):
	"""Возвращает площадь прямоугольника"""
	return a*b


def calculate_circle_area():
	"""Возвращает площадь круга с заданный радиусом"""
	return PI*r**2

__all__=[  #Указываем что импортировать при *
    'calculate_square_area'
    'calculate_circle_area'
    'calculate_rectangle_area'
]

