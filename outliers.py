import math # to round the positions of medians

def GetOutliers(col):
    Quartile=[] #Postions list of medians of different quartile
    SortedSeries=col.sort_values(ignore_index=True) #Sort series to get the medians of different Quartile
    Quart2Pos=1/2*(len(SortedSeries)+1) #Position of Quartile Values
    Quart1Pos=1/4*(len(SortedSeries)+1)
    Quart3Pos=3/4*(len(SortedSeries)+1)
    ElementPos=[Quart1Pos,Quart2Pos,Quart3Pos] 
    for i in range(len(ElementPos)):  #Getting values of the quartile
        Quartile.append((SortedSeries[math.floor(ElementPos[i])]+SortedSeries[math.floor(ElementPos[i]+1)])/2)
    IQR=Quartile[2]-Quartile[0]
    LowerLimit=Quartile[0]-1.5*IQR
    UpperLimit=Quartile[2]+1.5*IQR
    Outliers=SortedSeries.loc[(SortedSeries < LowerLimit) | (SortedSeries > UpperLimit)]
    if len(Outliers)>0:
        return Outliers #Returing series of Outliers
    elif len(Outliers)<=0:
        return "There are no Outliers"


GetOutliers(housing.price)
