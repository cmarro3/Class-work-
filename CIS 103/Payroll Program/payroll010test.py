# -------------------------
#  Payroll Program 10 file I/O
# -------------------------------
from datetime import *
# -------------------------
# blank lines
# ------------
def blkln(a):           
    print('\n'*a)
    return


# -------------------------
# open files
# -------------------------
def openfiles():
    infilept = ""
    eof = 0
    inputfile = "c:/data7/test/p1.txt"
    infilept = open(inputfile,'r')
    return (infilept)

# -------------------------
# Read a record
# -------------------------
def getrecord(inpt,rline,fields):
    ename=''
    rline = inpt.readline()
    fcount = rline.count(',')
    print('number of comma: ',fcount)
    if (fcount ==5):
        (fields) = rline.split(',')
        print('fields: ',fields)
        print('len: ',len(fields))
        ename = fields[1] + " " + fields[2]
        print('name: ',ename)  
    else:
        if (rline !=''):
            print(' Bad record, missing fields')
    print('RCD: ',rline)
    return(fields,rline) 
    

# ---------------------------------
#           main line
# ---------------------------------
def main():
    totals = [0] * 7
    cont = 'Y'
    errorcnt = 0
    readcnt = 0
    writecnt = 0
    rline = ''
    fields =[]
    blkln(60) # clear screen
    print(' PROGRAM STARTED: ', datetime.now())
    (infilept)=openfiles()
    (fields,rline) = getrecord(infilept,rline,fields)
    while (rline != ""):
        (fields,rline) = getrecord(infilept,rline,fields)
        print('--------------')

    return
# ---------------------------------
#     Entry Point
# ---------------------------------    
main()    
# ---------------------------------
#    End of Program
# ---------------------------------
