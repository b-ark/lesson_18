try:
    from module1 import add

    int1 = 10
    int2 = 20
    print(add(int1, int2))
except ModuleNotFoundError:
    print('Module not found in this directory')
