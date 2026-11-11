clean:
	$(RM) -r *~ proxy.out

run-server:
	./server.py container.config | tee proxy.out

run-client:
	./client.py '$(shell head -1 proxy.out)'
