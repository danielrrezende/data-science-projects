#!/bin/bash

echo "=== Stats NGINX ===================================================="
export REQS_PER_SEC=$(expr 100000 / $(expr $(date +'%s') - $(date -d "$(echo $(date +'%Y-%m-%d ') $(tail -n 100000 ~/cold-chain/backoffice/letsencrypt/log/nginx/access.log | head -n 1 | cut -d\  -f 4 | cut -c 14-))" +'%s')))
echo "Requests / sec: $REQS_PER_SEC"
echo ""
echo "Nro de Reqs / HTTP Status"
tail -n 100000 ~/cold-chain/backoffice/letsencrypt/log/nginx/access.log | cut -d\  -f 9 | sort | uniq -c
echo "=== Stats NGINX ===================================================="

echo "=== Passagens na Dutra ============================================="
mysql -h 127.0.0.1 -u root coldchain -e "select dutra_location.state, dutra_location.km, dutra_location.direction, dutra_location.extra, tag.alias, count(distinct datapoint.appinstance_id) as 'nro_smartphones', (24 * 60) / count(distinct datapoint.appinstance_id) as esp_leit_min, avg(timestampdiff(SECOND, datapoint.datetime, datapoint.create_time)) as delay_envio, (6 * 60) / sum(case when datapoint.datetime < date(now() - interval 24 hour) + interval 9 hour then 1 else 0 end) as  esp_00h_06h, (6 * 60) / sum(case when datapoint.datetime between date(now() - interval 24 hour) + interval 9 hour and date(now() - interval 24 hour) + interval 15 hour then 1 else 0 end) as  esp_06_12, (6 * 60) / sum(case when datapoint.datetime between date(now() - interval 24 hour) + interval 15 hour and date(now() - interval 24 hour) + interval 21 hour then 1 else 0 end) as esp_12_18, (6 * 60) / sum(case when datapoint.datetime between date(now() - interval 24 hour) + interval 21 hour and date(now() - interval 24 hour) + interval 27 hour then 1 else 0 end) as esp_18_24 from tag join session on session.tag_id = tag.id join datapoint on datapoint.session_id = session.id join dutra_location on tag.id = dutra_location.tag_id join appinstance on datapoint.appinstance_id = appinstance.id where tag.alias like 'GF-%' and datapoint.datetime > date(now() - interval 24 hour) + interval 3 hour and datapoint.datetime < date(now()) + interval 3 hour and appinstance.company_id = 14 group by tag.id order by dutra_location.seq;"
echo "=== Passagens na Dutra ============================================="


echo "=== Nro de reporters na rede ======================================="
mysql -h 127.0.0.1 -u root coldchain -e "select count(*) from appinstance join reporter on reporter.id = appinstance.reporter_id join reporterdevice on reporterdevice.id = reporter.reporterdevice_id join deviceosversion on deviceosversion.id = reporterdevice.deviceosversion_id  where company_id = 14 and deviceosversion.release not like 'iOS%' and appinstance.create_time > '2019-12-18';"
echo "=== Nro de reporters na rede ======================================="

echo "=== Nro de reporters Ativos nas ultimas 24h ========================"
mysql -h 127.0.0.1 -u root coldchain -e "select count(distinct appinstance.id) from appinstance join reporter on reporter.id = appinstance.reporter_id join reporterdevice on reporterdevice.id = reporter.reporterdevice_id join deviceosversion on deviceosversion.id = reporterdevice.deviceosversion_id join datapoint on datapoint.appinstance_id = appinstance.id where company_id = 14 and deviceosversion.release not like 'iOS%' and datapoint.create_time > now() - interval 24 hour;"
echo "=== Nro de reporters Ativos nas ultimas 24h ========================"

echo "=== Nro de reporters criados, por dia =============================="
mysql -h 127.0.0.1 -u root coldchain -e "select substring(appinstance.create_time, 1, 10), count(*) from appinstance join reporter on reporter.id = appinstance.reporter_id join reporterdevice on reporterdevice.id = reporter.reporterdevice_id join deviceosversion on deviceosversion.id = reporterdevice.deviceosversion_id  where company_id = 14 and deviceosversion.release not like 'iOS%' and appinstance.create_time > '2019-12-18' group by substring(appinstance.create_time, 1, 10) order by appinstance.create_time;"
echo "=== Nro de reporters criados, por dia =============================="

