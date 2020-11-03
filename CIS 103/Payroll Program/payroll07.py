# -------------------------
#  Payroll Program 7 loops
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
# -----------------------------------
def calcfit(gp):     
    fitrate = .12
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
    Fname = input('Enter first name of Employee: ')
    cname= Fname.strip()
    if cname.upper() != "END":
        Lname = input('Enter last name of Employee: ')
        cname = Fname + " " + Lname
    return cname
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
# ---------------------------------
#           main line
# ---------------------------------
def main():
    cont = 'Y'
    blkln(60) # clear screen
    while (cont.upper() == 'Y'):
        ename = getname()
        if ename.upper() == 'END':
            cont = 'n'
        else:
            blkln(2)
            (GP,PayRate,Hours,OT,msg)=calcgp()
            if (len(msg) == 0):
                prtname(ename,PayRate,Hours,OT)
                blkln(2)
                FIT = calcfit(GP)
                SIT = calcsit(GP)
                NP = GP - FIT - SIT
                payprt(GP,NP,FIT,SIT)
            blkln(2)
            print('--------------')
    print(' Program terminated')
    blkln(10)
    return
# ---------------------------------
#     Entry Point
# ---------------------------------    
main()    
# ---------------------------------
#    End of Program
# ---------------------------------
