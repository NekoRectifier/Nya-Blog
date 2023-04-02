---
title: 记 Rime 输入法在 Manjaro 上的部署及配置
date: 2023-03-31 23:49:12
tags: 
  - Linux
  - Software
---

## 前言

大概是半年前从 Arch Linux 切换到了 Manjaro 并将其作为 Linux 主力开发系统，而使用的桌面环境——Gnome却对 [fcitx](https://fcitx-im.org/wiki/Fcitx/zh-hans) 的支持并不是很好。要在 Gnome Extension 上安装 IM-KDE 插件还要捣鼓其他设置。听说新的 Gnome（Gnome 43）将 ibus 集成进了 Gnome Desktop ，于是就换掉 fcitx 同时体验一下早有耳闻的 [rime](https://rime.im/) 输入法。

## 安装

1. Manjaro ibus 支持包安装

    启动 “Manjaro Hello” 程序，点击最下方的 “Application/应用程序”，选择这个

    ![manjaro-hello-install](./%E8%AE%B0-Rime-%E8%BE%93%E5%85%A5%E6%B3%95%E5%9C%A8-Manjaro-%E4%B8%8A%E7%9A%84%E9%83%A8%E7%BD%B2%E5%8F%8A%E9%85%8D%E7%BD%AE/manjaro-hello-install.png)

    然后点击 “UPDATE SYSTEM/升级系统”进行安装。

2. Rime 本体安装

    终端输入

    ```bash
    yay -S ibus-rime
    # sudo pacman -S ibus-rime 一样的

    ```

    这样会安装 rime 本体及朙月拼音、地球拼音、注音、五笔等默认输入方案。

    > 具体方案可以到 `~/.config/ibus/rime` 下查看。其他输入方案在[这里](https://github.com/rime/plum#packages)

    重启后，打开 gnome 设置。在键盘选项卡里的“Input Source/输入法”下添加 rime 输入法，并将其他的输入法统统移除。（包括默认的英文）

    <!-- ![manjaro-hello-install](./%E8%AE%B0-Rime-%E8%BE%93%E5%85%A5%E6%B3%95%E5%9C%A8-Manjaro-%E4%B8%8A%E7%9A%84%E9%83%A8%E7%BD%B2%E5%8F%8A%E9%85%8D%E7%BD%AE/add-im.png) -->

    ![manjaro-hello-install](./%E8%AE%B0-Rime-%E8%BE%93%E5%85%A5%E6%B3%95%E5%9C%A8-Manjaro-%E4%B8%8A%E7%9A%84%E9%83%A8%E7%BD%B2%E5%8F%8A%E9%85%8D%E7%BD%AE/keyboard-add.png)

3. Rime 配置

    - `~/.config/ibus/rime` 在下文中称作“配置文件路径”

    ---

    我的配置（仅有 flypy）可以在[这里](/%E8%AE%B0-Rime-%E8%BE%93%E5%85%A5%E6%B3%95%E5%9C%A8-Manjaro-%E4%B8%8A%E7%9A%84%E9%83%A8%E7%BD%B2%E5%8F%8A%E9%85%8D%E7%BD%AE/raw/rime-config.zip)下载

    1. 「可选」安装 [东风破/Plum](https://github.com/rime/plum) （Rime 配置工具）

        ```bash
        curl -fsSL https://raw.githubusercontent.com/rime/plum/master/rime-install | bash
        ```

    > 安装时需要终端全局代理或者使用 [Proxychains](https://github.com/haad/proxychains)类工具。

    2. 「可选」安装其他方案包

        如果你喜欢的方案（如双拼）不在默认的输入方案内，你可能需要使用 plum 来手动安装。

        在执行上条命令的目录下找到 `plum/` 文件夹，进入后输入 `./rime-install double-pinyin`。plum 就会寻找 rime 的配置路径并且将双拼方案添加到 `~/.config/ibus/rime` 路径下。

    3. 配置文件修改

        - 配置文件原理

            配置文件路径内的文件会在按下“部署”时进行编译，并在 `build/` 目录下输出编译后配置。
            如果配置文件错误，会将有问题的文件移动至 `trash/` 文件夹。

        - 快捷键

        