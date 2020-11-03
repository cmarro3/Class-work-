#-------------------------
#  Payroll Program
#-------------------------

def main():
    print ('\n'*60)    # clear screen
    PayRate = 0.0
    Hours = 0.0
    Fname = ""
    Lname = ""
    Fname = input('Enter first name of Employee: ')
    Lname = input('Enter last name of Employee: ')
    PayRate = float(input('Enter Rate of Pay: '))
    Hours = float(input('Number of Hours worked: '))
    print ('\n' * 10)
    ename = Fname + " " + Lname
    print('Employee Name: ',ename,'\n')
    print('Rate of Pay: ',PayRate,'\n')
    print('Hours Worked: ', Hours)
    print('\n' *10)

main()
