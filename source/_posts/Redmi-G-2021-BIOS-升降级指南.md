---
title: Redmi G 2021 BIOS 升降级指南
date: 2022-04-07 15:30:51
tags: BIOS
---

## BIOS驱动

Redmi G 2021 BIOS驱动 303-707
[点击这里下载](https://nekorectifier.lanzouw.com/iVP5Y02rsx3e)

## 如何升级

1. 解压你下载的特定版本的BIOS压缩包，双击里面的exe可执行文件即可。

    ![file](file_exe.png)

2. 静待系统自动重启并开始BIOS升级。

## 如何禁止BIOS自动升级

1. 在`此电脑`上单击右键并点击`管理`。
  
    ![file](file_right_click.png)

2. 在计算机管理中选择**设备管理器**，并在右边的窗口中找到`固件`。

    ![file](com_mgr.png)

3. 最后在`Xiaomi System Firmware 1.X.X.X`上右键选择**禁用**。

    ![file](firmware_disable.png)

## 如何降级

BIOS升级后是不可以直接从`808`等版本降级到`707`的，升级软件会提示已安装版本高于即将要安装的版本。

![file](degrade_failed.png)

故需要采用先重新安装到`303`版本的方式来实现BIOS降级。

## 参考链接

[1] https://www.acfun.cn/a/ac33684886?from=video
[2] https://www.bilibili.com/video/BV1rY41137bd