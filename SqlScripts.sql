SELECT inet_server_port();
SELECT current_database();
SELECT current_user;
SELECT version();
SELECT current_time;
SELECT date_trunc('second', current_timestamp - pg_postmaster_start_time())
                                      as uptime;

-- CHF database 만들기
-- Rawdata TB 만들기							  
DROP TABLE rawdata_chf_tb;
CREATE TABLE rawdata_chf_tb (
	run_id VARCHAR(10)
	, tb_no INTEGER
	, year_no INTEGER
	, source VARCHAR(100)
	, refri VARCHAR(20)
	, geo VARCHAR(10)
	, flow VARCHAR(10)
	, dir VARCHAR(10)
	, matio VARCHAR(100)
	, matoi VARCHAR(100)
	, hsur VARCHAR(10)
	, doi NUMERIC(15,6)
	, dio NUMERIC(15,6)
	, dh NUMERIC(15,6)
	, gap NUMERIC(15,6)
	, lh NUMERIC(15,6)
	, p NUMERIC(15,6)
	, g NUMERIC(15,6)
	, q NUMERIC(15,6)
	, dtin NUMERIC(15,6)
	, xe NUMERIC(15,6)
);

-- OSV database 만들기
-- Rawdata TB 만들기							  
DROP TABLE rawdata_OSV_tb;
CREATE TABLE rawdata_OSV_tb (
	run_id INTEGER
	, datap VARCHAR(10)
	, source VARCHAR(100)
	, refri VARCHAR(20)
	, geo VARCHAR(10)
	, flow VARCHAR(10)
	, pp VARCHAR(10)
	, doi NUMERIC(15,6)
	, dio NUMERIC(15,6)
	, dh NUMERIC(15,6)
	, gap NUMERIC(15,6)
	, lh NUMERIC(15,6)
	, p NUMERIC(15,6)
	, g NUMERIC(15,6)
	, q NUMERIC(15,6)
	, ti NUMERIC(15,6)
	, hsur VARCHAR(10)
	, xosv NUMERIC(15,6)
	, tosv NUMERIC(15,6)
	, ar NUMERIC(15,6)
	, kf NUMERIC(15,6)
	, kv NUMERIC(15,6)
	, muf NUMERIC(15,12)
	, muv NUMERIC(15,12)
	, tsat NUMERIC(15,6)
	, dtin NUMERIC(15,6)
	, hfo NUMERIC(15,6)
	, hgo NUMERIC(15,6)
	, lam NUMERIC(15,6)
	, rhof NUMERIC(15,6)
	, rhov NUMERIC(15,6)
	, v NUMERIC(15,6)
	, cpf NUMERIC(15,6)
	, cpv NUMERIC(15,6)
	, sigma NUMERIC(15,6)
);

