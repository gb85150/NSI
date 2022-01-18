import threading as t

ledA = t.Lock()
ledB = t.Lock()
ledC = t.Lock()
ledD = t.Lock()

def p1():
    while True:
        ledA.acquire()
        ledB.acquire()
        print("p1")
        ledA.release()
        ledB.release()

def p2():
    while True:
        ledB.acquire()
        ledC.acquire()
        print("p2")
        ledB.release()
        ledC.release()

def p3():
    while True:
        ledC.acquire()
        ledD.acquire()
        print("p3")
        ledC.release()
        ledD.release()

if __name__ == "__main__":
    if input("bug ? (y/n)") == "n":
        t1 = t.Thread(target=p1)
        t2 = t.Thread(target=p2)
        t3 = t.Thread(target=p3)
        t1.start()
        t2.start()
        t3.start()
    else:
        p1()
        p2()
        p3()
