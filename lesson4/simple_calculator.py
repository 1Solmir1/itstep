a = int(input("Введите первое число: "))
what = input("Что вы собераететесь делать? +,-,*,/: ")
b = int(input("Ведите второе число: "))
if what == "+":
    t = a + b
    print(t)
elif what == "-":
    c = a - b
    print(c)
elif what == "*":
    m = a * b
    print(m)
elif what == "/":
    n = a / b
    print(n)
else:
    print("ОЙ, ты ввел что-то не то, попробуй еще раз!")
