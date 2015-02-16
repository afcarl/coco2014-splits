#!/usr/bin/env bash

wget http://cs.stanford.edu/people/karpathy/deepimagesent/coco.zip
unzip coco.zip
./split_lists.py
tar -czvf coco2014_aux.tar.gz *.txt
