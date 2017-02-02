#!/bin/sh
sudo docker build -t demangle .
sudo docker run --rm -it -p 8080:8000 demangle
