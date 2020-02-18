import numpy as np

def ex1():
    print("EX_1")
    arr = np.zeros(shape=(1,10))
    print(arr)

ex1()

def ex2():
    print("EX_2")
    arr = np.zeros(shape=(1,10))
    arr[ :, 4] = 5
    print(arr)

ex2()

def ex3():
    print("EX_3")
    arr = np.arange(10,50)
    print(arr)

ex3()

def ex4():
    print("EX_4")
    arr = np.arange(1,10)
    arr = arr.reshape((3,3))
    print(arr)

ex4()

def ex5():
    print("EX_5")
    arr = np.arange(1,10)
    arr = arr.reshape((3,3))
    #flip hor missing
    #...

    print(arr)

ex5()

def ex6():
    print("EX_6")
    arr = np.arange(1,10)
    arr = arr.reshape((3,3))
    #flip ver missing
    #...

    print(arr)

ex6()

def ex7():
    print("EX_7")
    arr = np.identity(3, int)
    print(arr)

ex7()

def ex8():
    print("EX_8")
    arr = np.random.random((3, 3))
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
    arr[1:1, 8:8] = 0
    #not working and don't know why :'(
    print(arr)

ex10()

def ex11():
    print("EX_11")
    arr = np.arange(1,6)

    for i in range(1,5):        
        arr2 = np.arange(1,6)
        arr = np.vstack((arr, arr2))
    else:
        print(arr)

ex11()

def ex12():
    print("EX_12")
    arr = np.random.randint(-100, 100, 9)
    arr = arr.reshape((3,3))
    arr = np.float64(arr)

    print(arr)

ex12()

def ex13():
    print("EX_13")
    arr = np.random.randint(-100, 100, 25)
    arr = arr.reshape((5 ,5)) 
    print(arr)
    av = arr.mean()
    print(av)
    arr = arr - av

    print(arr)

ex13()

def ex14():
    print("EX_14")
    arr = np.random.randint(-100, 100, 25)
    arr = arr.reshape((5 ,5)) 
    arr = np.float64(arr)

    for i in range(0,5):
        av = arr[i, :].mean()
        arr[i, :] = np.subtract(arr[i, :], av)
    else: 
        print(arr)

ex14()

def ex15():
    print("EX_14")
    arr = np.random.randint(-100, 100, 25)
    arr = arr.reshape((5 ,5)) 
    arr = np.float64(arr)

    