-- OSV result TB 만들기
DROP TABLE res_total_tb;
CREATE TABLE res_total_tb (
	no_nu INTEGER
	, run_id INTEGER
	, datap VARCHAR(10)
	, source VARCHAR(100)
	, refri VARCHAR(20)
	, geo VARCHAR(10)
	, flow VARCHAR(10)
	, pp VARCHAR(10)
	, doi NUMERIC(15,6)
	, dio NUMERIC(15,6)
	, dh NUMERIC(15,6)
	, gap NUMERIC(15,6)
	, lh NUMERIC(15,6)
	, p NUMERIC(15,6)
	, g NUMERIC(15,6)
	, q NUMERIC(15,6)
	, ti NUMERIC(15,6)
	, hsur VARCHAR(10)
	, xosv NUMERIC(15,6)
	, tosv NUMERIC(15,6)
	, ar NUMERIC(15,6)
	, kf NUMERIC(15,6)
	, kv NUMERIC(15,6)
	, muf NUMERIC(15,12)
	, muv NUMERIC(15,12)
	, tsat NUMERIC(15,6)
	, dtin NUMERIC(15,6)
	, hfo NUMERIC(15,6)
	, hgo NUMERIC(15,6)
	, lam NUMERIC(15,6)
	, rhof NUMERIC(15,6)
	, rhov NUMERIC(15,6)
	, v NUMERIC(15,6)
	, cpf NUMERIC(15,6)
	, cpv NUMERIC(15,6)
	, sigma NUMERIC(15,6)
	, de NUMERIC(15,6)
	, pe NUMERIC(15,6)
	, st NUMERIC(15,6)
	, re NUMERIC(15,6)
	, we NUMERIC(15,6)
	, bd NUMERIC(15,6)
	, bo NUMERIC(15,6)
	, bo_el NUMERIC(15,6)
	, ga NUMERIC(15,6)
	, jh NUMERIC(15,6)
	, gz NUMERIC(15,6)
	, ja NUMERIC(15,6)
	, z NUMERIC(15,6)
	, fr NUMERIC(15,6)
	, ca NUMERIC(15,6)
	, co NUMERIC(15,6)
	, pr NUMERIC(15,6)
	, qratio NUMERIC(15,6)
	, nu NUMERIC(15,6)
	, gsat NUMERIC(15,6)
	, dtosv_cal NUMERIC(15,6)
	, dt_js NUMERIC(15,6)
	, dt_sz NUMERIC(15,6)
	, dt_levy NUMERIC(15,6)
	, dt_bowr NUMERIC(15,6)
	, dt_unal NUMERIC(15,6)
	, x_js NUMERIC(15,6)
	, x_sz NUMERIC(15,6)
	, x_levy NUMERIC(15,6)
	, x_bowr NUMERIC(15,6)
	, x_unal NUMERIC(15,6)
	, dt_el NUMERIC(15,6) 
	, dt_msz NUMERIC(15,6)
	, dt_al NUMERIC(15,6)
	, dt_lee NUMERIC(15,6)
	, dt_kennedy NUMERIC(15,6)
	, x_el NUMERIC(15,6)
	, x_msz NUMERIC(15,6)
	, x_al NUMERIC(15,6)
	, x_lee NUMERIC(15,6)
	, x_kennedy NUMERIC(15,6)
);

DROP TABLE rawdata_1;
CREATE TABLE rawdata_1 (
	datap VARCHAR(10)
	, pp VARCHAR(10)
	, run_id VARCHAR(50)
	, source VARCHAR(100)
	, refri VARCHAR(20)
	, geo VARCHAR(10)
	, flow VARCHAR(10)
	, hsur VARCHAR(10)
	, doi NUMERIC(15,6)
	, dio NUMERIC(15,6)
	, dh NUMERIC(15,6)
	, gap NUMERIC(15,6)
	, lh NUMERIC(15,6)
	, ar NUMERIC(15,6)
	, ti NUMERIC(15,6)
	, p NUMERIC(15,6)
	, g NUMERIC(15,6)
	, q NUMERIC(15,6)	
	, xosv NUMERIC(15,6)
	, tosv NUMERIC(15,6)	
	, alpha VARCHAR(2000)
	, xeq VARCHAR(2000)
	, tsat NUMERIC(15,6)
	, rhof NUMERIC(15,6)
	, rhov NUMERIC(15,6)
	, cpf NUMERIC(15,6)
	, cpv NUMERIC(15,6)
	, lam NUMERIC(15,6)
	, kf NUMERIC(15,6)
	, kv NUMERIC(15,6)
	, muf NUMERIC(15,12)
	, muv NUMERIC(15,12)
	, sigma NUMERIC(15,6)
);

