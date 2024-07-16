"=== Passagens na Dutra ============================================="
SELECT dutra_location.state, dutra_location.km, dutra_location.direction, dutra_location.extra, tag.alias, count(distinct datapoint.appinstance_id) AS 'nro_smartphones', 
	   (24 * 60) / count(distinct datapoint.appinstance_id) AS esp_leit_min, 
	   avg(timestampdiff(SECOND, datapoint.datetime, datapoint.create_time)) AS delay_envio, 
	   (6 * 60) / sum(CASE WHEN datapoint.datetime < date(now() - interval 24 hour) + interval 9 hour THEN 1 ELSE 0 END) AS  esp_00h_06h, 
	   (6 * 60) / sum(CASE WHEN datapoint.datetime BETWEEN date(now() - interval 24 hour) + interval 9 hour AND date(now() - interval 24 hour) + interval 15 hour THEN 1 ELSE 0 END) AS  esp_06_12, 
	   (6 * 60) / sum(CASE WHEN datapoint.datetime BETWEEN date(now() - interval 24 hour) + interval 15 hour AND date(now() - interval 24 hour) + interval 21 hour THEN 1 ELSE 0 END) AS esp_12_18, 
	   (6 * 60) / sum(CASE WHEN datapoint.datetime BETWEEN date(now() - interval 24 hour) + interval 21 hour AND date(now() - interval 24 hour) + interval 27 hour THEN 1 ELSE 0 END) AS esp_18_24 
FROM tag 
	JOIN session 
		ON session.tag_id = tag.id 
	JOIN datapoint 
		ON datapoint.session_id = session.id 
	JOIN dutra_location 
		ON tag.id = dutra_location.tag_id 
	JOIN appinstance 
		ON datapoint.appinstance_id = appinstance.id 
WHERE tag.alias LIKE 'GF-%' 
	AND datapoint.datetime > date(now() - interval 24 hour) + interval 3 hour 
	AND datapoint.datetime < date(now()) + interval 3 hour 
	AND appinstance.company_id = 14 GROUP BY tag.id ORDER BY dutra_location.seq;


"=== Nro de reporters na rede ======================================="
SELECT count(*) 
FROM appinstance 
	JOIN reporter 
		ON reporter.id = appinstance.reporter_id 
	JOIN reporterdevice 
		ON reporterdevice.id = reporter.reporterdevice_id 
	JOIN deviceosversion 
		ON deviceosversion.id = reporterdevice.deviceosversion_id  
WHERE company_id = 14 
	AND deviceosversion.release NOT LIKE 'iOS%' 
	AND appinstance.create_time > '2019-12-18';


"=== Nro de reporters Ativos nas ultimas 24h ========================"
SELECT count(distinct appinstance.id) 
FROM appinstance 
	JOIN reporter 
		ON reporter.id = appinstance.reporter_id 
	JOIN reporterdevice 
		ON reporterdevice.id = reporter.reporterdevice_id 
	JOIN deviceosversion 
		ON deviceosversion.id = reporterdevice.deviceosversion_id 
	JOIN datapoint 
		ON datapoint.appinstance_id = appinstance.id 
WHERE company_id = 14 
	AND deviceosversion.release NOT LIKE 'iOS%' 
	AND datapoint.create_time > now() - interval 24 hour;


"=== Nro de reporters criados, por dia =============================="

SELECT substring(appinstance.create_time, 1, 10), count(*) 
FROM appinstance 
	JOIN reporter 
		ON reporter.id = appinstance.reporter_id 
	JOIN reporterdevice 
		ON reporterdevice.id = reporter.reporterdevice_id 
	JOIN deviceosversion 
		ON deviceosversion.id = reporterdevice.deviceosversion_id  
WHERE company_id = 14 
	AND deviceosversion.release NOT LIKE 'iOS%' 
	AND appinstance.create_time > '2019-12-18' 
GROUP BY substring(appinstance.create_time, 1, 10) 
ORDER BY appinstance.create_time;

