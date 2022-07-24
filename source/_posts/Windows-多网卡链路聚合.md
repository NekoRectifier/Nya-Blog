---
title: Windows 多网卡链路聚合
date: 2022-07-23 11:00:31
tags: 
  - Windows
  - Networking
---

> 本文在 Windows 11 Pro 22621.436 下测试有效

# 同时使用多个网络适配器的难题

在 Windows 系统下，系统默认采用仅**某个特定的网络适配器**进行连接（即便你的设备上存在着多个可同时联网的网卡）

如我的笔记本上就内置了一张 Intel AX200，连接 5G WiFi 时可达到 585 Mbps 的速度。而如果我使用手机进行 USB 网络共享则可以达到 425 Mbps。

如何将两者的速度同时利用起来以达到理论最快的网络呢？

# NIC Teaming （链路聚合）

想要实现多个网卡同时使用，最好的解决办法就是链路聚合。

有关链路聚合的概念可以在[这里](https://techlibrary.hpe.com/docs/enterprise/servers/icsp/7.5.1/webhelp/content/s_nicteaming_about.html#:~:text=NIC%20teaming%20is%20the%20process,network%20device%20called%20a%20bond.)看到，在这里不做解释。

## 实现 （NetSwitchTeam）

1. 在==具有管理员权限的== `Windows PowerShell` 窗口中，先执行 `Get-NetAdapter -Physical` 来获取当前设备上的**物理**网卡列表。
  ![ga](g_a.png)

2. 执行以下指令来创建 “多路网络适配器复用器”（Network Adapter Multiplexor）

  ```powershell
    New-NetSwitchTeam -Name "SWT01" -TeamMembers "WLAN","USB"
  ```
  > `Name` 可自定名称；
  `TeamMembers` 需指定为上图中的任意网络适配器名称

  ![g](gst.png)

3. 接下来转到 Windows 自带的网络设置界面

  ![wllj](wllj.png)

  此时网络连接的速度为 1292 Mbps，存在明显的叠加效果。 

## 问题

  - 出于未知原因，有时候链路聚合后存在无法获取 ip 的问题。
    可通过 `Remove-NetSwitchTeam -Name "{名称}"` 来恢复先前状态。

# 参考链接
【1】 https://www.wyr.me/post/659
【2】 https://blog.csdn.net/ytlzq0228/article/details/118071224
【3】 https://www.mr-fu.com/11014/