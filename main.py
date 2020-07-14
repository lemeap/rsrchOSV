# 분석 환경 모듈
import numpy as np
import pandas as pd
import psycopg2 as pg
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
#testst


# 데이터 분석 모듈
from CoolProp.CoolProp import PropsSI
from sklearn.preprocessing import MinMaxScaler, QuantileTransformer, PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from scipy.integrate import ode

# 내가 만든 모듈 임포트
from ModelOSV import *
from PhysicalProperty import *
from StructuredQuery import *
from Numeric import *

# Graph Font 설정
style.use('seaborn-talk')
krfont = {'family': 'Times New Roman', 'weight': 'bold', 'size': 10}
matplotlib.rc('font', **krfont)
matplotlib.rcParams['axes.unicode_minus'] = False

# Main
if __name__ == "__main__":
    # 클래스 정의 및  인스턴스 생성
    pro = PhysicalProperty()
    mod = ModelOSV()
    sql = StructuredQuery()

    # SQL 연결 쿼리문
    (conn, dbEngine) = sql.connect('localhost', 'Research', 'postgres', '5432', '1234')

    # 연결 확인
    print("PostgreSQL에 Research Database에 연결을 완료하였습니다.", conn)
    print(dbEngine)

    # OSV 데이터베이스 연결
    loadOSVQuery = "SELECT * FROM rawdata_1"
    osvTb = sql.read_sql(loadOSVQuery, dbEngine)
    print("현재 호출된 table은 osvTb입니다.")

    # Physical Properties 계산
    for i, row in osvTb.iterrows():
        if osvTb.loc[i, 'refri'] is "Water":
            # 미리 계산해두었던 physical properties
            osvTb.loc[i, 'tsat'] = round(PropsSI('T', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 4)
            osvTb.loc[i, 'kf'] = round(PropsSI('L', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osvTb.loc[i, 'kv'] = round(PropsSI('L', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osvTb.loc[i, 'muf'] = round(PropsSI('V', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 12)
            osvTb.loc[i, 'muv'] = round(PropsSI('V', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 12)
            osvTb.loc[i, 'rhof'] = round(PropsSI('D', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osvTb.loc[i, 'rhov'] = round(PropsSI('D', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osvTb.loc[i, 'cpf'] = round(PropsSI('C', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osvTb.loc[i, 'cpv'] = round(PropsSI('C', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osvTb.loc[i, 'sigma'] = round(PropsSI('I', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osvTb.loc[i, 'hgo'] = round(PropsSI('H', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 1, 'Water'), 6)
            osvTb.loc[i, 'hfo'] = round(PropsSI('H', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
            osvTb.loc[i, 'lam'] = round(osvTb.loc[i, 'hgo'] - osvTb[i, 'hfo'], 6)
            if osvTb.loc[i, 'ti'] is np.nan:
                osvTb.loc[i, 'dtin'] = np.nan
            else:
                osvTb.loc[i, 'dtin'] = round(osvTb.loc[i, 'tsat'] - osvTb.loc[i, 'ti'], 4)
            # Xosv 결정에 사용되므로 미리 계산
            osvTb.loc[i, 'bo'] = round(pro.calBo(osvTb.loc[i, 'q'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'g']), 6)

        else:
            # Xosv 결정에 사용되므로 미리 계산
            osvTb.loc[i, 'bo'] = round(pro.calBo(osvTb.loc[i, 'q'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'g']), 6)
            if osvTb.loc[i, 'ti'] is np.nan:
                osvTb.loc[i, 'dtin'] = np.nan
            else:
                osvTb.loc[i, 'dtin'] = round(osvTb.loc[i, 'tsat'] - osvTb.loc[i, 'ti'], 4)


    """# 조건에 따른 inlet subcooling, Gsat, Qratio 계산
    for i, row in osvTb.iterrows():
        if osvTb.loc[i, 'dtin'] == np.nan:
            osvTb.loc[i, 'gsat'] = np.nan
        else:
            osvTb['gsat'] = round(
                pro.calGsat(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'cpf'],
                            osvTb.loc[i, 'dtin'], osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'], osvTb.loc[i, 'hsur'],
                            osvTb.loc[i, 'dh']), 6)
            osvTb['qratio'] = round(
                pro.calQratio(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'],
                              osvTb.loc[i, 'hsur'], osvTb.loc[i, 'g'], osvTb.loc[i, 'cpf'], osvTb.loc[i, 'dtin'],
                              osvTb.loc[i, 'lh']), 6)
    """

    # xosv를 결정하기 위한 알고리즘
    for i, row in osvTb.iterrows():
        osvTb.loc[i, 'v'] = round(osvTb.loc[i, 'g'] / osvTb.loc[i, 'rhof'], 6)
        try:
            if osvTb.loc[i, 'alpha'] is np.nan:  # void fraction 데이터가 아니라 OSV 실험 데이터에서 xosv 계산
                print("{} 번째 {} source의 run_id {}는 OSV를 바로 계산합니다.".format(i, osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id']))
                osvTb.loc[i, 'xosv'] = round(-osvTb.loc[i, 'cpf'] * osvTb.loc[i, 'tosv'] / osvTb.loc[i, 'lam'], 6)
                # print("{} source의 run_id {}의 OSV: {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id'],osvTb.loc[i, 'xosv']))
                osvTb.loc[i, 'tosv'] = round(osvTb.loc[i, 'tosv'], 6)
                # print("OSV 계산 완료 : {}".format(osvTb.loc[i, 'tosv']))
            else:
                # void fraction profile 데이터에서 xosv 계산
                # print("{} is a np.nan".format(i))
                # print("{} 번째 {} source의 run_id {}는 OSV를 void fraction으로 계산합니다.".format(i, osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id']))
                alpha = list((map(float, osvTb.loc[i, 'alpha'].split('|'))))
                xeq = list((map(float, osvTb.loc[i, 'xeq'].split('|'))))

                alpha = np.array(alpha)
                xeq = np.array(xeq)

                # Polynomial regression (R2 > 0.8)

                x = xeq[:, np.newaxis]
                y = alpha[:, np.newaxis]

                # 첫 번째 Equlibrium quality 값 저장하기
                osvTb.loc[i,'xeq1'] = xeq[0]

                # Polynomial regression 진행
                polyFeatures = PolynomialFeatures(degree=3)
                xPoly = polyFeatures.fit_transform(x)
                linReg = LinearRegression()
                linReg.fit(xPoly, y)
                yPolyPred = linReg.predict(xPoly)

                r2 = round(r2_score(y, yPolyPred), 4)
                print("{}의 {} 실험 데이터의 r2: {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id'], r2))

                inflectionPoint = round(-linReg.coef_[0, 2] / (3 * linReg.coef_[0, 3]), 4)
                xMartin = linReg.intercept_[0]

                # R2 Score값 비교하여 계산
                if r2 < 0.9:
                    osvTb.loc[i, 'xMartin'] = np.nan
                    osvTb.loc[i, 'serizawaXeq'] = np.nan
                    osvTb.loc[i, 'martinXeq'] = np.nan
                    osvTb.loc[i, 'staubXeq'] = np.nan
                else:
                    osvTb.loc[i, 'xMartin'] = xMartin
                    osvTb.loc[i, 'serizawaXeq'] = inflectionPoint
                    osvTb.loc[i, 'martinXeq'] = round(-linReg.intercept_[0] / linReg.coef_[0, 1], 4)
                    osvTb.loc[i, 'staubXeq'] = round((2 * linReg.coef_[0, 3] * inflectionPoint ** 3 + linReg.coef_[
                        0, 2] * inflectionPoint ** 2 - linReg.intercept_[0]) / (
                                                              3 * linReg.coef_[0, 3] * inflectionPoint ** 2 + 2 *
                                                              linReg.coef_[0, 2] * inflectionPoint + linReg.coef_[
                                                                  0, 1]), 4)

                osvTb.loc[i, 'bo'] = round(pro.calBo(osvTb.loc[i, 'q'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'g']), 6)
                osvTb.loc[i, 'pe'] = round(pro.calPe(osvTb.loc[i, 'dh'], osvTb.loc[i, 'g'], osvTb.loc[i, 'cpf'], osvTb.loc[i, 'kf']), 6)
                osvTb.loc[i, 'pr'] = round(pro.calPr(osvTb.loc[i, 'cpf'], osvTb.loc[i, 'muf'], osvTb.loc[i, 'kf']), 6)

                if osvTb.loc[i, 'pr'] <= 1.5:
                    if osvTb.loc[i, 'xMartin'] < 0.45:
                        if osvTb.loc[i, 'martinXeq'] > 0:
                            osvTb.loc[i, 'xosv'] = round(min(osvTb.loc[i, ['serizawaXeq','staubXeq']]), 4)
                        else:
                            osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'martinXeq'], 4)
                    else:
                        osvTb.loc[i, 'xosv'] = round(min(osvTb.loc[i, ['martinXeq', 'staubXeq']]), 4)
                else:
                    if osvTb.loc[i, 'serizawaXeq'] > 0:
                        osvTb.loc[i, 'xosv'] = round(min(osvTb.loc[i, ['martinXeq','staubXeq']]), 4)
                    else:
                        osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'serizawaXeq'], 4)

                # OSV subcooling 계산
                osvTb.loc[i, 'tosv'] = round(-osvTb.loc[i, 'xosv'] * osvTb.loc[i, 'lam'] / osvTb.loc[i, 'cpf'], 6)
                # print("{} source OSV 계산 완료 : {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'tosv']))

                print("{}번째 데이터에서 계산된 Xosv: {}".format(i,osvTb.loc[i, 'xosv']))

            # 무차원 수 계산하기
            osvTb.loc[i, 'de'] = round(
                pro.calDe(osvTb.loc[i, 'doi'], osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'], osvTb.loc[i, 'hsur'],
                          osvTb.loc[i, 'dh']), 6)
            osvTb.loc[i, 'pe'] = round(
                pro.calPe(osvTb.loc[i, 'dh'], osvTb.loc[i, 'g'], osvTb.loc[i, 'cpf'], osvTb.loc[i, 'kf']), 6)
            osvTb.loc[i, 'st'] = round(
                pro.calSt(osvTb.loc[i, 'q'], osvTb.loc[i, 'cpf'], osvTb.loc[i, 'rhof'], osvTb.loc[i, 'v'],
                          osvTb.loc[i, 'tosv']), 6)
            osvTb.loc[i, 're'] = round(pro.calRe(osvTb.loc[i, 'g'], osvTb.loc[i, 'dh'], osvTb.loc[i, 'muf']), 6)
            osvTb.loc[i, 'we'] = round(
                pro.calWe(osvTb.loc[i, 'rhof'], osvTb.loc[i, 'v'], osvTb.loc[i, 'dh'], osvTb.loc[i, 'sigma']), 6)
            osvTb.loc[i, 'bd'] = round(
                pro.calBd(osvTb.loc[i, 'rhof'], osvTb.loc[i, 'rhov'], osvTb.loc[i, 'dh'], osvTb.loc[i, 'sigma']), 6)
            osvTb.loc[i, 'pr'] = round(pro.calPr(osvTb.loc[i, 'cpf'], osvTb.loc[i, 'muf'], osvTb.loc[i, 'kf']), 6)
            osvTb.loc[i, 'ca'] = round(
                pro.calCa(osvTb.loc[i, 'muf'], osvTb.loc[i, 'v'], osvTb.loc[i, 'sigma'], osvTb.loc[i, 'rhof']), 6)
            osvTb.loc[i, 'nu'] = round(
                pro.calNu(osvTb.loc[i, 'q'], osvTb.loc[i, 'dh'], osvTb.loc[i, 'kf'], osvTb.loc[i, 'tosv']), 6)
            osvTb.loc[i, 'ec'] = round(pro.calEc(osvTb.loc[i, 'v'], osvTb.loc[i, 'cpf'], osvTb.loc[i, 'tosv']), 6)
        except Exception as e:
            print('{} source의 run_id: {}에서 Error 발생. 낮은 Polyfit 예측정확도를 가집니다.'.format(osvTb.loc[i, 'source'],
                                                                                     osvTb.loc[i, 'run_id']))
            print(e)

    # 계산된 osvTb의 properties 데이터를 PostgreSQL로 옮기기
    osvTb.index.name = 'index'
    sql.write_sql(osvTb, 'prop_osv_tb', dbEngine)
    print("osvTb에 대한 기본적인 계산 알고리즘을 완료하였습니다.")
    print("corOSVTb에 대한 신규 알고리즘을 진행합니다.")

    # OSV 모델 계산하기 (신규 테이블 corOSVTb)
    corOSVTb = pd.DataFrame(data=osvTb[['source', 'run_id', 'xosv', 'tosv', 'xeq1', 'geo']])  # comparison table
    print("선택된 corOSVTB의 데이터 개수는 {}입니다.".format(len(corOSVTb)))

    for i, row in corOSVTb.iterrows():  # Apply models or correlations to dataframe
        try:
            # OSV
            corOSVTb.loc[i, 'dt_js'], corOSVTb.loc[i, 'x_js'] = mod.calJeong(osvTb.loc[i, 'q'],
                                                                                 osvTb.loc[i, 'rhof'],
                                                                                 osvTb.loc[i, 'dh'],
                                                                                 osvTb.loc[i, 'v'],
                                                                                 osvTb.loc[i, 'cpf'],
                                                                                 osvTb.loc[i, 'kf'],
                                                                                 osvTb.loc[i, 'pe'],
                                                                                 osvTb.loc[i, 'lam'],
                                                                                 osvTb.loc[i, 'ca'],
                                                                                 osvTb.loc[i, 'we'],
                                                                                 osvTb.loc[i, 'bo'],
                                                                                 osvTb.loc[i, 'bd'])# Jeong and Shim
            corOSVTb.loc[i, 'dt_sz'], corOSVTb.loc[i, 'x_sz'] = mod.calSahaZuber(osvTb.loc[i, 'q'],
                                                                                     osvTb.loc[i, 'rhof'],
                                                                                     osvTb.loc[i, 'dh'],
                                                                                     osvTb.loc[i, 'g'],
                                                                                     osvTb.loc[i, 'cpf'],
                                                                                     osvTb.loc[i, 'kf'],
                                                                                     osvTb.loc[i, 'pe'], osvTb.loc[
                                                                                         i, 'lam'])  # Saha and Zuber
            corOSVTb.loc[i, 'dt_levy'], corOSVTb.loc[i, 'x_levy'] = mod.calLevy(osvTb.loc[i, 'sigma'],
                                                                                    osvTb.loc[i, 'dh'],
                                                                                    osvTb.loc[i, 'rhof'],
                                                                                    osvTb.loc[i, 'muf'],
                                                                                    osvTb.loc[i, 'kf'],
                                                                                    osvTb.loc[i, 're'],
                                                                                    osvTb.loc[i, 'pr'],
                                                                                    osvTb.loc[i, 'cpf'],
                                                                                    osvTb.loc[i, 'g'],
                                                                                    osvTb.loc[i, 'q'],
                                                                                    osvTb.loc[i, 'lam'],
                                                                                    osvTb.loc[i, 'v'])  # Levy
            corOSVTb.loc[i, 'dt_bowr'], corOSVTb.loc[i, 'x_bowr'] = mod.calBowring(osvTb.loc[i, 'p'],
                                                                                       osvTb.loc[i, 'q'],
                                                                                       osvTb.loc[i, 'v'],
                                                                                       osvTb.loc[i, 'lam'],
                                                                                       osvTb.loc[i, 'cpf'])  # Bowring
            corOSVTb.loc[i, 'dt_unal'], corOSVTb.loc[i, 'x_unal'] = mod.calUnal(osvTb.loc[i, 'q'],
                                                                                    osvTb.loc[i, 'pr'],
                                                                                    osvTb.loc[i, 'dh'],
                                                                                    osvTb.loc[i, 'v'],
                                                                                    osvTb.loc[i, 'cpf'],
                                                                                    osvTb.loc[i, 'kf'],
                                                                                    osvTb.loc[i, 're'],
                                                                                    osvTb.loc[i, 'refri'],
                                                                                    osvTb.loc[i, 'lam'])  # Unal
            corOSVTb.loc[i, 'dt_msz'], corOSVTb.loc[i, 'x_msz'] = mod.calMSZ(osvTb.loc[i, 'q'],
                                                                                 osvTb.loc[i, 'rhof'],
                                                                                 osvTb.loc[i, 'dh'],
                                                                                 osvTb.loc[i, 'g'],
                                                                                 osvTb.loc[i, 'cpf'],
                                                                                 osvTb.loc[i, 'kf'],
                                                                                 osvTb.loc[i, 'pe'],
                                                                                 osvTb.loc[i, 'lam'],
                                                                                 osvTb.loc[i, 'hsur'],
                                                                                 osvTb.loc[i, 'geo'],
                                                                                 osvTb.loc[i, 'doi'],
                                                                                 osvTb.loc[i, 'dio'], osvTb.loc[
                                                                                     i, 'lh'])  # Modified Saha and Zuber (2013)
            corOSVTb.loc[i, 'dt_costa'], corOSVTb.loc[i, 'x_costa'] = mod.calCosta(osvTb.loc[i, 'geo'],
                                                                                       osvTb.loc[i, 'q'],
                                                                                       osvTb.loc[i, 'v'],
                                                                                       osvTb.loc[i, 'cpf'],
                                                                                       osvTb.loc[i, 'lam'])  # Costa
            corOSVTb.loc[i, 'dt_griffith'], corOSVTb.loc[i, 'x_griffith'] = mod.calGriffith(osvTb.loc[i, 'q'],
                                                                                                osvTb.loc[i, 'g'],
                                                                                                osvTb.loc[i, 'cpf'],
                                                                                                osvTb.loc[
                                                                                                    i, 'lam'])  # Griffith
            corOSVTb.loc[i, 'dt_hancox'], corOSVTb.loc[i, 'x_hancox'] = mod.calHancox(osvTb.loc[i, 'q'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[i, 'kf'],
                                                                                          osvTb.loc[i, 'de'],
                                                                                          osvTb.loc[i, 're'],
                                                                                          osvTb.loc[
                                                                                              i, 'pr'])  # Hancox and Nicoll
            corOSVTb.loc[i, 'dt_ha2005'], corOSVTb.loc[i, 'x_ha2005'] = mod.calHa2005(osvTb.loc[i, 'q'],
                                                                                          osvTb.loc[i, 'dh'],
                                                                                          osvTb.loc[i, 'kf'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[
                                                                                              i, 'pe'])  # Ha 2005
            corOSVTb.loc[i, 'dt_ha2018'], corOSVTb.loc[i, 'x_ha2018'] = mod.calHa2018(osvTb.loc[i, 'rhof'],
                                                                                          osvTb.loc[i, 'rhov'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'bo'],
                                                                                          osvTb.loc[i, 'v'])  # Ha 2018
            corOSVTb.loc[i, 'dt_dix'], corOSVTb.loc[i, 'x_dix'] = mod.calDix(osvTb.loc[i, 'kf'],
                                                                                 osvTb.loc[i, 'q'],
                                                                                 osvTb.loc[i, 'dh'],
                                                                                 osvTb.loc[i, 'cpf'],
                                                                                 osvTb.loc[i, 'lam'],
                                                                                 osvTb.loc[i, 're'],
                                                                                 osvTb.loc[i, 'pr'])  # Dix (1971)
            corOSVTb.loc[i, 'dt_sekoguchi'], corOSVTb.loc[i, 'x_sekoguchi'] = mod.calSekoguchi(osvTb.loc[i, 'q'],
                                                                                                   osvTb.loc[i, 'g'],
                                                                                                   osvTb.loc[i, 'cpf'],
                                                                                                   osvTb.loc[
                                                                                                       i, 'lam'])  # Sekoguchi (1980)
            corOSVTb.loc[i, 'dt_psz'], corOSVTb.loc[i, 'x_psz'] = mod.calParkSahaZuber(osvTb.loc[i, 'q'],
                                                                                           osvTb.loc[i, 'rhof'],
                                                                                           osvTb.loc[i, 'dh'],
                                                                                           osvTb.loc[i, 'g'],
                                                                                           osvTb.loc[i, 'cpf'],
                                                                                           osvTb.loc[i, 'kf'],
                                                                                           osvTb.loc[i, 'pe'],
                                                                                           osvTb.loc[
                                                                                               i, 'lam'])  # Park Saha and Zuber (2004)
            corOSVTb.loc[i, 'dt_costa'], corOSVTb.loc[i, 'x_costa'] = mod.calCosta(osvTb.loc[i, 'geo'],
                                                                                       osvTb.loc[i, 'q'],
                                                                                       osvTb.loc[i, 'v'],
                                                                                       osvTb.loc[i, 'cpf'],
                                                                                       osvTb.loc[i, 'lam'])
            corOSVTb.loc[i, 'dt_kal'], corOSVTb.loc[i, 'x_kal'] = mod.calKalitvianski(osvTb.loc[i, 'q'],
                                                                                          osvTb.loc[i, 'dh'],
                                                                                          osvTb.loc[i, 'kf'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[i, 'pe'])
            # corOSVTb.loc[i, 'dt_thom'], corOSVTb.loc[i, 'x_thom'] = mod.calThom(osvTb.loc[i, 'q'], osvTb.loc[i, 'g'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'cpf'], osvTb.loc[i, 'hfo']) # Thom (1966)

            # OFI
            """corOSVTb.loc[i, 'dt_el'], corOSVTb.loc[i, 'x_el'] = mod.calEl(osvTb.loc[i, 'bo_el'], osvTb.loc[i, 'pr'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'dh'],
                                        osvTb.loc[i, 'dtin'],
                                        osvTb.loc[i, 'cpf'], osvTb.loc[i, 'lam'])
            corOSVTb.loc[i, 'dt_msz'], corOSVTb.loc[i, 'x_msz'] = mod.calMSZ(osvTb.loc[i, 'q'], osvTb.loc[i, 'rhof'], osvTb.loc[i, 'dh'], osvTb.loc[i, 'g'],
                                          osvTb.loc[i, 'cpf'],
                                          osvTb.loc[i, 'kf'], osvTb.loc[i, 'pe'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'hsur'],
                                          osvTb.loc[i, 'geo'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'dio'], osvTb.loc[i, 'lh'])

            corOSVTb.loc[i, 'dt_al'], corOSVTb.loc[i, 'x_al'] = mod.calAl_Yahia(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'cpf'],
                                              osvTb.loc[i, 'dtin'],
                                              osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'], osvTb.loc[i, 'hsur'], osvTb.loc[i, 'dh'],
                                              osvTb.loc[i, 'gsat'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'p'])

            corOSVTb.loc[i, 'dt_lee'], corOSVTb.loc[i, 'x_lee'] = mod.calLee(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'cpf'],
                                          osvTb.loc[i, 'dtin'],
                                          osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'], osvTb.loc[i, 'hsur'], osvTb.loc[i, 'dh'],
                                          osvTb.loc[i, 'gsat'], osvTb.loc[i, 'lam'])

            corOSVTb.loc[i, 'dt_kennedy'], corOSVTb.loc[i, 'x_kennedy'] = mod.calKennedy(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'cpf'],
                                                  osvTb.loc[i, 'dtin'], osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'],
                                                  osvTb.loc[i, 'hsur'],
                                                  osvTb.loc[i, 'dh'], osvTb.loc[i, 'gsat'], osvTb.loc[i, 'lam'])"""
        except ZeroDivisionError as e:
            print("Index {:d}에서 ZeroDivisionError 발생".format(i))
        finally:
            pass
    cnt = 0

    # Tree 분석을 위한 solution column 만들기
    for i in range(0, len(corOSVTb)):
        if osvTb.loc[i,'alpha'] is np.nan:
            continue
        else:
            """
            각 method (Martin, Serizawa, Staub)의 값이 0 미만이면서 최소값을 solution으로 가정.
            solution column을 만들기 위한 작업
            """
            if osvTb.loc[i, 'martinXeq'] < 0 and osvTb.loc[i,'xeq1'] < osvTb.loc[i, 'martinXeq']:
                corOSVTb.loc[i, 'rmseMartinXeq'] = round((1 - (osvTb.loc[i, 'martinXeq'] / corOSVTb.loc[i, 'x_sz'])), 4)
                print("{}의 {} 실험 데이터의 rmseMartinXeq: {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id'], corOSVTb.loc[i, 'rmseMartinXeq']))
            else:
                corOSVTb.loc[i, 'rmseMartinXeq'] = 100
            if osvTb.loc[i, 'serizawaXeq'] < 0 and osvTb.loc[i,'xeq1'] < osvTb.loc[i, 'serizawaXeq']:
                corOSVTb.loc[i, 'rmseSerizawaXeq'] = round((1 - (osvTb.loc[i, 'serizawaXeq'] / corOSVTb.loc[i, 'x_sz'])), 4)
                print("{}의 {} 실험 데이터의 rmseSerizawaXeq: {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id'],
                                                                corOSVTb.loc[i, 'rmseSerizawaXeq']))
            else:
                corOSVTb.loc[i, 'rmseSerizawaXeq'] = 100
            if osvTb.loc[i, 'staubXeq'] < 0 and osvTb.loc[i,'xeq1'] < osvTb.loc[i, 'staubXeq']:
                corOSVTb.loc[i, 'rmseStaubXeq'] = round((1 - (osvTb.loc[i, 'staubXeq'] / corOSVTb.loc[i, 'x_sz'])), 4)
                print("{}의 {} 실험 데이터의 rmseStuabXeq: {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id'],
                                                                corOSVTb.loc[i, 'rmseStaubXeq']))
            else:
                corOSVTb.loc[i, 'rmseStaubXeq'] = 100

            # 최소값 찾기 알고리즘
            minRmse = list(np.abs(corOSVTb.loc[i, ['rmseSerizawaXeq', 'rmseMartinXeq', 'rmseStaubXeq']]))
            minKey = np.abs(minRmse[0])

            for num in minRmse[1:]:
                if np.abs(num) < minKey:
                    minKey = np.abs(num)

            corOSVTb.loc[i, 'tstXeq'] = round(minKey, 4)

            print(corOSVTb.loc[i, 'rmseStaubXeq'], corOSVTb.loc[i, 'rmseMartinXeq'], corOSVTb.loc[i, 'rmseSerizawaXeq'])

            if corOSVTb.loc[i, 'tstXeq'] == 100:
                corOSVTb.loc[i, 'sol'] = "None"
            elif corOSVTb.loc[i, 'tstXeq'] == abs(round(corOSVTb.loc[i, 'rmseMartinXeq'], 4)):
                corOSVTb.loc[i, 'sol'] = "Martin"
                print("sol은 {}이고, rmseMartinXeq는 {}, tstXeq는 {}".format(corOSVTb.loc[i, 'sol'],
                                                                        corOSVTb.loc[i, 'rmseMartinXeq'],
                                                                        corOSVTb.loc[i, 'tstXeq']))
            elif corOSVTb.loc[i, 'tstXeq'] == abs(round(corOSVTb.loc[i, 'rmseSerizawaXeq'], 4)):
                corOSVTb.loc[i, 'sol'] = "Serizawa"
                print("sol은 {}이고, rmseSerizawaXeq는 {}, tstXeq는 {}".format(corOSVTb.loc[i, 'sol'],
                                                                        corOSVTb.loc[i, 'rmseSerizawaXeq'],
                                                                            corOSVTb.loc[i, 'tstXeq']))
            elif corOSVTb.loc[i, 'tstXeq'] == abs(round(corOSVTb.loc[i, 'rmseStaubXeq'], 4)):
                corOSVTb.loc[i, 'sol'] = "Staub"
                print("sol은 {}이고, rmseStaubXeq는 {}, tstXeq는 {}".format(corOSVTb.loc[i, 'sol'],
                                                                        corOSVTb.loc[i, 'rmseStaubXeq'],
                                                                            corOSVTb.loc[i, 'tstXeq']))
            else:
                corOSVTb.loc[i, 'sol'] = "None"

            # solution set에 따라 데이터를 거르기 위한 작업 진행
            if osvTb.loc[i, 'pr'] <= 1.5:
                if osvTb.loc[i, 'xMartin'] < 0.45:
                    if osvTb.loc[i, 'martinXeq'] > 0:
                        corOSVTb.loc[i, 'corXosv'] = round(min(osvTb.loc[i, ['serizawaXeq', 'staubXeq']]), 4)
                    else:
                        if corOSVTb.loc[i, 'sol'] == "Martin":
                            corOSVTb.loc[i, 'corXosv'] = round(osvTb.loc[i, 'martinXeq'], 4)
                        else:
                            corOSVTb.loc[i, 'corXosv'] = np.nan
                            cnt +=1
                else:
                    corOSVTb.loc[i, 'corXosv'] = round(min(osvTb.loc[i, ['martinXeq', 'staubXeq']]), 4)
            else:
                if osvTb.loc[i, 'serizawaXeq'] > 0:
                    corOSVTb.loc[i, 'corXosv'] = round(min(osvTb.loc[i, ['martinXeq', 'staubXeq']]), 4)
                else:
                    if corOSVTb.loc[i, 'sol'] == "Serizawa":
                        corOSVTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'serizawaXeq'], 4)
                    else:
                        corOSVTb.loc[i, 'xosv'] = np.nan
                        cnt +=1

    print("계산된 cnt")
    print(cnt)


    # RMSE를 계산하기 위한 테이블. 각 correlation에 대한 data마다의 rmse값을 작성.
    model_who = ['js', 'sz', 'levy', 'bowr', 'unal', 'griffith', 'hancox', 'ha2005', 'ha2018', 'dix', 'sekoguchi',
                 'psz', 'kal', 'costa', 'msz']
    for i, rows in corOSVTb.iterrows():
        for j in model_who:
            corOSVTb.loc[i, 'rmse_' + j] = round((1 - corOSVTb.loc[i, 'x_' + j] / corOSVTb.loc[i, 'xosv']), 4)

    # correlation에대한 RMSE결과를 PostgreSQL로 이동
    sql.write_sql(corOSVTb, "rmse_osv_tb", dbEngine)

    # Feature analysis
    # 숫자값만 가지는 df 테이블 생성
    dfNur = osvTb[osvTb.columns.difference(['datap', 'run_id', 'source', 'refri', 'geo', 'flow', 'pp', 'alpha', 'xeq', 'xMartin', 'serizawaXeq',
         'martinXeq', 'staubXeq', 'gsat', 'qratio', 'dtin'])]
    #dfMer = pd.merge(dfNur, corOSVTb.loc[:,['rmse_js','rmse_sz']], on = "index", how ="inner")
    #condXosv = dfMer['xosv'] <0
    #condRmse = np.abs(dfMer['rmse_sz']) < 0.6
    #dfMer = dfMer[condXosv & condRmse]

    # MIN-MAX Scaler 적용한 데이터프레임 만들기
    min_max_scaler = MinMaxScaler(feature_range=[0, 1])
    fitted_minmax = min_max_scaler.fit(dfNur)
    out_minmax = min_max_scaler.transform(dfNur)
    out_minmax = pd.DataFrame(out_minmax, columns=dfNur.columns, index=list(dfNur.index.values))
    out_minmax.index.name = 'index'
    # Quantile Scaler 적용한 데이터프레임
    quantile_scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=0)
    fitted_quantile = quantile_scaler.fit(dfNur)
    out_quantile = quantile_scaler.transform(dfNur)
    out_quantile = pd.DataFrame(out_quantile, columns=dfNur.columns, index=list(dfNur.index.values))


    # PostgreSQL DB에 옮기기
    sql.write_sql(out_quantile, 'osv_quan_tb', dbEngine)
    sql.write_sql(out_minmax, 'osv_minmax_tb', dbEngine)

    conn.close()

    print("The progress for predicting and comparing between values of OSV is completed.")
