#!/bin/sh -x
sudo chmod +x start_catberry.py
sudo chmod +x stop_catberry.py
sudo cp -i catberry.service /etc/systemd/system/
sudo cp -i catberry_log /etc/logrotate.d/
sudo systemctl enable catberry.service
sudo systemctl start catberry.service
