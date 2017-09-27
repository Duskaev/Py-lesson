is_student = True
name = input("Введие имя:")
print( "Hello, " , name, "!")
#bool  - логические (True/ False)
#int   - целое
i1 = 666
i2 = 0x59 (0-9) # шеснатеричная СС
i3 = 0b10010 # двоичная СС
i4 = 0o255  #восмеричная СС
# float - с плавающей точкой (дробный)
f1 = 1.23
f2 = 12e-3   # 12*10^-3  
f3 = 12e3   # 12*10^3   
# str - строки
#bytes - байтовая строка
s1 = 'Some string'
s2 = "Some string"
s3 = r'Raw string' #сырые строки
s4 = u'Hello'
s5 = b'байтовая строка'
s6 = '''
'''
s7 = """
"""
# Комплексные числа - complex
c1 = 3.14j
# Структуированные (сложные)
В один момент времени переменная может хварить много типов данных
# tuple, list, set, dict, object

# Кортежи - tuple
t1 = (1,)
t2 = (True, 1, 1.2, 'string', (1, 2, 3))
print(t2[1], lst1[2], lst1[0] [0])

# Списки - list
lst1 = [[1], [2], 3, False]

# Множество - set
s1 = {1, 2, 3, ""}
s2 = {} # неправильно
s2 = set() # пустое множество

# Словари - dict
d = {
	'id': 1,
	'name': 'Вася',
	'is_student': True,
	'skills': ('python', 'linyx')
}
# Специальные типы
# None - пустота

a = None