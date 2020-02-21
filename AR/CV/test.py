import numpy as np
import cv2

def ex1():
    print("EX_1")
    arr = np.zeros(shape=(1, 10))
    print(arr)

ex1()

def ex2():
    print("EX_2")
    arr = np.zeros(shape=(1, 10))
    arr[ :, 4] = 5
    print(arr)

ex2()

def ex3():
    print("EX_3")
    arr = np.arange(10, 50)
    print(arr)

ex3()

def ex4():
    print("EX_4")
    arr = np.arange(1, 10)
    arr = arr.reshape((3, 3))
    print(arr)

ex4()

def ex5():
    print("EX_5")
    arr = np.arange(1, 10)
    arr = arr.reshape((3, 3))
    arr = np.fliplr(arr)

    print(arr)

ex5()

def ex6():
    print("EX_6")
    arr = np.arange(1, 10)
    arr = arr.reshape((3, 3))
    arr = np.flipud(arr)

    print(arr)

ex6()

def ex7():
    print("EX_7")
    arr = np.identity(3, int)
    print(arr)

ex7()

def ex8():
    print("EX_8")
    arr = np.random.random_sample((3, 3))
    print(arr)

ex8()

def ex9():
    print("EX_9")
    arr = np.random.randint(-100, 100, 10)
    average = arr.mean()

    print(arr)
    print(average)

ex9()

def ex10():
    print("EX_10")
    arr = np.ones(shape=(10, 10))
    arr[1:9, 1:9] = 0

    print(arr)

ex10()

def ex11():
    print("EX_11")

    rows = 1
    stacking = True
    arr = np.arange(1, 6)

    while stacking:
        arr2 = np.arange(1, 6)
        arr = np.vstack((arr, arr2))
        rows += 1
        if rows == 5:
            stacking = False

    print(arr)

ex11()

def ex12():
    print("EX_12")
    arr = np.random.randint(-100, 100, 9)
    arr = arr.reshape((3, 3))
    arr = np.float64(arr)

    print(arr)

ex12()

def ex13():
    print("EX_13")
    arr = np.random.randint(-100, 100, (5, 5))
    print(arr)
    av = arr.mean()
    arr = arr - av

    print(av)
    print(arr)

ex13()

def ex14():
    print("EX_14")
    arr = np.random.randint(-100, 100, (5, 5))
    arr = np.float64(arr)

    for i in range(0, 5):
        av = arr[i, :].mean()
        arr[i, :] = np.subtract(arr[i, :], av)

    print(arr)

ex14()

def ex15():
    print("EX_15")
    value = 0.5
    arr = np.random.random_sample((5, 5))

    print(arr)
    print(arr.flat[np.abs(arr - value).argmin()])

ex15()

def ex16():
    print("EX_16")
    arr = np.random.randint(0, 10, 9)
    arr = arr.reshape((3, 3))
    count = np.size(arr[arr > 5])
    print(count)

ex16()

#ex17 to ex23 about images see pdf:
#"Intro to Image Processing in Virtual Campus"

def ex17():
    print("EX_17")
    img = np.zeros((64, 64))
    grad = np.arange(0.0, 1.0, 1.0/64.0)
    img = img + grad

    cv2.imshow("image17", img)
    cv2.waitKey(0)

ex17()

def ex18():
    print("EX_18")
    img = np.zeros((64, 64))
    grad = np.arange(0.0, 1.0, 1.0/64.0)
    grad = grad.reshape((64, 1))
    img = img + grad

    cv2.imshow("image18", img)
    cv2.waitKey(0)

ex18()

def ex19():
    print("EX_19")
    img = 255 * np.ones((64, 64, 3), np.uint8())
    img[:, :, 0] = 0.0

    cv2.imshow("yellow", img)
    cv2.waitKey(0)

ex19()
