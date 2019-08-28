service rsyslog start
sleep 0.5
pppd
sleep 0.1
tail -f /var/log/messages
