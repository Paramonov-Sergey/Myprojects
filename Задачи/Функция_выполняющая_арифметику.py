# Учитывая два числа и арифметический оператор (имя его, как строка), верните результат двух чисел, имеющих этот оператор, используемый на них.
# a и bоба будут целыми положительными числами, и aвсегда будут первым числом в операции, и bвсегда вторым.
 # Эти четыре оператора - "сложение", "вычитание", "деление", "умножение".
 # Попробуйте сделать это без использования операторов if!

def arifmetic(a,b,operator):
    d={'add':a+b,'multiply':a*b,'subtract': a-b,'divide':a/b}
    return d[operator]

print(arifmetic(4,5,'multiply'))

