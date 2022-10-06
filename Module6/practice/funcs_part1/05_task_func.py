# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def triangle(p1, p2, p3):
# вычисляем стороны предполагаемого треугольника
    a = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    b = ((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2)**0.5
    c = ((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)**0.5
# проверяем:
    if a + b > c and a + c > b and b + c > a:
        half_p = (a + b + c) / 2
        square = (half_p*(half_p-a)*(half_p-b)*(half_p-c))**0.5
        return '{:.3f}'.format(half_p * 2), '{:.3f}'.format(square)
    else:
        return "Треугольник не существует"

# Пример вызова функции
res = triangle((0, 0), (0, 3), (4, 0))
# Не забудьте протестировать вашу функцию
print(res)
