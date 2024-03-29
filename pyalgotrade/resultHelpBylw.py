# -*- coding: utf-8 -*-
"""
20190819   14：30

@author: lw 李文
"""


# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
import numpy as np
import pandas as pd
from datetime import timezone
from datetime import timedelta
from collections import deque
import sys

from pyalgotrade import gm3HelpBylw
from pyalgotrade import commonHelpBylw
import copy
import time

try:
    import talib
except:
    print('请安装TA-Lib库')
from gm.api import *
from highcharts import plotHelpbylw
from pyalgotrade.utils import parseToGmFre,freMapFromGM

#本模块 用来 回测之后，一些动作。

#
# def writeBackTestResult(strategyParams, strategyBackTestIndicator, btestID, resultFile, enconding='gbk'):
#     arow = []
#
#     backTestID = btestID
#
#     arow.append(strategyParams['underlySym'])
#     arow.append(strategyParams['freStr'])
#     arow.append(strategyParams['backTestTime'])
#     arow.append(strategyParams['strategyParams'])
#     arow.append(strategyParams['orderPattern'])
#
#     # 下面是回测指标
#     arow.append(strategyBackTestIndicator.pnl_ratio)
#     arow.append(strategyBackTestIndicator.pnl_ratio_annual)
#     arow.append(strategyBackTestIndicator.max_drawdown)
#     arow.append(strategyBackTestIndicator.calmar_ratio)
#     arow.append(strategyBackTestIndicator.sharp_ratio)
#     arow.append(strategyBackTestIndicator.open_count)
#     arow.append(strategyBackTestIndicator.close_count)
#     arow.append(strategyBackTestIndicator.win_ratio)
#
#     # 回测id
#     arow.append(backTestID)
#     with open(resultFile, 'a', newline='', encoding=enconding) as csvFile:
#         # with open(resultFile, 'a',newline='',encoding='utf-8-sig') as csvFile:
#         import csv
#         writer = csv.writer(csvFile)
#
#         writer.writerow(arow)



def writeBackTestResult(strategyParams,strategyBackTestIndicator,btestID,resultFile,enconding='gbk'):
    arow = []


    backTestID=btestID




    arow.append(strategyParams)







    # 下面是回测指标
    arow.append(strategyBackTestIndicator.pnl_ratio)
    arow.append(strategyBackTestIndicator.pnl_ratio_annual)
    arow.append(strategyBackTestIndicator.max_drawdown)
    arow.append(strategyBackTestIndicator.calmar_ratio)
    arow.append(strategyBackTestIndicator.sharp_ratio)
    arow.append(strategyBackTestIndicator.open_count)
    arow.append(strategyBackTestIndicator.close_count)
    arow.append(strategyBackTestIndicator.win_ratio)

    # 回测id
    arow.append(backTestID)
    with open(resultFile, 'a', newline='', encoding=enconding) as csvFile:
    # with open(resultFile, 'a',newline='',encoding='utf-8-sig') as csvFile:
        import csv
        writer = csv.writer(csvFile)

        writer.writerow(arow)


def plotBackTestResult(underLysymbol,bTestParams,logDataPathDir,figPathDir,plotSDateTime,plotEDateTime,\
                       firstYVarsname=[],secondYVarsname=[]):

    #underLysymbol 是list


    # filePrefix = 'batch\\'
    # plotSDateTime = '2019-01-01'
    # plotEDateTime = '2019-06-30'
    # plotSDateTime = '2016-10-25 00:00:00'
    # plotEDateTime = '2016-11-25 23:59:59'

    for aUnderLyAsset in underLysymbol:

        # 取委托记录2
        try:
            with open(logDataPathDir + aUnderLyAsset + '-orderRecord.txt', encoding='gbk')as f:
                # with open(r'log\tradeRecord.txt',encoding='gbk')as f:

                dfOrderSingal = pd.read_csv(f, header=None, sep=",")

                dfOrderSingal.columns = ["createdAt", "symbol", 'signalname']
                dfOrderSingal = dfOrderSingal.loc[
                    (dfOrderSingal['createdAt'] >= plotSDateTime) & (dfOrderSingal['createdAt'] <= plotEDateTime)]
                dfOrderSingal['date'] = pd.to_datetime(dfOrderSingal['createdAt'], format='%Y-%m-%d %H:%M:%S')
                dfOrderSingal['date'] = dfOrderSingal['date'].dt.tz_localize(tz=timezone(timedelta(hours=8)))

            if dfOrderSingal.empty:
                pass
            else:
                symbol_ = dfOrderSingal['symbol'].iloc[-1]
        except Exception as e:
            print(e)
        # mainSymbol = commonHelpBylw.getMainContinContract(symbol_)
        mainSymbol=aUnderLyAsset


        # fields = 'eob,open,high,low,close'

        sfrestr=bTestParams[aUnderLyAsset]['fre']
        gmFreStr = parseToGmFre(sfrestr)
        H = plotHelpbylw.plotMainContractCandle(mainSymbol, plotSDateTime, plotEDateTime,fre=gmFreStr)

        plotHelpbylw.plotSingal(H, dfOrderSingal, mainSymbol)







