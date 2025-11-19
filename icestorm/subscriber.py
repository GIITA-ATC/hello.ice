#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import Ice
import IceStorm
Ice.loadSlice('Printer.ice')
import Example


class PrinterI(Example.Printer):
    def write(self, message, current=None):
        print("Event received: {0}".format(message))
        sys.stdout.flush()


class Subscriber:
    def __init__(self, communicator):
        self.ic = communicator

    def get_topic_manager(self):
        key = 'IceStorm.TopicManager.Proxy'
        proxy = self.ic.propertyToProxy(key)
        if proxy is None:
            print("property '{}' not set".format(key))
            return None

        print("Using IceStorm in: '%s'" % proxy)
        return IceStorm.TopicManagerPrx.checkedCast(proxy)

    def run(self):
        topic_mgr = self.get_topic_manager()
        if not topic_mgr:
            print("Invalid proxy")
            return 2

        servant = PrinterI()
        adapter = self.ic.createObjectAdapter("PrinterAdapter")
        subscriber = adapter.addWithUUID(servant)

        topic_name = "PrinterTopic"
        try:
            topic = topic_mgr.create(topic_name)
        except IceStorm.TopicExists:
            topic = topic_mgr.retrieve(topic_name)

        topic.subscribeAndGetPublisher({}, subscriber)
        print("Waiting events... '{}'".format(subscriber))

        adapter.activate()
        self.ic.waitForShutdown()
        topic.unsubscribe(subscriber)

        return 0


if __name__ == "__main__":
    try:
        with Ice.initialize(sys.argv[1]) as communicator:
            Subscriber(communicator).run()
    except KeyboardInterrupt:
        pass
