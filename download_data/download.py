import pandas as pd
from pandas_datareader import data as pdr
import datetime as date
import time

#Iniciamos parametros de fecha
startdate = date.datetime(2017, 1, 1)
enddate = date.datetime(2018, 1, 1)


tickers = ['OMAB.MX','VOLARA.MX','CUERVO.MX','NEMAKA.MX','KIMBERA.MX','GCARSOA1.MX',
           'CEMEXCPO.MX','GRUMAB.MX','BSMXB.MX','GMEXICOB.MX','GENTERA.MX',
           'MEXCHEM.MX','AMXL.MX','GAPB.MX','IENOVA.MX','MEGACPO.MX','FEMSAUBD.MX',
           'RA.MX','GFNORTEO.MX','ASURB.MX','AC.MX','GMXT.MX','ALSEA.MX','KOF-L.MX','PINFRA.MX',
           'LALAB.MX','ALPEKA.MX','GFINBURO.MX','LIVEPOLC1.MX','ALFAA.MX']
test =['TSLA']

def get_Data(index):
    data = pdr.get_data_yahoo(index, start=startdate, end=enddate)
    data1 = data['Adj Close']
    return data1

ipc = get_Data('^MXX')


for tick in tickers:
    try:
        a = get_Data(tick)
        a.name = tick
        ipc = pd.concat([ipc,a], axis=1,join_axes=[ipc.index])
        print 'Test for' + tick
        time.sleep(10)
    except:
        pass

ipc.to_csv('tickersIPC.csv')
