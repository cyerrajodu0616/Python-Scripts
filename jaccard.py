from os import sys
def jaccard (src_business,dst_business):
  if ((len(src_business) or len(dst_business)) == 0):
      #print(len(src_business))
      #print(len(dst_business))
      #print(src_business)
      #print(dst_business)
      return -1
  else:
    if(src_business == dst_business):
      return 1
    else:
      src_business=src_business.replace(" ","")
      dst_business=dst_business.replace(" ","")
      src_terms=set(src_business[i:i+3] for i in range(0, len(src_business)-2, 1))
      dst_terms=set(dst_business[i:i+3] for i in range(0, len(dst_business)-2, 1))
      src_nbr_term=len(src_terms)
      dst_nbr_term=len(dst_terms)
      all_terms = src_terms.union(dst_terms)
      common_terms=src_terms+dst_terms-len(all_terms)
      return float(common_terms)/float(len(all_terms))
if __name__ == "__main__":
  if len(sys.argv) == 3:
    #print(sys.argv[1])
    #print(sys.argv[2])
    x = jaccard(sys.argv[1],sys.argv[2])
  else:
    print ("Invalid arguments! Please pass input file and base output path")
    sys.exit(1)
