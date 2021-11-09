def local(inputfile,outputfile):
    outputfile.write(inputfile.read())
    outputfile.close()
    inputfile.close()