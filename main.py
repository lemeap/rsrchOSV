# 분석 환경 모듈
import numpy as np
import pandas as pd
import psycopg2 as pg
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

# 데이터 분석 모듈
from CoolProp.CoolProp import PropsSI
from sklearn.preprocessing import MinMaxScaler, QuantileTransformer, PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from scipy.integrate import ode

# 내가 만든 모듈 임포트
from ModelOSV import *
from PhysicalProperty import *
from StructuredQuery import *
from Numeric import *

# Graph Font 설정
style.use('seaborn-talk')
krfont = {'family':'Times New Roman', 'weight':'bold', 'size':10}
matplotlib.rc('font', **krfont)
matplotlib.rcParams['axes.unicode_minus'] = False

# Main
if __name__ == "__main__":
    # 클래스 정의 및  인스턴스 생성
    pro= PhysicalProperty()
    mod= ModelOSV()
    sql = StructuredQuery()

    # SQL 연결 쿼리문
    (conn, db_engine) = sql.connect('localhost', 'Research', 'postgres', '5432', '1234')

    # 연결 확인
    print("PostgreSQL에 Research Database에 연결을 완료하였습니다.", conn)
    print(db_engine)

    # OSV 데이터베이스 연결
    load_osv_query = "SELECT * FROM rawdata_1"
    osv_tb = sql.read_sql(load_osv_query, db_engine)
    print("현재 호출된 table은 osv_tb입니다.")

    # Physical Properties 계산
    for i,row in osv_tb.iterrows():
        if osv_tb.loc[i, 'refri'] is 'Water':
            # 미리 계산해두었던 physical properties
            osv_tb.loc[i, 'tsat']  = round(PropsSI('T', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osv_tb.loc[i, 'kf']    = round(PropsSI('L', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osv_tb.loc[i, 'kv']    = round(PropsSI('L', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osv_tb.loc[i, 'muf']   = round(PropsSI('V', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 12)
            osv_tb.loc[i, 'muv']   = round(PropsSI('V', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 12)
            osv_tb.loc[i, 'rhof']  = round(PropsSI('D', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osv_tb.loc[i, 'rhov']  = round(PropsSI('D', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osv_tb.loc[i, 'cpf']   = round(PropsSI('C', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osv_tb.loc[i, 'cpv']   = round(PropsSI('C', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osv_tb.loc[i, 'sigma'] = round(PropsSI('I', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osv_tb.loc[i, 'hgo']   = round(PropsSI('H', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osv_tb.loc[i, 'hfo']   = round(PropsSI('H', 'P', osv_tb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osv_tb.loc[i, 'lam']   = round(osv_tb.loc[i, 'hgo'] - osv_tb[i, 'hfo'], 6)
            if osv_tb.loc[i, 'ti'] == np.nan:
                osv_tb.loc[i, 'dtin'] = np.nan
            else:
                osv_tb.loc[i, 'dtin'] = round(osv_tb.loc[i, 'tsat'] - osv_tb[i, 'ti'], 6)
            # Xosv 결정에 사용되므로 미리 계산
            osv_tb.loc[i, 'bo'] = round(pro.calBo(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'g']), 6)

        else:
            # Xosv 결정에 사용되므로 미리 계산
            osv_tb.loc[i, 'bo'] = round(pro.calBo(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'g']), 6)
            continue

    """# 조건에 따른 inlet subcooling, Gsat, Qratio 계산
    for i, row in osv_tb.iterrows():
        if osv_tb.loc[i, 'dtin'] == np.nan:
            osv_tb.loc[i, 'gsat'] = np.nan
        else:
            osv_tb['gsat'] = round(
                pro.calGsat(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'doi'], osv_tb.loc[i, 'lh'], osv_tb.loc[i, 'cpf'],
                            osv_tb.loc[i, 'dtin'], osv_tb.loc[i, 'dio'], osv_tb.loc[i, 'geo'], osv_tb.loc[i, 'hsur'],
                            osv_tb.loc[i, 'dh']), 6)
            osv_tb['qratio'] = round(
                pro.calQratio(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'doi'], osv_tb.loc[i, 'dio'], osv_tb.loc[i, 'geo'],
                              osv_tb.loc[i, 'hsur'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'dtin'],
                              osv_tb.loc[i, 'lh']), 6)
    """

    # xosv를 결정하기 위한 알고리즘
    for i,row in osv_tb.iterrows():
        osv_tb.loc[i, 'v'] = round(osv_tb.loc[i, 'g'] / osv_tb.loc[i, 'rhof'], 6)
        try:
            if osv_tb.loc[i, 'alpha'] is np.nan:  # void fraction 데이터가 아니라 OSV 실험 데이터에서 xosv 계산
                #print("{} 번째 {} source의 run_id {}는 OSV를 바로 계산합니다.".format(i, osv_tb.loc[i, 'source'], osv_tb.loc[i, 'run_id']))
                osv_tb.loc[i, 'xosv'] = round(-osv_tb.loc[i, 'cpf'] * osv_tb.loc[i, 'tosv'] / osv_tb.loc[i, 'lam'], 6)
                #print("{} source의 run_id {}의 OSV: {}".format(osv_tb.loc[i, 'source'], osv_tb.loc[i, 'run_id'],osv_tb.loc[i, 'xosv']))
            else:
                # void fraction profile 데이터에서 xosv 계산
                #print("{} is a np.nan".format(i))
                #print("{} 번째 {} source의 run_id {}는 OSV를 void fraction으로 계산합니다.".format(i, osv_tb.loc[i, 'source'], osv_tb.loc[i, 'run_id']))
                alpha = list((map(float, osv_tb.loc[i, 'alpha'].split('|'))))
                xeq = list((map(float, osv_tb.loc[i, 'xeq'].split('|'))))
                fitPoly = np.polyfit(xeq, alpha, 3)
                inflectionPoint = round(-fitPoly[1] / (3 * fitPoly[0]), 4)
                xMartin = fitPoly[3]
                osv_tb.loc[i, 'xMartin'] = xMartin
                osv_tb.loc[i, 'serizawaXeq'] = inflectionPoint
                osv_tb.loc[i, 'martinXeq'] = round(-fitPoly[3] / fitPoly[2], 4)
                osv_tb.loc[i, 'staubXeq'] = round((2 * fitPoly[0] * inflectionPoint ** 3 + fitPoly[1] * inflectionPoint ** 2 - fitPoly[3]) / (3 * fitPoly[0] * inflectionPoint ** 2 + 2 * fitPoly[1] * inflectionPoint + fitPoly[2]), 4)
                # Boiling number 가 0.001 이하 이고, xmaritn (y절편)이 0.5 이상일 때 xosv를 계산
                if osv_tb.loc[i, 'serizawaXeq'] < -0.014:
                    if osv_tb.loc[i, 'bo'] < 0.0005:
                        osv_tb.loc[i, 'xosv'] = round(osv_tb.loc[i, 'martinXeq'], 4)
                    else:
                        if osv_tb.loc[i, 'staubXeq'] > 0:
                            osv_tb.loc[i, 'xosv'] = round(min(osv_tb.loc[i, ['serizawaXeq', 'martinXeq']]), 4)
                        else:
                            osv_tb.loc[i, 'xosv'] = round(osv_tb.loc[i, 'staubXeq'], 4)
                else:
                    if osv_tb.loc[i, 'serizawaXeq'] < -0.075:
                        osv_tb.loc[i, 'xosv'] = round(osv_tb.loc[i, 'serizawaXeq'], 4)
                    else:
                        osv_tb.loc[i, 'xosv'] = round(osv_tb.loc[i, 'martinXeq'], 4)
        except Exception as e:
            print('{} source의 run_id: {}에서 Error 발생. 낮은 Polyfit 예측정확도를 가집니다.'.format(osv_tb.loc[i, 'source'], osv_tb.loc[i, 'run_id']))
            print(e)

    # 무차원 수 계산하기
    for i in range(0, len(osv_tb)):
        if osv_tb.loc[i, 'alpha'] is not np.nan:
            osv_tb.loc[i, 'tosv'] = round(-osv_tb.loc[i, 'xosv'] * osv_tb.loc[i, 'lam'] / osv_tb.loc[i, 'cpf'], 6)
            #print("{} source OSV 계산 완료 : {}".format(osv_tb.loc[i, 'source'], osv_tb.loc[i, 'tosv']))
        else:
            osv_tb.loc[i, 'tosv'] = round(osv_tb.loc[i, 'tosv'], 6)
            #print("OSV 계산 완료 : {}".format(osv_tb.loc[i, 'tosv']))

    osv_tb['de'] = round(osv_tb[['doi', 'dio', 'geo', 'hsur', 'dh']].apply(lambda x: pro.calDe(x[0], x[1], x[2], x[3], x[4]), axis=1), 6)
    osv_tb['pe'] = round(osv_tb[['dh', 'g', 'cpf', 'kf']].apply(lambda x: pro.calPe(x[0], x[1], x[2], x[3]), axis=1), 6)
    osv_tb['st'] = round(osv_tb[['q', 'cpf', 'rhof', 'v', 'tosv']].apply(lambda x: pro.calSt(x[0], x[1], x[2], x[3], x[4]), axis=1), 6)
    osv_tb['re'] = round(osv_tb[['g', 'dh', 'muf']].apply(lambda x: pro.calRe(x[0], x[1], x[2]), axis=1), 6)
    osv_tb['we'] = round(osv_tb[['rhof', 'v', 'dh', 'sigma']].apply(lambda x: pro.calWe(x[0], x[1], x[2], x[3]), axis=1), 6)
    osv_tb['bd'] = round(osv_tb[['rhof', 'rhov', 'dh', 'sigma']].apply(lambda x: pro.calBd(x[0], x[1], x[2], x[3]), axis=1), 6)
    osv_tb['pr'] = round(osv_tb[['cpf', 'muf', 'kf']].apply(lambda x: pro.calPr(x[0], x[1], x[2]), axis=1), 6)
    osv_tb['ca'] = round(osv_tb[['muf', 'v', 'sigma', 'rhof']].apply(lambda x: pro.calCa(x[0], x[1], x[2], x[3]), axis=1), 6)
    osv_tb['nu'] = round(osv_tb[['q', 'dh', 'kf', 'tosv']].apply(lambda x: pro.calNu(x[0], x[1], x[2], x[3]), axis=1), 6)

    # 계산된 osv_tb의 properties 데이터를 PostgreSQL로 옮기기
    osv_tb.index.name = 'index'
    sql.write_sql(osv_tb, 'prop_osv_tb', db_engine)

    # OSV 모델 계산하기
    cor_osv_tb = pd.DataFrame(data=osv_tb[['source','run_id','xosv','tosv']]) # comparison table

    for i, row in cor_osv_tb.iterrows():  # Apply models or correlations to dataframe
        try:
            # OSV
            cor_osv_tb.loc[i, 'dt_js'], cor_osv_tb.loc[i, 'x_js']               = mod.calJeong(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'rhof'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'v'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'pe'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'pr'],  osv_tb.loc[i, 'we']) # Jeong and Shim
            cor_osv_tb.loc[i, 'dt_sz'], cor_osv_tb.loc[i, 'x_sz']               = mod.calSahaZuber(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'rhof'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'pe'], osv_tb.loc[i, 'lam']) # Saha and Zuber
            cor_osv_tb.loc[i, 'dt_levy'], cor_osv_tb.loc[i, 'x_levy']           = mod.calLevy(osv_tb.loc[i, 'sigma'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'rhof'], osv_tb.loc[i, 'muf'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 're'], osv_tb.loc[i, 'pr'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'q'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'v']) # Levy
            cor_osv_tb.loc[i, 'dt_bowr'], cor_osv_tb.loc[i, 'x_bowr']           = mod.calBowring(osv_tb.loc[i, 'p'], osv_tb.loc[i, 'q'], osv_tb.loc[i, 'v'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'cpf']) # Bowring
            cor_osv_tb.loc[i, 'dt_unal'], cor_osv_tb.loc[i, 'x_unal']           = mod.calUnal(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'pr'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'v'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 're'], osv_tb.loc[i, 'refri'], osv_tb.loc[i, 'lam']) # Unal
            cor_osv_tb.loc[i, 'dt_msz'], cor_osv_tb.loc[i, 'x_msz']             = mod.calMSZ(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'rhof'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'pe'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'hsur'], osv_tb.loc[i, 'geo'],osv_tb.loc[i, 'doi'], osv_tb.loc[i, 'dio'], osv_tb.loc[i, 'lh']) # Modified Saha and Zuber (2013)
            cor_osv_tb.loc[i, 'dt_costa'], cor_osv_tb.loc[i, 'x_costa']         = mod.calCosta(osv_tb.loc[i, 'geo'], osv_tb.loc[i, 'q'], osv_tb.loc[i, 'v'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam']) # Costa
            cor_osv_tb.loc[i, 'dt_griffith'], cor_osv_tb.loc[i, 'x_griffith']   = mod.calGriffith(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam']) # Griffith
            cor_osv_tb.loc[i, 'dt_hancox'], cor_osv_tb.loc[i, 'x_hancox']       = mod.calHancox(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'de'], osv_tb.loc[i, 're'], osv_tb.loc[i, 'pr']) # Hancox and Nicoll
            cor_osv_tb.loc[i, 'dt_ha2005'], cor_osv_tb.loc[i, 'x_ha2005']       = mod.calHa2005(osv_tb.loc[i, 'q'],osv_tb.loc[i, 'dh'],osv_tb.loc[i, 'kf'],osv_tb.loc[i, 'cpf'],osv_tb.loc[i, 'lam'],osv_tb.loc[i, 'pe']) # Ha 2005
            cor_osv_tb.loc[i, 'dt_ha2018'], cor_osv_tb.loc[i, 'x_ha2018']       = mod.calHa2018(osv_tb.loc[i, 'rhof'], osv_tb.loc[i, 'rhov'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'bo'], osv_tb.loc[i, 'v']) # Ha 2018
            cor_osv_tb.loc[i, 'dt_dix'], cor_osv_tb.loc[i, 'x_dix']             = mod.calDix(osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'q'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 're'], osv_tb.loc[i, 'pr']) # Dix (1971)
            cor_osv_tb.loc[i, 'dt_sekoguchi'], cor_osv_tb.loc[i, 'x_sekoguchi'] = mod.calSekoguchi(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam']) # Sekoguchi (1980)
            cor_osv_tb.loc[i, 'dt_psz'], cor_osv_tb.loc[i, 'x_psz']             = mod.calParkSahaZuber(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'rhof'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'pe'], osv_tb.loc[i, 'lam']) # Park Saha and Zuber (2004)
            cor_osv_tb.loc[i, 'dt_costa'], cor_osv_tb.loc[i, 'x_costa']         = mod.calCosta(osv_tb.loc[i, 'geo'], osv_tb.loc[i, 'q'], osv_tb.loc[i, 'v'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam'])
            cor_osv_tb.loc[i, 'dt_kal'], cor_osv_tb.loc[i, 'x_kal']             = mod.calKalitvianski(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'pe'])
            #cor_osv_tb.loc[i, 'dt_thom'], cor_osv_tb.loc[i, 'x_thom'] = mod.calThom(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'g'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'hfo']) # Thom (1966)

            # OFI
            """cor_osv_tb.loc[i, 'dt_el'], cor_osv_tb.loc[i, 'x_el'] = mod.calEl(osv_tb.loc[i, 'bo_el'], osv_tb.loc[i, 'pr'], osv_tb.loc[i, 'lh'], osv_tb.loc[i, 'dh'],
                                        osv_tb.loc[i, 'dtin'],
                                        osv_tb.loc[i, 'cpf'], osv_tb.loc[i, 'lam'])
            cor_osv_tb.loc[i, 'dt_msz'], cor_osv_tb.loc[i, 'x_msz'] = mod.calMSZ(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'rhof'], osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'g'],
                                          osv_tb.loc[i, 'cpf'],
                                          osv_tb.loc[i, 'kf'], osv_tb.loc[i, 'pe'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'hsur'],
                                          osv_tb.loc[i, 'geo'], osv_tb.loc[i, 'doi'], osv_tb.loc[i, 'dio'], osv_tb.loc[i, 'lh'])

            cor_osv_tb.loc[i, 'dt_al'], cor_osv_tb.loc[i, 'x_al'] = mod.calAl_Yahia(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'doi'], osv_tb.loc[i, 'lh'], osv_tb.loc[i, 'cpf'],
                                              osv_tb.loc[i, 'dtin'],
                                              osv_tb.loc[i, 'dio'], osv_tb.loc[i, 'geo'], osv_tb.loc[i, 'hsur'], osv_tb.loc[i, 'dh'],
                                              osv_tb.loc[i, 'gsat'], osv_tb.loc[i, 'lam'], osv_tb.loc[i, 'p'])

            cor_osv_tb.loc[i, 'dt_lee'], cor_osv_tb.loc[i, 'x_lee'] = mod.calLee(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'doi'], osv_tb.loc[i, 'lh'], osv_tb.loc[i, 'cpf'],
                                          osv_tb.loc[i, 'dtin'],
                                          osv_tb.loc[i, 'dio'], osv_tb.loc[i, 'geo'], osv_tb.loc[i, 'hsur'], osv_tb.loc[i, 'dh'],
                                          osv_tb.loc[i, 'gsat'], osv_tb.loc[i, 'lam'])

            cor_osv_tb.loc[i, 'dt_kennedy'], cor_osv_tb.loc[i, 'x_kennedy'] = mod.calKennedy(osv_tb.loc[i, 'q'], osv_tb.loc[i, 'doi'], osv_tb.loc[i, 'lh'], osv_tb.loc[i, 'cpf'],
                                                  osv_tb.loc[i, 'dtin'], osv_tb.loc[i, 'dio'], osv_tb.loc[i, 'geo'],
                                                  osv_tb.loc[i, 'hsur'],
                                                  osv_tb.loc[i, 'dh'], osv_tb.loc[i, 'gsat'], osv_tb.loc[i, 'lam'])"""
        except ZeroDivisionError as e:
            print("Index {:d}에서 ZeroDivisionError 발생".format(i))
        finally:
            pass

    print("계산을 완료하였습니다.")


    # Tree 분석을 위한 solution column 만들기
    for i in range(0, len(cor_osv_tb)):
        """
        각 method (Martin, Serizawa, Staub)의 값이 0 미만이면서 최소값을 solution으로 가정.
        solution column을 만들기 위한 작업
        """
        if osv_tb.loc[i, 'martinXeq'] > 0:
            cor_osv_tb.loc[i, 'rmseMartinXeq'] = np.nan
        else:
            cor_osv_tb.loc[i, 'rmseMartinXeq'] = round((1 - cor_osv_tb.loc[i, 'x_js'] / osv_tb.loc[i, 'martinXeq']), 6)

        if osv_tb.loc[i, 'serizawaXeq'] > 0:
            cor_osv_tb.loc[i, 'rmseSerizawaXeq'] = np.nan
        else:
            cor_osv_tb.loc[i, 'rmseSerizawaXeq'] = round((1 - cor_osv_tb.loc[i, 'x_js'] / osv_tb.loc[i, 'serizawaXeq']), 6)

        if osv_tb.loc[i, 'staubXeq'] > 0:
            cor_osv_tb.loc[i, 'rmseStaubXeq'] = np.nan
        else:
            cor_osv_tb.loc[i, 'rmseStaubXeq'] = round((1 - cor_osv_tb.loc[i, 'x_js'] / osv_tb.loc[i, 'staubXeq']), 6)

        cor_osv_tb.loc[i, 'tstXeq'] = min(np.abs(cor_osv_tb.loc[i, 'rmseSerizawaXeq']),
                                          np.abs(cor_osv_tb.loc[i, 'rmseMartinXeq']),
                                          np.abs(cor_osv_tb.loc[i, 'rmseStaubXeq']))

        #print(cor_osv_tb.loc[i, 'rmseStaubXeq'], cor_osv_tb.loc[i, 'rmseMartinXeq'], cor_osv_tb.loc[i, 'rmseSerizawaXeq'])

        if cor_osv_tb.loc[i, 'tstXeq'] == abs(cor_osv_tb.loc[i, 'rmseMartinXeq']):
            cor_osv_tb.loc[i, 'sol'] = "Martin"
        elif cor_osv_tb.loc[i, 'tstXeq'] == abs(cor_osv_tb.loc[i, 'rmseSerizawaXeq']):
            cor_osv_tb.loc[i, 'sol'] = "Serizawa"
        elif cor_osv_tb.loc[i, 'tstXeq'] == abs(cor_osv_tb.loc[i, 'rmseStaubXeq']):
            cor_osv_tb.loc[i, 'sol'] = "Staub"
        else:
            cor_osv_tb.loc[i, 'sol'] = "None"

    # RMSE를 계산하기 위한 테이블. 각 correlation에 대한 data마다의 rmse값을 작성.
    model_who = ['js', 'sz', 'levy', 'bowr', 'unal', 'griffith', 'hancox', 'ha2005', 'ha2018', 'dix', 'sekoguchi', 'psz', 'kal', 'costa', 'msz']
    for i, rows in cor_osv_tb.iterrows():
        for j in model_who:
            cor_osv_tb.loc[i, 'rmse_' + j] = round((1 - cor_osv_tb.loc[i, 'x_' + j] / cor_osv_tb.loc[i, 'xosv']), 4)

    # correlation에대한 RMSE결과를 PostgreSQL로 이동
    sql.write_sql(cor_osv_tb,"rmse_osv_tb",db_engine)

    # Feature analysis
    # 숫자값만 가지는 df 테이블 생성
    df_nur = osv_tb[osv_tb.columns.difference(['datap', 'run_id','source', 'refri', 'geo','flow','pp','alpha','xeq', 'xMartin','serizawaXeq','martinXeq','staubXeq','gsat','qratio'])]

    # MIN-MAX Scaler 적용한 데이터프레임 만들기
    min_max_scaler = MinMaxScaler(feature_range=[0, 1])
    fitted_minmax=min_max_scaler.fit(df_nur)
    out_minmax = min_max_scaler.transform(df_nur)
    out_minmax = pd.DataFrame(out_minmax, columns=df_nur.columns, index=list(df_nur.index.values))
    out_minmax.index.name='index'
    # Quantile Scaler 적용한 데이터프레임
    quantile_scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state =0)
    fitted_quantile = quantile_scaler.fit(df_nur)
    out_quantile = quantile_scaler.transform(df_nur)
    out_quantile = pd.DataFrame(out_quantile, columns=df_nur.columns, index=list(df_nur.index.values))

    # PostgreSQL DB에 옮기기
    sql.write_sql(out_quantile, 'osv_quan_tb', db_engine)
    sql.write_sql(out_minmax, 'osv_minmax_tb', db_engine)

    print("The progress for predicting and comparing between values of OSV is completed.")
