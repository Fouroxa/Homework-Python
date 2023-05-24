def my_max(*args):
    compare = None
    if len(args) == 1:
        for argument in args:
            for nums in argument:
                compare = argument[0]
            if compare < nums:
                compare = nums
        return compare
    else:
        for nums in args:
            compare = args[0]
        if compare < nums:
                compare = nums
        return compare


print(my_max(1,2))