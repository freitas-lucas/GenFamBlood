import os
import re

count = 0
for log_file in os.listdir("/path/to/GBlocksLog/"):
        if log_file.endswith(".htm"):
                arquivo = open("/path/to/GBlocksLog/" + str(log_file), "r")
                for line in arquivo:
                        if "New number of positions in" in line:
                                number_sites = re.search("(\d+)%", line)
                        elif "Number of sequences:" in line:
                                number_sp = re.search(">(\d+)<", line)
                        else:
                            pass
                if int(number_sites.group(1)) >= 50 and int(number_sp.group(1)) >= 17:
                    os.system("cp /path/to/Gblocked_alignments/" + log_file[:-4] + " /path/to/MCMCtree/Seqs/")
                else:
                 	pass
        else:
             	pass
