def test_function():
    def inner_function():
        return 'Я в области видимости функции test_function'
    return inner_function()


print(test_function())

#print(inner_function()) - Функция упала в ошибку из-за того, что её появление и существование происходит только в локальном уровне функции test_function
