# 🤖 Base Node

⚡ Fundamental package for robotchain.. ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> This package is already built-in within robotchain, so there's no need for redundant installation. The following documentation is provided for manual compilation and building as a reference for learning purposes.

## 📖 Initialization

> Before compiling and building, please complete the installation and deployment of robotchain on your Ubuntu device.

```shell
sudo curl -s https://cdn.geekros.com/robotchain/install.sh|bash
```

Clone the repository to your Ubuntu device using `git`.

```shell
git clone git@github.com:geekros/base_node_package.git
```

## 📖 Build

```shell
cd base_node_package
```

```shell
cd serial_foxy
mkdir build && cd build
cmake .. && make && sudo make install
cd ../ && sudo rm -rf build && cd ../

sudo cp /usr/local/lib/libserial.so ./debian/opt/tros/lib/

colcon build --packages-select serial_port_node
colcon build --packages-select vision_dnn
```

## 📖 Publishing a Debian (deb) software package.

```shell
cd base_node_package
```

Packaging into a deb file.

```shell
robotchain pack package
```

Publishing the deb to a software repository.

```shell
robotchain publish
```

## 📖 Install

```shell
sudo apt install base_node_package
```

## 🌞 Development Team

> GEEKROS
> https://www.geekros.com