# Import Modules
import time
from CoolProp.CoolProp import PropsSI
from PhysicalProperty import *

class ModelOSV(PhysicalProperty):

    def __init__(self):
        print("Model_OSV is successfully started.")

    # Models or correlations
    def calGriffith(self, q, g, cpf, lam): # Griffith et al. (1958) 1/10
        dtOSV = 5 * (q * 10 ** 6) / (g * cpf/10)
        xOSV = -cpf * dtOSV / lam
        return round(dtOSV,4), round(xOSV,4)

    def calHancox(self,q, cpf, lam, kf, de, re, pr): # Hancox and Nicoll (1971) 1/100배
        h = 0.4 * (re**0.662)*pr*(kf/de)
        dtOSV = (q*10**6)/h
        xOSV = -cpf * dtOSV / lam
        return round(dtOSV,4), round(xOSV,4)

    def calCosta(self, geo, q, v, cpf, lam): # Costa (1967) # costa 는 10배 정도 크게 나옴
        if geo == 'C':
            dtOSV = 1.8*(q)/(np.sqrt(v/100))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        if geo == 'R':
            dtOSV = 1.28*(q)/(np.sqrt(v/100))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = np.nan
            xOSV = np.nan
            return round(dtOSV,4), round(xOSV,4)
    
    def calThom(self, q, g, lam, cpf, hfo): # Thom (1966)
        dtOSV = 0.02*hfo*(q*10**6)/(g*lam)
        xOSV = -cpf * dtOSV / lam
        return round(dtOSV,4), round(xOSV,4)
    
    """
    def calStaub(self): # Staub (1968)
        pass

    def calRogers(self,): # Rogers et al. (1987)
        theta = 30
        c1 = 2 + 3*np.cos(theta) - np.cos(theta)**3
        c2 = np.pi - theta + np.cos(theta)*np.sin(theta)
        c3 = np.sin(theta)*(np.cos(theta-10) - np.cos(theta+10))
        cs = 58 / (theta + 5) + 0.14
        rb = (3/(4*np.pi)) * ((c2 / c1) * cd * (u**2/9.8)) * (np.sqrt(1 + (8*np.pi**2/3)*(c1*c3/c2**2)*(cs/cd**2)*(9.8 * sigma / (rhof*u ** 4))) - 1)
        reb = rhof * u * (2*rb) / muf
        if reb < 20:
            cd = 24 / reb
        else:
            cd = 1.22
        cc = np.sqrt(1+)
        f = 0.046*re**(-0.2)
        tau = (0.046/8)*re**(-0.2)
        YB = (rhof/muf)*np.sqrt(tau/rhof) * (1+np.cos(theta)) * (3/(4*np.pi))*(c2/c1)*(cd*muf**2/9.8)*cc 
    
    def calJinghui(self,): # Jinghui and Rogers (1988)
        pass
    """

    def calHa2005(self,q,dh,kf,cpf,lam,pe): # Ha et al. (2005)
        if pe < 52000:
            dtOSV = (1/918.5)*((q*10**6)*dh/kf)*pe**0.08
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = 34.84*((q*10**6)*dh/kf)*(1/pe)**0.876
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
    
    def calHa2018(self,rhof, rhov, lam, cpf, bo, v):
        ui = v /(1.18*(9.8*(rhof-rhov)/rhof**2)**0.25)
        if ui <= 1.55:
            dtOSV = 7.29*(lam/cpf)*bo**0.8203
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = 32.94*(lam/cpf)*bo**0.9016
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calDix(self, kf, q, dh, cpf, lam, re, pr): # Dix (1971)
        h = 0.036 * (kf / dh) * (re ** 0.8) * (pr ** 0.3)
        dtOSV = 0.00135*(q*10**6/h)*np.sqrt(re)
        xOSV = -cpf * dtOSV / lam
        return round(dtOSV,4), round(xOSV,4)
    
    def calKalitvianski(self,q, dh, kf, cpf, lam, pe): # Kalitvianski (2000)
        if pe <= 36400:
            dtOSV = (5/455)*((q*10**3)*dh/kf)
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = (173.408/0.0065) * ((q*10**3)*dh/kf)*(1/pe)
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
    
    def calSekoguchi(self,q, g, cpf, lam): # Sekoguchi et al. (1980)
        dtOSV = 13.5 * (lam/cpf) *((q*10**6)/(lam*g))**0.65
        xOSV = -cpf * dtOSV / lam
        return round(dtOSV,4), round(xOSV,4)

    def calSahaZuber(self, q, rhof, dh, g, cpf, kf, Pe, lam):  # Saha and Zuber (1974)
        """
        :param q: Heat flux [MW/m2]
        :param rhof: Liquid density [kg/m3]
        :param dh: Hydraulic diameter [m]
        :param g: Mass flux [kg/m2-s]
        :param cpf: Liquid specific heat [J/kg-K]
        :param kf: Thermal conductivity [W/m-K]
        :param Pe: Peclet number [-]
        :param lam: Heat of vaporization [J/kg]
        :return: Equilibrium thermal quality [-]
        """
        if Pe <= 70000:
            dtOSV = 0.0022 * (q * (10 ** 6) * dh) / kf
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = 153.8 * (q * (10 ** 6)) / (g * cpf)
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
    
    def calParkSahaZuber(self, q, rhof, dh, g, cpf, kf, Pe, lam): # Park (2004)
        """
        :param q: Heat flux [MW/m2]
        :param rhof: Liquid density [kg/m3]
        :param dh: Hydraulic diameter [m]
        :param g: Mass flux [kg/m2-s]
        :param cpf: Liquid specific heat [J/kg-K]
        :param kf: Thermal conductivity [W/m-K]
        :param Pe: Peclet number [-]
        :param lam: Heat of vaporization [J/kg]
        :return: Equilibrium thermal quality [-]
        """
        if Pe <= 70000:
            dtOSV = 0.0022 * (q * (10 ** 6) * dh) / kf
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        elif Pe > 200000:
            dtOSV = 0.08923 * np.exp(-(Pe * (kf ** 0.45) / (dh ** 0.53 * g ** 0.37)) / 25313.63287) + 0.00659 * np.exp(-(Pe * (kf ** 0.45) / (dh ** 0.53 * g ** 0.37)) / 211422.70151) + 0.00146
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = 153.8 * (q * (10 ** 6)) / (g * cpf)
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calMSZ(self, q, rhof, dh, g, cpf, kf, Pe, lam, hsur, geo, doi, dio, lh):  # Modified Saha and Zuber (2013)
        """
        :param q: Heat flux [MW/m2]
        :param rhof: Liquid density [kg/m3]
        :param dh: Hydraulic diameter [m]
        :param g: Mass flux [kg/m2-s]
        :param cpf: Liquid specific heat [J/kg-K]
        :param kf: Thermal conductivity [W/m-K]
        :param Pe: Peclet number [-]
        :param lam: Heat of vaporization [J/kg]
        :param hsur: Heated surface of cross-sectional geometry of channel [-]
        :param geo: Channel geometry [-]
        :param doi: Outer or longer length of channel geometry [m]
        :param dio: Inner or shorter length of channel geometry [m]
        :param lh: Heated length of channel [m]
        :return: Equilibrium thermal quality [-]
        """
        qq = q * (10 ** 6)
        R_phpw_1h = doi / (2 * (doi + dio))
        R_phpw_2h = doi / (doi + dio)
        A_phpw_1h = dio / (2 * (doi + dio))
        A_phpw_2h = doi / (doi + dio)

        if Pe > 70000:
            if geo == 'R':
                if hsur == 1:
                    dtOSV = ((153.8 * (qq)) / (g * cpf))*R_phpw_1h
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
                else:
                    dtOSV = ((153.8 * (qq)) / (g * cpf))*R_phpw_2h
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
            elif geo == 'A':
                if hsur == 1:
                    dtOSV = ((153.8 * (qq)) / (g * cpf)) * A_phpw_1h
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
                else:
                    dtOSV = ((153.8 * (qq)) / (g * cpf)) * A_phpw_2h
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
            else:
                dtOSV = (153.8 * (qq) / (g * cpf))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        else:
            if geo == 'R':
                if hsur == 1:
                    dtOSV = (0.0022 * (qq * dh) / kf) * R_phpw_1h
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
                else:
                    dtOSV = (0.0022 * (qq * dh) / kf) * R_phpw_2h
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
            elif geo == 'A':
                if hsur == 1:
                    dtOSV = (0.0022 * (qq ** dh) / kf) * A_phpw_1h
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
                else:
                    dtOSV = (0.0022 * (qq * dh) / kf)
                    xOSV = -cpf * dtOSV / lam
                    return round(dtOSV,4), round(xOSV,4)
            else:
                dtOSV = (0.0022 * (qq * dh) / kf)
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)

    def calLevy(self, sigma, dh, rhof, muf, kf, re, pr, cpf, g, q, lam, v):  # Levy (1967)
        """
        :param sigma: Suface tension [N/m]
        :param dh: Hydraulic diameter [m]
        :param rhof: Liquid density [kg/m3]
        :param muf: Liquid viscosity [kg/m-s]
        :param kf: Thermal conductivity [W/m-K]
        :param re: reynolds number [-]
        :param pr: prandtl number [-]
        :param cpf: Liquid specific heat [J/kg-K]
        :param g: Mass flux [kg/m2-s]
        :param q: Heat flux [MW/m2]
        :param lam: Heat of vaporization [J/kg]
        :param v: flow velocity [m/s]
        :return: Equilibrium thermal quality [-]
        """
        YB = 0.015 * np.sqrt(sigma * dh * rhof) / muf
        h = 0.023 * (kf / dh) * (re ** 0.8) * (pr ** 0.4)
        f = 0.0055 * (1 + (20000*(10**-4) + 10**6 / re) ** (1 / 3))
        tau = (f * g**2)/(8*rhof)
        Q = (q * 10 ** 6) / (rhof * cpf * np.sqrt(tau / rhof))
        if YB > 30:
            dtOSV = (q * 10 ** 6) / h - 5 * Q * (pr + np.log(1 + 5 * pr) + 0.5 * np.log(YB / 30))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        elif YB <= 5:
            dtOSV = (q * 10 ** 6) / h - Q * pr * YB
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = (q * 10 ** 6) / h - 5 * Q * (pr + np.log(1 + pr * ((YB / 5) - 1)))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calBowring(self, p, q, v, lam, cpf):  # Bowring (1960)
        """
        :param p: pressure [bar]
        :param q: Heat flux [MW/m2]
        :param v: flow velocity [m/s]
        :param lam: Heat of vaporization [J/kg]
        :param cpf: Liquid specific heat [J/kg-K]
        :return: Equilibrium thermal quality [-]
        """
        dtOSV = ((14 + p / 10)) * q / v
        xOSV = -cpf * dtOSV / lam
        return round(dtOSV,4), round(xOSV,4)

    def calUnal(self, q, pr, dh, v, cpf, kf, re, refri, lam):  # Unal (1975)
        """
        :param q: Heat flux [MW/m2]
        :param pr: prandtl number [-]
        :param dh: Hydraulic diameter [m]
        :param v: flow velocity [m/s]
        :param cpf: Liquid specific heat [J/kg-K]
        :param kf: Thermal conductivity [W/m-K]
        :param re: reynolds number [-]
        :param refri: refrigerants
        :param lam: Heat of vaporization [J/kg]
        :return: Equilibrium thermal quality [-]
        """
        if refri == 'Water':
            if v > 0.45:
                dtOSV = (0.24 * (q * 10 ** 6)) / ((kf / dh) * 0.023 * re ** 0.8 * pr ** 0.4)
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            elif v <= 0.45:
                dtOSV = (0.11 * (q * 10 ** 6)) / ((kf / dh) * 0.023 * re ** 0.8 * pr ** 0.4)
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        else:
            if v > 0.45:
                dtOSV = (0.28 * (q * 10 ** 6)) / ((kf / dh) * 0.023 * re ** 0.8 * pr ** 0.4)
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            elif v <= 0.45:
                dtOSV = (0.11 * (q * 10 ** 6)) / ((kf / dh) * 0.023 * re ** 0.8 * pr ** 0.4)
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)

    def calEl(self, Bo_el, pr, lh, de, dtin, cpf, lam): # El-Morshedy (2012)
        """
        :param Bo_el: Boiling number of El-Mosherdy [-]
        :param pr: prandtl number [-]
        :param lh: Heated length of channel [m]
        :param dh: Hydraulic diameter [m][
        :param dtin: Inlet liquid subcooling [K]
        :param cpf: Liquid specific heat [J/kg-K]
        :param lam: Heat of vaporization [J/kg]
        :return: Equilibrium thermal quality [-]
        """
        if dtin is None:
            dtOSV = np.nan
            xOSV = np.nan
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = dtin * (Bo_el ** 0.0094) * (pr ** 1.606) / ((lh / de) ** 0.533)
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calJeong(self, q, rhof, dh, v, cpf, kf, Pe, lam, Ca, We):  # Jeong and Shim (2019)
        """

        :param q: Heat flux [MW/m2]
        :param rhof: Liquid density [kg/m3]
        :param dh: Hydraulic diameter [m]
        :param v: flow velocity [m/s]
        :param cpf: Liquid specific heat [J/kg-K]
        :param kf: Thermal conductivity [W/m-K]
        :param Pe: Peclet number [-]
        :param lam: Heat of vaporization [J/kg]
        :return: Equilibrium thermal quality [-]
        """
        if We <= 500:
            dtOSV = (q * (10 ** 6)) / (rhof*v*cpf*(240 * (Pe) ** -0.92))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = (q * (10 ** 6)) / (rhof*v*cpf*(0.1259 * (Pe) ** -0.24))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calLee(self, q, doi, lh, cpf, dtin, dio, geo, hsur, dh, gsat, lam):
        """

        :param q: Heat flux [MW/m2]
        :param doi: Outer or longer length of channel geometry [m]
        :param lh: Heated length of channel [m]
        :param cpf: Liquid specific heat [J/kg-K]
        :param dtin: Inlet liquid subcooling [K]
        :param dio: Inner or shorter length of channel geometry [m]
        :param geo: Channel geometry [-]
        :param hsur: Heated surface of cross-sectional geometry of channel [-]
        :param dh: Hydraulic diameter [m]
        :param gsat: gsat: Saturation mass flux [kg/m2-s]
        :param lam: Heat of vaporization [J/kg]
        :return: Equilibrium thermal quality [-]
        """
        qq = q * (10 ** 6)
        R_heated_1h = doi * lh
        R_heated_2h = 2 * doi * lh
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio) * lh
        A_heated_2h = (np.pi * (dio + doi)) * lh
        A_heated_3h = (np.pi * doi)
        A_flow = (np.pi / 4) * (doi ** 2 - dio ** 2)
        C_heated = (np.pi) * doi * lh
        C_flow = (np.pi / 4) * doi ** 2
        R_phpw_1h = doi / (2 * (doi + dio))
        R_phpw_2h = doi / (doi + dio)
        A_phpw_1h = dio / (2 * (doi + dio))
        A_phpw_3h = doi / (doi + dio)

        if geo == 'R':
            if hsur == 1:
                dtOSV = (qq * R_heated_1h) / (R_flow * cpf * ((gsat + 27) / 0.58))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            else:
                dtOSV = (qq * R_heated_2h) / (R_flow * cpf * ((gsat + 27) / 0.58))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        elif geo == 'A':
            if hsur == 1:
                dtOSV = (qq * A_heated_1h) / (A_flow * cpf * ((gsat + 27) / 0.58))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            else:
                dtOSV = (qq * A_heated_2h) / (A_flow * cpf * ((gsat + 27) / 0.58))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = (qq * C_heated) / (C_flow * cpf * ((gsat + 27) / 0.58))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calKennedy(self, q, doi, lh, cpf, dtin, dio, geo, hsur, dh, gsat, lam):
        """
        :param q: Heat flux [MW/m2]
        :param doi: Outer or longer length of channel geometry [m]
        :param lh: Heated length of channel [m]
        :param cpf: Liquid specific heat [J/kg-K]
        :param dtin: Inlet liquid subcooling [K]
        :param dio: Inner or shorter length of channel geometry [m]
        :param geo: Channel geometry [-]
        :param hsur: Heated surface of cross-sectional geometry of channel [-]
        :param dh: Hydraulic diameter [m]
        :param gsat: gsat: Saturation mass flux [kg/m2-s]
        :param lam: Heat of vaporization [J/kg]
        :return: Equilibrium thermal quality [-]
        """
        qq = q * (10 ** 6)
        R_heated_1h = doi * lh
        R_heated_2h = 2 * doi * lh
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio) * lh
        A_heated_2h = (np.pi * (dio + doi)) * lh
        A_heated_3h = (np.pi * doi)
        A_flow = (np.pi / 4) * (doi ** 2 - dio ** 2)
        C_heated = (np.pi) * doi * lh
        C_flow = (np.pi / 4) * doi ** 2
        R_phpw_1h = doi / (2 * (doi + dio))
        R_phpw_2h = doi / (doi + dio)
        A_phpw_1h = dio / (2 * (doi + dio))
        A_phpw_3h = doi / (doi + dio)

        if geo == 'R':
            if hsur == 1:
                dtOSV = (qq * R_heated_1h) / (R_flow * cpf * (gsat * 1.11))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            else:
                dtOSV = (qq * R_heated_2h) / (R_flow * cpf * (gsat * 1.11))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        elif geo == 'A':
            if hsur == 1:
                dtOSV = (qq * A_heated_1h) / (A_flow * cpf * (gsat * 1.11))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            elif hsur == 2:
                dtOSV = (qq * A_heated_2h) / (A_flow * cpf * (gsat * 1.11))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            elif hsur == 3:
                dtOSV = (qq * A_heated_2h) / (A_flow * cpf * (gsat * 1.11))
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        else:
            dtOSV = (qq * C_heated) / (C_flow * cpf * (gsat * 1.11))
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calAl_Yahia(self, q, doi, lh, cpf, dtin, dio, geo, hsur, dh, gsat, lam, p):
        """
        :param q: Heat flux [MW/m2]
        :param doi: Outer or longer length of channel geometry [m]
        :param lh: Heated length of channel [m]
        :param cpf: Liquid specific heat [J/kg-K]
        :param dtin: Inlet liquid subcooling [K]
        :param dio: Inner or shorter length of channel geometry [m]
        :param geo: Channel geometry [-]
        :param hsur: Heated surface of cross-sectional geometry of channel [-]
        :param dh: Hydraulic diameter [m]
        :param gsat: Saturation mass flux [kg/m2-s]
        :param lam: Heat of vaporization [J/kg]
        :param p: pressure [bar]
        :return: Equilibrium thermal quality [-]
        """
        qq = q * (10 ** 6)
        R_heated_1h = doi * lh
        R_heated_2h = 2 * doi * lh
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio) * lh
        A_heated_2h = (np.pi * (dio + doi)) * lh
        A_heated_3h = (np.pi * doi)
        A_flow = (np.pi / 4) * (doi ** 2 - dio ** 2)
        C_heated = (np.pi) * doi * lh
        C_flow = (np.pi / 4) * doi ** 2
        R_phpw_1h = doi / (2 * (doi + dio))
        R_phpw_2h = doi / (doi + dio)
        A_phpw_1h = dio / (2 * (doi + dio))
        A_phpw_2h = 1
        A_phpw_3h = doi / (doi + dio)

        if geo == 'R':
            if hsur == 1:
                dtOSV = (qq * R_heated_1h) / (R_flow * cpf * (1.25 * gsat * R_phpw_1h * (1.12 / p) ** 0.4)) /100
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            else:
                dtOSV = (qq * R_heated_2h) / (R_flow * cpf * (1.25 * gsat * R_phpw_2h * (1.12 / p) ** 0.4)) /100
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        elif geo == 'A':
            if hsur == 1:
                dtOSV = (qq * A_heated_1h) / (A_flow * cpf * (1.25 * gsat * A_phpw_1h * (1.12 / p) ** 0.4)) /100
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            elif hsur == 2:
                dtOSV = (qq * A_heated_2h) / (A_flow * cpf * (1.25 * gsat * A_phpw_2h * (1.12 / p) ** 0.4)) /100
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
            elif hsur == 2:
                dtOSV = (qq * A_heated_2h) / (A_flow * cpf * (1.25 * gsat * A_phpw_3h * (1.12 / p) ** 0.4)) /100
                xOSV = -cpf * dtOSV / lam
                return round(dtOSV,4), round(xOSV,4)
        elif geo == 'C':
            dtOSV = (qq * C_heated) / (C_flow * cpf * (1.25 * gsat * (1.12 / p) ** 0.4)) /100
            xOSV = -cpf * dtOSV / lam
            return round(dtOSV,4), round(xOSV,4)

    def calOfiSZ(self, df):
        """
        :param df: dataframe
        :return: Heat flux [MW/m2]
        """
        # Time
        # 시작부분 코드

        start_time = time.time()
        # ------------------------
        # Saha and Zuber (1974) correlation
        print('Saha and Zuber Correlation (1974) OFI analysis')
        # Step 1
        # tsat     Saturation Temperature at P [K]
        # hfo      Saturated liquid Enthalpy at P [J/kg]
        # hgo      Saturated vapor Enthalpy at P [J/kg]
        # lam     Heat of vaporization at P [J/kg]
        # To Exit Temperature [K]

        for i in df.index:
            df.loc[i, 'To'] = df.loc[i, 'Ti'] + 1  # To 의 초기값설정

            for k in range(1, 10000):  # step 2 - 7 반복
                # Step 2
                # ho Enthalpy at exit [J/kg]
                df.loc[i, 'ho'] = PropsSI('H', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                              df.loc[i, 'refri'])

                # Step 3
                # Pi Inlet pressure [bar]
                df.loc[i, 'Pi_new'] = df.loc[i, 'p']

                for j in range(3):
                    df.loc[i, 'Pi_old'] = df.loc[i, 'Pi_new']

                    # Step 4
                    # P_ave     Average pressure [bar]
                    # T_ave     Average Temperature [K]
                    # rho_ave   Density at Average pressure & Temperature [kg/m3]
                    # mu_ave    Viscosity at Average pressure & Temperature [Pa s]
                    # re_ave    reynolds number [-]

                    df.loc[i, 'P_ave'] = 0.5 * (df.loc[i, 'Pi_new'] + df.loc[i, 'p'])
                    df.loc[i, 'T_ave'] = 0.5 * (df.loc[i, 'Ti'] + df.loc[i, 'To'])
                    df.loc[i, 'rho_ave'] = PropsSI('D', 'T', df.loc[i, 'T_ave'], 'P', df.loc[i, 'P_ave'] * 1e5,
                                                       df.loc[i, 'refri'])
                    df.loc[i, 'mu_ave'] = PropsSI('V', 'T', df.loc[i, 'T_ave'], 'P', df.loc[i, 'P_ave'] * 1e5,
                                                      df.loc[i, 'refri'])
                    df.loc[i, 're_ave'] = PhysicalProperty.re(self,df.loc[i, 'g'], df.loc[i, 'dh'], df.loc[i, 'mu_ave'])

                    # f_ave Friction factor
                    if df.loc[i, 're_ave'] < 2300:
                        df.loc[i, 'f_ave'] = 4 * (24 / df.loc[i, 're_ave'])
                    elif df.loc[i, 're_ave'] >= 4000:
                        df.loc[i, 'f_ave'] = 4 * (1.2810 ** -3 + 0.1143 * (df.loc[i, 're_ave'] ** (-0.3)))
                    else:
                        df.loc[i, 'f_ave'] = 4 * (5.4 * 10 ** -3 + (2.3 * 1e-8) * (df.loc[i, 're_ave'] ** 0.75))

                    # Step 5
                    if df.loc[i, 'flow'] == 'Ho':  # in horizontal flow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                df.loc[i, 'f_ave'] * df.loc[i, 'lh'] / df.loc[i, 'de']) * 0.00001
                    elif df.loc[i, 'flow'] == 'Down':  # in vertical downflow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                (df.loc[i, 'f_ave'] * df.loc[i, 'lh'] / df.loc[i, 'de'])
                                - (df.loc[i, 'rho_ave'] * 9.80665 * df.loc[i, 'lh'])) * 0.00001
                    elif df.loc[i, 'flow'] == 'Up':  # in vertical upflow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                df.loc[i, 'f_ave'] * (df.loc[i, 'lh'] / df.loc[i, 'de'])
                                + (df.loc[i, 'rho_ave'] * 9.80665 * df.loc[i, 'lh'])) * 0.00001

                    df.loc[i, 'P_diff'] = (df.loc[i, 'Pi_old'] - df.loc[i, 'Pi_new']) * 100 / df.loc[i, 'Pi_old']

                    # Step 6
                # hi Enthalpy at inlet [J/kg]
                # q_guess Heat Flux based on heat balance [MW/m2]

                df.loc[i, 'hi'] = PropsSI('H', 'T', df.loc[i, 'Ti'], 'P', df.loc[i, 'Pi_new'] * 1e5,
                                              df.loc[i, 'refri'])
                df.loc[i, 'q_guess'] = PhysicalProperty.calQ(self,df.loc[i, 'doi'], df.loc[i, 'dio'], df.loc[i, 'lh'],
                                                     df.loc[i, 'g'],
                                                     df.loc[i, 'geo'], df.loc[i, 'hsur'], df.loc[i, 'dh'],
                                                     df.loc[i, 'ho'], df.loc[i, 'hi'],
                                                     df.loc[i, 'de'])

                # Step 7
                # Cpo       Cp at exit [J/kg K]
                # Ko        Thermal Conductivity at exit [W/m K]
                # Pe        Peclet number
                # Xo        Quality at exit

                df.loc[i, 'Cpo'] = PropsSI('C', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                               df.loc[i, 'refri'])
                df.loc[i, 'Ko'] = PropsSI('L', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                              df.loc[i, 'refri'])
                df.loc[i, 'Pe'] = df.loc[i, 'dh'] * df.loc[i, 'g'] * df.loc[i, 'Cpo'] / df.loc[i, 'Ko']
                df.loc[i, 'Xo'] = (df.loc[i, 'ho'] - df.loc[i, 'hfo']) / (df.loc[i, 'lam'])

                # Model
                # 1 SZ
                """
                Saha and Zuber (1974)
                """
                if df.loc[i, 'Pe'] > 70000:
                    df.loc[i, 'St_SZ'] = 0.0065
                else:
                    df.loc[i, 'St_SZ'] = 455 / df.loc[i, 'Pe']

                # q_SZ      Heat Flux using the Saha-Zuber correlation [MW/m2]
                df.loc[i, 'q_SZ'] = -df.loc[i, 'g'] * df.loc[i, 'lam'] * df.loc[i, 'Xo'] * df.loc[
                    i, 'St_SZ'] * 10 ** -6
                df.loc[i, 'q_diff_SZ'] = (df.loc[i, 'q_SZ'] - df.loc[i, 'q_guess'])

                # Error analysis
                if df.loc[i, 'q_diff_SZ'] <= 0.01 and df.loc[i, 'q_diff_SZ'] >= -0.01:
                    break
                elif df.loc[i, 'q_diff_SZ'] > 0.01:
                    df.loc[i, 'To'] = df.loc[i, 'To'] + 0.1
                    continue
                elif df.loc[i, 'q_diff_SZ'] < -0.01:
                    df.loc[i, 'To'] = df.loc[i, 'To'] - 0.1
                    continue
            print(
                'Saha and Zuber (1974): {:d}번째 데이터 완료, 최적화는 {:d}번 / Pi_new: {:.4f} / P_diff: {:.2f} / q_guess: {:.4f} / q_SZ: {:.4f} / q_diff_SZ: {:.2f}'
                    .format(i + 1, k, df.loc[i, 'Pi_new'], df.loc[i, 'P_diff'], df.loc[i, 'q_guess'],
                            df.loc[i, 'q_SZ'],
                            df.loc[i, 'q_diff_SZ']))

        # ----------------------------
        # 종료부분 코드
        print("start_time", start_time)
        print("--- %s seconds ---" % (time.time() - start_time))

    def calOfiJeong(self, df):
        # Jeong and Shim (2018) correlation
        print('Jeong and Shim Correlation (2019) OFI analysis')

        start_time = time.time()
        # ------------------------
        # Step 1
        # tsat     Saturation Temperature at P [K]
        # hfo      Saturated liquid Enthalpy at P [J/kg]
        # hgo      Saturated vapor Enthalpy at P [J/kg]
        # lam     Heat of vaporization at P [J/kg]
        # To Exit Temperature [K]

        for i in df.index:
            df.loc[i, 'To'] = df.loc[i, 'Ti'] + 1  # To 의 초기값설정

            for k in range(1, 10000):  # step 2 - 7 반복
                # Step 2
                # ho Enthalpy at exit [J/kg]
                df.loc[i, 'ho'] = PropsSI('H', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                              df.loc[i, 'refri'])

                # Step 3
                # Pi Inlet pressure [bar]
                df.loc[i, 'Pi_new'] = df.loc[i, 'p']

                for j in range(3):
                    df.loc[i, 'Pi_old'] = df.loc[i, 'Pi_new']

                    # Step 4
                    # P_ave     Average pressure [bar]
                    # T_ave     Average Temperature [K]
                    # rho_ave   Density at Average pressure & Temperature [kg/m3]
                    # mu_ave    Viscosity at Average pressure & Temperature [Pa s]
                    # re_ave    reynolds number [-]

                    df.loc[i, 'P_ave'] = 0.5 * (df.loc[i, 'Pi_new'] + df.loc[i, 'p'])
                    df.loc[i, 'T_ave'] = 0.5 * (df.loc[i, 'Ti'] + df.loc[i, 'To'])
                    df.loc[i, 'rho_ave'] = PropsSI('D', 'T', df.loc[i, 'T_ave'], 'P', df.loc[i, 'P_ave'] * 1e5,
                                                       df.loc[i, 'refri'])
                    df.loc[i, 'mu_ave'] = PropsSI('V', 'T', df.loc[i, 'T_ave'], 'P', df.loc[i, 'P_ave'] * 1e5,
                                                      df.loc[i, 'refri'])
                    df.loc[i, 're_ave'] = PhysicalProperty.calRe(self,df.loc[i, 'g'], df.loc[i, 'dh'], df.loc[i, 'mu_ave'])

                    # f_ave Friction factor
                    if df.loc[i, 're_ave'] < 2300:
                        df.loc[i, 'f_ave'] = 4 * (24 / df.loc[i, 're_ave'])
                    elif df.loc[i, 're_ave'] >= 4000:
                        df.loc[i, 'f_ave'] = 4 * (1.2810 ** -3 + 0.1143 * (df.loc[i, 're_ave'] ** (-0.3)))
                    else:
                        df.loc[i, 'f_ave'] = 4 * (5.4 * 10 ** -3 + (2.3 * 1e-8) * (df.loc[i, 're_ave'] ** 0.75))

                    # Step 5
                    # Calculate Pi_new according to flow direction
                    if df.loc[i, 'flow'] == 'Ho':  # in horizontal flow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                    df.loc[i, 'f_ave'] * df.loc[i, 'lh'] / df.loc[i, 'de']) * 0.00001
                    elif df.loc[i, 'flow'] == 'Down':  # in vertical downflow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                    (df.loc[i, 'f_ave'] * df.loc[i, 'lh'] / df.loc[i, 'de'])
                                    - (df.loc[i, 'rho_ave'] * 9.80665 * df.loc[i, 'lh'])) * 0.00001
                    elif df.loc[i, 'flow'] == 'Up':  # in vertical upflow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                    df.loc[i, 'f_ave'] * (df.loc[i, 'lh'] / df.loc[i, 'de'])
                                    + (df.loc[i, 'rho_ave'] * 9.80665 * df.loc[i, 'lh'])) * 0.00001

                    df.loc[i, 'P_diff'] = (df.loc[i, 'Pi_old'] - df.loc[i, 'Pi_new']) * 100 / df.loc[i, 'Pi_old']

                # Step 6
                # hi Enthalpy at inlet [J/kg]
                # q_guess Heat Flux based on heat balance [MW/m2]

                df.loc[i, 'hi'] = PropsSI('H', 'T', df.loc[i, 'Ti'], 'P', df.loc[i, 'Pi_new'] * 1e5,
                                              df.loc[i, 'refri'])
                df.loc[i, 'q_guess'] = PhysicalProperty.calQ(self,df.loc[i, 'doi'], df.loc[i, 'dio'], df.loc[i, 'lh'], df.loc[i, 'g'],
                                                df.loc[i, 'geo'], df.loc[i, 'hsur'], df.loc[i, 'dh'],
                                                df.loc[i, 'ho'], df.loc[i, 'hi'],
                                                df.loc[i, 'de'])

                # Step 7
                # Cpo       Cp at exit [J/kg K]
                # Ko        Thermal Conductivity at exit [W/m K]
                # Pe        Peclet number
                # Xo        Quality at exit

                df.loc[i, 'Cpo'] = PropsSI('C', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                               df.loc[i, 'refri'])
                df.loc[i, 'Ko'] = PropsSI('L', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                              df.loc[i, 'refri'])
                df.loc[i, 'Pe'] = df.loc[i, 'dh'] * df.loc[i, 'g'] * df.loc[i, 'Cpo'] / df.loc[i, 'Ko']
                df.loc[i, 'Xo'] = (df.loc[i, 'ho'] - df.loc[i, 'hfo']) / (df.loc[i, 'lam'])

                # Models
                # 1 Jeong and Shim
                """
                Jeong and Shim (2019)
                """
                if df.loc[i, 'Pe'] > 70000:
                    df.loc[i, 'St_JS'] = 0.15 / (df.loc[i, 'Pe'] ** (0.25))
                else:
                    df.loc[i, 'St_JS'] = 500 / df.loc[i, 'Pe']

                # q_JS      Heat Flux using the Jeong and Shim correlation [MW/m2]
                df.loc[i, 'q_JS'] = -df.loc[i, 'g'] * df.loc[i, 'lam'] * df.loc[i, 'Xo'] * df.loc[
                    i, 'St_JS'] * (10 ** -6)
                df.loc[i, 'q_diff_JS'] = (df.loc[i, 'q_JS'] - df.loc[i, 'q_guess'])

                # Error analysis
                if df.loc[i, 'q_diff_JS'] <= 0.01 and df.loc[i, 'q_diff_JS'] >= -0.01:
                    break
                elif df.loc[i, 'q_diff_JS'] > 0.01:
                    df.loc[i, 'To'] = df.loc[i, 'To'] + 0.1
                    continue
                elif df.loc[i, 'q_diff_JS'] < -0.01:
                    df.loc[i, 'To'] = df.loc[i, 'To'] - 0.1
                    continue

            print(
                'Jeong and Shim (2019): {:d}번째 데이터 완료, 최적화는 {:.2f}번 / Pi_new: {:.4f} / P_diff: {:.2f} / q_guess: {:.4f} / q_JS: {:.4f} / q_diff_JS: {:.2f}'
                .format(i + 1, k, df.loc[i, 'Pi_new'], df.loc[i, 'P_diff'], df.loc[i, 'q_guess'], df.loc[i, 'q_JS'],
                        df.loc[i, 'q_diff_JS']))

        # ----------------------------
        # 종료부분 코드
        print("start_time", start_time)
        print("--- %s seconds ---" % (time.time() - start_time))

    def calOfiWF(self, df):
        # Whittle and Forgan (1967) correlation
        print('Whittle and Forgan Correlation (1967) OFI analysis')
        start_time = time.time()
        # ------------------------
        # Step 1
        # tsat     Saturation Temperature at P [K]
        # hfo      Saturated liquid Enthalpy at P [J/kg]
        # hgo      Saturated vapor Enthalpy at P [J/kg]
        # lam     Heat of vaporization at P [J/kg]
        # To Exit Temperature [K]

        for i in df.index:
            df.loc[i, 'eta'] = 25
            # eta=14+(0.1*P(k)*0.986923)
            df.loc[i, 'R'] = 1 / (1 + (df.loc[i, 'eta'] * df.loc[i, 'dh'] / df.loc[i, 'lh']))
            df.loc[i, 'To'] = df.loc[i, 'Ti'] + df.loc[i, 'R'] * (df.loc[i, 'tsat'] - df.loc[i, 'Ti'])

            for k in range(1, 5000):  # step 2 - 7 반복
                # Step 2
                # ho Enthalpy at exit [J/kg]
                df.loc[i, 'ho'] = PropsSI('H', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                              df.loc[i, 'refri'])

                # Step 3
                # Pi Inlet pressure [bar]
                df.loc[i, 'Pi_new'] = df.loc[i, 'p']

                for j in range(3):
                    df.loc[i, 'Pi_old'] = df.loc[i, 'Pi_new']

                    # Step 4
                    # P_ave     Average pressure [bar]
                    # T_ave     Average Temperature [K]
                    # rho_ave   Density at Average pressure & Temperature [kg/m3]
                    # mu_ave    Viscosity at Average pressure & Temperature [Pa s]
                    # re_ave    reynolds number [-]

                    df.loc[i, 'P_ave'] = 0.5 * (df.loc[i, 'Pi_new'] + df.loc[i, 'p'])
                    df.loc[i, 'T_ave'] = 0.5 * (df.loc[i, 'Ti'] + df.loc[i, 'To'])
                    df.loc[i, 'rho_ave'] = PropsSI('D', 'T', df.loc[i, 'T_ave'], 'P', df.loc[i, 'P_ave'] * 1e5,
                                                       df.loc[i, 'refri'])
                    df.loc[i, 'mu_ave'] = PropsSI('V', 'T', df.loc[i, 'T_ave'], 'P', df.loc[i, 'P_ave'] * 1e5,
                                                      df.loc[i, 'refri'])
                    df.loc[i, 're_ave'] = PhysicalProperty.calRe(self,df.loc[i, 'g'], df.loc[i, 'dh'], df.loc[i, 'mu_ave'])

                    # f_ave Friction factor
                    if df.loc[i, 're_ave'] < 2300:
                        df.loc[i, 'f_ave'] = 4 * (24 / df.loc[i, 're_ave'])
                    elif df.loc[i, 're_ave'] >= 4000:
                        df.loc[i, 'f_ave'] = 4 * (1.2810 ** -3 + 0.1143 * (df.loc[i, 're_ave'] ** (-0.3)))
                    else:
                        df.loc[i, 'f_ave'] = 4 * (5.4 * 10 ** -3 + (2.3 * 1e-8) * (df.loc[i, 're_ave'] ** 0.75))

                    # Step 5
                    if df.loc[i, 'flow'] == 'Ho':  # in horizontal flow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                    df.loc[i, 'f_ave'] * df.loc[i, 'lh'] / df.loc[i, 'de']) * 0.00001
                    elif df.loc[i, 'flow'] == 'Down':  # in vertical downflow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                    (df.loc[i, 'f_ave'] * df.loc[i, 'lh'] / df.loc[i, 'de'])
                                    - (df.loc[i, 'rho_ave'] * 9.80665 * df.loc[i, 'lh'])) * 0.00001
                    elif df.loc[i, 'flow'] == 'Up':  # in vertical upflow
                        df.loc[i, 'Pi_new'] = df.loc[i, 'Pi_old'] + (
                                    df.loc[i, 'f_ave'] * (df.loc[i, 'lh'] / df.loc[i, 'de'])
                                    + (df.loc[i, 'rho_ave'] * 9.80665 * df.loc[i, 'lh'])) * 0.00001

                    df.loc[i, 'P_diff'] = (df.loc[i, 'Pi_old'] - df.loc[i, 'Pi_new']) * 100 / df.loc[i, 'Pi_old']

                # Step 6
                # hi Enthalpy at inlet [J/kg]
                # q_guess Heat Flux based on heat balance [MW/m2]

                df.loc[i, 'hi'] = PropsSI('H', 'T', df.loc[i, 'Ti'], 'P', df.loc[i, 'Pi_new'] * 1e5,
                                              df.loc[i, 'refri'])
                df.loc[i, 'q_guess'] = PhysicalProperty.calQ(self,df.loc[i, 'doi'], df.loc[i, 'dio'], df.loc[i, 'lh'], df.loc[i, 'g'],
                                                df.loc[i, 'geo'], df.loc[i, 'hsur'], df.loc[i, 'dh'],
                                                df.loc[i, 'ho'], df.loc[i, 'hi'],
                                                df.loc[i, 'de'])

                # Step 7
                # Cpo       Cp at exit [J/kg K]
                # Ko        Thermal Conductivity at exit [W/m K]
                # Pe        Peclet number
                # Xo        Quality at exit

                df.loc[i, 'Cpo'] = PropsSI('C', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                               df.loc[i, 'refri'])
                df.loc[i, 'Ko'] = PropsSI('L', 'T', df.loc[i, 'To'], 'P', df.loc[i, 'p'] * 1e5,
                                              df.loc[i, 'refri'])
                df.loc[i, 'Pe'] = df.loc[i, 'dh'] * df.loc[i, 'g'] * df.loc[i, 'Cpo'] / df.loc[i, 'Ko']
                df.loc[i, 'Xo'] = (df.loc[i, 'ho'] - df.loc[i, 'hfo']) / (df.loc[i, 'lam'])

                # Models
                # 1 Whittle and Forgan
                """
                Whittle and Forgan (1967)
                """
                df.loc[i, 'q_WF'] = (df.loc[i, 'dh'] * df.loc[i, 'g'] * (df.loc[i, 'ho'] - df.loc[i, 'hi'])) / 4 / \
                                     df.loc[i, 'lh'] * 10 ** -6
                df.loc[i, 'q_diff_WF'] = (df.loc[i, 'q'] - df.loc[i, 'q_WF']) / df.loc[i, 'q']

                # Error analysis
                if df.loc[i, 'q_diff_WF'] <= 0.1 and df.loc[i, 'q_diff_JS'] >= -0.1:
                    break
                elif df.loc[i, 'q_diff_WF'] > 0.1:
                    df.loc[i, 'To'] = df.loc[i, 'To'] + 0.1
                    continue
                elif df.loc[i, 'q_diff_WF'] < -0.1:
                    df.loc[i, 'To'] = df.loc[i, 'To'] - 0.1
                    continue

            print(
                'Whittle and Forgan (1967): {:d}번째 데이터 완료, 최적화는 {:.2f}번 / Pi_new: {:.4f} / P_diff: {:.2f} / q_guess: {:.4f} / q_WF: {:.4f} / q_diff_WF: {:.2f}'
                .format(i + 1, k, df.loc[i, 'Pi_new'], df.loc[i, 'P_diff'], df.loc[i, 'q_guess'], df.loc[i, 'q_WF'],
                        df.loc[i, 'q_diff_WF']))

        # ----------------------------
        # 종료부분 코드
        print("start_time", start_time)
        print("--- %s seconds ---" % (time.time() - start_time))

    # statistic margin method
    def calMPE(self, y_true, y_pred):
        return np.mean((y_true - y_pred) / y_true)

    def calMSE(self, y_true, y_pred):
        return np.mean(np.square((y_true - y_pred)))

    def calMAPE(self, y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    # The equations for CHF algorithm (Local hypothesis)


