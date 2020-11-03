# property tax program calculator 2
def GetPropertyValue()
    aa=float(input('Enter value of property:')
    return aa
def GetLocalTaxRate()
    aa = float(input('Enter loacal tax rate: ')
        return aa
def GetEqual()
    aa = float(input('Enter state equalizer rate: '))
    return aa
def blkln(x):
    print('\n'*a)
    return
def main():
    blkln(10)
    AssesmentLevel = .10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue=GetPropertyValue()
    LocalTaxRate = getLocalTaxRate()
    StateEqualizer = GetEqualizer()
    blkln(5)
    AssessedValue= PropertyValue * AssesssmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertTaxBefore = EqualizeValue * LocalTaxRate
    TotalPropertyTax = PropertyTaxBefroe - HomeOwnerEx - SeniorCEX
    blkln(5)
    print(' Property tax due: ',TotalPropertyTax)
    blkln(5)
    return
main()
