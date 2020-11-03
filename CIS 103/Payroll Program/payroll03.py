#-------------------------
#  Payroll Program
#-------------------------
def blkln(a):
    print('\n'*a)
def calcgp():
    rate = float(input('Enter Rate of Pay: '))
    hrs = float(input('Number of Hours worked: '))
    gp =  rate * hrs
    return(gp,rate,hrs)
def calcfit(gp):
    fitrate = .12
    cfit = gp * fitrate
    return cfit
def calcsit(gp):
    sitrate =0.0495
    csit = gp * sitrate
    return csit
def getname():
    Fname = input('Enter first name of Employee: ')
    Lname = input('Enter last name of Employee: ')
    cname = Fname + " " + Lname
    return cname
def main():
    blkln(60) # clear screen
    (GP,PayRate,Hours)=calcgp()
    FIT = calcfit(GP)
    SIT = calcsit(GP)
    NP = GP - FIT - SIT
    ename = getname()
    blkln(10)
    print('Employee Name: ',ename,'\n')
    print('Rate of Pay: ',PayRate,'\n')
    print('Hours Worked: ', Hours,'\n')
    print('Gross Pay: ',GP)
    print('FIT: ', FIT)
    print('SIT: ', SIT)
    print('Net Pay: ', NP)
    blkln(10)
main()
