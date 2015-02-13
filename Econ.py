#Use the following national income data to calculate
#(1) GDP (2) GNP (3) NNI(NI) &(4) PI
#GDP = C+I+G+(X-M) = 180 +46 +84+(9-10) =309
#GNP = 309 -2  =307
#NNI = GNP - indirect taxes - depreciation = 307-22-52=233
#PI = DI+personal taxes = 190 +38 =228
 
Gross_Investment = 46
Exports_of_Canada = 9
Disposable_income = 190
Personal_Saving = 10
Government_current_purchases_of_goods_and_services = 84
Capital_consumption_Allowances =52
Interest_and_misc_investment_income = 13
Imports_of_Canada = 10
Indirect_taxes = 22
Personal_taxes = 38
Other_earnings_not_paid_out_to_persons = 23
Net_Investment_income_from_nonresidents = -2

Q2 = 800
Q1 = 240

P2 = 180
P1 = 120

PED = ((Q2-Q1) / ((Q1+Q2) / 2)) / ((P2-P1)/((P1+P2)/2))
Slope = (P2-P1)/(Q2-Q1)

print(PED)
print(Slope)
