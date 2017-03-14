import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from decimal import Decimal
import csv

def processFile(inFile):
    lst = []
    with open(inFile) as f:
        for line in f:
            tmp = line.strip().split(",")
            lst.append(tmp)
    # sums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    arr = []
    for j in range(len(lst[0])):
        tmp = []
        for i in range(len(lst)):                    #get list without "?"
            if lst[i][j]!='?':
                tmp.append(lst[i][j])
        arr.append(tmp)
    #print(arr)
    
    
    median = []
    for l in arr:
        l.sort()                                     #find median, then assign to "?" value
        m = l[int(len(l)/2)]
        median.append(m)
    #print(median)
    
    newlst = []
    for i in range(len(lst)):
        tmp = []
        for j in range(len(lst[0])):
            if lst[i][j]!='?':
                tmp.append(lst[i][j])
            else:
                tmp.append(median[j])
        newlst.append(tmp)
    #print(newlst)
    
    #newlst2 = []
    #std = []
    #for j in range(len(lst[0])):
    #    temp = []
    #    for i in range(len(lst)):
    #        temp.append(newlst[i][j])
    #    newlst2.append(temp)
        #std.append(np.std(temp))
    #print(newlst2)
    #print(std)
    
    #for l in newlst2:
       # np.mean(l)
    
    #vectorizer = TfidfVectorizer(stop_words='english', min_df=10,max_df=0.8)
    #dtm = vectorizer.fit_transform(newlst) 
    #print(dtm)
    cat = []
    for i in range(len(newlst[0])):
        tmp = []
        cat.append(tmp)
    #print(cat)
    notDigital = [0,3,4,5,6,8,9,11,12]
    for i in range(len(newlst)):
        for j in range(len(newlst[0])):
            x = newlst[i][j]
            if j in notDigital:
                if x not in cat[j]:
                    cat[j].append(x)
                    
                    
    # newlst2 will make all attributes become digital numbers
    newlst2=[]
    for i in range(len(newlst)):
        tmp = []
        for j in range(len(newlst[0])):
            x = newlst[i][j]
            if j in notDigital:
                tmp.append(cat[j].index(x))
            else:
                tmp.append(x)
        newlst2.append(tmp)
    #print(newlst2)
    
    std = []
    average = []
    
    for j in range (len(newlst2[0])-1):
        tmp = []
        for i in range (len(newlst2)):
            tmp.append(float(newlst2[i][j]))
        std.append(np.std(tmp))
        average.append(np.average(tmp))
    #print(std)
    #print(average)
    
    normalize = []
    for i in range(len(newlst2)):
        tmp = []
        for j in range(len(newlst2[0])):
            if(j == len(newlst2[0])-1):
                if(newlst2[i][j] == '+'):
                    tmp.append(1)
                else:
                    tmp.append(2)
            else:
                x = float(newlst2[i][j])
                z = (x-average[j])/std[j]
                tmp.append(z)
        normalize.append(tmp)
    #print(normalize)
    
    # int_normalize = []
    # for i in range(len(normalize)):
    #     tmp = []
    #     for j in range(len(normalize[0])):
    #         s = normalize[i][j]
    #         x = int(s*100)
    #         tmp.append(x)
    #     int_normalize.append(tmp)



    if(inFile == 'crx.data.training'):
       with open("crx.training.processed",'a') as f:
            datawriter = csv.writer(f, delimiter= ',')
            for line in normalize:
                datawriter.writerow(line)
    if(inFile == 'crx.data.testing'):
        with open("crx.testing.processed",'a') as f:
            datawriter = csv.writer(f, delimiter= ',')
            for line in normalize:
                datawriter.writerow(line)


    # test = [0,1,2,3]
    # std = np.std(test)
    # average = np.average(test)
    # print((test[3]-average)/std)

def run(infile1, infile2):
    processFile(infile1)
    
    processFile(infile2)
    