# def plotVar(H,aUnderLyAsset,varsName,logDataPathDir,plotSDateTime,plotEDateTime):


        # 如果外界参数显示，需要画图的中间变量至少有1个
        # 设置y
        if len(secondYVarsname)>=1:
            yAxis = [{'height': '70%', 'resize': {'enabled': True}},
                     {'top': '70%', 'height': '30%'}]

            H.set_options('yAxis', yAxis)

            # 取中间变量

            # varsName = ['diff', 'dea', 'macd']
            # for aname in varsName:
            #             #
            #             #     with open(logDataPathDir+'%s-%s.txt' % (aUnderLyAsset, aname), encoding='gbk')as f:
            #             #         # with open('log\\%s.txt'%(aname),encoding='gbk')as f:
            #             #
            #             #         aVar = pd.read_csv(f, header=None, sep=",")
            #             #         aVar.columns = ["createdAt", aname]
            #             #         aVar = aVar.loc[(aVar['createdAt'] >= plotSDateTime) & (aVar['createdAt'] <= plotEDateTime)]
            #             #         aVar['date'] = pd.to_datetime(aVar['createdAt'], format='%Y-%m-%d %H:%M:%S')
            #             #         aVar['date'] = aVar['date'].dt.tz_localize(tz=timezone(timedelta(hours=8)))
            #             #     if aname == 'macd':
            #             #         plotHelpbylw.addASeries(H, aVar[['date', aname]], aname, yaxisIndex=1, seriesType='column')
            #             #     else:
            #             #         plotHelpbylw.addASeries(H, aVar[['date', aname]], aname, yaxisIndex=1)

        def addASeries(varsname, yaxisindex):
            for aname in varsname:

                with open(logDataPathDir + '%s-%s.txt' % (aUnderLyAsset, aname), encoding='gbk')as f:
                    # with open('log\\%s.txt'%(aname),encoding='gbk')as f:

                    aVar = pd.read_csv(f, header=None, sep=",")
                    aVar.columns = ["createdAt", aname]
                    aVar = aVar.loc[(aVar['createdAt'] >= plotSDateTime) & (aVar['createdAt'] <= plotEDateTime)]
                    aVar['date'] = pd.to_datetime(aVar['createdAt'], format='%Y-%m-%d %H:%M:%S')
                    aVar['date'] = aVar['date'].dt.tz_localize(tz=timezone(timedelta(hours=8)))
                if aname == 'macd':
                    plotHelpbylw.addASeries(H, aVar[['date', aname]], aname, yaxisIndex=yaxisindex,
                                            seriesType='column')
                else:
                    plotHelpbylw.addASeries(H, aVar[['date', aname]], aname, yaxisIndex=yaxisindex)


        addASeries(firstYVarsname,0)
        addASeries(secondYVarsname,1)

        filename = figPathDir + mainSymbol
        H.save_file(filename)
    # return  H
    i = 1



