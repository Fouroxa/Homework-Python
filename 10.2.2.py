def three_args(var1, var2 = None, var3 = None):
    dict_args = locals()
    list_arg = []
    for key, values in dict_args.items():
        if values is not None:
            list_arg.append(f'{key} = {values}')
    print(f'Переданы аргументы: ', ", ".join(list_arg))

three_args(var1=1, var3=3)