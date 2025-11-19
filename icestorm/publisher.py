#!/usr/bin/python3

import sys
import Ice
import IceStorm
Ice.loadSlice('./Printer.ice')
import Example


class Publisher:
    def __init__(self, communicator):
        self.ic = communicator

    def get_topic_manager(self):
        key = 'IceStorm.TopicManager.Proxy'
        proxy = self.ic.propertyToProxy(key)
        if proxy is None:
            print("property {} not set".format(key))
            return None

        print("Using IceStorm in: '%s'" % proxy)
        return IceStorm.TopicManagerPrx.checkedCast(proxy)

    def run(self):
        topic_mgr = self.get_topic_manager()
        if not topic_mgr:
            print('Invalid proxy')
            return 2

        topic_name = "PrinterTopic"
        try:
            topic = topic_mgr.create(topic_name)
        except IceStorm.TopicExists:
            topic = topic_mgr.retrieve(topic_name)

        publisher = topic.getPublisher()
        printer = Example.PrinterPrx.uncheckedCast(publisher)

        print("publishing 10 'Hello World' events")
        for i in range(10):
            printer.write("Hello World %s!" % i)


if __name__ == "__main__":
    try:
        with Ice.initialize(sys.argv[1]) as communicator:
            Publisher(communicator).run()
    except KeyboardInterrupt:
        pass