-- 10개 범위를 나누는 param TB 만들기 (quantile 기준)
DROP TABLE dimnsl_param_quan_tb;
CREATE TABLE dimnsl_param_quan_tb AS (
SELECT T1.index
	, CASE
		WHEN T2.doi < 0.1 THEN 1
		WHEN T2.doi BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.doi BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.doi BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.doi BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.doi BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.doi BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.doi BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.doi BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_doi
	, CASE
		WHEN T2.dio < 0.1 THEN 1
		WHEN T2.dio BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.dio BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.dio BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.dio BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.dio BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.dio BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.dio BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.dio BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_dio
	, CASE
		WHEN T2.dh < 0.1 THEN 1
		WHEN T2.dh BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.dh BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.dh BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.dh BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.dh BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.dh BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.dh BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.dh BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_dh
	, CASE
		WHEN T2.gap < 0.1 THEN 1
		WHEN T2.gap BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.gap BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.gap BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.gap BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.gap BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.gap BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.gap BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.gap BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_gap
	, CASE
		WHEN T2.lh < 0.1 THEN 1
		WHEN T2.lh BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.lh BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.lh BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.lh BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.lh BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.lh BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.lh BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.lh BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_lh
	, CASE
		WHEN T2.p < 0.1 THEN 1
		WHEN T2.p BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.p BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.p BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.p BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.p BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.p BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.p BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.p BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_p
	, CASE
		WHEN T2.g < 0.1 THEN 1
		WHEN T2.g BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.g BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.g BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.g BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.g BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.g BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.g BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.g BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_g
	, CASE
		WHEN T2.q < 0.1 THEN 1
		WHEN T2.q BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.q BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.q BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.q BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.q BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.q BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.q BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.q BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_q
	, CASE
		WHEN T2.ti < 0.1 THEN 1
		WHEN T2.ti BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.ti BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.ti BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.ti BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.ti BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.ti BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.ti BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.ti BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_ti
	, CASE
		WHEN T2.xosv < 0.1 THEN 1
		WHEN T2.xosv BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.xosv BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.xosv BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.xosv BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.xosv BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.xosv BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.xosv BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.xosv BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_xosv
	, CASE
		WHEN T2.tosv < 0.1 THEN 1
		WHEN T2.tosv BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.tosv BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.tosv BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.tosv BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.tosv BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.tosv BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.tosv BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.tosv BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_tosv
	, CASE
		WHEN T2.ar < 0.1 THEN 1
		WHEN T2.ar BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.ar BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.ar BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.ar BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.ar BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.ar BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.ar BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.ar BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_ar
	, CASE
		WHEN T2.v < 0.1 THEN 1
		WHEN T2.v BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.v BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.v BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.v BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.v BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.v BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.v BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.v BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_v
	, CASE
		WHEN T2.de < 0.1 THEN 1
		WHEN T2.de BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.de BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.de BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.de BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.de BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.de BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.de BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.de BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_de
	, CASE
		WHEN T2.pe < 0.1 THEN 1
		WHEN T2.pe BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.pe BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.pe BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.pe BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.pe BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.pe BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.pe BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.pe BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_pe
	, CASE
		WHEN T2.st < 0.1 THEN 1
		WHEN T2.st BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.st BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.st BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.st BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.st BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.st BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.st BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.st BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_st
	, CASE
		WHEN T2.re < 0.1 THEN 1
		WHEN T2.re BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.re BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.re BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.re BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.re BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.re BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.re BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.re BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_re
	, CASE
		WHEN T2.we < 0.1 THEN 1
		WHEN T2.we BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.we BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.we BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.we BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.we BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.we BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.we BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.we BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_we
	, CASE
		WHEN T2.bd < 0.1 THEN 1
		WHEN T2.bd BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.bd BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.bd BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.bd BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.bd BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.bd BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.bd BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.bd BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_bd
	, CASE
		WHEN T2.bo < 0.1 THEN 1
		WHEN T2.bo BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.bo BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.bo BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.bo BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.bo BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.bo BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.bo BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.bo BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_bo
	, CASE
		WHEN T2.ca < 0.1 THEN 1
		WHEN T2.ca BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.ca BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.ca BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.ca BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.ca BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.ca BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.ca BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.ca BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_ca
	, CASE
		WHEN T2.pr < 0.1 THEN 1
		WHEN T2.pr BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.pr BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.pr BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.pr BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.pr BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.pr BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.pr BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.pr BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_pr
	, CASE
		WHEN T2.nu < 0.1 THEN 1
		WHEN T2.nu BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.nu BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.nu BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.nu BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.nu BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.nu BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.nu BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.nu BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_nu
	, CASE
		WHEN T2.ec < 0.1 THEN 1
		WHEN T2.ec BETWEEN 0.1 AND 0.2 THEN 2
		WHEN T2.ec BETWEEN 0.2 AND 0.3 THEN 3
		WHEN T2.ec BETWEEN 0.3 AND 0.4 THEN 4
		WHEN T2.ec BETWEEN 0.4 AND 0.5 THEN 5
		WHEN T2.ec BETWEEN 0.5 AND 0.6 THEN 6
		WHEN T2.ec BETWEEN 0.6 AND 0.7 THEN 7
		WHEN T2.ec BETWEEN 0.7 AND 0.8 THEN 8
		WHEN T2.ec BETWEEN 0.8 AND 0.9 THEN 9
	ELSE 10
	END AS param_ec
FROM prop_osv_tb T1
INNER JOIN osv_quan_tb T2
ON T1.index = T2.index
INNER JOIN rmse_osv_tb T3
ON T2.index = T3.index
WHERE T1.xosv < 0
AND ABS(T3.rmse_sz) < 0.6
ORDER BY T1.index
);

