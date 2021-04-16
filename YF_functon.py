# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:47:50 2021

@author: hualiya
"""
    
def yh_download_price():
    ''''given a list of security and a date range download the marketcap '''
    # setting directory
    import os
    from getwd import getwd
    path = getwd()
    parent = os.path.dirname(path)
    # get ui input
    from userinput import readinput    
    SecurityList, sheet_PortSecurities, UI_SD, UI_ED, UI_StartValue = readinput()
    # import packages
    import yfinance as yf
    
    # obtain a list security which has removed BB_format 'US EQUITY' 
    list_Sec = [SecurityList[i][:-10] for i in range(len(SecurityList))]
    # return OHLC, volume
    df_px = yf.download(tickers = list_Sec,
                           start=UI_SD,
                           end=UI_ED,
                           group_by=list_Sec,
                           # Corporate Actions
                           # action = 'inline'
                           )    
    df_px.to_excel(parent + '\\Inputs\\OHLCV_YH.xlsx')
    
def yh_download_mkt():
    ''''not available for ETF only, it works for  EQ
        list_Sec = ['AAPL','TSLA','GME'] '''
    import os
    from getwd import getwd
    path = getwd()
    parent = os.path.dirname(path)
    # get ui input
    from userinput import readinput    
    SecurityList, sheet_PortSecurities, UI_SD, UI_ED, UI_StartValue = readinput()
    list_Sec = [SecurityList[i][:-10] for i in range(len(SecurityList))]
    #testing purpose
    # import packages
    import yfinance as yf
    import pandas as pd
    
    mkt = [yf.Ticker(list_Sec[i]).info['marketCap'] for i in range(len(list_Sec))]                         
    # construct df
    df_mkt = pd.DataFrame()  
    for j in range(len(list_Sec)):     
        df_mkt['Ticker'] = list_Sec
        df_mkt['MarketCap'] = mkt        
    df_mkt.to_excel(parent + '\\Inputs\\Marketoverview_YH.xlsx')     

def yh_update_download_mkt():
    pass
   
def bb_download_mkt():
    ''''given a list of security and a date range download the marketcap'''
    import os
    from getwd import getwd
    path = getwd()
    parent = os.path.dirname(path)
    
    from userinput import readinput    
    SecurityList, sheet_PortSecurities, UI_SD, UI_ED, UI_StartValue = readinput()
    print(list_security)
    
def bb_update_download_mkt():    
    pass
   #
   # import yfinance as yf
    
    # ticker = yf.Ticker("aapl")
    
    # # corperate actions
    # # show dividends
    # dividends = ticker.dividends
    # # show splits
    # splits = ticker.splits
    # # recommendations from other investment
    # recomm = ticker.recommendations
    # # institutional holders
    # hold_instit = ticker.institutional_holders
    # ticker.info['marketCap']

