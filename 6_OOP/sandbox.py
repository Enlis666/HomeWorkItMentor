from functools import wraps


def decor(param):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            print(*args)
            print(param)
            func()
        return wrapper2
    return wrapper1


@decor(1)
def main():
    print('hello word')


if __name__ == '__main__':
    main()
