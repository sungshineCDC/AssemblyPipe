__author__ = 'sungshine'
#!/usr/bin/env python
import os
import subprocess

#Invokes prinseq-lite on raw read files using default settings passing files in as argument

def modulePrinseq(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    subprocess.call(['prinseq-lite', '-verbose', '-fastq', file, '-out_format','3', '-out_good', ODprinseq+filename+".prinseq", "-out_bad", ODerrors+filename+".bad.prinseq",])