-- dimnsl_param_minmax_tb와 prop_osv_Tb를 연결 (quantile 기준)
DROP TABLE dimnsl_param_quan_prop_tb;
CREATE TABLE dimnsl_param_quan_prop_tb AS (
SELECT T1.*
	, T2.param_doi
	, T2.param_dio
	, T2.param_dh
	, T2.param_gap
	, T2.param_lh
	, T2.param_p
	, T2.param_g
	, T2.param_q
	, T2.param_ti
	, T2.param_ar
	, T2.param_v
	, T2.param_de
	, T2.param_pe
	, T2.param_st
	, T2.param_re
	, T2.param_we
	, T2.param_bd
	, T2.param_bo
	, T2.param_ca
	, T2.param_pr
	, T2.param_nu
FROM (SELECT a.*, b.source, b.refri, b.flow, b.geo, b.we AS real_we
												  , b.re AS real_re
												  , b.ca AS real_ca
												  , b.nu AS real_nu
												  , b.st AS real_st
	  FROM osv_quan_tb a
	  INNER JOIN prop_osv_tb b
	  ON a.index = b.index) T1
INNER JOIN dimnsl_param_quan_tb T2
ON T1.index = T2.index
ORDER BY T1.index
);

-- quantile range 뽑기
DISTINCT CAST(MAX(b.p) OVER (PARTITION BY a.param_p) AS NUMERIC(10,2)) AS max_p, a.param_p
	 , DISTINCT CAST(MAX(b.dh) OVER (PARTITION BY a.param_dh) AS NUMERIC(10,2)) AS max_dh
	 , DISTINCT CAST(MAX(b.ga) OVER (PARTITION BY a.param_ga) AS NUMERIC(10,2)) AS max_ga
	 , DISTINCT CAST(MAX(b.lh) OVER (PARTITION BY a.param_lh) AS NUMERIC(10,2)) AS max_lh
	 , DISTINCT CAST(MAX(b.p) OVER (PARTITION BY a.param_p) AS NUMERIC(10,2)) AS max_p
	 , DISTINCT CAST(MAX(b.g) OVER (PARTITION BY a.param_g) AS NUMERIC(10,2)) AS max_g
	 , DISTINCT CAST(MAX(b.q) OVER (PARTITION BY a.param_q) AS NUMERIC(10,2)) AS max_q
	 , DISTINCT CAST(MAX(b.ar) OVER (PARTITION BY a.param_ar) AS NUMERIC(10,2)) AS max_ar
	 , DISTINCT CAST(MAX(b.v) OVER (PARTITION BY a.param_v) AS NUMERIC(10,2)) AS max_v
	 , DISTINCT CAST(MAX(b.de) OVER (PARTITION BY a.param_de) AS NUMERIC(10,2)) AS max_de
	 , DISTINCT CAST(MAX(b.pe) OVER (PARTITION BY a.param_pe) AS NUMERIC(10,2)) AS max_pe
	 , DISTINCT CAST(MAX(b.st) OVER (PARTITION BY a.param_st) AS NUMERIC(10,2)) AS max_st
	 , DISTINCT CAST(MAX(b.re) OVER (PARTITION BY a.param_re) AS NUMERIC(10,2)) AS max_re
	 , DISTINCT CAST(MAX(b.we) OVER (PARTITION BY a.param_we) AS NUMERIC(10,2)) AS max_we
	 , DISTINCT CAST(MAX(b.ca) OVER (PARTITION BY a.param_ca) AS NUMERIC(10,2)) AS max_ca
	 , DISTINCT CAST(MAX(b.bo) OVER (PARTITION BY a.param_bo) AS NUMERIC(10,2)) AS max_bo
	 , DISTINCT CAST(MAX(b.fr) OVER (PARTITION BY a.param_fr) AS NUMERIC(10,2)) AS max_fr
	 , DISTINCT CAST(MAX(b.bd) OVER (PARTITION BY a.param_bd) AS NUMERIC(10,2)) AS max_bd
	 , DISTINCT CAST(MAX(b.co) OVER (PARTITION BY a.param_co) AS NUMERIC(10,2)) AS max_co
	 , DISTINCT CAST(MAX(b.pr) OVER (PARTITION BY a.param_pr) AS NUMERIC(10,2)) AS max_pr
	 , DISTINCT CAST(MAX(b.nu) OVER (PARTITION BY a.param_nu) AS NUMERIC(10,2)) AS max_nu
	 , DISTINCT CAST(MAX(b.ga) OVER (PARTITION BY a.param_ga) AS NUMERIC(10,2)) AS max_ga
	 , DISTINCT CAST(MAX(b.jh) OVER (PARTITION BY a.param_jh) AS NUMERIC(10,2)) AS max_jh
	 , DISTINCT CAST(MAX(b.gz) OVER (PARTITION BY a.param_gz) AS NUMERIC(10,2)) AS max_gz
	 , DISTINCT CAST(MAX(b.ja) OVER (PARTITION BY a.param_ja) AS NUMERIC(10,2)) AS max_ja
	 , DISTINCT CAST(MAX(b.z) OVER (PARTITION BY a.param_z) AS NUMERIC(10,2)) AS max_z 
