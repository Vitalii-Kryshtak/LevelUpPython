def check_arguments_function(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            new_args.append(set(arg)) if isinstance(arg, (list, tuple)) else new_args.append(arg)
        for k, v in kwargs.items():
            if isinstance(v, (list, tuple)):
                kwargs[k] = set(v)
        return func(*new_args, **kwargs)
    return wrapper

@check_arguments_function
def print_argument(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == '__main__':
    print_argument(1, 2, 3, [6,8,8],(5,7,5), name='John', sex='Male', age=[3,5,2,3,4,5], level=(44,23,12,44,15,23))
    
