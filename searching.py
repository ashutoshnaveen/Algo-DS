import math
import random
import threading


def binary_search(a,b):



def jump_search(a, b):
    index = -1
    step = math.floor(math.sqrt(len(a)))
    for i in range(0, len(a), step):
        if a[i] == b:
            index = i
            break
        elif a[i] < b:
            prev = i
        else:
            for j in range(prev, i):
                if a[j] == b:
                    index = j
                    break
            break
    print("jp%d:" % index)


def linear_search(a, b):
    index=-1
    for i in range(len(a)):
        if a[i] == b:
            index=i
    print("lp%d:" % index)


def interpolation_search(a, b):


def main():
    a = sorted([random.randint(0, 1000000) for i in range(1000000)])
    b = a[random.randrange(0, len(a))]
    print(threading.enumerate())
    print(threading.active_count())
    t1 = threading.Thread(target=jump_search(a, b))
    t2 = threading.Thread(target=linear_search(a, b))
    t1.start()
    t2.start()
    print(threading.enumerate())
    print(threading.active_count())


if __name__ == "__main__":
#    main()

# Conclusions:: Not even a slight difference seen b/w jump search and linear search
