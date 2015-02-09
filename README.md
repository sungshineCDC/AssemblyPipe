#AssemblyPipe

Usage:  assemblyMagic.py /path/to/inputDirectory /path/to/outputDirectory
        
        inputDirectory  - is the directory containing raw read files in fastq format (gziped is acceptable)
        outputDirectory - is the path to the output directory where all the program outputs will be placed
        
        Running this script passes in a single-end or paired-end set of reads to be trimmed and assembled by de novo
        & reference assemblers. These assemblies are merged using CISA for the highest quality consensus sequence in
        fasta format.

Programs: Prinseq, FastQC, SPAdes, ABYSS, Edena, SMALT, CISA, QUAST