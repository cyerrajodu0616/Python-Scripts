import json
import os.path
from os import sys
from itertools import repeat
import csv
if __name__ == "__main__":
  if len(sys.argv) == 5:
      input_file = open(sys.argv[1])
      src_recordid = sys.argv[2]
      output_file_location = sys.argv[3]
      id_type = sys.argv[4]
      #id_type="TG"  
      with open(output_file_location, 'a+') as csvfile:
          print(src_recordid)
          pair_writer = csv.writer(csvfile, delimiter=',')
          json_hits = json.load(input_file)
          if 'hits' not in json_hits:
              sys.exit(0)
          inner_hits = json_hits["hits"]
          #print(json_hits)
          #print(inner_hits)
          for x in inner_hits['hits']:
            source = x['_source']
            dst_recordid = source['recordid']
            pair_writer.writerow([src_recordid,dst_recordid,id_type])
            #print(dst_recordid)
  else:
    print ("Invalid arguments! Please pass input file and base output path")
    sys.exit(1)

