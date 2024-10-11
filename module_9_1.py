print(f'{"Задача"} {"«Вызов разом»"}')


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            results[func.__name__] = func(int_list)
        except Exception as exc:
            results[func.__name__] = str(exc)
    return results


# Пример работы кода
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

