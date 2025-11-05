#!/usr/bin/python3

import sys
import Ice
Ice.loadSlice('PrinterFactory.ice')
import Example
import time


class PrinterI(Example.Printer):
    def __init__(self, name):
        self.name = name

    def write(self, message, current):
        print(f'{self.name} says: {message}', flush=True)
        time.sleep(10)

    def destroy(self, current):
        current.adapter.remove(current.id)
        print(f'{self.name} destroyed', flush=True)


class PrinterFactoryI(Example.PrinterFactory):
    def create(self, name, current):
        servant = PrinterI(name)
        proxy = current.adapter.addWithUUID(servant)
        return Example.PrinterPrx.checkedCast(proxy)


def main(ic):
    factory = PrinterFactoryI()
    adapter = ic.createObjectAdapter("PrinterFactoryAdapter")
    proxy = adapter.add(factory, ic.stringToIdentity("PF1"))

    print(proxy, flush=True)

    adapter.activate()
    ic.waitForShutdown()


if __name__ == "__main__":
    try:
        with Ice.initialize(sys.argv[1]) as communicator:
            main(communicator)
    except KeyboardInterrupt:
        pass
