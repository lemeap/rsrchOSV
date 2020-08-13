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


DROP TABLE res_osv_tb;
CREATE TABLE res_osv_tb AS (
WITH a AS (
	SELECT *
	FROM rmse_osv_tb
	WHERE xosv IS NOT NULL -- 88개 데이터 제거 / 602
	AND xosv < 0 -- 7개 데이터 제거 / 595
	AND xeq1 IS NOT NULL -- 246개 데이터 제거 / 349
	AND geo = 'R' -- Rectangular channel / 146
	AND rmse_sz > -0.85 -- RMSE_sz 0.6보다 큰 것만 남김. / 73
	AND rmse_sz < 0.6
	UNION
	SELECT *
	FROM rmse_osv_tb
	WHERE xosv IS NOT NULL -- 88개 데이터 제거 / 602
	AND xosv < 0 -- 7개 데이터 제거 / 595
	AND xeq1 IS NOT NULL -- 246개 데이터 제거 / 349
	AND geo != 'R' -- Rectangular channel / 146
	AND rmse_sz > -0.8 -- RMSE_sz 0.6보다 큰 것만 남김. / 73
	AND rmse_sz < 0.55
	ORDER BY index ASC
	-- Total 276
), tbb AS (
	SELECT *
	FROM rmse_osv_tb
	WHERE xosv IS NOT NULL -- 88개 데이터 제거 / 602
	AND xosv < 0 -- 7개 데이터 제거 / 595
	AND xeq1 IS NULL
) SELECT b.*
FROM a a
INNER JOIN prop_osv_tb b
ON a.index = b.index
UNION
SELECT b.*
FROM tbb c
INNER JOIN prop_osv_tb b
ON c.index = b.index
ORDER BY index ASC);

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
FROM res_osv_tb T1
INNER JOIN osv_quan_tb T2
ON T1.index = T2.index
INNER JOIN rmse_osv_tb T3
ON T2.index = T3.index
WHERE T1.xosv < 0
--AND ABS(T3.rmse_sz) < 0.6
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
	  INNER JOIN res_osv_tb b
	  ON a.index = b.index) T1
INNER JOIN dimnsl_param_quan_tb T2
ON T1.index = T2.index
ORDER BY T1.index
);

-- Result data range 추출하기
SELECT source, count(*), refri, geo
	, CAST(MIN(dh) AS NUMERIC(10,4)) AS min_dh
	, CAST(MAX(dh) AS NUMERIC(10,4)) AS max_dh
	, CAST(MIN(p) AS NUMERIC(10,2)) AS min_p
	, CAST(MAX(p) AS NUMERIC(10,2)) AS max_p
	, CAST(MIN(g) AS NUMERIC(10,2)) AS min_g
	, CAST(MAX(g) AS NUMERIC(10,2)) AS max_g
	, CAST(MIN(q) AS NUMERIC(10,2)) AS min_q
	, CAST(MAX(q) AS NUMERIC(10,2)) AS max_q
	, CAST(MIN(dtin) AS NUMERIC(10,2)) AS min_dtin
	, CAST(MAX(dtin) AS NUMERIC(10,2)) AS max_dtin	
FROM res_osv_tb
GROUP BY source, refri, geo
ORDER BY source, refri, geo;

-- 수렴하지 않은 데이터 분석 (Void fraction profile 그리기 위한 데이터값 추출)
WITH a AS (
	SELECT index, run_id, source, refri,geo, hsur, dh, lh, ar, p, g, q, dtin, alpha,xeq, "serizawaXeq", "martinXeq", "staubXeq"
	FROM prop_osv_tb
	WHERE "serizawaXeq" IS NOT NULL
	AND dtin IS NOT NULL
	EXCEPT
	SELECT index, run_id, source, refri,geo, hsur, dh, lh, ar, p, g, q, dtin, alpha,xeq, "serizawaXeq", "martinXeq", "staubXeq"
	FROM res_osv_tb
	WHERE "serizawaXeq" IS NOT NULL
	AND dtin IS NOT NULL
	ORDER BY p DESC)
