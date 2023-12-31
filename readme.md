# 🤖 Python Framework SDK

⚡ Python development framework for robotchain. ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 已经内置在robotchain中，无需单独、重复安装，该仓库仅供学习参考。
> 
> It is already built-in within robotchain, so there is no need for separate or redundant installation. This repository is provided for learning and reference purposes only.

## 📖 Initialization

> 安装相关依赖
> 
> Install the required dependencies.

```shell
pip3 install robotchain colorlog websocket-client==0.48.0 requests pyserial roslibpy empy colcon-common-extensions pymongo tornado
```

## 📖 Using templates

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import robotchain as framework

def robot_start(sdk):
    while True:
        pass

def robot_message(sdk, message):
    pass

def robot_exit(sdk):
    pass

if __name__ == '__main__':
    framework_sdk = framework.Init()
    robot_start(framework_sdk)
```

## 📖 Development

> 安装相关依赖
>
> Install the required dependencies.

```shell
pip3 install twine setuptools wheel
```

> 构建软件包
>
> Build software package.

```shell
python3 setup.py sdist bdist_wheel
```

> 上传软件包到PyPI
>
> Upload software package to PyPI.

```shell
twine upload dist/*
```

## 🌞 Development Team

> GEEKROS
> https://www.geekros.com