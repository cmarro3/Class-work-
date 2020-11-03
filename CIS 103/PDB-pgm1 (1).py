# property tax calculator 1
def blkln(a):
    print('\n'*a)
    return
def misctax() 
    nheac = .004
    mwrdc = .406
    pmab = .006
    cpd = .362
    aa = nheac + mwrdc + pmab + cpd
    return aa
def schooltax() 
    bec = 3.726
    cccd = .169
    aa = bec + cccd
    return aa
def citytax():
    csbif=.128
    clf=.122
    city = 1.630
    aa = csbif + clf + city
    return aa
def countytax() 
    ccfpd = .063
    cook = .316
    ccps = .130
    cchf = .087
    aa = cfpd + cook + ccps + cchf
    return aa
def main():
    blkln(5)
    MiscTax = misctax()
    Schooltax = schooltax()
    City =citytax()
    CookCty = countytax()
    TotalTaxRate = MiscTax + SchoolTax + City + CookCty
    print('Property Tax Rate is: ', TotalTaxRate)

main()
