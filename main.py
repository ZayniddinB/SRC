from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import func, funx


if __name__ == "__main__":
    #task 1
    kwargsAcceptFun(name="Zayniddin", car = "Ford", phone = "Samsung")

    #task 2
    output = typeBasedTransformer(int_type=3, text_type="Data", boolen_type=True, list_type=[1, 2, 3])
    print(output)

    #task 3
    func()
    funx()
    func()
    funx()
    func()
