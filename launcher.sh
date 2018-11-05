cd /home/tc/beepbeep
git fetch --all
git reset --hard origin/master
git pull origin master
sudo python beep.py &