FROM dimnsl_param_quan_prop_tb a
INNER JOIN prop_osv_tb b
ON a.index = b.index
ORDER BY a.param_nu
; -- 하나씩 해야 한다. 일단 이렇게라도..


-- TREE OSV 분석 테이블 만들기
DROP TABLE tree_osv_tb;
CREATE TABLE tree_osv_tb AS (
SELECT a.run_id, a.source, a.xosv, a.rmse_sz, a.sol, b.re, b.pe, b.ca, b.st, b.geo, b.refri, a.tosv
	, CAST(SPLIT_PART(b.xeq,'|',1) AS NUMERIC(10,4))AS stxeq
	, CAST(SPLIT_PART(b.alpha,'|',1) AS NUMERIC(10,4))AS stalpha
	, b.we, b.bo, b.pr, a."tstXeq" AS tstxeq,
	a.rmse_js, b."serizawaXeq" as serizawaxeq, b."xMartin" as xmartin
FROM rmse_osv_tb a
INNER JOIN prop_osv_tb b
ON a.index = b.index
);


SELECT SQRT(AVG(rmse_js*rmse_js)) AS rmse_js	 
	 , SQRT(AVG(rmse_sz*rmse_sz)) AS rmse_sz
	 , SQRT(AVG(rmse_levy*rmse_levy)) AS rmse_levy
	 , SQRT(AVG(rmse_bowr*rmse_bowr)) AS rmse_bowr
	 , SQRT(AVG(rmse_unal*rmse_unal)) AS rmse_unal
	 , SQRT(AVG(rmse_griffith*rmse_griffith)) AS rmse_griffith
	 , SQRT(AVG(rmse_hancox*rmse_hancox)) AS rmse_hancox
 	 , SQRT(AVG(rmse_ha2005*rmse_ha2005)) AS rmse_ha2005
	 , SQRT(AVG(rmse_ha2018*rmse_ha2018)) AS rmse_ha2018
	 , SQRT(AVG(rmse_sekoguchi*rmse_sekoguchi)) AS rmse_sekoguchi
	 , SQRT(AVG(rmse_costa*rmse_costa)) AS rmse_costa
	 , COUNT(*)
FROM rmse_osv_tb
WHERE ABS(rmse_js) < 0.6;

