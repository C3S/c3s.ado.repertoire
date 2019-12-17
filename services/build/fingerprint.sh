#!/bin/bash

INGEST=$(ls /opt/echoprint-data | grep casket)

/bin/ttserver -port 1978 -dmn -pid /tmp/tokyotyrant.pid -log /var/log/tokyotyrant.log /opt/echoprint-data/casket.tch#bnum=100000
/bin/sh -c "cd /opt/echoprint-server/solr/solr/ && /usr/bin/java -Dsolr.solr.home=/opt/echoprint-server/solr/solr/solr/ -Djava.awt.headless=true -jar start.jar 2>&1 > /var/log/solr.log" &
/bin/sh -c "python /opt/echoprint-server/API/api.py 80 2>&1 > /var/log/echorint.log" &

if [ $INGEST ]; then
    cd /opt/echoprint-server/util && /usr/bin/python /opt/echoprint-server/util/fastingest.py /root/fingerprint-data.json
fi

tail -f /var/log/tokyotyrant.log /var/log/solr.log /var/log/echoprint.log