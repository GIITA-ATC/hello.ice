#!/usr/bin/make -f
# -*- mode:makefile -*-

clean:
	$(RM) -r *~ proxy.out Printer_ice.py Example/ __pycache__/

run-server:
	./Server.py Server.config | tee proxy.out

run-client:
	./Client.py '$(shell head -1 proxy.out)'

gen-src:
	slice2py Printer.ice
