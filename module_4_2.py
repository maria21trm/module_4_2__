def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
inner_function() # программа выдаст ошибку т.к данная функция существует только внутри test_function
test_function()