SELECT a.*, b.x_sz, b.rmse_sz
FROM a a
INNER JOIN rmse_osv_tb b
ON a.index = b.index;

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


-- MPE, RMSPE 계산하기
SELECT CAST(SQRT(AVG(rmse_griffith*rmse_griffith)) AS NUMERIC(10,4)) AS rmse_griffith
	 , CAST(SQRT(AVG(rmse_bowr*rmse_bowr)) AS NUMERIC(10,4)) AS rmse_bowr
	 , CAST(SQRT(AVG(rmse_costa*rmse_costa)) AS NUMERIC(10,4)) AS rmse_costa
	 , CAST(SQRT(AVG(rmse_levy*rmse_levy)) AS NUMERIC(10,4)) AS rmse_levy
	 , CAST(SQRT(AVG(rmse_dix*rmse_dix)) AS NUMERIC(10,4)) AS rmse_dix
	 , CAST(SQRT(AVG(rmse_hancox*rmse_hancox)) AS NUMERIC(10,4)) AS rmse_hancox
	 , CAST(SQRT(AVG(rmse_sz*rmse_sz)) AS NUMERIC(10,4)) AS rmse_sz	 
	 , CAST(SQRT(AVG(rmse_unal*rmse_unal)) AS NUMERIC(10,4)) AS rmse_unal
	 , CAST(SQRT(AVG(rmse_sekoguchi*rmse_sekoguchi)) AS NUMERIC(10,4)) AS rmse_sekoguchi
	 , CAST(SQRT(AVG(rmse_kal*rmse_kal)) AS NUMERIC(10,4)) AS rmse_kal
 	 , CAST(SQRT(AVG(rmse_ha2005*rmse_ha2005)) AS NUMERIC(10,4)) AS rmse_ha2005
	 , CAST(SQRT(AVG(rmse_msz*rmse_msz)) AS NUMERIC(10,4)) AS rmse_msz
	 , CAST(SQRT(AVG(rmse_ha2018*rmse_ha2018)) AS NUMERIC(10,4)) AS rmse_ha2018
	 , CAST(SQRT(AVG(rmse_js*rmse_js)) AS NUMERIC(10,4)) AS rmse_js
	 
	 , CAST(AVG(rmse_griffith) AS NUMERIC(10,4))   AS me_griffith
	 , CAST(AVG(rmse_bowr) AS NUMERIC(10,4))       AS me_bowr
	 , CAST(AVG(rmse_costa) AS NUMERIC(10,4))      AS me_costa
	 , CAST(AVG(rmse_levy) AS NUMERIC(10,4))       AS me_levy
	 , CAST(AVG(rmse_dix) AS NUMERIC(10,4))        AS me_dix
	 , CAST(AVG(rmse_hancox) AS NUMERIC(10,4))     AS me_hancox
	 , CAST(AVG(rmse_sz) AS NUMERIC(10,4))         AS me_sz	 
	 , CAST(AVG(rmse_unal) AS NUMERIC(10,4))       AS me_unal
	 , CAST(AVG(rmse_sekoguchi) AS NUMERIC(10,4))  AS me_sekoguchi
	 , CAST(AVG(rmse_kal) AS NUMERIC(10,4))        AS me_kal
 	 , CAST(AVG(rmse_ha2005) AS NUMERIC(10,4))     AS me_ha2005
	 , CAST(AVG(rmse_msz) AS NUMERIC(10,4))        AS me_msz
	 , CAST(AVG(rmse_ha2018) AS NUMERIC(10,4))     AS me_ha2018
	 , CAST(AVG(rmse_js) AS NUMERIC(10,4))         AS me_js
FROM rmse_osv_tb a
INNER JOIN res_osv_tb b
ON a.index = b.index;

