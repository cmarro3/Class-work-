# -------------------------
#  Payroll Program 9 dictionary
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
# -----------------------------------
# calc overtime
# -----------------------------------
def overtime(thrs):      
    hrsov = 0.0
    if thrs > 40:
        hrsov = thrs-40
        otr = hrsov *   .5
        thrs = thrs + otr
    return (thrs,hrsov)
# ------------------------------------------
#  get rate of pay 
# ------------------------------------------
def getrate():
    rate = 0
    msg=''
    srate = input('Enter Rate of Pay: ')
    if (len(srate) ==0):
        msg = '***Error  Rate must have a value'
    else:
        if srate.isdecimal():
            try:
                rate = float(srate)
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
                rate = float(srate)
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
def gethrs():   
    hrs = 0
    msg=''
    shrs = input('Enter Hours worked: ')
    if (len(shrs) ==0):
        msg = '***Error  Hours must have a value'
    else:
        if shrs.isdecimal():
            try:
                hrs = float(shrs)
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
                hrs = float(shrs)
                if hrs < 0:
                    msg=' **** error  hours cannot be negative' 
            except:
                msg=' **** error: hours has invalid value' 
    if len(msg)> 0:
        hrs=0
    return (hrs,msg)     
# --------------------------------
# calculate gross pay
# --------------------------------
def calcgp():       
    ot = 0.0
    (rate,msg) = getrate()
    errormsg(msg)
    (hrs,msg) = gethrs()
    errormsg(msg)
    if (rate == 0) or (hrs == 0):
        gp = 0
        ot = 0
    else:    
        (hrsot,ot) = overtime(hrs)
        gp =  rate * hrsot
    return(gp,rate,hrs,ot,msg)
# -----------------------------------
# calculate federal income tax
#      codes A =.12, B =.15, c =.18
# -----------------------------------
def calcfit(gp,cd):
    ratecode={'A':.12,'B':.15,'C':.18}
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
# get name of employee
# ---------------------------------
def getname():
    cd='A'       # set default code
    Fname = input('Enter first name of Employee: ')
    cname= Fname.strip()
    if cname.upper() != "END":
        Lname = input('Enter last name of Employee: ')
        cname = Fname + " " + Lname
        cd = input('Enter FIX tax code: ')
        if (cd.upper() == 'A') or (cd.upper()== 'B') or (cd.upper()=='C'):
            cd = cd.upper()
        else:
            print('Invalid FIT code, code set to default A')
    return (cname, cd)
# ---------------------------------
# show report
# ----------------------------------
def prtname(ename,PayRate,Hours,OT):
    blkln(2)
    print(' ==============================')
    print('Employee Name: ',ename) 
    print('Rate of Pay: ',PayRate)
    print('Hours Worked: ', Hours,'\n')
    if OT > 0:
        print('    Overtime Hours: ',OT, '\n')
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
# ---------------------------------
#           main line
# ---------------------------------
def main():
    totals = [0] * 7
    cont = 'Y'
    error = 0
    blkln(60) # clear screen
    print(' PROGRAM STARTED: ', datetime.now())
    blkln(2)
    while (cont.upper() == 'Y'):
        (ename,cd) = getname()
        if ename.upper() == 'END':
            cont = 'n'
        else:
            blkln(2)
            (GP,PayRate,Hours,OT,msg)=calcgp()
            if (len(msg) == 0):
                prtname(ename,PayRate,Hours,OT)
                blkln(2)
                FIT = calcfit(GP,cd)
                SIT = calcsit(GP)
                NP = GP - FIT - SIT
                payprt(GP,NP,FIT,SIT)
                totals =ptotals(GP,NP,FIT,SIT,totals)
            else:
                error=error + 1
            blkln(2)
            print('--------------')
    blkln(2)
    prttotals(totals)
    blkln(2)
    if error > 0:
        print(' number of errors: ',error)
        blkln(2)
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
