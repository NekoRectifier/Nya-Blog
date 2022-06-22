---
title: 在termux上部署VSCode Codespace
date: 2021-09-06 09:54:31
tags: 
    - Web
    - Termux
    - VSC
---

## 前言

VSCode 作为一款轻量级的代码编辑器, 将其部署在移动平台上来运行简单代码是再好不过的选择了.

## 安装步骤

打开你在[F-droid](https://f-droid.org/en/packages/com.termux/)或[GPlay](https://play.google.com/store/apps/details?id=com.termux&hl=zh&gl=US)商店上下载的 Termux.

1. 更换镜像源 (可选)

   > 以下参考 Tuna 站的[教程](https://mirrors.tuna.tsinghua.edu.cn/help/termux/)

   - 输入 `termux-change-repo` 在图形界面下手动使用方向键来选择要切换到的源.

   - 使用如下命令来切换源

     ```shell
         sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list

         sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list

         sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list

         apt update && apt upgrade
     ```

   - 手动修改 (不推荐)

2. 升级程序包

    ```shell
        pkg update
    ```

3. 安装 code-server 必要依赖

    ```shell
        pkg install -y python nodejs yarn
    ```

    > **参见你自己的情况!**

    如 `python` 无效就试试 `python3`

3. 安装 code-server

    ```shell
        yarn global add code-server
    ```

    > 该步骤需要较长时间, 请耐心等待

4. 修复 VSCode 依赖的 spdlog

    ```shell
        cd ~/.config/yarn/global/node_modules/code-server/lib/vscode/node_modules/spdlog/
        nano binding.gyp
    ```

    使用 `nano` 或 `vim` 编辑 binging.gyp 文件  
    将 `"target_name": "spdlog"`一行的下面添加 `"libraries": [ "-latomic" ]`

    修改过后的文件如下所示:

    ```gyp
        "targets": [{
            "target_name": "spdlog",
            "libraries": [ "-latomic" ],
            "sources": [
                    "src/main.cc",
                    "src/logger.cc"
            ],
    ```

    别忘了保存退出

5. 重新编译 spdlog

    > 不用`cd`,在当前目录执行即可

    ```shell
        npm install
    ```

6. 启动 code-server

    ```shell
        cd ~
        code-server --auth none --disable-telemetry
    ```

    之后就可以在浏览器访问 http://localhost:8080 来打开 VSCode 了

## 其他配置

- 在其它设备上也使用 VSCode  
  当然不是让你再重装一遍,而是使用如下启动方式

    ```shell
        code-server --bind-addr 0.0.0.0:8080 --disable-telemetry
    ```

    登陆密码可以在 `~/.config/code-server/config.yaml` 找到

- 启用 HTTPS 功能

    ```shell
        pkg install openssl-tool
        code-server --bind-addr 0.0.0.0:8080 --cert --disable-telemetry
    ```

    Termux便会针对VSC自动生成https证书了

## 后记 2022/04/09

在酷安上出现一款`Code FA`的软件, 可以在移动设备上一键部署基于Ubuntu的VSCode，还提供了与其无缝衔接的已包装好的远程桌面。使用起来效果确实不错。  
下载链接：https://www.coolapk.com/apk/com.nightmare.code 或 https://nightmare.fun/YanTool/resources/VSCode/

原作者博文：https://www.imgeek.org/article/825360015
