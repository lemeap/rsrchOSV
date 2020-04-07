import numpy as np
import pandas as pd

class PhysicalProperty():
    def __init__(self):
        print("Property_OSV is successfully started.")

    # Dimensionless number
    def calPe(self, dh, g, cpf, kf):  # Peclet number
        Pe = (g * dh * cpf) / kf
        return Pe

    def calSt(self, q, cpf, rhof, v, tosv):  # Stanton number
        St = (q * (10 ** 6)) / (cpf * rhof * v * tosv)
        return St

    def calWe(self, rhof, v, dh, sigma):  # Weber number
        We = rhof * (v ** 2) * dh / sigma
        return We

    def calRe(self, g, dh, muf):  # Reynolds number
        Re = (g * dh) / muf
        return Re

    def calBd(self, rhof, rhov, dh, sigma):  # Bond number
        Bd = (9.8 * (rhof - rhov) * (dh ** 2)) / (sigma)
        return Bd

    def calGr(self, dh, rhof, tosv, muf):
        pass
        #Gr = 9.8*(dh**3)*(rhof**2)*()
        #return Gr

    def calBo_el(self, q, rhof, rhov, sigma, v, lam):  # Boiling number of El-Morshedy
        Ug = 1.53*((sigma*(rhof-rhov))/rhof**2)**0.25
        Bo_el = (q * 10**6 / (rhov * Ug * lam))
        return Bo_el

    def calBo(self,q,lam,g): # Boiling number
        Bo = q*10**6/(lam*g)
        return Bo

    def calGa(self,rhof, dh, muf): # Galileo number == archimedes number
        Ar = (9.8 * rhof * dh ** 3) / muf ** 2
        return Ar

    def calJh(self, q, cpf, rhof, v, tosv, muf, kf ): # Colburn j factor (jH)
        Jh = ((q * (10 ** 6)) / (cpf * rhof * v * tosv))* ((cpf * muf) / kf)**(2/3)
        return Jh

    def calGz(self, dh, lh, re, pr): # Graetz number
        if lh is None:
            Gz = np.nan
        else:
            Gz = (dh/lh) * re * pr
        return Gz

    def calEc(self, v, cpf, tosv): # Eckert number
        Ec = v ** 2 / (cpf * tosv)
        return Ec * 10**6

    def calJa(self, cpf, tosv, lam): # Jakob number
        Ja = cpf * tosv / lam
        return Ja

    def calZ(self, muf, rhof, dh, sigma): # Ohnesorge number
        Z = muf / (rhof * dh * sigma) ** 0.5
        return Z

    def calFr(self, v, dh):  # Lewis number or Froude number
        Fr = (v ** 2) / (9.8 * dh)
        return Fr

    def calCa(self, muf, v, sigma, rhof): # capillary number
        Ca = (muf*v)/(sigma)
        return Ca

    def calCo(self, tosv, rhof, lam, dh, kf, muf): # Condensation number
        Co = (9.8*(rhof**2)*lam*dh**3)/(kf*muf*tosv)
        return Co

    def calPr(self, cpf, muf, kf):  # Prandtl number
        Pr = (cpf * muf) / kf
        return Pr

    def calQratio(self, q, doi, dio, geo, hsur, g, cpf, dtin, lh):
        qq = q * (10 ** 6)
        R_heated_1h = doi * lh
        R_heated_2h = 2 * doi * lh
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio) * lh
        A_heated_2h = (np.pi * (dio + doi)) * lh
        A_flow = (np.pi / 4) * (doi ** 2 - dio ** 2)
        C_heated = (np.pi) * doi * lh
        C_flow = (np.pi / 4) * doi ** 2

        if geo == 'R':
            if hsur == 1:
                Qratio = (qq * R_heated_1h) / (R_flow * g * cpf * dtin)
                return Qratio
            else:
                Qratio = (qq * R_heated_2h) / (R_flow * g * cpf * dtin)
                return Qratio
        elif geo == 'A':
            if hsur == 1:
                Qratio = (qq * A_heated_1h) / (A_flow * g * cpf * dtin)
                return Qratio
            else:
                Qratio = (qq * A_heated_2h) / (A_flow * g * cpf * dtin)
                return Qratio
        else:
            Qratio = (qq * C_heated) / (C_flow * g * cpf * dtin)
            return Qratio
        
    def calXout(self, q, doi, dio, geo, hsur, g, cpf, lam, dtin, lh):
        qq = q * (10 ** 6)
        R_heated_1h = doi * lh
        R_heated_2h = 2 * doi * lh
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio) * lh
        A_heated_2h = (np.pi * (dio + doi)) * lh
        A_flow = (np.pi / 4) * (doi ** 2 - dio ** 2)
        C_heated = (np.pi) * doi * lh
        C_flow = (np.pi / 4) * doi ** 2
        if geo == 'R':
            if hsur == 1: # Lambda [=] J/kg
                xout = - (cpf * dtin) / lam + (qq * R_heated_1h) / (R_flow * g * lam)
                return xout
            else:
                xout = -(cpf * dtin) / lam + (qq * R_heated_2h) / (R_flow * g * lam)
                return xout
        elif geo == 'A':
            if hsur == 1:
                xout = -(cpf * dtin) / lam + (qq * A_heated_1h) / (A_flow * g * lam)
                return xout
            else:
                xout = -(cpf * dtin) / lam + (qq * A_heated_2h) / (A_flow * g * lam)
                return xout
        else:
            xout = -(cpf * dtin) / lam + (qq * C_heated) / (C_flow * g * lam)
            return xout

    def calXi(self, cpf, dtin, lam): # Inlet thermal equilibrium quality
        Xi = - (cpf * dtin) / lam
        return Xi

    def calNu(self, q, dh, kf, tosv):  # Nusselt number
        Nu = ((q * (10 ** 6)) * dh) / (kf * tosv)
        return Nu

    def calGsat(self, q, doi, lh, cpf, dtin, dio, geo, hsur, dh):
        qq = q * (10 ** 6)
        R_heated_1h = doi * lh
        R_heated_2h = 2 * doi * lh
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio) * lh
        A_heated_2h = (np.pi * (dio + doi)) * lh
        A_flow = (np.pi / 4) * (doi ** 2 - dio ** 2)
        C_heated = (np.pi) * doi * lh
        C_flow = (np.pi / 4) * doi ** 2

        if geo == 'R':
            if hsur == 1:
                Gsat = (qq * R_heated_1h) / (R_flow * cpf * dtin)
                return Gsat
            else:
                Gsat = (qq * R_heated_2h) / (R_flow * cpf * dtin)
                return Gsat
        elif geo == 'A':
            if hsur == 1:
                Gsat = (qq * A_heated_1h) / (A_flow * cpf * dtin)
                return Gsat
            else:
                Gsat = (qq * A_heated_2h) / (A_flow * cpf * dtin)
                return Gsat
        else:
            Gsat = (qq * C_heated) / (C_flow * cpf * dtin)
            return Gsat

    def calTin(self, tsat, dtin):
        tin = tsat - 273.15 - dtin
        return tin

    def calDtOSV(self, q, g, cpf, dio, doi, lh, geo, hsur, datap, tosv, tsat, ti):
        qq = q * (10 ** 6)
        R_heated_1h = doi * lh
        R_heated_2h = 2 * doi * lh
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio) * lh
        A_heated_2h = (np.pi * (dio + doi)) * lh
        A_flow = (np.pi / 4) * (doi ** 2 - dio ** 2)
        C_heated = (np.pi) * doi * lh
        C_flow = (np.pi / 4) * doi ** 2

        if datap == 'OSV':
            dTOSV_Cal = tosv
        else:
            if geo == 'R':
                if hsur == 1:
                    dTOSV_Cal = tsat - (ti + ((qq)*R_heated_1h) / (g*cpf*R_flow))
                    return dTOSV_Cal
                else:
                    dTOSV_Cal = tsat - (ti + ((qq)*R_heated_2h) / (g*cpf*R_flow))
                    return dTOSV_Cal
            elif geo == 'A':
                if hsur == 1:
                    dTOSV_Cal = tsat - (ti + ((qq)*A_heated_1h) / (g*cpf*A_flow))
                    return dTOSV_Cal
                else:
                    dTOSV_Cal = tsat - (ti + ((qq)*A_heated_2h) / (g*cpf*A_flow))
                    return dTOSV_Cal
            else:
                dTOSV_Cal = tsat - (ti + ((qq)*C_heated / (g*cpf*C_flow)))
                return dTOSV_Cal

    def calDe(self, doi, dio, geo, hsur, dh):
        R_heated_1h = doi
        R_heated_2h = 2 * doi
        R_flow = doi * dio
        A_heated_1h = (np.pi * dio)
        A_heated_2h = (np.pi * (dio + doi))
        A_heated_3h = (np.pi * doi)
        A_flow = ((np.pi) / 4) * (doi ** 2 - dio ** 2)
        if geo == 'R':
            if hsur == 1:
                De = 4 * R_flow / R_heated_1h
                return De
            else:
                De = 4 * R_flow / R_heated_2h
                return De
        elif geo == 'A':
            if hsur == 1:
                De = 4 * A_flow / A_heated_1h
                return De
            elif hsur == 2:
                De = 4 * A_flow / A_heated_2h
                return De
            else:
                De = 4 * A_flow / A_heated_3h
                return De
        else:
            De = dh
            return De

    def calQ(self, doi, dio, lh, g, geo, hsur, dh, ho, hi, de):
        q_guess = g * (de / (4 * lh)) * (ho - hi) * 1e-6

        # R_heated_1h = doi*lh
        # R_heated_2h = 2*doi*lh
        # R_flow = doi*dio
        # A_heated_1h = (np.pi*dio)*lh
        # A_heated_2h = (np.pi*(dio+doi))*lh
        # A_heated_3h = (np.pi*doi)
        # A_flow = (np.pi/4)*(doi**2-dio**2)
        # C_heated = (np.pi)*doi*lh
        # C_flow = (np.pi/4)*doi**2
        # R_phpw_1h = doi/(2*(doi+dio))
        # R_phpw_2h = doi/(doi+dio)
        # A_phpw_1h = dio/(2*(doi+dio))
        # A_phpw_3h = doi/(doi+dio)
        # param_DD = de/dh

        # if geo == 'R':
        #    if hsur == 1:
        #        q_guess = g*param_DD*(R_flow/R_heated_1h)*(ho-hi)*1e-6
        #    else:
        #        q_guess = g*param_DD*(R_flow/R_heated_2h)*(ho-hi)*1e-6
        # elif geo == 'A':
        #    if hsur == 1:
        #        q_guess = g*param_DD*(A_flow/A_heated_1h)*(ho-hi)*1e-6
        #    elif hsur == 2:
        #        q_guess = g*(A_flow/A_heated_2h)*(ho-hi)*1e-6
        #    else:
        #        q_guess = g*param_DD*(A_flow/A_heated_3h)*(ho-hi)*1e-6
        # else:
        #    q_guess = g*(C_flow/C_heated)*(ho-hi)*1e-6
        return q_guess