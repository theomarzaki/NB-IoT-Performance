service rsyslog start
sleep 0.5
pppd
sleep 1
route add default dev ppp0
sleep 0.5
cat /var/log/messages
