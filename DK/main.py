
import os
import csv
import pandas as pd
import Function as FFF

symPath='./ABG/ABG.csv'

Realpath = os.path.realpath(symPath)


headerCSV, df = FFF.LoadLog(symPath)
#print(headerCSV)
#print(df)

feature=headerCSV[0:31]
#print(len(feature))
D_41401  =  headerCSV[31:32]
D_4019  =  headerCSV[32:33]
D_4280  =  headerCSV[33:34]
D_486  =  headerCSV[34:35]
D_99592  =  headerCSV[35:36]
D_0389  =  headerCSV[36:37]
D_51881  =  headerCSV[37:38]
D_5845  =  headerCSV[38:39]
D_78791  =  headerCSV[39:40]
D_3051  =  headerCSV[40:41]
D_4168  =  headerCSV[41:42]
D_78551  =  headerCSV[42:43]
D_4928  =  headerCSV[43:44]
D_41519  =  headerCSV[44:45]
D_570  =  headerCSV[45:46]
D_1625  =  headerCSV[46:47]
D_5130  =  headerCSV[47:48]
D_7994  =  headerCSV[48:49]
D_5531  =  headerCSV[49:50]
D_7504  =  headerCSV[50:51]
'''
print("feature=",feature)


print("D_41401=",D_41401)
print("D_4019=",D_4019)
print("D_4280=",D_4280)
print("D_486=",D_486)
print("D_99592=",D_99592)
print("D_0389=",D_0389)
print("D_51881=",D_51881)
print("D_5845=",D_5845)
print("D_78791=",D_78791)
print("D_3051=",D_3051)
print("D_4168=",D_4168)
print("D_78551=",D_78551)
print("D_4928=",D_4928)
print("D_41519=",D_41519)
print("D_570=",D_570)
print("D_1625=",D_1625)
print("D_5130=",D_5130)
print("D_7994=",D_7994)
print("D_5531=",D_5531)
print("D_7504=",D_7504)
'''
X=df[feature]
#print(X)

Y=df[D_41401]
#print(Y)

A1=[3,0,3,0,3,3,3,3,3,3,3,3,0,3,3,3,0,3,3,3,3,0,3,3,1,3,3,3,3,3,3]
A2=[3,0,3,1,3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,1,3,3,0,3,3,3,3,3,3]
A3=[3,0,3,0,3,3,3,1,3,3,3,3,3,3,3,3,1,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A4=[3,0,3,0,3,3,1,0,3,3,3,3,0,3,3,3,1,3,3,3,3,0,3,3,1,3,3,0,3,3,3]
A5=[3,0,3,0,3,3,1,3,3,3,3,3,0,3,3,3,0,3,3,3,3,1,3,3,0,3,3,3,3,3,3]
A6=[3,0,3,1,3,3,3,1,3,3,3,3,0,3,3,3,1,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A7=[3,0,3,1,3,3,1,3,3,3,3,3,0,3,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A8=[3,0,3,0,3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,0,3,3,0,3,3,3,3,3,3]
A9=[3,0,3,0,3,3,3,3,3,3,3,3,0,0,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,0]
A10=[3,0,3,0,3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,0,3,3,1,3,3,3,3,3,3]
A11=[3,0,3,0,3,3,0,3,3,3,1,0,0,3,3,3,0,3,3,3,3,0,3,3,1,3,3,3,3,3,3]
A12=[3,0,3,0,3,3,3,3,3,3,1,0,0,3,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A13=[3,0,3,1,3,3,1,3,3,3,1,3,0,0,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,0]
A14=[3,0,3,1,3,3,1,3,3,3,1,0,0,3,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A15=[3,0,3,0,3,3,1,3,3,3,1,3,3,0,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,0]
A16=[3,0,3,0,3,3,3,3,3,3,3,3,0,3,3,3,1,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A17=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A18=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0]
A19=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A20=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A21=[3,0,3,1,3,3,1,0,3,3,1,3,0,3,3,3,0,3,3,3,3,1,3,3,1,3,3,0,3,3,3]
A22=[3,0,3,1,3,3,3,3,3,3,3,3,0,3,3,3,0,3,3,3,3,1,3,3,0,3,3,3,3,3,3]
A23=[3,0,3,1,3,3,3,3,0,1,3,0,0,3,3,3,1,3,3,3,3,0,3,3,1,3,3,3,3,3,3]
A24=[3,0,3,0,3,3,3,3,3,3,3,3,0,3,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,0]
A25=[3,0,3,0,3,3,3,3,3,3,3,3,0,3,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A26=[3,0,3,0,3,3,3,1,3,3,1,3,0,3,3,3,1,3,3,3,3,0,3,3,1,3,3,3,3,3,3]
A27=[3,0,3,0,3,3,3,3,3,3,3,3,0,3,3,3,1,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A28=[3,0,3,1,3,3,3,3,3,3,3,3,3,3,3,3,1,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A29=[3,0,3,0,3,3,3,3,3,3,3,3,0,3,3,3,1,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A30=[3,0,3,0,3,3,1,3,3,3,1,0,0,3,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A31=[3,0,3,0,3,3,1,3,0,1,3,3,0,3,3,3,1,3,3,3,3,1,3,3,1,3,3,0,3,0,3]
A32=[3,0,3,0,3,3,3,3,3,3,1,3,3,3,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,3]
A33=[3,0,3,0,3,3,3,3,3,3,3,3,0,3,3,3,0,3,3,3,3,0,3,3,1,3,3,3,3,3,3]
A34=[3,0,3,1,3,3,1,3,3,3,1,3,0,0,3,3,0,3,3,3,3,1,3,3,1,3,3,3,3,3,0]
A35=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A36=[3,3,3,3,3,3,3,3,0,1,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A37=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A38=[3,3,3,3,3,3,3,1,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A39=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A40=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
A41=[3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]


from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, Y)



print(dtree.predict([A1]))
print(dtree.predict([A2]))
print(dtree.predict([A3]))
print(dtree.predict([A4]))
print(dtree.predict([A5]))
print(dtree.predict([A6]))
print(dtree.predict([A7]))
print(dtree.predict([A8]))
print(dtree.predict([A9]))
print(dtree.predict([A10]))
print(dtree.predict([A11]))
print(dtree.predict([A12]))
print(dtree.predict([A13]))
print(dtree.predict([A14]))
print(dtree.predict([A15]))
print(dtree.predict([A16]))
print(dtree.predict([A17]))
print(dtree.predict([A18]))
print(dtree.predict([A19]))
print(dtree.predict([A20]))
print(dtree.predict([A21]))
print(dtree.predict([A22]))
print(dtree.predict([A23]))
print(dtree.predict([A24]))
print(dtree.predict([A25]))
print(dtree.predict([A26]))
print(dtree.predict([A27]))
print(dtree.predict([A28]))
print(dtree.predict([A29]))
print(dtree.predict([A30]))
print(dtree.predict([A31]))
print(dtree.predict([A32]))
print(dtree.predict([A33]))
print(dtree.predict([A34]))
print(dtree.predict([A35]))
print(dtree.predict([A36]))
print(dtree.predict([A37]))
print(dtree.predict([A38]))
print(dtree.predict([A39]))
print(dtree.predict([A40]))
print(dtree.predict([A41]))



