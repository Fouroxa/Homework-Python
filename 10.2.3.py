def my_max(*args):
    compare = None
    for argument in args:
        if type(argument) is list:
            for nums in argument:
                compare = argument[0]
                if compare < nums:
                    compare = nums
            return compare
        elif type(argument) is str:
            compare = argument[0]
            for letters in argument:
                if compare > letters:
                    compare = letters
            return compare
        else:
            compare = args[0]
            if compare < argument:
                compare = argument
    return compare


print(my_max([3,3,1]))