import rpyc
from rpyc.utils.server import ThreadedServer # or ForkingServer

class CalculatorService(rpyc.Service):
    def exposed_add(self, a, b):
        print("\nAdd Method Called")
        print('a :',a,' b :',b)
        return a + b
    def exposed_sub(self, a, b):
        print("\nSubtract Method Called")
        print('a :',a,' b :',b)
        return a - b
    def exposed_mul(self, a, b):
        print("\nMultipy Method Called")
        print('a :',a,' b :',b)
        return a * b
    def exposed_div(self, a, b):
        print("\nDivsion Method Called")
        print('a :',a,' b :',b)
        return a / b
    def foo(self):                          # Alais for Fail
        print("foo")

if __name__ == "__main__":
    server = ThreadedServer(CalculatorService, port = 12345)
    print("Server and service Started")
    server.start()
    