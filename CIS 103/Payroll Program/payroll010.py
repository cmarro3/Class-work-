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
# ---------------------
# Print error message
# ---------------------
def errormsg(msg):
    if (len(msg) != 0):
        print('******************************')
        print(msg)
        print('*******************************')
    return
# --------------------------------
# print payroll information
# --------------------------------
def payprt(GP,NP,FIT,SIT):    
    print('------------------------------')
    print('Gross Pay: ',GP)
    print('FIT: ', FIT)
    print('SIT: ', SIT)
    print('Net Pay: ', NP)
    print('------------------------------')
    return

# ------------------------------------------
#  get rate of pay 
# ------------------------------------------
def getrate(rate):
    msg=''
    if rate.isdecimal():
        try:
            rate = float(rate)
            if rate == 0:
                msg='***Error  rate of pay cannot be zero' 
            else:
                if rate >50.00:
                    msg='  ***error  rate of pay over the limit' 
                    rate = 0
        except:
            msg=' **** error: rate of pay unknown error' 
    else:
        try:
            rate = float(rate)
            if rate < 0:
                msg=' **** error  rate of pay cannot be negative' 
        except:
            msg=' **** error: rate has invalid value' 
    if len(msg) > 0:
        rate = 0
    return (rate,msg)
# ------------------------------------------
#  get hours worked
# ------------------------------------------
def gethrs(hrs):   
    msg=''
    if hrs.isdecimal():
        try:
            hrs = float(hrs)
            if hrs == 0:
                msg='***Error  Hours cannot be zero' 
            else:
                if hrs >60.00:
                    msg='  ***error  hours over the limit' 
                    hrs = 0
        except:
            msg=' **** error: hours unknown error' 
    else:
        try:
            hrs = float(hrs)
            if hrs < 0:
                msg=' **** error  hours cannot be negative' 
        except:
            msg=' **** error: hours has invalid value' 
    if len(msg)> 0:
        hrs=0
    return (hrs,msg)
# -----------------------------------
# calc overtime
# -----------------------------------
def overtime(thrs):      
    hrsov = 0.0
    thrs = float(thrs)
    if thrs > 40:
        hrsov = thrs-40
        otr = hrsov *   .5
        thrs = thrs + otr
    return (thrs,hrsov)
# --------------------------------
# calculate gross pay
# --------------------------------
def calcgp(rate, hour):       
    OT = 0.0
    (hrsot,OT) = overtime(hour)
    gp =  (rate * hrsot)
    return(gp,OT)
# -----------------------------------
# calculate federal income tax
#      codes A =.12, B =.15, c =.18
# -----------------------------------
def calcfit(gp,cd):
    ratecode={'A':.12,'B':.15,'C':.18}
    cd = cd.strip()
    fitrate = ratecode[cd]
    cfit = gp * fitrate
    return cfit
# ---------------------------------
# calculate state income tax
# ---------------------------------
def calcsit(gp):    
    sitrate =0.0495
    csit = gp * sitrate
    return csit
# ---------------------------------
# show report
# ----------------------------------
def prtname(ename,PayRate,Hours):
    ovte = 0
    blkln(2)
    print(' ==============================')
    print('Employee Name: ',ename) 
    print('Rate of Pay: ',PayRate)
    print('Hours Worked: ', Hours,'\n')
    if (float(Hours) > 40.00):
        ovte = Hours - 40
        print('    Overtime Hours: ',ovte, '\n')
    return
# ----------------------------------
#  acumalate totals
# ---------------------------------
def ptotals(GP,NP,FIT,SIT,totals):
    totals[1] = totals[1] + GP
    totals[2] = totals[2] + FIT
    totals[3] = totals[3] + SIT
    totals[4] = totals[4] + NP
    totals[5] = totals[5] + 1
    return totals
# --------------
# print ttotals
# ------------
def prttotals(totals):
    blkln(2)
    ptitle=['total','Gross Pay','FIT','SIT','Net Pay','Number processed']
    for x in range(1,6):
         print(ptitle[0],' ',ptitle[x],': ',totals[x])
    blkln(5)
    return
# -----------------------------
#  validate input record
# ----------------------------
def rcdval(rate,hour):
    (rate,msg) = getrate(rate)
    errormsg(msg)
    (hrs,msg) = gethrs(hour)
    errormsg(msg)
    return (rate,hour,msg)
