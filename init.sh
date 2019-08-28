service rsyslog start
sleep 0.5
pppd
sleep 2
cat /var/log/messages
sleep 2
route add default dev ppp0
