import os

def handle_file_info(directory,filename, status):
        #print(directory)
        #print(os.path.isfile(directory+'info'))
        if not os.path.isfile(directory+'info'):
            with open(directory+'info','w') as outfile:
                json.dump({filename:status}, outfile)
                outfile.close()
        else:
            with open(directory+'info', 'r+') as outfile:
                info = json.load(outfile)
                info[filename]=status
                outfile.seek(0)
                outfile.write(json.dumps(info))
                outfile.truncate()
                outfile.close()