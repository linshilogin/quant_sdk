# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:33:56 2018

@author: SH
"""
from gm.api import *
import pandas as pd
import time
from pandas.tseries.offsets import DateOffset
from pandas.tseries.offsets import Second
import datetime

from pyalgotrade import calendayBylw
from pyalgotrade.broker import gmEnum

from pyalgotrade import commonHelpBylw
from pyalgotrade import observer



from datetime import timezone
from datetime import timedelta


## 用来获取当前主力合约的下一个主力合约的ID
#虽然这不太正确，因为下一个主力合约 是要根据当时成交量来判断的
#但是当前国内商品期货，主力合约都是固定的。比如 zc，的主力合约都是01，05，09 三个合约。所以
#主要针对这种情况
from pyalgotrade import loggerHelpbylw

month159CZCE = ['CZCE.TA', 'CZCE.SR', 'CZCE.CF', 'CZCE.OI', 'CZCE.MA',
                'CZCE.FG', 'CZCE.RM', 'CZCE.ZC', 'CZCE.SF', 'CZCE.SM']
month1510CZCE = ['CZCE.AP']

# 13个
month159DCE = ['DCE.A', 'DCE.B', 'DCE.C', 'DCE.CS', 'DCE.I', 'DCE.J',
               'DCE.JD', 'DCE.JM', 'DCE.L', 'DCE.M', 'DCE.P',
               'DCE.PP', 'DCE.V', 'DCE.Y', 'DCE.EG']

month1to12INE = ['INE.SC']


# 12个
# 铜  铝 锌 铅
month1to12SHFE = ['SHFE.AL', 'SHFE.CU', 'SHFE.PB', 'SHFE.ZN']
# 镍  锡 橡胶
month159SHFE = ['SHFE.SN', 'SHFE.NI', 'SHFE.RU', 'SHFE.FU', 'SHFE.SP']
# 螺纹 热卷
month1510SHFE = ['SHFE.HC', 'SHFE.RB']
# 沥青  黄金  白银
month612SHFE = ['SHFE.AU', 'SHFE.BU', 'SHFE.AG']

allCon = ['CFFEX.IC', 'CFFEX.IH', 'CFFEX.IF', 'CFFEX.T', 'CFFEX.TF']


def getNextContractID(currContractID):
    
  
    
    newContractID=''
   
    if 'CZCE.ZC' in currContractID:
        if currContractID[-2:]=='01':
            newContractID=currContractID[:-2]+'05'
        if currContractID[-2:]=='05':
            newContractID=currContractID[:-2]+'09'
        if currContractID[-2:]=='09':
            temp=str(int(currContractID[-3])+1)
            newContractID=currContractID[:-3]+temp+'01'
            
    return newContractID


# 即将相关系数矩阵 处理为 各个配对 排序的方式
def corrMatrixToPairs(corrMatrixOriginal):
    
    
    
    
    au_corr = corrMatrixOriginal.unstack()
    pairs_to_drop = set()
    cols = corrMatrixOriginal.columns
    for i in range(0, corrMatrixOriginal.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    au_corr = au_corr.drop(labels=pairs_to_drop).sort_values(ascending=False)
    au_corr.rename('corrCoeff',inplace=True)
    return au_corr
#    
    
'''

  #10g个
    month159CZCE=['CZCE.TA','CZCE.SR','CZCE.CF','CZCE.OI','CZCE.MA',
                      'CZCE.FG','CZCE.RM','CZCE.ZC','CZCE.SF','CZCE.SM']
    
    #13个
    month159DCE=['DCE.A','DCE.C','DCE.CS','DCE.I','DCE.J',
                      'DCE.JD','DCE.JM','DCE.L','DCE.M','DCE.P',
                      'DCE.PP','DCE.V','DCE.Y']
    
    #12个
   #铜  铝 锌 铅
    month1to12SHFE=['SHFE.AL','SHFE.CU','SHFE.PB','SHFE.ZN']
    
    #镍  锡 橡胶
    month159SHFE=['SHFE.SN','SHFE.NI','SHFE.RU']
    
    #螺纹 热卷
    month1510SHFE=['SHFE.HC','SHFE.RB']
    
    #沥青  黄金  白银
    month612SHFE=['SHFE.AU','SHFE.BU','SHFE.AG']

    
    
'''






#
#'''
#
##取出指定时间内正在市场上交易的合约。
#
#'''
#
#def getSomeContractBylw(month159CZCE,month159DCE,\
#                        month1to12SHFE,month159SHFE,month1510SHFE,month612SHFE,\
#                        sDateTime,eDateTime):
#    
#    
#    
#    
#    
#    
#    currAllFutureContract=get_instruments(symbols=None, exchanges=None, sec_types=[SEC_TYPE_FUTURE], names=None, skip_suspended=True, skip_st=True, fields='symbol,exchange,sec_id,listed_date,delisted_date', df=True)
#    
#    if sDateTime and eDateTime:
#        currAllFutureContract=currAllFutureContract\
#        [~((currAllFutureContract['listed_date'].astype(str)>eDateTime)|\
#         (currAllFutureContract['delisted_date'].astype(str)<sDateTime))]
#    
#    tempContract=currAllFutureContract
#    
#    finalContract=[]
#    
#    for inx, row in tempContract.iterrows():
#        
#        currVirtualContract=''
#        if row['exchange']=='CZCE':
#            currVirtualContract=row['exchange']+'.'+row['sec_id'][:-3].upper()
#        else:
#            currVirtualContract=row['exchange']+'.'+row['sec_id'][:-4].upper()
#    
#        if row['exchange']=='SHFE':
#            i=1
#            
#        if  currVirtualContract in month159CZCE+month159DCE+month159SHFE:
#            if row['sec_id'][-2:] in ['01','05','09']:
#                finalContract.append(row['symbol'])
#        if  currVirtualContract in month1to12SHFE:
#            if row['sec_id'][-2:] in ['01','02','03','04','05','06']:
#                finalContract.append(row['symbol'])
#        if  currVirtualContract in month1510SHFE:
#            if row['sec_id'][-2:] in ['01','05','10']:
#                finalContract.append(row['symbol'])
#        if  currVirtualContract in month612SHFE:
#            if row['sec_id'][-2:] in ['06','12']:
#                finalContract.append(row['symbol'])
#                
#    i=1
#    return finalContract
#               
      
    
'''

取出指定时间内正在市场上交易的合约。

'''
#
#def getSomeContract2Bylw(month159,month1to12,month1510,month612,\
#                        sDateTime,eDateTime):
#    
#    
#    
#    
#    
#    
#    currAllFutureContract=get_instruments(symbols=None, exchanges=None, sec_types=[SEC_TYPE_FUTURE], names=None, skip_suspended=True, skip_st=True, fields='symbol,exchange,sec_id,listed_date,delisted_date', df=True)
#    
#    if sDateTime and eDateTime:
#        currAllFutureContract=currAllFutureContract\
#        [~((currAllFutureContract['listed_date'].astype(str)>eDateTime)|\
#         (currAllFutureContract['delisted_date'].astype(str)<sDateTime))]
#    
#    tempContract=currAllFutureContract
#    
#    finalContract=[]
#    
#    for inx, row in tempContract.iterrows():
#        
#        currVirtualContract=''
#        if row['exchange']=='CZCE':
#            currVirtualContract=row['exchange']+'.'+row['sec_id'][:-3].upper()
#        else:
#            currVirtualContract=row['exchange']+'.'+row['sec_id'][:-4].upper()
#    
#        if row['exchange']=='SHFE':
#            i=1
#        if row['sec_id'][:-4]=='cu':
#            i=1
#            
#            
#        if  currVirtualContract in month159:
#            if row['sec_id'][-2:] in ['01','05','09']:
#                finalContract.append(row['symbol'])
#        if  currVirtualContract in month1to12:
#            if row['sec_id'][-2:] in ['01','03','05','07','09','11']:
#                finalContract.append(row['symbol'])
#        if  currVirtualContract in month1510:
#            if row['sec_id'][-2:] in ['01','05','10']:
#                finalContract.append(row['symbol'])
#        if  currVirtualContract in month612:
#            if row['sec_id'][-2:] in ['06','12']:
#                finalContract.append(row['symbol'])
#                
#    i=1
#    return finalContract
#               




'''

取出到当前时间点所有历史上出现过的沪深A股

'''
def getHSAStockBylw():


    
    # 取出所有沪深A股。 掘金上，没法直接取，只能绕一绕。
    #取出最新时间时刻的 沪深300股票。
    
    
    #下面函数取所有交易所的所有标的，查掘金文档知道，支持的交易所只有国内的
    #上交所	SHSE
    #深交所	SZSE
    #中金所	CFFEX
    #上期所	SHFE
    #大商所	DCE
    #郑商所	CZCE
    #上海国际能源交易中心	INE
    #所以限定取股票后基本上取的就是沪深2市的股票了。
    stock300=get_instruments(symbols=None, exchanges=None, sec_types=[SEC_TYPE_STOCK], names=None, skip_suspended=False, skip_st=False, fields='symbol,sec_type,exchange,sec_id,sec_name,listed_date,delisted_date,is_suspended', df=True)
    
    
    #清除b股
    aStock=stock300.loc[(stock300['sec_id'].str[0]!='2') & (stock300['sec_id'].str[0]!='9')]
    
    
    
    return list(aStock['symbol'].values)




    

def getExchangeFromGmSymbol(gmSymbol):
    return gmSymbol.split('.')[0]

'''

获取指定时间段内，某些品种的在 上市交易的 符合 要求的合约。

'''

def getContractsByUnderlyingSymbols(symbolsCode,sDateTime,eDateTime):
    
    #sDateTime是字符串类型。只有日期
    #symbolsCode 是标的资产的代码。是个list
    
          #10g个

    exchangelist=[]
    for asym in symbolsCode:
        exchangelist.append(getExchangeFromGmSymbol(asym))
    exchangelist=list(set(exchangelist))


    month159=month159CZCE+month159DCE+month159SHFE
    month1to12=month1to12SHFE+month1to12INE
    month1510=month1510SHFE+month1510CZCE
    month612=month612SHFE
    
    currAllFutureContract=get_instruments(symbols=None, exchanges=exchangelist, sec_types=[SEC_TYPE_FUTURE], names=None, skip_suspended=True, skip_st=True, fields='symbol,exchange,sec_id,listed_date,delisted_date', df=True)

    currAllFutureContract['listed_date']=currAllFutureContract['listed_date'].dt.strftime('%Y-%m-%d %H:%M:%S')
    currAllFutureContract['listed_date'] = currAllFutureContract['listed_date'].str[0:10]
    currAllFutureContract['delisted_date'] = currAllFutureContract['delisted_date'].dt.strftime('%Y-%m-%d %H:%M:%S')
    currAllFutureContract['delisted_date'] = currAllFutureContract['delisted_date'].str[0:10]


    if sDateTime and eDateTime:

     currAllFutureContract=currAllFutureContract[(currAllFutureContract['listed_date']<=sDateTime) & \
     (currAllFutureContract['delisted_date']>=eDateTime)]
    
    tempContract=currAllFutureContract
    

    finalDf=pd.DataFrame(columns=currAllFutureContract.columns)
    
    for inx, row in tempContract.iterrows():
        underLyingSymbol=commonHelpBylw.getMainContinContract(row['symbol'])
    

        #确认当前品种是我们需要的品种
        if underLyingSymbol in symbolsCode:
            if  underLyingSymbol in month159:
                if row['sec_id'][-2:] in ['01','05','09']:

                    finalDf.loc[finalDf.shape[0]]=row
            if  underLyingSymbol in month1to12:
                if row['sec_id'][-2:] in ['01','03','05','07','09','11']:

                    finalDf.loc[finalDf.shape[0]] = row
            if  underLyingSymbol in month1510:
                if row['sec_id'][-2:] in ['01','05','10']:

                    finalDf.loc[finalDf.shape[0]] = row
            if  underLyingSymbol in month612:
                if row['sec_id'][-2:] in ['06','12']:

                    finalDf.loc[finalDf.shape[0]] = row
            if underLyingSymbol in allCon:

                finalDf.loc[finalDf.shape[0]] = row
                
    i=1
    return finalDf
               











'''

价差价比计算

apair 可以是元组，可以是list
'''

def ratioSpreadCal(aPair,astartTime,aendTime):
    aData= history(symbol=aPair[0], frequency='1d', start_time=astartTime,end_time=aendTime, fields='close,symbol,eob', df=True)
    
    if aData.empty:
        print(aPair[0]+' is empty')
        return pd.DataFrame()
    
    aData.rename(columns={"close": aPair[0]},inplace=True)
    
    
    
    bData= history(symbol=aPair[1], frequency='1d', start_time=astartTime,end_time=aendTime, fields='close,symbol,eob', df=True)
    if bData.empty:
        print(aPair[1]+' is empty')
        return pd.DataFrame()
        
    bData.rename(columns={"close": aPair[1]},inplace=True)
    
    
    concatData=pd.merge(aData,bData,on='eob') 
        
    
    if aPair[0]=='CZCE.SM' and aPair[1]=='DCE.J':
        iiid=1
    
    concatData[aPair[0]+'-'+aPair[1]]=concatData[aPair[0]]-concatData[aPair[1]]
    concatData[aPair[0]+'/'+aPair[1]]=concatData[aPair[0]]/concatData[aPair[1]]
    
    return concatData
        
        

def getHQDataFromGm(symbol,sDateTime,eDateTime,fields=None):


    

    aaa=history(symbol=symbol,frequency='60s',start_time=sDateTime,end_time=eDateTime,fields=fields,df=True)
    return aaa




#
# # 本函数，根据gm下单结果（开仓和平仓下单），来增加或者减少list中的orderPosition对象
# #
# def updateOrderPositionMFElist(orderRe,strategyObj):
#     if orderRe is  None:
#         return
#     position_effect = orderRe[0]['position_effect']
#     position_side = orderRe[0]['position_side']
#     volNum_ = orderRe[0]['filled_volume']
#     symbol_ = orderRe[0]['symbol']
#
#     if position_side == PositionSide_Long:
#         positionSideStr = 'long'
#     if position_side == PositionSide_Short:
#         positionSideStr = 'short'
#
#
#     # 开仓
#     if position_effect == PositionEffect_Open:
#
#         cost_ = orderRe[0]['filled_vwap']
#         commission_ = 0
#
#         aOrderPosition = BaseOrderHoldingPostion(symbol_, positionSideStr, volNum_, cost_,
#                                                  commission=commission_)
#         aOrderPosition.barsSinceEntry = -1  # 这里是因为 真正成交是下个bar成交的
#         adict = {}
#         adict['strategyOrderID'] = None
#         adict['orderPosition'] = aOrderPosition
#         adict['HH'] = None
#         adict['LL'] = None
#         adict['MFE'] = None
#
#         if symbol_ == strategyObj.symbol:
#             # self.orderPostionMfeList.append(adict)
#             strategyObj.orderPostionMfeList.append(adict)
#         else:
#             # 访问其他合约的 策略对象
#             strategyObj.allSymStrategy[symbol_].orderPostionMfeList.append(adict)
#
#     # 平仓
#     if position_effect == PositionEffect_Close:
#
#         if symbol_ == strategyObj.symbol:
#             for aOrderPosi in reversed(strategyObj.orderPostionMfeList):
#                 if aOrderPosi['orderPosition'].positionSide == positionSideStr:
#
#                     if aOrderPosi['orderPosition'].volume >= volNum_:
#                         aOrderPosi['orderPosition'].volume = aOrderPosi['orderPosition'].volume - volNum_
#                         break
#                     else:
#                         aOrderPosi['orderPosition'].volume = 0
#                         volNum_ = volNum_ - aOrderPosi['orderPosition'].volume
#
#         else:
#             for aOrderPosi in reversed(rangBreakSys.allSymStrategy[symbol_].orderPostionMfeList):
#                 if aOrderPosi['orderPosition'].positionSide == positionSideStr:
#
#                     if aOrderPosi['orderPosition'].volume >= volNum_:
#                         aOrderPosi['orderPosition'].volume = aOrderPosi['orderPosition'].volume - volNum_
#                         break
#                     else:
#                         aOrderPosi['orderPosition'].volume = 0
#                         volNum_ = volNum_ - aOrderPosi['orderPosition'].volume
#


def getTradeMsg(OrderRes):


    # if OrderRes[0].ord_rej_reason == gmEnum.OrderRejectReason_Unknown:
    #     tradeMsg = 'normal'
    if OrderRes[0].ord_rej_reason == gmEnum.OrderRejectReason_NoEnoughCash :
        tradeMsg = 'NoEnoughCash'
        return  tradeMsg

class gmOrder():
    
    orderLog=None
    clearOrderEvent = observer.Event()

    def __init__(self):

        self.i=1

    # @classmethod
    # def reverseClear(cls,clearFun,symbol_,signalName,dt,**kwargs):
    #     context = kwargs.get('context', None)
    #     # 空头持仓要平掉
    #     symbolHolding = context.account().position(symbol=symbol_, side=PositionSide_Short)
    #     if symbolHolding:
    #         vol1_ = symbolHolding['volume']
    #         context.clearPositionSignalNames = ['all']
    #         clearShortOrderRes = clearFun(symbol_, vol1_, signalName, dt)
    # @classmethod
    # def _getALog(cls,bTestID,underLySym):
    #     # loggerHelpbylw.getFileLogger(self.context.bTestID + '-' + self.underLySym + '-orderlog',
    #     #                                     'log\\'+self.context.bTestID+'\\' + self.underLySym + '-orderRecord.txt',mode_='a')
    #
    #     aLog=loggerHelpbylw.getFileLogger(bTestID + '-' + underLySym + '-orderlog',
    #                                  'log\\' + bTestID + '\\' + underLySym + '-orderRecord.txt',
    #                                  mode_='a')
    #     return aLog

    @classmethod
    def openLong(cls,symbol_,vol_,signalName,dt,clearReverse=False,**kwargs):
        context = kwargs.get('context', None)

        if clearReverse:
            # 空头持仓要平掉
            symbolHolding = context.account().position(symbol=symbol_, side=PositionSide_Short)
            if symbolHolding:
                vol1_ = symbolHolding['volume']
                context.clearPositionSignalNames = ['allShort']
                clearShortOrderRes = cls.clearShort(symbol_, vol1_, 'cshort',dt,**kwargs)

            # cls.reverseClear(cls.clearShort,symbol_,'cshort',dt,**kwargs)


        openLongOrderRes = order_volume(symbol=symbol_, volume=vol_, side=OrderSide_Buy,
                                        order_type=OrderType_Market, position_effect=PositionEffect_Open, price=0)
        # print(openLongOrderRes)
        tradeMsg = getTradeMsg(openLongOrderRes)


        # if writeOrderLog:
        orderLog = kwargs.get('orderLog', None)
        if orderLog is not None:

            if tradeMsg is not None:
                sigMsg = signalName + '-' + tradeMsg
            else:
                sigMsg = signalName
            # cls.orderLog.info("%s,%s,%d,%d,%d,%s",dt, symbol_,vol_,OrderSide_Buy,PositionEffect_Open,signalName)
            # cls.orderLog.info("%s,%s,%s", dt, symbol_,sigMsg+'-'+symbol_)
            orderLog.info("%s,%s,%s", dt, symbol_, sigMsg + '-' + symbol_)
        return openLongOrderRes

    @classmethod
    def openShort(cls, symbol_, vol_,signalName,dt,clearReverse=False,**kwargs):

        if clearReverse:
            # 多头持仓要平掉
            context = kwargs.get('context', None)
            symbolHolding = context.account().position(symbol=symbol_, side=PositionSide_Long)
            if symbolHolding:
                vol1_ = symbolHolding['volume']
                context.clearPositionSignalNames = ['allLong']
                clearLongOrderRes = cls.clearLong(symbol_, vol1_, 'clong',dt,**kwargs)
            # cls.reverseClear(cls.clearLong, symbol_, 'clong', dt,**kwargs)


        openShortOrderRes = order_volume(symbol=symbol_, volume=vol_, side=OrderSide_Sell,
                                        order_type=OrderType_Market, position_effect=PositionEffect_Open, price=0)



        tradeMsg = getTradeMsg(openShortOrderRes)
        orderLog = kwargs.get('orderLog', None)
        # if writeOrderLog:
        if orderLog is not None:


            if tradeMsg is not None:
                sigMsg = signalName + '-' + tradeMsg
            else:
                sigMsg = signalName

            # cls.orderLog.info("%s,%s,%d,%d,%d,%s",dt, symbol_,vol_,OrderSide_Sell,PositionEffect_Open,signalName)
            # cls.orderLog.info("%s,%s,%s", dt, symbol_, sigMsg+'-'+symbol_)
            orderLog.info("%s,%s,%s", dt, symbol_, sigMsg + '-' + symbol_)
        return openShortOrderRes

    @classmethod
    def clearLong(cls, symbol_, vol_,signalName,dt,clearSignals=['allLong'],**kwargs):
        clearLongOrderRes = order_volume(symbol=symbol_, volume=vol_, side=OrderSide_Sell,
                                        order_type=OrderType_Market, position_effect=PositionEffect_Close, price=0)
        orderLog = kwargs.get('orderLog', None)
        if orderLog is not None:
        # if writeOrderLog:

            # underLySym = commonHelpBylw.getMainContinContract(symbol_)
            # orderLog = cls._getALog(context.bTestID, underLySym)

            # cls.orderLog.info("%s,%s,%d,%d,%d,%s",dt, symbol_,vol_,OrderSide_Sell,PositionEffect_Close,signalName)
            # cls.orderLog.info("%s,%s,%s", dt, symbol_, signalName+'-'+symbol_)
            orderLog.info("%s,%s,%s", dt, symbol_, signalName + '-' + symbol_)
        cls.clearOrderEvent.emit(clearLongOrderRes[0],clearSignals)
        return clearLongOrderRes

    @classmethod
    def clearShort(cls, symbol_, vol_,signalName,dt,clearSignals=['allShort'],**kwargs):


        clearShortOrderRes = order_volume(symbol=symbol_, volume=vol_, side=OrderSide_Buy,
                                        order_type=OrderType_Market, position_effect=PositionEffect_Close, price=0)
        orderLog=kwargs.get('orderLog', None)
        if orderLog is not None:
        # if writeOrderLog:

            # cls.orderLog.info("%s,%s,%d,%d,%d,%s",dt, symbol_,vol_,OrderSide_Buy,PositionEffect_Close,signalName)
            # cls.orderLog.info("%s,%s,%s", dt, symbol_, signalName+'-'+symbol_)
            orderLog.info("%s,%s,%s", dt, symbol_, signalName + '-' + symbol_)
        cls.clearOrderEvent.emit(clearShortOrderRes[0], clearSignals)
        return clearShortOrderRes


    @classmethod
    def clearLongAllPo(cls, symbol_,  signalName,dt,**kwargs):

        context = kwargs.get('context', None)
        symbolHolding = context.account().position(symbol=symbol_, side=PositionSide_Long)
        if symbolHolding:
            vol_ = symbolHolding['volume']
            clearLongOrderRes = cls.clearLong(symbol_,vol_,signalName,dt,**kwargs)
            return clearLongOrderRes

    @classmethod
    def clearShortAllPo(cls, symbol_, signalName,dt,**kwargs):

        context = kwargs.get('context', None)
        symbolHolding = context.account().position(symbol=symbol_, side=PositionSide_Short)
        if symbolHolding:
            vol_ = symbolHolding['volume']
            clearShortOrderRes = cls.clearShort(symbol_, vol_, signalName,dt,**kwargs)
            return clearShortOrderRes





    @classmethod
    # 这函数 股票是可以这么弄，但是期货就不对了。期货要有合约乘数，保证金比例等信息
    # def openLongWithCash(cls, symbol_, cash_, upPriceV, cusComRatio, signalName, clearReverse=False):
    def openLongWithCash(cls, symbol_, cash_,signalName,dt,clearReverse=False,**kwargs):
        
        #clearReverse 表示是否平掉反向的持仓。即开多，那么已有的空头持仓要平仓。
        
        # realVol = int(cash_ / (100 * upPriceV * (1 + cusComRatio))) * 100

        # openLongOrderRes = order_volume(symbol=symbol_, volume=realVol, side=OrderSide_Buy,
        #                                 order_type=OrderType_Market, position_effect=PositionEffect_Open, price=0)

        context = kwargs.get('context', None)
        if clearReverse:

            # 空头持仓要平掉
            symbolHolding = context.account().position(symbol=symbol_, side=PositionSide_Short)
            if symbolHolding:
                vol1_ = symbolHolding['volume']
                context.clearPositionSignalNames = ['allShort']
                clearShortOrderRes = cls.clearShort(symbol_, vol1_, 'cshort',dt,**kwargs)
            # cls.reverseClear(cls.clearShort, symbol_, 'cshort', dt,**kwargs)


        openLongOrderRes=order_value(symbol=symbol_, value=cash_, price=0, side=OrderSide_Buy, order_type=OrderType_Market,
                    position_effect=PositionEffect_Open)


        tradeMsg=getTradeMsg(openLongOrderRes)

        # if writeOrderLog:
        orderLog = kwargs.get('orderLog', None)
        if orderLog is not None:
            # cls.orderLog.info("%s,%s,%f,%d,%d,%s",dt, symbol_,cash_,OrderSide_Buy,PositionEffect_Open,signalName)

            if tradeMsg is not None:
                sigMsg=signalName+'-'+tradeMsg
            else:
                sigMsg = signalName

            # cls.orderLog.info("%s,%s,%s", dt, symbol_, sigMsg+'-'+symbol_)
            orderLog.info("%s,%s,%s", dt, symbol_, sigMsg + '-' + symbol_)
        return openLongOrderRes

    @classmethod
    # vol_是手数
    def openShortWithCash(cls, symbol_, cash_,signalName,dt,clearReverse=False,**kwargs):
        context = kwargs.get('context', None)
        if clearReverse:
            # 多头持仓要平掉

            symbolHolding = context.account().position(symbol=symbol_, side=PositionSide_Long)
            if symbolHolding:
                vol1_ = symbolHolding['volume']
                context.clearPositionSignalNames = ['allLong']
                clearLongOrderRes = cls.clearLong(symbol_, vol1_, 'clong',dt,**kwargs)
            # cls.reverseClear(cls.clearLong, symbol_, 'clong', dt,**kwargs)



        openShortOrderRes = order_value(symbol=symbol_, value=cash_, price=0, side=OrderSide_Sell,order_type=OrderType_Market,
                                       position_effect=PositionEffect_Open)

        tradeMsg=getTradeMsg(openShortOrderRes)
        orderLog = kwargs.get('orderLog', None)
        if orderLog is not None:
        # if writeOrderLog:


            if tradeMsg is not None:
                sigMsg=signalName+'-'+tradeMsg
            else:
                sigMsg = signalName

            # cls.orderLog.info("%s,%s,%f,%d,%d,%s",dt, symbol_,cash_,OrderSide_Sell,PositionEffect_Open,signalName
            # cls.orderLog.info("%s,%s,%s", dt, symbol_, sigMsg+'-'+symbol_)
            orderLog.info("%s,%s,%s", dt, symbol_, sigMsg + '-' + symbol_)

        return openShortOrderRes











    def writeOrderToFile(self,side_,position_effect_,filename='order.txt'):

        """ 装饰器 """

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                """ A wrapper function """

                symbol_=args[0]
                vol_=args[1]
                signalName_=args[2]

                if side_==OrderSide_Buy:
                    strSide='buy'
                if side_==OrderSide_Sell:
                    strSide='sell'
                if position_effect_==PositionEffect_Open:
                    strPosEffect='open'
                if position_effect_==PositionEffect_Close:
                    strPosEffect='close'


                msg = "%s,%s,%s,%s,%s"%(symbol_,str(vol_),strSide,strPosEffect,signalName_)
                current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                pathAndName =current_date+'-'+filename
                f = open(pathAndName, 'a')  # 若是'wb'就表示写二进制文件
                f.write(msg)
                f.close()



                res = func(*args, **kwargs)
                return res
            return wrapper
        return decorator





def getMainContractData_Fade(continuousContract,sDatetime,eDatetime):
    #sDatetime 可以是日期带时间，也可以仅仅是日期

    dateList=commonHelpBylw.splitDates(sDatetime,eDatetime)
    dfMainContract = pd.DataFrame(columns=['mainContract', 'symbol', 'datetime'])
    index_ = 0
    for aContinu in continuousContract:
        for sDtime_,eDtime_ in dateList:
            tempMainContract=get_continuous_contracts(csymbol=aContinu, \
                                                  start_date=sDtime_, end_date=eDtime_)

            for atem in tempMainContract:
                dfMainContract.loc[index_, 'mainContract'] = aContinu
                dfMainContract.loc[index_, 'symbol'] = atem['symbol']
                dfMainContract.loc[index_, 'datetime'] = atem['trade_date']
                index_ = index_ + 1
            i=1
    


    dfMainContract['datetime']=dfMainContract['datetime'].dt.strftime('%Y-%m-%d')
    mainContractData = dfMainContract.pivot(index='datetime', columns='mainContract', values='symbol')

    return mainContractData

def getMainSymbolLastFinishTradingDate(underlySyms,lastDate):
    #lastDate 表示当前时刻，已经走完了的交易日。具体来源于calendar模块中 get_latest_finished_tradingdate函数

    mainContractData = getMainContractData_Fade(underlySyms, lastDate, lastDate)
    if not mainContractData.empty:
        currNeedMainSymbol = mainContractData.to_numpy()[0].tolist()
        return currNeedMainSymbol


def getHQData_Fade(symbolist,sDateTime,eDateTim,fre='60s',fields_='symbol,eob,open,high,low,close'):
    # dateList = commonHelpBylw.splitDates(sDateTime, eDateTim)
    # dfData = pd.DataFrame()
    #
    # for symbol_ in symbolist:
    #     for sDtime_, eDtime_ in dateList:
    #         tempHQdata = history(symbol=symbol_,frequency=fre,start_time=sDtime_,end_time=eDtime_,fields=fields_,df=True)
    #
    #         dfData=dfData.append(tempHQdata)
    #
    # return dfData



    #上面由于splitDates无法对于分钟线日期准确的拆分。所以上面这种方式取数据不太对
    #下面用新逻辑。
    # 先取全部数据，然后查看刚出来数据的最后一个日期，取他的下一个秒时间。一直循环到最后取不出来数据为止。
    # sDtime_=sDateTime
    # eDtime_=eDateTim

    if fre=='tick':
        dateName='created_at'
    else:
        dateName='eob'


    dfData = pd.DataFrame()
    for symbol_ in symbolist:
        sDtime_ = sDateTime
        eDtime_ = eDateTim
        tempHQdata = history(symbol=symbol_, frequency=fre, start_time=sDtime_, end_time=eDtime_, fields=fields_, df=True)

        while not tempHQdata.empty:
            tempHQdata = tempHQdata.sort_values(dateName)
            dfData = dfData.append(tempHQdata)
            latestDateTime=tempHQdata[dateName].iloc[-1]

            nextDT=latestDateTime+Second()
            sDtime_=nextDT.strftime('%Y-%m-%d %H:%M:%S')
            if sDtime_<=eDtime_:
                tempHQdata = history(symbol=symbol_, frequency=fre, start_time=sDtime_, end_time=eDtime_,
                                     fields=fields_, df=True)
            else:
                #即下一个初始时间大于了最终结束时间，说明数据已经取完了。
                break
    return dfData







#获取主力连续的数据。不是简单的标的资产，而是每个具体时间，都是具体的合约代码

def getHQDataOfMainContract_Fade(underlyingSymbolList,sDateTime,eDateTim,fre='60s',fields_='symbol,eob,open,high,low,close'):

    #1 先获取主力连续行情表，只带上了标的资产的id，
    #2、将具体时间 计算出其所属的交易日
    #3、取出标的资产的主力连续表
    #4、主力连续表和主力连续行情表，以交易日 做连接

    hqDF=getHQData_Fade(underlyingSymbolList,sDateTime,eDateTim,fre=fre,fields_=fields_)

    aNewTradeCalendar = calendayBylw.getACalendarInstance()
    hqDF['eob']=hqDF['eob'].dt.strftime("%Y-%m-%d %H:%M:%S")
    hqDF['tradeDate']=hqDF['eob'].apply(aNewTradeCalendar.tradeDateTimeTradingDateOffset,aoffset=0)

    mainContractDf=getMainContractData_Fade(underlyingSymbolList,sDateTime,eDateTim)
    mainContractDfAdjust=mainContractDf.stack().reset_index(name='symbol')

    mergeDf=pd.merge(hqDF,mainContractDfAdjust,left_on=['tradeDate','symbol'],right_on=['datetime','mainContract'])

    resulDf=mergeDf.copy()

    resulDf.rename(index=str,columns={"symbol_y": "symbol"},inplace=True)

    strList=fields_.split(',')
    resulDf=resulDf[strList]

    resulDf['eob'] = pd.to_datetime(resulDf['eob'], format="%Y-%m-%d %H:%M:%S")
    resulDf['eob'] = resulDf['eob'].dt.tz_localize(tz=timezone(timedelta(hours=8)))

    

    return resulDf


def getInstumInfo(symbols,fields='symbol,exchange,sec_id,listed_date,delisted_date'):
    #symbols 是list

    instuInfo=get_instruments(symbols=symbols, fields=fields, df=True)
    return instuInfo





# # 切换到 commonhelp
# def getSymboInfoDataFromGm(aGmAPIfun,symbolList,sDateTime,eDateTime,fields=None,step_=3000):
# # def getSymboInfoDataFromGm(symbolList,sDateTime,eDateTime,fields=None,step_=3000):
#
#     #aGmAPIfun 是掘金的提取数据的函数，可以是history，也可以是get_history_instruments，等等。反正是一次提取历史数据
#     #不能太长的话，都可以用这里的这个函数包一层。
#
#
#     #准备一个 日历对象。
#     currDateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     currDate = currDateTime[0:10]
#     nextYearofToday = datetime.datetime.strptime(currDate, '%Y-%m-%d') \
#                       + DateOffset(years=1)
#     nextYearofTodayStr = nextYearofToday.strftime('%Y-%m-%d')
#     aTradingDays = get_trading_dates(exchange='SHSE', start_date='2000-01-01', end_date=nextYearofTodayStr)
#     aNewTradeCalendar = calendayBylw.customTradeCalendar(aTradingDays)
#
#
#
#     #起始日期 和 结束日期 分别往前 和 往后扩展一下。
#     sDate=sDateTime[0:10]
#     eDate=eDateTime[0:10]
#
#     ssDate=aNewTradeCalendar.mDatesOffset(sDate,doffset=-1,leftOrright=-1)
#     eeDate = aNewTradeCalendar.mDatesOffset(eDate, doffset=1, leftOrright=1)
#
#
#     atradeDateSerial=aNewTradeCalendar.getADateTimeSeries(ssDate,eeDate)
#
#
#
#     dfInfo=pd.DataFrame()
#     for aSymbol in symbolList:
#         sIndex=0
#         eIndex=sIndex+step_-1
#         while True:
#             cSdate=atradeDateSerial.iloc[sIndex]
#             if eIndex>=atradeDateSerial.shape[0]:
#                 cEdate=atradeDateSerial.iloc[-1]
#             else:
#                 cEdate=atradeDateSerial.iloc[eIndex]
#
#             # tempInfoDf=get_history_instruments(aSymbol, fields=fields, start_date=cSdate, \
#             #                         end_date=cEdate, df=True)
#             tempInfoDf = aGmAPIfun(aSymbol, fields=fields, start_date=cSdate, \
#                                                  end_date=cEdate, df=True)
#
#             dfInfo=dfInfo.append(tempInfoDf)
#
#             if eIndex>=atradeDateSerial.shape[0]:
#                 break
#             else:
#                 sIndex = sIndex+step_
#                 eIndex = eIndex + step_
#     return dfInfo
#






