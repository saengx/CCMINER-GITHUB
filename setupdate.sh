#!/bin/sh

apt-get update -y
apt-get upgrade -y

chmod +x edit-miner
chmod +x run-miner
chmod +x add-file
chmod +x update
chmod +x down-grade
chmod +x ANSI_Shadow.flf
chmod +x backup
chmod +x restore
chmod +x install.txt

mv mobile-mining ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin
mv add-file ../../bin
mv update ../../bin
mv down-grade ../../bin
mv ANSI_Shadow.flf ../../usr/share/figlet
mv backup /data/data/com.termux/files/usr/bin
mv restore /data/data/com.termux/files/usr/bin
mv install.txt /storage/emulated/0/download

run-miner


cd && cd ../etc/mobile-mining/ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
CXX=clang++ CC=clang ./build.sh

run-miner
