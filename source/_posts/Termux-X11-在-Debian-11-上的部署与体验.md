---
title: Termux X11 在 Debian 11 上的部署与体验
date: 2023-02-10 13:09:44
tags: 
  - Termux
---

## 前言

以前在 Termux 上跑 proot/chroot 环境都是通过 (tiger/tight) VNC 或者 novnc 之类的方式来与桌面环境交互的，使用起来要么不太稳定；要么与原生系统契合感欠佳。于是便渐渐抛弃了给这些容器用上花里胡哨的桌面环境，只走普普通通的 cli 操作。 但现在听说出了个 X11 实现原生级别的交互，并且看[B站上的演示](https://www.bilibili.com/video/BV13Y4y1u7Wy)也的确眼馋，所以来自己试试。

## Termux X11 基础配置

> 由于 Termux X11 的开发仍在初始阶段，并没有被纳入到 Termux 自身当中，因而需要手动安装。

- 下载 CI 的自动构建包
  
  到[这里](https://github.com/termux/termux-x11/actions/workflows/debug_build.yml)任意点击一个 workflow

  ![workflow](workflow.png)

  点击 `termux-x11` 下载压缩包即可。

- 安装

  安装压缩包内的 apk 文件与 deb 文件。

  可以先将 deb 文件拷贝至设备内置存储 (/sdcard) 下，接着打开 Termux 运行：

  ```bash
    pkg update
    pkg install x11-repo
    cd /sdcard/
    pkg install termux-x11.deb
  ```

  没有报错的话就可以进行下一步了。

- 配置
  
  还是在 Termux 中，需要修改 `~/.termux/termux.properties` 文件。

  ```bash
    nano ~/.termux/termux.properties
  ```

  现在用 nano 编辑器打开了 termux 配置文件，接着用方向键找到 `#   allow-external-apps = true` 的这一行。

  ![termux-properties](termux-properties.png)

  将这一行行首的 “#” 号去掉，按 <kbd>ctrl</kbd> + <kbd>s</kbd> （termux小键盘上的 `ctrl` 与输入法上的 `s`）保存。然后按 <kbd>ctrl</kbd> + <kbd>x</kbd> 退出即可。

  - 检查

  运行 `termux-x11`，如果弹出 termux-x11 的窗口即为安装成功。

## 安装 & 设置 Debian

> 推荐使用 [tmoe](https://doc.tmoe.me/zh/android.html)

运行这条命令

```bash
curl -LO https://gitee.com/mo2/linux/raw/2/2.awk; awk -f 2.awk
```

并在接下来的选择中一直选 `y`，（当选择语言时直接点击回车） 就可以见到 tmoe 的主界面了。

![ttmoe](termux-tmoe.png)

> 如果你是 Android 12 及以上,则建议运行下 "修复Android 12 (signal9)" 以修复 Phantom Killer 的问题。

接着安装 proot 容器，选择一个合适的发行版安装。

- 设置好非 root 账户

  如果你使用 tmoe 则在安装过程中会自动提示你进行设置。

- 更新软件源

  如果使用 tmoe 则国内源已经配置好，手动更新即可。
  
  ```bash
    # Debian 情况
    sudo apt update
    sudo apt upgrade
    # 其他发行版请自行查看
  ```

- 安装 xfce4 桌面环境

  ```bash
    sudo apt install xfce
    sudo apt install dbus-x11
  ```

- 编写启动脚本
  
  使用 `nano start.sh` 创建文件

  内容如下

  ```bash
  #!/bin/bash
  export DISPLAY=:0
  dbus-launch --exit-with-session startxfce4 &
  ```

  保存之后，使用命令修改权限 `chmod +x ./start.sh`

- 设置 `/tmp` 目录共享

  在宿主机的环境内运行 tmoe，编辑其 “环境变量与登录项管理”

  ![](tmoe-con-edit.png)

  然后选择 “共享tmp”

  ![](tmp.png)

  在新窗口中

  - 第一次选 true
  - 剩余两次选 cancel
  - 最后退出设定

  这样就完成了 proot 容器的全部设置。

## 运行

1. 关掉 Termux 重开
2. 执行 `termux-x11`
3. 打开第二个 session，执行 `tmoe p` 启动上一次启动的 proot 容器
4. 在容器环境中运行脚本 `./start.sh`
5. 回到 Termux X11 app 中看看启动的 xfce4 桌面

## 参考链接

【1】<https://ivonblog.com/posts/termux-x11/>  
【2】<https://github.com/kde-yyds/termux-x11-plasma-installation-guide>
