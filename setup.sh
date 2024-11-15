#!/bin/bash
sudo apt-get update
sudo apt-get install -y wget unzip
sudo apt-get install -y chromium-browser
wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver
