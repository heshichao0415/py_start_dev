import threading

class myThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, module, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.module = module
        self.counter = counter

    def run(self):
        print('开启线程:{}'.format(self.name))
        Login_auth().test_auth_login(self.module)  #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数


class Login_auth():
    def __init__(self):
        pass

    def test_auth_login(self, moudle):

            if moudle % 2 == 0:
                print(moudle)
            else:
                print('it is 是基数')

class ALL_moudle():
    def __init__(self):
        pass

    def allmoudle(self):
        moudle = []
        for a in range(1, 100):
            moudle.append(a)
        return moudle

    def run_all(self):
        count = 0
        moudle = self.allmoudle()
        if len(moudle) != 0:
            print('共计{}个测试类'.format(len(moudle)))
            while count <= 10:
                if len(moudle) != 0:
                    threads = []
                    for i in moudle:
                        threads.append(myThread(count, "thread-{}".format(count), i, 0))
                        count += 1
                    for t in threads:
                        t.start()
                    for t in threads:
                        t.join()
    def run(self):
        self.run_all()

if __name__ == "__main__":
    ALL_moudle().run()