"=== Indexes ========================================================"
SELECT 
   #count(*),
   datapoint.id AS datapoint_tab_id, datetime, latitude, longitude, geo_accuracy, temperature, session_id AS datapoint_tab_session_id,
   session.id AS session_tab_id, session.tag_id AS session_tab_tag_id,
   tag_ehook.tag_id AS tag_ehook_tab_tag_id,
   HOUR(datapoint.datetime) BETWEEN 00 AND 05 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59 AS esp_00h_06hs,
   HOUR(datapoint.datetime) BETWEEN 06 AND 11 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59 AS esp_06_12hs,
   HOUR(datapoint.datetime) BETWEEN 12 AND 17 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59 AS esp_12_18,
   HOUR(datapoint.datetime) BETWEEN 18 AND 23 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59 AS esp_18_24hs
   #CAST(sum(HOUR(datapoint.datetime) BETWEEN 00 AND 05 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59) AS SIGNED) AS esp_00h_06hs,
   #CAST(sum(HOUR(datapoint.datetime) BETWEEN 06 AND 11 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59) AS SIGNED) AS esp_06_12hs,
   #CAST(sum(HOUR(datapoint.datetime) BETWEEN 12 AND 17 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59) AS SIGNED) AS esp_12_18,
   #CAST(sum(HOUR(datapoint.datetime) BETWEEN 18 AND 23 AND MINUTE(datapoint.datetime) BETWEEN 00 AND 59) AS SIGNED) AS esp_18_24hs
FROM datapoint
   JOIN session
       ON session.id = datapoint.session_id
   JOIN tag_ehook
       ON tag_ehook.tag_id = session.tag_id
   #JOIN tag 
       #ON tag.id = session.tag_id
   #JOIN tag_ehook
       #ON tag_ehook.tag_id = tag.id
WHERE (longitude BETWEEN -46.589 AND -46.587)
   AND (latitude BETWEEN -23.527 AND -23.525)
   #AND (datetime BETWEEN (last_day(datetime) - interval 3 day) AND last_day(datetime))
   #AND ((datetime > now() - interval 3 day) AND (datetime < now()))
   AND ((datetime > '2020-03-07' - interval 3 day) AND (datetime < '2020-03-07'))
   AND (geo_accuracy <= 700)
   AND (tag_ehook.tag_id IS NOT NULL)
   AND (session_id IS NOT null)
   AND (temperature IS NULL)
ORDER BY datetime DESC;

"=== Indexes ========================================================"
SHOW INDEX FROM datapoint;
CREATE INDEX datapoint_predict_model ON datapoint(longitude, latitude);
CREATE INDEX datapoint_predict_model ON datapoint(longitude, latitude, datetime, geo_accuracy, session_id, temperature);

drop index id on table;

SHOW INDEX FROM session;
CREATE INDEX datapoint_predict_model_session ON session(id, tag_id);

SHOW INDEX FROM tag;
CREATE INDEX datapoint_predict_model_tag ON tag(id);

SHOW INDEX FROM tag_ehook; 
CREATE INDEX datapoint_predict_model_tag_ehook ON tag_ehook(tag_id);

CREATE INDEX appinstance_reporter_id ON appinstance(reporter_id);

DROP INDEX index ON table;

"=== See sizes ======================================================"
'MB'
SELECT
  TABLE_NAME AS `Table`,
  ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024) AS `Size (MB)`
FROM
  information_schema.TABLES
WHERE
    TABLE_SCHEMA = "coldchain"
  AND
    TABLE_NAME = "dutra_kms"
ORDER BY
  (DATA_LENGTH + INDEX_LENGTH)
DESC;

'GB'
SELECT
  TABLE_NAME AS `Table`,
  ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024 / 1024) AS `Size (GB)`
FROM
  information_schema.TABLES
WHERE
    TABLE_SCHEMA = "coldchain"
  AND
    TABLE_NAME = "datapoint"
ORDER BY
  (DATA_LENGTH + INDEX_LENGTH)
DESC;


"=== Create table ==================================================="
CREATE TABLE dutra_kms(id int NOT NULL AUTO_INCREMENT UNIQUE key, 
                       km int NOT NULL,
                       state char(2) NOT NULL,
                       lat_min decimal(10,3) NOT NULL,
                       lat_max decimal(10,3) NOT NULL,
                       long_min decimal(10,3) NOT NULL,
                       long_max decimal(10,3) NOT NULL);

ALTER TABLE dutra_kms change column latitude lat_min float NOT NULL, change column longitude lat_max float NOT NULL;
ALTER TABLE dutra_kms add long_min float NOT NULL after lat_max, add long_max float NOT NULL after long_min;

ALTER TABLE dutra_kms change column lat_min lat_min decimal(10,3) NOT NULL, change column lat_max lat_max decimal(10,3) NOT NULL;
ALTER TABLE dutra_kms change column long_min long_min decimal(10,3) NOT NULL, change column long_max long_max decimal(10,3) NOT NULL;

