---
title: 在termux上部署VSCode Codespace
date: 2021-09-06 09:54:31
tags: Web, Termux, VSC
---

VSCode作为一款轻量级的代码编辑器, 其丰富的插件给其增加了许多扩展性. 将其部署在移动平台上很适用于轻量级代码的运行.

## 安装步骤

1. 升级程序包

```shell
    pkg update
```

2. 安装code-server必要依赖

```shell
    pkg install -y python nodejs yarn
```

>在此处的`python`实际是`python3`

3. 安装code-server

```shell
    yarn global add code-server
```

> 该步骤需要较长时间, 请耐心等待

4. 修复VSCode依赖的spdlog

```shell
    cd ~/.config/yarn/global/node_modules/code-server/lib/vscode/node_modules/spdlog/
    nano binding.gyp
```

编辑binging.gyp文件, 将`"target_name": "spdlog"`,一行的下面添加`"libraries": [ "-latomic" ],`  
修改过后的文件如下所示:

``` gyp
    "targets": [{
        "target_name": "spdlog",
        "libraries": [ "-latomic" ],
        "sources": [
                "src/main.cc",
                "src/logger.cc"
        ],
```

之后保存退出

5. 重新编译spdlog

> 不用`cd`,在当前目录执行即可

```shell
    npm install
```

6. 启动code-server

```shell
    cd ~
    code-server --auth none --disable-telemetry
```

之后就可以在浏览器访问 http://localhost:8080 来打开VSCode了

## 其他配置

* 在其它设备上也使用VSCode  
当然不是让你再重装一遍,而是使用如下启动方式

``` shell
    code-server --bind-addr 0.0.0.0:8080 --disable-telemetry
```

登陆密码可以在 `~/.config/code-server/config.yaml` 找到

* 启用HTTPS功能

``` shell
    pkg install openssl-tool
    code-server --bind-addr 0.0.0.0:8080 --cert --disable-telemetry
```

便会自动生成https证书了
