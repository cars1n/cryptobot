'''rsi uses 14 periods. 1.25 (Avg. Gain over last 13 bars) +. 25 (Current Gain) / (.75 (Avg. Loss over last 13 bars) + 0 (Current Loss))
Relative Strength = 1.50 / .75 = 2
RSI = 100 – [100/(1+2)] = 66.67'''

def rsi(li):

    counter = 0
    
    num_li = li[10:]
    
    order_lis = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    
    dic = dict(zip(order_lis, num_li))
    
    a = dic['1'] - dic['2']
    
    b = dic['2'] - dic['3']
    
    c = dic['3'] - dic['4']
    
    d = dic['4'] - dic['5']
    
    e = dic['5'] - dic['6']
    
    f = dic['6'] - dic['7']
    
    g = dic['7'] - dic['8']
    
    h = dic['8'] - dic['9']
    
    i = dic['9'] - dic['10']
    
    j = dic['10'] - dic['11']
    
    k = dic['11'] - dic['12']
    
    l = dic['12'] - dic['13']
    
    m = dic['13'] - dic['14']
    
    n = (a+b+c+d+e+f+g+h+i+j+k+l+m) / 13
        
    print(n)
    
rsi([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,5.0,4.0,5.0,5.0,6.0,7.0,8.0,5.0,6.0,7.0,7.0,6.0,5.0,6.0,7.0])