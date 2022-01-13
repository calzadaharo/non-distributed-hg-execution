#! /usr/bin/python

import os, sys

os.environ['RAPHTORY_BUILD_SERVERS']="1"
os.environ['RAPHTORY_PARTITION_SERVERS']="1"
os.environ['RAPHTORY_BUILDERS_PER_SERVER']="1"
os.environ['RAPHTORY_PARTITIONS_PER_SERVER']="8"

# Change the RAM asigned to Java (Scala)
os.environ["JAVA_OPTS"]="-Xmx128G -XX:MaxPermSize=128G -Xss128M"

os.system('scala -classpath ' + sys.argv[1] +" es.dit.upm.Runner")
