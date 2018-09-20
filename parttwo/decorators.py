def new_decorator(func):

    def wrap_func():
        print('Code before func')
        func()
        print('Code after func')

    return wrap_func


# def func_need_decorator():
#     print('This function need decorator')


# func_need_decorator = new_decorator(func_need_decorator)
# print(func_need_decorator)

@new_decorator
def func_need_decorator():
    print('This function need decorator')


func_need_decorator()
