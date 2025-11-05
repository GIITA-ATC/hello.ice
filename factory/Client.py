#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('-I. --all PrinterFactory.ice')
import Example


def main(ic):
    proxy = ic.stringToProxy(sys.argv[1])
    factory = Example.PrinterFactoryPrx.checkedCast(proxy)

    if not factory:
        raise RuntimeError('Invalid proxy')

    printer = factory.create("Printer1")
    printer.write('Hello World!')
    printer.destroy()


if __name__ == "__main__":
    with Ice.initialize() as communicator:
        main(communicator)
