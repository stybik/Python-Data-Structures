import threading

def print_cube(num):
    """
    function to print cube of a given number
    """
    print("Cube: {}".format(num*num*num))

def print_square(num):
    """
    function to print square of a number
    """
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # Creating Thread
    t1 = threading.Thread(target=print_square, args=(10, ))
    t2 = threading.Thread(target=print_cube, args=(10, ))

    # Starting thread 1
    t1.start()
    # Starting thread 2
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