-- Quantile range에 따른 개별 MPE, RMSPE 계산 값
SELECT param_we
	 , COUNT(*)
	 , CAST(SQRT(AVG(rmse_griffith*rmse_griffith)) AS NUMERIC(10,4)) AS rmse_griffith
	 , CAST(SQRT(AVG(rmse_bowr*rmse_bowr)) AS NUMERIC(10,4)) AS rmse_bowr
	 , CAST(SQRT(AVG(rmse_costa*rmse_costa)) AS NUMERIC(10,4)) AS rmse_costa
	 , CAST(SQRT(AVG(rmse_levy*rmse_levy)) AS NUMERIC(10,4)) AS rmse_levy
	 , CAST(SQRT(AVG(rmse_dix*rmse_dix)) AS NUMERIC(10,4)) AS rmse_dix
	 , CAST(SQRT(AVG(rmse_hancox*rmse_hancox)) AS NUMERIC(10,4)) AS rmse_hancox
	 , CAST(SQRT(AVG(rmse_sz*rmse_sz)) AS NUMERIC(10,4)) AS rmse_sz	 
	 , CAST(SQRT(AVG(rmse_unal*rmse_unal)) AS NUMERIC(10,4)) AS rmse_unal
	 , CAST(SQRT(AVG(rmse_sekoguchi*rmse_sekoguchi)) AS NUMERIC(10,4)) AS rmse_sekoguchi
	 , CAST(SQRT(AVG(rmse_kal*rmse_kal)) AS NUMERIC(10,4)) AS rmse_kal
 	 , CAST(SQRT(AVG(rmse_ha2005*rmse_ha2005)) AS NUMERIC(10,4)) AS rmse_ha2005
	 , CAST(SQRT(AVG(rmse_msz*rmse_msz)) AS NUMERIC(10,4)) AS rmse_msz
	 , CAST(SQRT(AVG(rmse_ha2018*rmse_ha2018)) AS NUMERIC(10,4)) AS rmse_ha2018
	 , CAST(SQRT(AVG(rmse_js*rmse_js)) AS NUMERIC(10,4)) AS rmse_js
	 
	 , CAST(AVG(rmse_griffith) AS NUMERIC(10,4))   AS me_griffith
	 , CAST(AVG(rmse_bowr) AS NUMERIC(10,4))       AS me_bowr
	 , CAST(AVG(rmse_costa) AS NUMERIC(10,4))      AS me_costa
	 , CAST(AVG(rmse_levy) AS NUMERIC(10,4))       AS me_levy
	 , CAST(AVG(rmse_dix) AS NUMERIC(10,4))        AS me_dix
	 , CAST(AVG(rmse_hancox) AS NUMERIC(10,4))     AS me_hancox
	 , CAST(AVG(rmse_sz) AS NUMERIC(10,4))         AS me_sz	 
	 , CAST(AVG(rmse_unal) AS NUMERIC(10,4))       AS me_unal
	 , CAST(AVG(rmse_sekoguchi) AS NUMERIC(10,4))  AS me_sekoguchi
	 , CAST(AVG(rmse_kal) AS NUMERIC(10,4))        AS me_kal
 	 , CAST(AVG(rmse_ha2005) AS NUMERIC(10,4))     AS me_ha2005
	 , CAST(AVG(rmse_msz) AS NUMERIC(10,4))        AS me_msz
	 , CAST(AVG(rmse_ha2018) AS NUMERIC(10,4))     AS me_ha2018
	 , CAST(AVG(rmse_js) AS NUMERIC(10,4))         AS me_js
FROM rmse_osv_tb a
INNER JOIN res_osv_tb b
ON a.index = b.index
INNER JOIN dimnsl_param_quan_prop_tb c
ON b.index = c.index
GROUP BY param_we
ORDER BY param_we ASC;

