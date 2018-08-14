#!/usr/bin/env bash
mkdir ~/.pip/
echo "[global]" >> ~/.pip/pip.conf
echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf

sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python-pip python3.6 python3.6-dev rabbitmq-server redis-server git tmux vim emacs
pip install virtualenv
sudo pip install virtualenvwrapper
echo  "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc 
mkvirtualenv cinema -p python3.6
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh
sudo mkdir /code
sudo mkdir /var/log/cinema
sudo chmod -R 777 /var/log/cinema
sudo chmod -R 777 /code
cd /code
git clone https://github.com/hikelee/cinema-python



