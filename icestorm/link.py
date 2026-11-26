#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import Ice
import IceStorm

from icestorm_utils import get_topic


def main(ic, unlink=False):
    topic_a = get_topic(ic, 'IceStormA.TopicManager.Proxy', 'PrinterTopic1')
    topic_b = get_topic(ic, 'IceStormB.TopicManager.Proxy', 'PrinterTopic2')
    if not topic_a or not topic_b:
        return 2

    if unlink:
        try:
            topic_a.unlink(topic_b)
            print("Link A -> B removed")
        except IceStorm.NoSuchLink:
            print("There was no link A -> B")
    else:
        try:
            topic_a.link(topic_b, 10)
            print("Link A -> B created")
        except IceStorm.LinkExists:
            print("Link A -> B already exists")


if __name__ == "__main__":
    with Ice.initialize(sys.argv[1]) as communicator:
        unlink = len(sys.argv) > 2 and sys.argv[2] == "unlink"
        sys.exit(main(communicator, unlink))
