def test_decorator(class_):
    instances = {}
    # print("outer function ")

    print("instances", instances)
    def get_instance(*args, **kwargs):


        print("initial value:", [cls.__name__ for cls, obj in instances.items()])
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        print("value just before returning:", [cls.__name__ for cls, obj in instances.items()])
        print("\n")
        return instances[class_]

    return get_instance


@test_decorator
class Database:
    def __init__(self):
        print('Print from Database class ')


@test_decorator
class DatabaseNew:
    def __init__(self):
        print('Print from DatabaseNew class')


if __name__ == '__main__':
    print("1st execution")
    d1 = Database()
    print("2nd execution")
    d2 = DatabaseNew()
    print("3rd execution")
    d3 = Database()  # WHY THIS IS NOT EXECUTING 2ND TIME
    print("4th execution")
    d4 = DatabaseNew() # WHY THIS IS NOT EXECUTING 2ND TIME
