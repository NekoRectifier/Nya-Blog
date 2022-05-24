---
title: 解决Windows蓝牙连接不稳定问题
date: 2022-05-24 21:45:03
tags: Windows, Bluetooth
---

在日常使用WIndows蓝牙连接耳机使用时，经常会出现音频突然出现中断随后变得断断续续或直接失去与设备连接的情况。

## 导致原因

- 有其他设备（如手机）正尝试连接到目前已连接至Windows的设备

- Windows蓝牙适配器的电源设置不正确

## 解决方式

> 本文仅针对后一种问题

- 打开Windows设备管理器界面

- 找到相应的蓝牙适配器（注意：不是已经连接的蓝牙设备，是**适配器**）

![bl_adapter](bl_adapter.png)

- 在“电源管理”选项卡中，选择关闭“允许关闭此设备以节约电源”

![power_setting](power_setting.png)

- 至此问题解决

## 参考链接

[1] https://blog.csdn.net/weixin_51229662/article/details/118640811