ALTER TABLE dutra_kms drop column id;
ALTER TABLE dutra_kms add id int NOT NULL AUTO_INCREMENT UNIQUE key first;

'delete rows'
delete ignore from dutra_kms;
ALTER TABLE dutra_kms drop column id;
ALTER TABLE dutra_kms add id int NOT NULL AUTO_INCREMENT UNIQUE key first;


"=== Gerador de table ==============================================="

for i in range(len(addresses)):
    val.append((str(addresses['KM'][i]),
               str(addresses['State'][i]),
               str('%06.3f'%(float(addresses['Latitude'][i]) - 0.001)),
               str('%06.3f'%(float(addresses['Latitude'][i]) + 0.001)),
               str('%06.3f'%(float(addresses['Longitude'][i]) - 0.001)),
               str('%06.3f'%(float(addresses['Longitude'][i]) + 0.001))))

"=== Gerado de query ================================================"

for y in range(len(addresses)):
    addresses['Query'][y] = "SELECT * FROM coldchain.datapoint WHERE latitude " \
    +  str(addresses['Latitude'][y]) + " AND longitude " + str(addresses['Longitude'][y]) + ";"



"=== Comando de query leitura de tag ==============================================="
start=timeit.default_timer()

df_dutra_kms_7_days = pd.read_sql_query('''SELECT
                                               k.id, k.km, k.state, d.datetime,
                                               d.id AS datapoint_tab_id, d.geo_accuracy, d.session_id,
                                               reporter.reporterdevice_id, reporter.identifier,
                                               tag_ehook.tag_id,
                                               count(distinct d.appinstance_id) AS 7_days_nro_smartphones,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 00 AND 05 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_00h_06hs,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 06 AND 11 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_06_12hs,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 12 AND 17 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_12_18,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 18 AND 23 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_18_24hs,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 00 AND 23 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_total
                                           FROM datapoint AS d
                                               JOIN dutra_kms AS k
                                               JOIN session
                                                   ON session.id = d.session_id
                                               JOIN tag_ehook
                                                   ON tag_ehook.tag_id = session.tag_id
                                               JOIN appinstance 
                                                   ON appinstance.id = d.appinstance_id
                                               JOIN reporter
                                                   ON reporter.id = appinstance.reporter_id
                                               JOIN reporterdevice    
                                                   ON reporterdevice.id = reporter.reporterdevice_id
                                           WHERE d.longitude > k.long_min AND d.longitude < k.long_max
                                               AND d.latitude > k.lat_min AND d.latitude < k.lat_max
                                               AND ((datetime > '2020-02-07' - interval 7 day) AND (datetime < '2020-02-07' - interval 6 day))
                                               AND (geo_accuracy <= 700)
                                               AND (session_id IS NOT null)
                                               AND (temperature IS NULL)
                                               AND (tag_ehook.tag_id IS NOT NULL)
                                               AND (reporter.reporterdevice_id IS NOT NULL)
                                           group by k.km
                                           ORDER BY k.id
                                           ;''', connection)

end=timeit.default_timer()

check_time(start, end)

df_dutra_kms_7_days

"=== Comando de query leitura celulares ==============================================="

start=timeit.default_timer()

df_dutra_kms_7_days_B = pd.read_sql_query('''SELECT
                                               k.id, k.km, k.state, d.datetime,
                                               d.id AS datapoint_tab_id, d.geo_accuracy, d.session_id,
                                               reporter.reporterdevice_id, reporter.identifier,
                                               count(distinct d.appinstance_id) AS 7_days_nro_smartphones_B,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 00 AND 05 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_00h_06hs_B,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 06 AND 11 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_06_12hs_B,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 12 AND 17 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_12_18_B,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 18 AND 23 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_esp_18_24hs_B,
                                               CAST(sum(CASE WHEN HOUR(d.datetime) BETWEEN 00 AND 23 AND MINUTE(d.datetime) BETWEEN 00 AND 59 THEN 1 ELSE 0 END) AS SIGNED) AS 7_days_total_B
                                           FROM datapoint AS d
                                               JOIN dutra_kms AS k
                                               JOIN appinstance 
                                                   ON appinstance.id = d.appinstance_id
                                               JOIN reporter
                                                   ON reporter.id = appinstance.reporter_id
                                               JOIN reporterdevice    
                                                   ON reporterdevice.id = reporter.reporterdevice_id
                                           WHERE d.longitude > k.long_min AND d.longitude < k.long_max
                                               AND d.latitude > k.lat_min AND d.latitude < k.lat_max
                                               AND ((datetime > '2020-02-07' - interval 7 day) AND (datetime < '2020-02-07' - interval 6 day))
                                               AND (geo_accuracy <= 700)
                                               AND (session_id IS null)
                                               AND (temperature IS NULL)
                                               AND (reporterdevice_id IS NOT NULL)
                                           group by k.km
                                           ORDER BY k.id
                                           ;''', connection)

