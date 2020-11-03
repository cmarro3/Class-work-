# -------------------------
#  Payroll Program 5  error handling
# -------------------------
# blank lines
# ------------
def blkln(a):           
    print('\n'*a)
    return
# ---------------------
# Print error message
# ---------------------
def errormsg():          
    print('******************************')
    print('  INPUT ERROR')
    print(' Rate of pay or Hours')
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
#  get rate of pay and hours worked
# ------------------------------------------
def getratehrs():   
    try:
        rate = float(input('Enter Rate of Pay: '))
    except:
        rate = 0
    try:
        hrs = float(input('Number of Hours worked: '))
    except:
        hrs = 0
    return (rate,hrs)
# --------------------------------
# calculate gross pay
# --------------------------------
def calcgp():       
    ot = 0.0
    (rate,hrs) = getratehrs()
    if (rate == 0) or (hrs == 0):
        gp = 0
        ot = 0
    else:    
        (hrsot,ot) = overtime(hrs)
        gp =  rate * hrsot
    return(gp,rate,hrs,ot)
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
    Lname = input('Enter last name of Employee: ')
    cname = Fname + " " + Lname
    return cname
# ---------------------------------
#           main line
# ---------------------------------
def main():     
    blkln(60) # clear screen
    ename = getname()
    (GP,PayRate,Hours,OT)=calcgp()
    blkln(5)
    print('Employee Name: ',ename)
    print('Rate of Pay: ',PayRate)
    print('Hours Worked: ', Hours,'\n')
    if (PayRate == 0) or (Hours == 0):
        errormsg()        
    else:
        FIT = calcfit(GP)
        SIT = calcsit(GP)
        NP = GP - FIT - SIT
        blkln(2)
        if OT > 0:
            print('    Overtime Hours: ',OT, '\n')
        payprt(GP,NP,FIT,SIT)
    blkln(10)
    return
# ---------------------------------
#     Entry Point
# ---------------------------------    
main()    
# ---------------------------------
#    End of Program
# ---------------------------------
