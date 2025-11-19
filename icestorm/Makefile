
all:

clean:
	$(RM) *~
	$(RM) -r db

run-icestorm:
	mkdir -p db/
	icebox --Ice.Config=icebox.config

run-publisher:  icestorm.config
	./publisher.py publisher.config

run-subscriber: icestorm.config
	./subscriber.py subscriber.config
