def liveSMA(histst, histmt, histlt, live):
    histST = histst
    histMT = histmt
    histLT = histlt
    x = 0
    y = 0
    z = 0
    histST.pop(0)
    histST.append(live)
    histMT.pop(0)
    histMT.append(live)
    histLT.pop(0)
    histLT.append(live)
    
    for i in histST:
        x += float(i)
        
    liveST = round((x / 7), 4)
    
    for i in histMT:
        y += float(i)
        
    liveMT = round((y / 25), 4)
        
    for i in histLT:
        z += float(i)
        
    liveLT = round((z / 99), 4)
    
    return liveST, liveMT, liveLT, histMT