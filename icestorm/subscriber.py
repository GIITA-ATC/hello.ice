#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('Printer.ice')
import Example

from icestorm_utils import get_topic


class PrinterI(Example.Printer):
    def write(self, message, current=None):
        print("Event received: {0}".format(message))
        sys.stdout.flush()


def main(ic):
    servant = PrinterI()
    adapter = ic.createObjectAdapter("PrinterAdapter")
    subscriber = adapter.addWithUUID(servant)

    topic_name = ic.getProperties().getProperty('Topic')
    topic = get_topic(ic, 'IceStorm.TopicManager.Proxy', topic_name)

    topic.subscribeAndGetPublisher({}, subscriber)
    print("Waiting events... '{}'".format(subscriber))

    adapter.activate()
    ic.waitForShutdown()
    topic.unsubscribe(subscriber)


if __name__ == "__main__":
    with Ice.initialize(sys.argv[1]) as communicator:
        main(communicator)
