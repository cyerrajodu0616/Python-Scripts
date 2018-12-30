import os.path
from os import sys
from itertools import repeat
import csv

def parsetsv(tsvfile):
        cols=['name','businessId','recordid','vendorname','state','zip','phone','hashraw']
        rc=0
        count=0
        with open(tsvfile,'rb') as tsvin:
                tsvin = csv.reader(tsvin, delimiter='\t')
                for row in tsvin:
                   if rc==0:
                       rc = rc+1
                       continue

                   index='{"index":{"_index":"matching_2_elastisearch", "_type":"business"}}'
                   #print(index)
                   data=''
                   count += 1
                   data=[]
                   for col in cols:
                        x=row[cols.index(col)]
                        if len(x) > 0:
                           str='"%s":"%s"' % (col,x)
                        else:
                           x='null'
                           str='"%s":%s' % (col,x)
                        data.append(str)
                   json=",".join(data)
                   json="'{"+json+"}'"
                   print(json)
                   #csvout.writerow(row[2:5])
if __name__ == "__main__":
  if len(sys.argv) == 2:
    parsetsv(sys.argv[1])
  else:
    print len(sys.argv)
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    print sys.argv[1]
    print sys.argv[0]
    print "Invalid arguments! Please pass input file and base output path"
    sys.exit(1)

