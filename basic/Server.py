#!/usr/bin/python3 -u

import sys
import Ice

Ice.loadSlice('Printer.ice')
import Example


class PrinterI(Example.Printer):
    n = 0
    def write(self, message, current=None):
        print("{0}: {1}".format(self.n, message))
        sys.stdout.flush()
        self.n += 1


class Server(Ice.Application):
    def run(self, argv):
        ic = self.communicator()
        servant = PrinterI()

        adapter = ic.createObjectAdapter("PrinterAdapter")
        proxy = adapter.add(servant, ic.stringToIdentity("printer1"))

        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        ic.waitForShutdown()

        return 0


server = Server()
sys.exit(server.main(sys.argv))