-- Jeong and Shim (2020) 508, -0.0142, 0.2176
SELECT COUNT(*)      , CAST(AVG(rmse_js) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_js,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
		AND ABS(rmse_js) < 0.5;

-- Saha and Zuber (1974) 386, -0.2148, 0.3353
SELECT COUNT(*)      , CAST(AVG(rmse_sz) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_sz,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    --AND refri = 'Water'
		AND p BETWEEN 1 AND 138
		AND g BETWEEN 102 AND 2818
	    AND q BETWEEN 0.01 AND 1.91
		AND ABS(rmse_js) < 0.5
;


-- Griffith et al.(1958) 15, 0.7117, 0.7146,
SELECT COUNT(*)      , CAST(AVG(rmse_griffith) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_griffith,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 35 AND 103
		AND v BETWEEN 6 AND 9
	    AND q BETWEEN 0.2 AND 4.73
		AND ABS(rmse_js) < 0.5
;
	
-- Bowring (1960) 98, 0.4166, 0.4667
SELECT COUNT(*)      , CAST(AVG(rmse_bowr) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_bowr,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND q > 0.2
	    AND v > 2
	    AND p BETWEEN 1 AND 140
	    AND refri = 'Water'
		AND ABS(rmse_js) < 0.5
;

-- Levy (1967) 158, 0.1202, 0.3017
SELECT COUNT(*)      , CAST(AVG(rmse_levy) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_levy,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 4 AND 138
		AND g BETWEEN 130 AND 1420
	    AND q BETWEEN 0.24 AND 1.91
		AND ABS(rmse_js) < 0.5
;

-- Dix (1971), 46, 0.0833, 0.2050
SELECT COUNT(*)      , CAST(AVG(rmse_dix) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_dix,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'R114'
		AND ABS(rmse_js) < 0.5
;

-- Hancox and Nicoll (1971), 118, -0.3209, 0.9862
SELECT COUNT(*)      , CAST(AVG(rmse_hancox) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_hancox,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 11 AND 138
		AND v BETWEEN 0.6 AND 5.5
	    AND q BETWEEN 0.5 AND 1.93
;

-- Costa (1960), 36, 0.0173, 0.0725
SELECT COUNT(*)      , CAST(AVG(rmse_costa) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_costa,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 1 AND 5
		AND g BETWEEN 3000 AND 7500
	    AND q BETWEEN 1 AND 4
		AND ABS(rmse_js) < 0.5
;

-- Unal (1975), 317, -0.073, 0.4230
SELECT COUNT(*)      , CAST(AVG(rmse_unal) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_unal,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri IN ('Water', 'R22')
		AND p BETWEEN 1 AND 160
		AND g BETWEEN 132 AND 2818
	    AND q BETWEEN 0.02 AND 1.92
;

-- Sekoguchi (1980), 346, -1.8976, 2.5269
SELECT COUNT(*)      , CAST(AVG(rmse_sekoguchi) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_sekoguchi,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 1 AND 140
		AND g BETWEEN 130 AND 5100
	    AND q BETWEEN 0.18 AND 3.26
		AND ABS(rmse_js) < 0.5
;

-- Kalitvianski (2000), 77, 0.7648, 0.7668
SELECT COUNT(*)      , CAST(AVG(rmse_kal) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_kal,2))) AS NUMERIC(10,4) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 44 AND 110
		AND pe BETWEEN 32000 AND 311000
		AND ABS(rmse_js) < 0.5
;

-- Park (2004), 36, 0.9995, 0.9995
SELECT COUNT(*)      , CAST(AVG(rmse_psz) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_psz,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND pe > 200000
		AND ABS(rmse_js) < 0.5
;

-- Ha (2005), 383, -0.2549, 0.3763
SELECT COUNT(*)      , CAST(AVG(rmse_ha2005) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_ha2005,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND pe BETWEEN 5000 AND 345000
		AND ABS(rmse_js) < 0.5
;

-- MSZ (2013), 18, -0.1051, 0.1810
SELECT COUNT(*)      , CAST(AVG(rmse_msz) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_msz,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 7 AND 10
		AND g BETWEEN 150 AND 600
	    AND q BETWEEN 0.1 AND 0.8
		AND ABS(rmse_js) < 0.5
;

-- Ha (2018), 204, -0.0084, 0.6419
SELECT COUNT(*)      , CAST(AVG(rmse_ha2005) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_ha2005,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND pe BETWEEN 3600 AND 70000
		AND ABS(rmse_js) < 0.5
;