end=timeit.default_timer()

check_time(start, end)

df_dutra_kms_7_days_B

"=== querys para criação de index ==============================================="
'datapoint'

create index datapoint_index on datapoint(id, temperature, datetime, latitude, longitude, geo_accuracy, session_id, appinstance_id);
create index datapoint_id on datapoint(id);
create index datapoint_temperature on datapoint(temperature);
create index datapoint_datetime on datapoint(datetime);
create index datapoint_latitude on datapoint(latitude);
create index datapoint_longitude on datapoint(longitude);
create index datapoint_geo_accuracy on datapoint(geo_accuracy);
create index datapoint_session_id on datapoint(session_id);
create index datapoint_appinstance_id on datapoint(appinstance_id);

====================================================================================================================================================================
'appinstance'

create index appinstance_index on appinstance(id, position, company_id, reporter_id, sector_id, active, otacfg_id);
create index appinstance_id on appinstance(id);
create index appinstance_position on appinstance(position);
create index appinstance_company_id on appinstance(company_id);
create index appinstance_reporter_id on appinstance(reporter_id);
create index appinstance_sector_id on appinstance(sector_id);
create index appinstance_active on appinstance(active);
create index appinstance_otacfg_id on appinstance(otacfg_id);


====================================================================================================================================================================
'reporter'

create index reporter_index on reporter(id, identifier, alias, user_agent, active, reporterdevice_id);
create index reporter_id on reporter(id);
create index reporter_identifier on reporter(identifier);
create index reporter_alias on reporter(alias);
create index reporter_reporterdevice_id on reporter(reporterdevice_id);

====================================================================================================================================================================
'reporterdevice'

create index reporterdevice_index on reporterdevice(id, active, devicemodel_id, deviceosversion_id, libversion_id);
create index reporterdevice_id on reporter(id);
create index reporterdevice_active on reporterdevice(active);
create index reporterdevice_devicemodel_id on reporterdevice(devicemodel_id);
create index reporterdevice_deviceosversion_id on reporterdevice(deviceosversion_id);
create index reporterdevice_libversion_id on reporterdevice(libversion_id);

drop index reporterdevice_index on reporterdevice;
drop index reporterdevice_id on reporterdevice;
drop index reporterdevice_identifier on reporterdevice;
drop index reporterdevice_alias on reporterdevice;
drop index reporterdevice_user_agent on reporterdevice;
drop index reporterdevice_active on reporterdevice;

====================================================================================================================================================================
'session'

create index session_index on session(id, identifier, active, tag_id);
create index session_id on session(id);
create index session_identifier on session(identifier);
create index session_active on session(active);
create index session_tag_id on session(tag_id);

drop index session_index on session;
drop index session_id on session;
drop index session_identifier on session;
drop index session_alias on session;
drop index session_user_agent on session;

====================================================================================================================================================================
'tag_ehook'

create index tag_ehook_index on tag_ehook(id, timestamp_base, active, tag_id, tag_group_id, tag_use_id);
create index tag_ehook_id on tag_ehook(id);
create index tag_ehook_identifier on tag_ehook(timestamp_base);
create index tag_ehook_alias on tag_ehook(active);
create index tag_ehook_user_agent on tag_ehook(tag_id);
create index tag_ehook_alias on tag_ehook(tag_group_id);
create index tag_ehook_user_agent on tag_ehook(tag_use_id);

drop index tag_ehook_index on tag_ehook;
drop index tag_ehook_id on tag_ehook;
drop index tag_ehook_identifier on tag_ehook;
drop index tag_ehook_alias on tag_ehook;
drop index tag_ehook_user_agent on tag_ehook;
drop index tag_ehook_alias on tag_ehook;
drop index tag_ehook_user_agent on tag_ehook;

====================================================================================================================================================================
'status'

create index status_index on status(id, bluetooth, datapoint_id);
create index status_id on status(id);
create index status_bluetooth on status(bluetooth);
create index status_datapoint_id on status(datapoint_id);


drop index status_index on status;
drop index status_id on status;
drop index status_identifier on status;
drop index status_alias on status;
drop index status_user_agent on status;
drop index status_alias on status;
drop index status_user_agent on status;