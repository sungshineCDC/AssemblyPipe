#AssemblyPipe 

Usage:  assemblyMagic.py /path/to/inputDirectory /path/to/outputDirectory

Variables:  inputDirectory  - is the directory containing raw read files in fastq format (gziped is acceptable)
            outputDirectory - is the path to the output directory where all the program outputs will be placed
            inputfileOne    - takes the R1 labeled values in the generated hash to be passed into assembly modules
            inputfileTwo    - takes the R2 labeled values in the generated hash to be passed into assembly modules
            paths           - is a list containing the paths to the raw read files
            prinseqPaths    - is the path to the trimmed Prinseq files, fileHash will be generated from this directory
            fileHash = {}   - is a hash map pairing PE reads and SE reads to their respective file names (keys) 

Modules:    createDirectories() - checks to see if output directories exists and creates them if needed
            fastQC() - invokes fastQC and puts metric files into output directory
            wranglePairedEnds() - generates hash map, fileHash
            prinseq() - invokes prinseq with set flags on raw read files in "outputDirectory"
            SPAdes() - contains function calls for both PE and SE reads
            preProcess() - runs fastQC and prinseq as a single function before key hashing and assembly
                        
Running this script passes in a single-end or paired-end set of reads to be trimmed and assembled by de novo
& reference assemblers. These assemblies are merged using CISA for the highest quality consensus sequence in
fasta format.

Programs: Prinseq, FastQC, SPAdes, ABYSS, Edena, SMALT, CISA, QUAST