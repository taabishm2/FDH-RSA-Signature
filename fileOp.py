import os.path

save_path = '/home/tabis/Dropbox/Documents/Code/FDH RSA Signature/Files'

def write_list(filename,l):
    '''write a list l into file'''

    completeName = os.path.join(save_path, filename + ".txt")

    file = open(str(completeName),'w')
    file.write(str(l)[1:-1])
    file.close()

def read_list(filename):
    '''return data from file read as list, READS ONLY INTEGERS'''

    completeName = os.path.join(save_path, filename + ".txt")

    file = open(completeName,'r')
    arr = file.read().split(',')
    return (list(map(int,arr)))

def read_list_noint(filename):
    '''return data from file read as list, READS ONLY INTEGERS'''

    completeName = os.path.join(save_path, filename + ".txt")

    file = open(completeName,'r')
    arr = file.read().split(',')
    return (arr)
