#!/usr/bin/python3

import sys
import Ice
Ice.loadSlice('./Printer.ice')
import Example

from icestorm_utils import get_topic


def main(ic):
    topic = get_topic(ic, 'IceStorm.TopicManager.Proxy', 'PrinterTopic1')

    publisher = topic.getPublisher()
    printer = Example.PrinterPrx.uncheckedCast(publisher)

    print("publishing 10 'Hello World' events")
    for i in range(10):
        printer.write("Hello World %s!" % i)


if __name__ == "__main__":
    with Ice.initialize(sys.argv[1]) as communicator:
        main(communicator)
