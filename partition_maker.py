#! /usr/bin/env python
import re
import sys

partition_file = """## ALIGNMENT FILE ##
alignment = infile.phy;

## BRANCHLENGTHS: linked | unlinked ##
branchlengths = unlinked;

## MODELS OF EVOLUTION for PartitionFinder: all | mrbayes | beast | <list> ##
models = all;

## MODEL SELECTION: AIC | AICc | BIC ##
model_selection = AICc;

## DATA BLOCKS ##
[data_blocks]
{}


## SCHEMES, search: all | greedy | rcluster | hcluster | user ##
[schemes]
search = rcluster;

"""
file = sys.argv[1]

with open(file, 'r') as inFile:
    partitions = "\n".join(inFile.readlines())

basename = file.split(".")[0]

with open('{}_partitions.cfg'.format(basename), 'w+') as outFile:
    outString = ""
    for line in partitions.split(';'):
        line = line.strip()
        regex = re.compile('(\w+) \= (\d+)\-(\d+)', re.IGNORECASE)
        matched = regex.match(line)
        if matched:
            gene = matched.group(1)
            start = int(matched.group(2))
            end = int(matched.group(3))
            for position in range(1,4):
                outString += '\t{}_pos{} = {}-{}\\3;\n'.format(gene, str(position), str(start-1+position), str(end))
    outFile.write(partition_file.format(outString))
    