-- Jeong and Shim (2020) 501, 0.14, 29.36
SELECT COUNT(*)      , CAST(AVG(rmse_js) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_js,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
		INNER JOIN res_osv_tb b
		ON a.index = b.index
		group by source;

-- Griffith et al.(1958) 44, 64.37, 65.37
SELECT COUNT(*)      , CAST(AVG(rmse_griffith) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_griffith,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 35 AND 103
		AND v BETWEEN 3 AND 9
	    AND q BETWEEN 0.2 AND 4.73
;

-- Bowring (1960) 149, 49.59, 55.01
SELECT COUNT(*)      , CAST(AVG(rmse_bowr) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_bowr,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND q > 0.2
	    AND v > 2
	    AND p BETWEEN 1 AND 140
	    AND refri = 'Water'
;

-- Costa (1960), 36, 1.73, 7.25
SELECT COUNT(*)      , CAST(AVG(rmse_costa) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_costa,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN prop_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 1 AND 5
		AND g BETWEEN 3000 AND 7500
	    AND q BETWEEN 1 AND 4
;

-- Levy (1967) 131, 29.34, 41.25
SELECT COUNT(*)      , CAST(AVG(rmse_levy) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_levy,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 4 AND 138
		AND g BETWEEN 130 AND 1420
	    AND q BETWEEN 0.24 AND 1.91
;


-- Dix (1971), 46, 5.32, 20.00
SELECT COUNT(*)      , CAST(AVG(rmse_dix) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_dix,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'R114'
;


-- Hancox and Nicoll (1971), 99, -22.31, 48.12
SELECT COUNT(*)      , CAST(AVG(rmse_hancox) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_hancox,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 11 AND 138
		AND v BETWEEN 0.6 AND 5.5
	    AND q BETWEEN 0.5 AND 1.93
;

-- Saha and Zuber (1974) 344, -10.58, 34.91
SELECT COUNT(*)      , CAST(AVG(rmse_sz) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_sz,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    --AND refri = 'Water'
		AND p BETWEEN 1 AND 138
		AND g BETWEEN 102 AND 2818
	    AND q BETWEEN 0.01 AND 1.91
;

-- Unal (1975), 282, 6.32, 39.59
SELECT COUNT(*)      , CAST(AVG(rmse_unal) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_unal,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri IN ('Water', 'R22')
		AND p BETWEEN 1 AND 160
		AND g BETWEEN 132 AND 2818
	    AND q BETWEEN 0.02 AND 1.92
;

-- Sekoguchi (1980), 326, -136.2, 194.83
SELECT COUNT(*)      , CAST(AVG(rmse_sekoguchi) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_sekoguchi,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 1 AND 140
		AND g BETWEEN 130 AND 5100
	    AND q BETWEEN 0.18 AND 3.26
;

-- Kalitvianski (2000), 79, 76.55, 76.78
SELECT COUNT(*)      , CAST(AVG(rmse_kal) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_kal,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 44 AND 110
		AND pe BETWEEN 32000 AND 311000
;

-- Ha (2005), 339, -15.12, 38.97
SELECT COUNT(*)      , CAST(AVG(rmse_ha2005) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_ha2005,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND pe BETWEEN 5000 AND 345000
;

-- MSZ (2013), 18, 24.19, 50.87
SELECT COUNT(*)      , CAST(AVG(rmse_msz) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_msz,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND p BETWEEN 7 AND 10
		AND g BETWEEN 150 AND 600
	    AND q BETWEEN 0.1 AND 0.8
;

- Ha (2018), 167, -7.27, 67.10
SELECT COUNT(*)      , CAST(AVG(rmse_ha2005) AS NUMERIC(10,4)) * 100 AS me
		  , CAST(SQRT(AVG(POWER(rmse_ha2005,2))) AS NUMERIC(10,4)) * 100 AS rmse
	   	FROM rmse_osv_tb a
	    INNER JOIN res_osv_tb b
	    ON a.index = b.index
	    AND refri = 'Water'
		AND pe BETWEEN 3600 AND 70000
;