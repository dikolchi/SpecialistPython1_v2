# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
# вычисляем стороны предполагаемого треугольника
    a = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    b = ((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2)**0.5
    c = ((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)**0.5
# проверяем:
    return a + b > c and a + c > b and b + c > a

# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
