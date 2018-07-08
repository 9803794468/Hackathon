from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error
from tkinter import *
from scipy import stats

class socialData:
    faceb = {2009: [197, 242, 305, 360], 2010: [431, 482, 550, 608], 2011: [680, 739, 800, 845],
             2012: [901, 955, 1007, 1056], 2013: [1010, 1155, 1189, 128], 2014: [1276, 1317, 1350, 1393],
             2015: [1441, 1490, 1545, 1591], 2016: [1654, 1712, 1788, 1860], 2017: [1936, 2006, 2072, 2129],
             2018: [2196]}

    insta = {2013: [90, 100, 130, 150], 2014: [200, 300, 400], 2015: [400], 2016: [500, 600], 2017: [700, 800],
             2018: [1000]}

    snap = {2014: [46, 57, 62, 71], 2015: [80, 86, 94, 107], 2016: [122, 143, 153, 158], 2017: [166, 173, 178, 187],
            2018: [191]}




class plot(socialData):
    yearsf = []
    facebook = []
    for i, j in socialData.faceb.items():
        yearsf.append(i)
        facebook.append(j[0])
    yearsf = yearsf[:len(yearsf) - 1]

    yearsi = []
    instagram = []
    for i, j in socialData.insta.items():
        yearsi.append(i)
        instagram.append(j[0])
    yearsi = yearsi[:len(yearsi) - 1]

    yearss = []
    snapchat = []
    for i, j in socialData.snap.items():
        yearss.append(i)
        snapchat.append(j[0])
    yearss = yearss[:len(yearss) - 1]

    grtfcb = []
    for i in range(len(facebook) - 1):
        diff = facebook[i + 1] - facebook[i]
        per = (diff / facebook[i]) * 100
        grtfcb.append(per)

    grint = []
    for i in range(len(instagram) - 1):
        diff = instagram[i + 1] - instagram[i]
        per = (diff / instagram[i]) * 100
        grint.append(per)

    grsnp = []
    for i in range(len(snapchat) - 1):
        diff = snapchat[i + 1] - snapchat[i]
        per = (diff / snapchat[i]) * 100
        grsnp.append(per)

    regression = LinearRegression()

    l = len(yearsf)
    yearsf = np.arange(2009, 2018)
    yearsf = yearsf.reshape(l, 1)

    regf = regression.fit(yearsf, grtfcb)  # We are providing Training Data

    Y1f = regf.predict(yearsf)
    msef = regf.score(yearsf, grtfcb)
    # plt.plot(yearsf,Y1,label="facebook")

    regression = LinearRegression()

    l = len(yearsi)
    yearsi = np.arange(2013, 2018)
    yearsi = yearsi.reshape(l, 1)

    regi = regression.fit(yearsi, grint)  # We are providing Training Data

    Y1i = regi.predict(yearsi)
    msei = regi.score(yearsi, grint)
    # plt.plot(yearsi,Y1,label="instagram")

    regression = LinearRegression()

    l = len(yearss)
    yearss = np.arange(2014, 2018)
    yearss = yearss.reshape(l, 1)

    regs = regression.fit(yearss, grsnp)  # We are providing Training Data

    Y1s = regs.predict(yearss)
    mses = regs.score(yearss, grsnp)




    def __init__(self):

        print("Enter 1 For Growth Rate Comparisons")
        print("Enter 2 For Regression Line")
        print("Enter 3 to Know The Prediction")
        ch=input()
        if ch=='1':
            plt.plot(plot.yearsf, plot.grtfcb, label="facebook")
            plt.plot(plot.yearsi, plot.grint, label="instagram")
            plt.plot(plot.yearss, plot.grsnp, label="snapchat")
            plt.xlabel("Years")
            plt.ylabel("Growth Rate%")
            plt.grid()
            plt.legend()
            plt.show()

        elif ch=='2':
            plt.plot(plot.yearsf, plot.Y1f, label="facebook")
            plt.plot(plot.yearsi, plot.Y1i, label="facebook")
            plt.plot(plot.yearss, plot.Y1s, label="facebook")
            plt.grid()
            plt.xlabel("years")
            plt.ylabel("Growth Rate")
            plt.legend()
            plt.show()

        elif ch=='3':
            ey=int(input("Enter the last year:"))
            years=list(map(int,range(2019,ey+1)))
            arr=np.arange(2019,ey+1).reshape(ey-2019+1,1)
            Y1 = plot.regf.predict(arr)
            print(Y1)
            plt.plot(arr,Y1,label="Facebook")
            plt.xlabel("Years")
            plt.ylabel("Growth Rate")
            plt.legend()
            plt.grid()
            plt.show()

            us=[]
            pu=2196
            print(len(Y1))
            print(len(years))
            for j in Y1:
                a=((j*pu)/100)+pu
                us.append(a)

            plt.plot(years,us,label="Facebook")
            plt.legend()
            plt.xlabel("Years")
            plt.ylabel("Active Users(millions)")
            plt.grid()
            plt.show()


        else:
            exit()




i=1
while i==1:

    user=plot()

print("Facebook will end in 2027 if this will be growth rate ")

######Group:Ravneet Singh,Prabhudeep Singh,Saurav Rathore,Surender yadav
