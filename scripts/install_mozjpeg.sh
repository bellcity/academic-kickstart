### Install NASM
wget http://www.nasm.us/pub/nasm/releasebuilds/<VERSION NUMBER>/nasm-<VERSION NUMBER>.tar.gz
cd nasm<VERSION NUMBER>
./configure 
make  -j8
sudo make install

### Install mozjpeg
sudo apt-get update
sudo apt-get install cmake autoconf automake libtool nasm make pkg-config libpng-dev zlib1g-dev
git clone https://github.com/mozilla/mozjpeg.git
cd mozjpeg
mkdir build && cd build
sudo cmake -G"Unix Makefiles" ../
sudo make install
cd /usr/local/bin
sudo ln -s /opt/mozjpeg/bin/cjpeg