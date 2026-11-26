import IceStorm


def get_topic(communicator, key, topic_name):
    proxy = communicator.propertyToProxy(key)
    if proxy is None:
        print("property '{}' not set".format(key))
        return None

    print("Using IceStorm in: '%s'" % proxy)
    topic_mgr = IceStorm.TopicManagerPrx.checkedCast(proxy)
    if not topic_mgr:
        print("Invalid proxy for '{}'".format(key))
        return None

    try:
        return topic_mgr.create(topic_name)
    except IceStorm.TopicExists:
        return topic_mgr.retrieve(topic_name)
