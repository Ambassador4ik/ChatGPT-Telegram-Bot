sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install docker docker.io

cd ..

docker build ChatGPT-Telegram-Bot -t chatgpt-telegram-bot
docker run -it chatgpt-telegram-bot