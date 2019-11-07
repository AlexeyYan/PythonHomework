"""Find a way to call inner_function without moving it from inside of enclosed_function"""

a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)
    inner_function()


if __name__ == "__main__":
    enclosing_funcion()
