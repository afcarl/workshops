import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopy
from geopy.distance import vincenty
import networkx as nx
import sys
from lxml import etree
from collections import defaultdict
from io import StringIO, BytesIO

def rec_print(elem, level=0):
    for i in range(level):
        sys.stdout.write('\t')
    sys.stdout.write(elem.tag)
    if elem.text is not None:
        sys.stdout.write(elem.text)
    ecount = 0
    for k in range(len(elem.keys())):
        key = elem.keys()[k]
        val = elem.values()[k]
        if ecount > 0:
            sys.stdout.write(';')
        sys.stdout.write(' ' + key + '=' + val)
        ecount += 1
    print ''
    for child in elem.getchildren():
        rec_print(child, level+1)





tree = etree.parse("sm_map.xml")




node_counts = defaultdict(int)
r=tree.getroot()
r.get('generator')
children = r.getchildren()
for child in children:
    node_counts[child.tag] += 1

#print(node_counts)






tags = {}
interesting = ['node', 'relation', 'way']
for interest in interesting:
    tags[interest] = defaultdict(int)

for child in children:
    tag = child.tag
    if tag == 'node' or tag == 'relation' or tag == 'way':
        tag_counts = tags[tag]
        gchildren = child.getchildren()
        for gchild in gchildren:
            key = gchild.get('k')
            tag_counts[key] += 1






roads = {}
values = defaultdict(int)
children = r.getchildren()
for child in children:
    tag = child.tag
    if tag == 'way':
        gchildren = child.getchildren()
        for gchild in gchildren:
            k = gchild.get('k')
            if k=='highway':
                i = child.keys().index('id')
                road_id = child.values()[i]
                v = gchild.get('v')
                if v=='primary' or v=='secondary' or v=='tertiary' or v=='residential':
                    roads[road_id] = child
                values[v] += 1







nodes = {}
children = r.getchildren()
for child in children:
    tag = child.tag
    if tag == 'node':
        ref = child.values()[child.keys().index('id')]
        lat = float(child.values()[child.keys().index('lat')])
        lon = float(child.values()[child.keys().index('lon')])
        nodes[ref] = [lat, lon]