# -------------------------
# open files
# -------------------------
def openfiles():
    infilept = ""
    goodfilept = ""
    errorpt = ""
    msg = ""
    eof = 0
    filepath = input("Enter folder (ex: c:/temp): ")
    empfile = input("file to be processed: ")
    inputfile = filepath + "/" + empfile
    outputfile = filepath + "/" + "empgood.txt"
    errfile = filepath + "/" + "emperr.txt"
    try:
        infilept = open(inputfile,'r')
        goodfilept = open(outputfile,'w')
        errorpt = open(errfile,'w')
    except FileNotFoundError:
        msg = " file not found: " + inputfile
        eof = 1
    except:
        msg = "unknown file error"
        eof = 1
    errormsg(msg)
    return (infilept,goodfilept,errorpt,eof)

# -------------------------
# Read a record
# -------------------------
def getrecord(inpt,eof):
    print(' read  eof: ',eof)
    empno = ''
    ename = ''
    rate = ''
    hour = ''
    code = ''    
    if (eof == 0):
        rline = inpt.readline()
        if (rline ==""):
            eof = 1
        else:
            (empno, fname,lname,rate,hour,code) = rline.split(',')
            ename = fname + " " + lname
    print('return eof: ',eof)
    return(eof, empno, ename,rate,hour,code) 
    
# -------------------------
# Write a record
# -------------------------
def putgood(goodfilept,empno,ename,GP,FIT,SIT,NP,hour,OT):
    comma = ","
    outline = empno + comma + ename + comma + str(GP) + comma + str(FIT) + comma
    outline = outline + str(SIT) + comma + str(NP) + comma + hour + comma + str(OT) + '/n'
    goodfilept.write(outline)
    return

# -------------------------
# Write Error record
# -------------------------
def puterror(errorpt,empno, ename,rate,hour,code,msg ):
    comma = ','
    errline = empno + comma + ename + comma +rate + comma +hour
    errline = errline + comma +code + comma +msg + '\n'
    errorpt.write(errline)
    return
# -------------------------
# close files
# -------------------------
def closefiles():
    return
    
# ---------------------------------
#           main line
# ---------------------------------
def main():
    totals = [0] * 7
    cont = 'Y'
    errorcnt = 0
    readcnt = 0
    writecnt = 0
    eof = 0
    msg=''
    blkln(60) # clear screen
    print(' PROGRAM STARTED: ', datetime.now())
    blkln(2)
    print('open files ', 'eof: ',eof)
    (infilept,goodfilept,errorpt,eof)=openfiles()
    print(' first call to read ', 'eof: ',eof)
    (eof, empno, ename,rate,hour,code) = getrecord(infilept,eof)
    while (eof == 0):
        if (eof == 0):
            readcnt = readcnt + 1
            blkln(2)
            (rate,hour,msg) = rcdval(rate,hour)
            if (len(msg) == 0):
                prtname(ename,rate,hour)
                (GP,OT)=calcgp(rate,hour)
                blkln(2)
                FIT = calcfit(GP,code)
                SIT = calcsit(GP)
                NP = GP - FIT - SIT
                payprt(GP,NP,FIT,SIT)
                totals =ptotals(GP,NP,FIT,SIT,totals)
                putgood(goodfilept,empno,ename,GP,FIT,SIT,NP,hour,OT)
                writecnt = writecnt  + 1
                (eof, empno, ename,rate,hour,code) = getrecord(infilept,eof)
            else:
                errorcnt = errorcnt + 1
                puterror(errorpt,empno, ename,rate,hour,code,msg )
 
            blkln(2)
            print('--------------')
    if (len(msg) > 0):
        print(" Program terminated: ", msg)
    else:
        blkln(2)
        prttotals(totals)
        blkln(2)
        print(" Number of records read: ", readcnt) 
        print(" Number of records written: ", writecnt)
        print(" Number of errors: ", errorcnt)
        print(' PROGRAM ENDED: ', datetime.now())
        blkln(10)
    return
# ---------------------------------
#     Entry Point
# ---------------------------------    
main()    
# ---------------------------------
#    End of Program
# ---------------------------------
