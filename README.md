# OSV 모델 개발 연구

1. 목적
본 연구 프로젝트는 약 70년 동안 수집된 void fraction 데이터에 대한 OSV 결정방법과 새로운 예측상관식의 개발이다.
데이터는 약 35편의 논문, 보고서, 초록집 등에서 수집되었으며, 약 3000개의 void fraction profile데이터에서 695개의 데이터가 추출되었다.

2. 새로운 예측상관식의 개발
새로운 예측상관식은 Saha and Zuber (1974) correlation에서 사용된 Stanton number와 Peclet number의 관계성을 차용하여, 새로운 dimensionless number, Weber number를 도입하여 weak bubble detached region과 strong bubble detached region으로 구분하여 각각에 대해 상관식이 개발되었다.

3. 데이터베이스 구성 및 계산 가이드라인
데이터베이스는 PostgreSQL로 local 영역에서 접근할 수 있도록 구성하였으며, 논문에서 수집된 1차 데이터와 SI 단위 환산(SI unit conversion)이 적용된 소수점 6째 자리까지의 데이터가 raw data로 저장된다.
NIST사에서 제공된 REFPROP python module인 CoolProp module로 해당 데이터의 압력값을 토대로 saturation temperature에서의 physical properties(eg. liquid/vapor density, liquid/vapor specific heat, surface tension etc.)이 계산되어 추출된 property table이 PostgreSQL에 만들어진다.
저장된 데이터 DB에서 Python으로 호출되어 원본데이터 훼손없이 row by row 계산이 진행된다(간혹 apply를 사용하여 데이터 1개 단위의 계산과정을 추적할 이유가 없는 데이터는 apply method가 적용).
