## Un solo broker

Una terminal por paso:

```
make run-icestorm-1
make run-subscriber-a
make run-publisher
```

## Dos brokers federados (PrinterTopic1 -> PrinterTopic2)

El publicador habla con el broker 1 y un suscriptor conectado al broker 2 recibe los eventos gracias al enlace.

```
make run-icestorm-1
make run-icestorm-2
make admin-link          # crea los topics y el enlace 1 -> 2 (persistente)
make run-subscriber-b    # opcional: make run-subscriber-a
make run-publisher
```
