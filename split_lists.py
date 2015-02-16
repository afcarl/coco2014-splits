#!/usr/bin/env python

import json

FILENAME = './coco/dataset.json'
OUT_PATTERN = './coco2014_%s.%s.txt'
KEYS = ('cocoid', 'filename')
SUBSETS = ('train', 'val', 'test')

with open(FILENAME, 'r') as json_file:
    data = json.load(json_file)

subset_data = {}
for key in KEYS:
    for subset in SUBSETS:
        subset_data = \
            [image[key].__str__() for image in data['images']
                 if image['split'] == subset]
        out_filename = OUT_PATTERN % (key, subset)
        with open(out_filename, 'w') as out_file:
            out_file.write('\n'.join(subset_data) + '\n')
        print "Wrote data for subset '%s' to file: %s" % (subset, out_filename)
