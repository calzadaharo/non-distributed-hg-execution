#! /home/rodrigo/yes/bin/python

import os, sys

os.environ['RAPHTORY_BUILD_SERVERS']="1"
os.environ['RAPHTORY_PARTITION_SERVERS']="1"
os.environ['RAPHTORY_BUILDERS_PER_SERVER']="1"
os.environ['RAPHTORY_PARTITIONS_PER_SERVER']="1"

# Change the RAM asigned to Java (Scala)
os.environ["JAVA_OPTS"]="-Xmx2G -XX:MaxPermSize=2G -Xss2M"

os.system('scala ' + sys.argv[1])
