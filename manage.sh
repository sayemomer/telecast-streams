#!/bin/sh

argument=$1

if [ $argument = "newb" ]; then
    echo "installing prerequisites..."
    sudo apt update -y
    sleep 2
    sudo amazon-linux-extras install docker
    sleep 2
    sudo service docker start
    echo "Docker installed..."
    docker --version
    sleep 2
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    sleep 2
    unzip awscliv2.zip
    sleep 2 
    sudo ./aws/install
    sleep 2
    echo "AWS CLI installed..."
    aws --version
    sleep 2


elif [ $argument = "test" ]; then
    echo "creating local infrastructure..."
    cd ./app
    sam local invoke

elif [ $argument = "up" ]; then
    echo "Creating infrastructure..."

else
  echo "Unknown argumnet! Options: newb, test, up"
fi