#
def plotResultMulContract(logDataPathDir,plotSDateTime,plotEDateTime,bTestParams,
                            firstYVarsname=[],secondYVarsname=[]):



        import os
        import re
        def getOrder(filePath):
            fileNameList = os.listdir(filePath)
            absPath = os.path.abspath(filePath)

            dfOrderSingal = pd.DataFrame(columns=["createdAt", "symbol", 'signalname'])
            for afName in fileNameList:
                fDirAndName = os.path.join(absPath, afName)

                try:
                    with open(fDirAndName, encoding='gbk')as f:
                        # with open(r'log\tradeRecord.txt',encoding='gbk')as f:
                        tmpd = pd.read_csv(f, header=None, sep=",")
                        tmpd.columns = ["createdAt", "symbol", 'signalname']
                        dfOrderSingal = dfOrderSingal.append(tmpd, ignore_index=True)


                except Exception as e:
                    print(e)
            return dfOrderSingal

        dfOrderSingal=getOrder(logDataPathDir+'orderRecord')

        lastPath=os.path.abspath(os.path.join(logDataPathDir, "../.."))
        stopFilePath=lastPath+'\\stopLossProfitLog\\livemode\\'
        stopOrder=getOrder(stopFilePath+''+'orderRecord')

        dfOrderSingal=dfOrderSingal.append(stopOrder)
        # #取委托记录
        # fileNameList=os.listdir(logDataPathDir+'orderRecord')
        # absPath=os.path.abspath(logDataPathDir+'orderRecord')
        #
        # dfOrderSingal=pd.DataFrame(columns = ["createdAt", "symbol", 'signalname'])
        # for afName in fileNameList:
        #     fDirAndName = os.path.join(absPath, afName)
        #
        #
        #
        #     try:
        #         with open(fDirAndName, encoding='gbk')as f:
        #             # with open(r'log\tradeRecord.txt',encoding='gbk')as f:
        #             tmpd=pd.read_csv(f, header=None, sep=",")
        #             tmpd.columns = ["createdAt", "symbol", 'signalname']
        #             dfOrderSingal = dfOrderSingal.append(tmpd,ignore_index=True)
        #
        #
        #     except Exception as e:
        #         print(e)

        dfOrderSingal = dfOrderSingal.loc[
            (dfOrderSingal['createdAt'] >= plotSDateTime) & (dfOrderSingal['createdAt'] <= plotEDateTime)]
        dfOrderSingal['date'] = pd.to_datetime(dfOrderSingal['createdAt'], format='%Y-%m-%d %H:%M:%S')
        dfOrderSingal['date'] = dfOrderSingal['date'].dt.tz_localize(tz=timezone(timedelta(hours=8)))






        def addASeries(varsname, yaxisindex):
            interResultAbsPath = os.path.abspath(logDataPathDir + 'interResult')
            for aname in varsname:

                filenameAndPath= os.path.join(interResultAbsPath, asymbol+'-'+aname+'.txt')
                with open(filenameAndPath, encoding='gbk')as f:
                    # with open('log\\%s.txt'%(aname),encoding='gbk')as f:

                    aVar = pd.read_csv(f, header=None, sep=",")
                    aVar.columns = ["createdAt", aname]
                    aVar = aVar.loc[(aVar['createdAt'] >= plotSDateTime) & (aVar['createdAt'] <= plotEDateTime)]
                    aVar['date'] = pd.to_datetime(aVar['createdAt'], format='%Y-%m-%d %H:%M:%S')
                    aVar['date'] = aVar['date'].dt.tz_localize(tz=timezone(timedelta(hours=8)))
                if aname == 'macd':
                    plotHelpbylw.addASeries(H, aVar[['date', aname]], aname, yaxisIndex=yaxisindex,
                                            seriesType='column')
                else:
                    plotHelpbylw.addASeries(H, aVar[['date', aname]], aname, yaxisIndex=yaxisindex)





        symlist=list(dfOrderSingal['symbol'].drop_duplicates().values)
        for asymbol in symlist:


            #先画合约的k线，然后委托标记 打上去。
            aUnderLyAsset = commonHelpBylw.getMainContinContract(asymbol)
            # print(asymbol)
            # if aUnderLyAsset!='CZCE.MA':
            #     continue

            if asymbol=='DCE.j2001':
                i=1


            sfrestr = bTestParams[aUnderLyAsset]['fre']
            gmFreStr = parseToGmFre(sfrestr)
            H = plotHelpbylw.plotAContractCandle(asymbol, plotSDateTime, plotEDateTime, fre=gmFreStr)

            currDf = dfOrderSingal.loc[dfOrderSingal['symbol'] == asymbol]
            plotHelpbylw.plotSingal(H, currDf, asymbol)





           #画该品种的中间结果

            # interResultFileNameList = os.listdir(logDataPathDir + 'interResult')
            # interResultAbsPath = os.path.abspath(logDataPathDir + 'interResult')
            #
            # for afile in interResultFileNameList:
            #
            #     splits=re.split('-|.',afile)
            #
            #     sym=splits[0]
            #     varName=splits[1]
            #
            #
            #     interResultFilePath = os.path.join(interResultFileNameList, interResultAbsPath)

            addASeries(firstYVarsname, 0)

            # 如果外界参数显示，需要画图的中间变量至少有1个
            # 设置y
            if len(secondYVarsname) >= 1:
                yAxis = [{'height': '70%', 'resize': {'enabled': True}},
                         {'top': '70%', 'height': '30%'}]

                H.set_options('yAxis', yAxis)
                addASeries(secondYVarsname, 1)

            filename = logDataPathDir + asymbol
            H.save_file(filename)

        












        # addASeries(firstYVarsname, 0)
        # addASeries(secondYVarsname, 1)


