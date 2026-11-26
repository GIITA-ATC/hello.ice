.PHONY: all clean run-icestorm-1 run-icestorm-2 \
        run-publisher run-subscriber-a run-subscriber-b \
        admin admin-link admin-unlink admin-links

ADMIN = icestormadmin \
  --IceStormAdmin.TopicManager.Default="IceStorm1/TopicManager:tcp -h 127.0.0.1 -p 10000" \
  --IceStormAdmin.TopicManager.Second="IceStorm2/TopicManager:tcp -h 127.0.0.1 -p 10001"

all:

clean:
	$(RM) *~
	$(RM) -r db-1 db-2

run-icestorm-1:
	mkdir -p db-1/
	icebox --Ice.Config=icebox1.config

run-icestorm-2:
	mkdir -p db-2/
	icebox --Ice.Config=icebox2.config

run-publisher:
	./publisher.py publisher.config

run-subscriber-a:
	./subscriber.py subscriber-a.config

run-subscriber-b:
	./subscriber.py subscriber-b.config

admin:
	$(ADMIN)

admin-link:
	-$(ADMIN) -e "create IceStorm1/PrinterTopic1"
	-$(ADMIN) -e "create IceStorm2/PrinterTopic2"
	$(ADMIN) -e "link IceStorm1/PrinterTopic1 IceStorm2/PrinterTopic2 10"

admin-unlink:
	$(ADMIN) -e "unlink IceStorm1/PrinterTopic1 IceStorm2/PrinterTopic2"
