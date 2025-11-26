#!/usr/bin/make -f

clean:
	$(RM) -r *~ *.out Printer_ice.py Example/ data/

run-registry:
	mkdir -p data/db/registry
	icegridregistry --Ice.Config=Registry.config

run-server:
	./Server.py Server.config | tee server-proxy.out

run-client:
	./Client.py Client.config '$(shell head -1 server-proxy.out)'
