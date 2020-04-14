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
    loadOsvQuery = "SELECT * FROM rawdata_1"
    osvTb = sql.read_sql(loadOsvQuery, dbEngine)
    print("현재 호출된 table은 osvTb입니다.")

    # Physical Properties 계산
    for i, row in osvTb.iterrows():
        if osvTb.loc[i, 'refri'] is 'Water':
            # 미리 계산해두었던 physical properties
            osvTb.loc[i, 'tsat'] = round(PropsSI('T', 'P', osvTb.loc[i, 'p'] * 1e5, 'Q', 0, 'Water'), 6)
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
            if osvTb.loc[i, 'ti'] == np.nan:
                osvTb.loc[i, 'dtin'] = np.nan
            else:
                osvTb.loc[i, 'dtin'] = round(osvTb.loc[i, 'tsat'] - osvTb[i, 'ti'], 6)
            # Xosv 결정에 사용되므로 미리 계산
            osvTb.loc[i, 'bo'] = round(pro.calBo(osvTb.loc[i, 'q'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'g']), 6)

        else:
            # Xosv 결정에 사용되므로 미리 계산
            osvTb.loc[i, 'bo'] = round(pro.calBo(osvTb.loc[i, 'q'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'g']), 6)
            continue


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
                # print("{} 번째 {} source의 run_id {}는 OSV를 바로 계산합니다.".format(i, osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id']))
                osvTb.loc[i, 'xosv'] = round(-osvTb.loc[i, 'cpf'] * osvTb.loc[i, 'tosv'] / osvTb.loc[i, 'lam'], 6)
                # print("{} source의 run_id {}의 OSV: {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id'],osvTb.loc[i, 'xosv']))
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

                polyFeatures = PolynomialFeatures(degree=3)
                xPoly = polyFeatures.fit_transform(x)
                linReg = LinearRegression()
                linReg.fit(xPoly, y)
                yPolyPred = linReg.predict(xPoly)

                r2 = round(r2_score(y, yPolyPred), 4)
                print("{}의 {} 실험 데이터의 r2: {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'run_id'], r2))

                inflectionPoint = round(-linReg.coef_[0, 2] / (3 * linReg.coef_[0, 3]), 4)
                xMartin = linReg.intercept_[0]

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


                print("{}번째 데이터에서 계산된 Xosv: {}".format(i,osvTb.loc[i, 'xosv']))




                """
                if osvTb.loc[i, 'serizawaXeq'] < -0.014:
                    if osvTb.loc[i, 'bo'] < 0.0005:
                        osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'martinXeq'], 4)
                    else:
                        if osvTb.loc[i, 'staubXeq'] > 0:
                            osvTb.loc[i, 'xosv'] = round(min(osvTb.loc[i, ['serizawaXeq', 'martinXeq']]), 4)
                        else:
                            osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'staubXeq'], 4)
                else:
                    if osvTb.loc[i, 'serizawaXeq'] < -0.075:
                        osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'serizawaXeq'], 4)
                    else:
                        osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'martinXeq'], 4)
                """
        except Exception as e:
            print('{} source의 run_id: {}에서 Error 발생. 낮은 Polyfit 예측정확도를 가집니다.'.format(osvTb.loc[i, 'source'],
                                                                                     osvTb.loc[i, 'run_id']))
            print(e)

    # 무차원 수 계산하기
    for i in range(0, len(osvTb)):
        if osvTb.loc[i, 'alpha'] is not np.nan:
            osvTb.loc[i, 'tosv'] = round(-osvTb.loc[i, 'xosv'] * osvTb.loc[i, 'lam'] / osvTb.loc[i, 'cpf'], 6)
            # print("{} source OSV 계산 완료 : {}".format(osvTb.loc[i, 'source'], osvTb.loc[i, 'tosv']))
        else:
            osvTb.loc[i, 'tosv'] = round(osvTb.loc[i, 'tosv'], 6)
            # print("OSV 계산 완료 : {}".format(osvTb.loc[i, 'tosv']))

    osvTb['de'] = round(
        osvTb[['doi', 'dio', 'geo', 'hsur', 'dh']].apply(lambda x: pro.calDe(x[0], x[1], x[2], x[3], x[4]), axis=1), 6)
    osvTb['pe'] = round(osvTb[['dh', 'g', 'cpf', 'kf']].apply(lambda x: pro.calPe(x[0], x[1], x[2], x[3]), axis=1), 6)
    osvTb['st'] = round(
        osvTb[['q', 'cpf', 'rhof', 'v', 'tosv']].apply(lambda x: pro.calSt(x[0], x[1], x[2], x[3], x[4]), axis=1), 6)
    osvTb['re'] = round(osvTb[['g', 'dh', 'muf']].apply(lambda x: pro.calRe(x[0], x[1], x[2]), axis=1), 6)
    osvTb['we'] = round(
        osvTb[['rhof', 'v', 'dh', 'sigma']].apply(lambda x: pro.calWe(x[0], x[1], x[2], x[3]), axis=1), 6)
    osvTb['bd'] = round(
        osvTb[['rhof', 'rhov', 'dh', 'sigma']].apply(lambda x: pro.calBd(x[0], x[1], x[2], x[3]), axis=1), 6)
    osvTb['pr'] = round(osvTb[['cpf', 'muf', 'kf']].apply(lambda x: pro.calPr(x[0], x[1], x[2]), axis=1), 6)
    osvTb['ca'] = round(
        osvTb[['muf', 'v', 'sigma', 'rhof']].apply(lambda x: pro.calCa(x[0], x[1], x[2], x[3]), axis=1), 6)
    osvTb['nu'] = round(osvTb[['q', 'dh', 'kf', 'tosv']].apply(lambda x: pro.calNu(x[0], x[1], x[2], x[3]), axis=1),
                         6)
    osvTb['ec'] = round(osvTb[['v', 'cpf', 'tosv']].apply(lambda x: pro.calEc(x[0], x[1], x[2]), axis=1), 6)

    # OSV 모델 계산하기
    corOsvTb = pd.DataFrame(data=osvTb[['source', 'run_id', 'xosv', 'tosv']])  # comparison table
    print("선택된 corOsvTB의 데이터 개수는 {}입니다.".format(len(corOsvTb)))

    for i, row in corOsvTb.iterrows():  # Apply models or correlations to dataframe
        try:
            # OSV
            corOsvTb.loc[i, 'dt_js'], corOsvTb.loc[i, 'x_js'] = mod.calJeong(osvTb.loc[i, 'q'],
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
            corOsvTb.loc[i, 'dt_sz'], corOsvTb.loc[i, 'x_sz'] = mod.calSahaZuber(osvTb.loc[i, 'q'],
                                                                                     osvTb.loc[i, 'rhof'],
                                                                                     osvTb.loc[i, 'dh'],
                                                                                     osvTb.loc[i, 'g'],
                                                                                     osvTb.loc[i, 'cpf'],
                                                                                     osvTb.loc[i, 'kf'],
                                                                                     osvTb.loc[i, 'pe'], osvTb.loc[
                                                                                         i, 'lam'])  # Saha and Zuber
            corOsvTb.loc[i, 'dt_levy'], corOsvTb.loc[i, 'x_levy'] = mod.calLevy(osvTb.loc[i, 'sigma'],
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
            corOsvTb.loc[i, 'dt_bowr'], corOsvTb.loc[i, 'x_bowr'] = mod.calBowring(osvTb.loc[i, 'p'],
                                                                                       osvTb.loc[i, 'q'],
                                                                                       osvTb.loc[i, 'v'],
                                                                                       osvTb.loc[i, 'lam'],
                                                                                       osvTb.loc[i, 'cpf'])  # Bowring
            corOsvTb.loc[i, 'dt_unal'], corOsvTb.loc[i, 'x_unal'] = mod.calUnal(osvTb.loc[i, 'q'],
                                                                                    osvTb.loc[i, 'pr'],
                                                                                    osvTb.loc[i, 'dh'],
                                                                                    osvTb.loc[i, 'v'],
                                                                                    osvTb.loc[i, 'cpf'],
                                                                                    osvTb.loc[i, 'kf'],
                                                                                    osvTb.loc[i, 're'],
                                                                                    osvTb.loc[i, 'refri'],
                                                                                    osvTb.loc[i, 'lam'])  # Unal
            corOsvTb.loc[i, 'dt_msz'], corOsvTb.loc[i, 'x_msz'] = mod.calMSZ(osvTb.loc[i, 'q'],
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
            corOsvTb.loc[i, 'dt_costa'], corOsvTb.loc[i, 'x_costa'] = mod.calCosta(osvTb.loc[i, 'geo'],
                                                                                       osvTb.loc[i, 'q'],
                                                                                       osvTb.loc[i, 'v'],
                                                                                       osvTb.loc[i, 'cpf'],
                                                                                       osvTb.loc[i, 'lam'])  # Costa
            corOsvTb.loc[i, 'dt_griffith'], corOsvTb.loc[i, 'x_griffith'] = mod.calGriffith(osvTb.loc[i, 'q'],
                                                                                                osvTb.loc[i, 'g'],
                                                                                                osvTb.loc[i, 'cpf'],
                                                                                                osvTb.loc[
                                                                                                    i, 'lam'])  # Griffith
            corOsvTb.loc[i, 'dt_hancox'], corOsvTb.loc[i, 'x_hancox'] = mod.calHancox(osvTb.loc[i, 'q'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[i, 'kf'],
                                                                                          osvTb.loc[i, 'de'],
                                                                                          osvTb.loc[i, 're'],
                                                                                          osvTb.loc[
                                                                                              i, 'pr'])  # Hancox and Nicoll
            corOsvTb.loc[i, 'dt_ha2005'], corOsvTb.loc[i, 'x_ha2005'] = mod.calHa2005(osvTb.loc[i, 'q'],
                                                                                          osvTb.loc[i, 'dh'],
                                                                                          osvTb.loc[i, 'kf'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[
                                                                                              i, 'pe'])  # Ha 2005
            corOsvTb.loc[i, 'dt_ha2018'], corOsvTb.loc[i, 'x_ha2018'] = mod.calHa2018(osvTb.loc[i, 'rhof'],
                                                                                          osvTb.loc[i, 'rhov'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'bo'],
                                                                                          osvTb.loc[i, 'v'])  # Ha 2018
            corOsvTb.loc[i, 'dt_dix'], corOsvTb.loc[i, 'x_dix'] = mod.calDix(osvTb.loc[i, 'kf'],
                                                                                 osvTb.loc[i, 'q'],
                                                                                 osvTb.loc[i, 'dh'],
                                                                                 osvTb.loc[i, 'cpf'],
                                                                                 osvTb.loc[i, 'lam'],
                                                                                 osvTb.loc[i, 're'],
                                                                                 osvTb.loc[i, 'pr'])  # Dix (1971)
            corOsvTb.loc[i, 'dt_sekoguchi'], corOsvTb.loc[i, 'x_sekoguchi'] = mod.calSekoguchi(osvTb.loc[i, 'q'],
                                                                                                   osvTb.loc[i, 'g'],
                                                                                                   osvTb.loc[i, 'cpf'],
                                                                                                   osvTb.loc[
                                                                                                       i, 'lam'])  # Sekoguchi (1980)
            corOsvTb.loc[i, 'dt_psz'], corOsvTb.loc[i, 'x_psz'] = mod.calParkSahaZuber(osvTb.loc[i, 'q'],
                                                                                           osvTb.loc[i, 'rhof'],
                                                                                           osvTb.loc[i, 'dh'],
                                                                                           osvTb.loc[i, 'g'],
                                                                                           osvTb.loc[i, 'cpf'],
                                                                                           osvTb.loc[i, 'kf'],
                                                                                           osvTb.loc[i, 'pe'],
                                                                                           osvTb.loc[
                                                                                               i, 'lam'])  # Park Saha and Zuber (2004)
            corOsvTb.loc[i, 'dt_costa'], corOsvTb.loc[i, 'x_costa'] = mod.calCosta(osvTb.loc[i, 'geo'],
                                                                                       osvTb.loc[i, 'q'],
                                                                                       osvTb.loc[i, 'v'],
                                                                                       osvTb.loc[i, 'cpf'],
                                                                                       osvTb.loc[i, 'lam'])
            corOsvTb.loc[i, 'dt_kal'], corOsvTb.loc[i, 'x_kal'] = mod.calKalitvianski(osvTb.loc[i, 'q'],
                                                                                          osvTb.loc[i, 'dh'],
                                                                                          osvTb.loc[i, 'kf'],
                                                                                          osvTb.loc[i, 'cpf'],
                                                                                          osvTb.loc[i, 'lam'],
                                                                                          osvTb.loc[i, 'pe'])
            # corOsvTb.loc[i, 'dt_thom'], corOsvTb.loc[i, 'x_thom'] = mod.calThom(osvTb.loc[i, 'q'], osvTb.loc[i, 'g'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'cpf'], osvTb.loc[i, 'hfo']) # Thom (1966)

            # OFI
            """corOsvTb.loc[i, 'dt_el'], corOsvTb.loc[i, 'x_el'] = mod.calEl(osvTb.loc[i, 'bo_el'], osvTb.loc[i, 'pr'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'dh'],
                                        osvTb.loc[i, 'dtin'],
                                        osvTb.loc[i, 'cpf'], osvTb.loc[i, 'lam'])
            corOsvTb.loc[i, 'dt_msz'], corOsvTb.loc[i, 'x_msz'] = mod.calMSZ(osvTb.loc[i, 'q'], osvTb.loc[i, 'rhof'], osvTb.loc[i, 'dh'], osvTb.loc[i, 'g'],
                                          osvTb.loc[i, 'cpf'],
                                          osvTb.loc[i, 'kf'], osvTb.loc[i, 'pe'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'hsur'],
                                          osvTb.loc[i, 'geo'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'dio'], osvTb.loc[i, 'lh'])

            corOsvTb.loc[i, 'dt_al'], corOsvTb.loc[i, 'x_al'] = mod.calAl_Yahia(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'cpf'],
                                              osvTb.loc[i, 'dtin'],
                                              osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'], osvTb.loc[i, 'hsur'], osvTb.loc[i, 'dh'],
                                              osvTb.loc[i, 'gsat'], osvTb.loc[i, 'lam'], osvTb.loc[i, 'p'])

            corOsvTb.loc[i, 'dt_lee'], corOsvTb.loc[i, 'x_lee'] = mod.calLee(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'cpf'],
                                          osvTb.loc[i, 'dtin'],
                                          osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'], osvTb.loc[i, 'hsur'], osvTb.loc[i, 'dh'],
                                          osvTb.loc[i, 'gsat'], osvTb.loc[i, 'lam'])

            corOsvTb.loc[i, 'dt_kennedy'], corOsvTb.loc[i, 'x_kennedy'] = mod.calKennedy(osvTb.loc[i, 'q'], osvTb.loc[i, 'doi'], osvTb.loc[i, 'lh'], osvTb.loc[i, 'cpf'],
                                                  osvTb.loc[i, 'dtin'], osvTb.loc[i, 'dio'], osvTb.loc[i, 'geo'],
                                                  osvTb.loc[i, 'hsur'],
                                                  osvTb.loc[i, 'dh'], osvTb.loc[i, 'gsat'], osvTb.loc[i, 'lam'])"""
        except ZeroDivisionError as e:
            print("Index {:d}에서 ZeroDivisionError 발생".format(i))
        finally:
            pass

    print("계산을 완료하였습니다.")

    cnt = 0

    # Tree 분석을 위한 solution column 만들기
    for i in range(0, len(corOsvTb)):
        """
        각 method (Martin, Serizawa, Staub)의 값이 0 미만이면서 최소값을 solution으로 가정.
        solution column을 만들기 위한 작업
        """
        if osvTb.loc[i, 'martinXeq'] > 0:
            corOsvTb.loc[i, 'rmseMartinXeq'] = 100
        else:
            corOsvTb.loc[i, 'rmseMartinXeq'] = round((1 - (osvTb.loc[i, 'martinXeq'] / corOsvTb.loc[i, 'x_sz'])), 4)
        if osvTb.loc[i, 'serizawaXeq'] > 0:
            corOsvTb.loc[i, 'rmseSerizawaXeq'] = 100
        else:
            corOsvTb.loc[i, 'rmseSerizawaXeq'] = round((1 - (osvTb.loc[i, 'serizawaXeq'] / corOsvTb.loc[i, 'x_sz'])), 4)
        if osvTb.loc[i, 'staubXeq'] > 0:
            corOsvTb.loc[i, 'rmseStaubXeq'] = 100
        else:
            corOsvTb.loc[i, 'rmseStaubXeq'] = round((1 - (osvTb.loc[i, 'staubXeq'] / corOsvTb.loc[i, 'x_sz'])), 4)

        # 최소값 찾기 알고리즘
        minRmse = list(np.abs(corOsvTb.loc[i, ['rmseSerizawaXeq', 'rmseMartinXeq', 'rmseStaubXeq']]))
        minKey = np.abs(minRmse[0])

        for num in minRmse[1:]:
            if np.abs(num) < minKey:
                minKey = np.abs(num)

        corOsvTb.loc[i, 'tstXeq'] = round(minKey, 4)

        # print(corOsvTb.loc[i, 'rmseStaubXeq'], corOsvTb.loc[i, 'rmseMartinXeq'], corOsvTb.loc[i, 'rmseSerizawaXeq'])

        if corOsvTb.loc[i, 'tstXeq'] == abs(round(corOsvTb.loc[i, 'rmseMartinXeq'], 4)):
            corOsvTb.loc[i, 'sol'] = "Martin"
        elif corOsvTb.loc[i, 'tstXeq'] == abs(round(corOsvTb.loc[i, 'rmseSerizawaXeq'], 4)):
            corOsvTb.loc[i, 'sol'] = "Serizawa"
        elif corOsvTb.loc[i, 'tstXeq'] == abs(round(corOsvTb.loc[i, 'rmseStaubXeq'], 4)):
            corOsvTb.loc[i, 'sol'] = "Staub"
        else:
            corOsvTb.loc[i, 'sol'] = "None"


        # solution set에 따라 데이터를 거르기 위한 작업 진행
        if osvTb.loc[i, 'pr'] <= 1.5:
            if osvTb.loc[i, 'xMartin'] < 0.45:
                if osvTb.loc[i, 'martinXeq'] > 0:
                    osvTb.loc[i, 'xosv'] = round(min(osvTb.loc[i, ['serizawaXeq', 'staubXeq']]), 4)
                else:
                    if corOsvTb.loc[i, 'sol'] == "Martin":
                        osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'martinXeq'], 4)
                    else:
                        osvTb.loc[i, 'xosv'] = np.nan
                        cnt +=1
            else:
                osvTb.loc[i, 'xosv'] = round(min(osvTb.loc[i, ['martinXeq', 'staubXeq']]), 4)
        else:
            if osvTb.loc[i, 'serizawaXeq'] > 0:
                osvTb.loc[i, 'xosv'] = round(min(osvTb.loc[i, ['martinXeq', 'staubXeq']]), 4)
            else:
                if corOsvTb.loc[i, 'sol'] == "Serizawa":
                    osvTb.loc[i, 'xosv'] = round(osvTb.loc[i, 'serizawaXeq'], 4)
                else:
                    osvTb.loc[i, 'xosv'] = np.nan
                    cnt +=1


    print("계산된 cnt")
    print(cnt)

    # 계산된 osvTb의 properties 데이터를 PostgreSQL로 옮기기
    osvTb.index.name = 'index'
    sql.write_sql(osvTb, 'prop_osv_tb', dbEngine)

    # RMSE를 계산하기 위한 테이블. 각 correlation에 대한 data마다의 rmse값을 작성.
    model_who = ['js', 'sz', 'levy', 'bowr', 'unal', 'griffith', 'hancox', 'ha2005', 'ha2018', 'dix', 'sekoguchi',
                 'psz', 'kal', 'costa', 'msz']
    for i, rows in corOsvTb.iterrows():
        for j in model_who:
            corOsvTb.loc[i, 'rmse_' + j] = round((1 - corOsvTb.loc[i, 'x_' + j] / corOsvTb.loc[i, 'xosv']), 4)

    # correlation에대한 RMSE결과를 PostgreSQL로 이동
    sql.write_sql(corOsvTb, "rmse_osv_tb", dbEngine)

    # Feature analysis
    # 숫자값만 가지는 df 테이블 생성
    dfNur = osvTb[osvTb.columns.difference(
        ['datap', 'run_id', 'source', 'refri', 'geo', 'flow', 'pp', 'alpha', 'xeq', 'xMartin', 'serizawaXeq',
         'martinXeq', 'staubXeq', 'gsat', 'qratio'])]
    dfMer = pd.merge(dfNur, corOsvTb.loc[:,['rmse_js','rmse_sz']], on = "index", how ="inner")
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

    print("The progress for predicting and comparing between values of OSV is completed.")

