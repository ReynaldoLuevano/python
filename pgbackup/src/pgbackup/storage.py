def local(inputfile,outputfile):
    outputfile.write(inputfile.read())
    outputfile.close()
    inputfile.close()

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile,bucket,name)
    