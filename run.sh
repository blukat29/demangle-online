#!/bin/sh
sudo docker build -t demangle .
sudo docker run --rm -it -p 9999:80 demangle
