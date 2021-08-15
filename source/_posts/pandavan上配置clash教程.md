---
title: pandavan上配置clash教程
date: 2021-08-15 19:20:02
tags: 路由器
---

本次使用的设备是 **极路由 B70** 已刷入最新breed与pandavan.

## clash配置文件生成

此文件用于在路由器上的clash配置所需,我使用的机场运营商支持yaml的配置文件直接下载.文件长这样:

```yaml
    #!MANAGED-CONFIG https://cp.antigfw.net/link/aizid1SSNZnHmkph?clash=1

#---------------------------------------------------#
## 上次更新于：2021-08-15 07:25:20
#---------------------------------------------------#

port: 7890
socks-port: 7891
redir-port: 7892
allow-lan: false
mode: rule
log-level: silent
external-controller: '0.0.0.0:9090'
secret: ''
dns:
  enable: true
  ipv6: false
  listen: '0.0.0.0:53'
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  nameserver:
    - 114.114.114.114
    - 'tcp://223.5.5.5'
  fallback:
    - 'tls://223.5.5.5:853'
    - 'https://223.5.5.5/dns-query'
  fallback-filter:
    geoip: true
    ipcidr:
      - 240.0.0.0/4
proxies:
  -
    name: '中新IEPL [1倍] B - 50004 单端口'
    type: ss
    server: csg.zsdcloud.xxx
    port: 50xxx
    cipher: aes-128-gcm
    password: ************
    udp: true
  -
    name: '中日IEPL [1倍] A - 50003 单端口'
    type: ss
    server: cjp.zsdcloud.xxx
    port: 50xxx
    cipher: aes-128-gcm
    password: ************
    udp: true
  -
    name: '中日IEPL [1倍] B - 50003 单端口'
    type: ss
    server: cjp.zsdcloud.xx
    port: 50xxx
    cipher: aes-128-gcm
    password: ************
    udp: true
    ...
proxy-groups:
  -
    name: 🔰国外流量
    type: select
    proxies:
      - '3【必看！！！节点名称的1倍、0.1倍、10倍是流量倍率，实际消耗1G流量计算为1G、0.1G、10G。】 - 567 单端口'
      ...
  -
    name: 🚀直接连接
    type: select
    proxies:
      - DIRECT


rules:
  - DOMAIN-SUFFIX,smtp,DIRECT
  - DOMAIN-KEYWORD,aria2,DIRECT
  ...

```

先复制备用

## 路由器端设置

* 登入路由器[192.168.123.1](192.168.123.1)

* ![](/images/clashsetup/1.png)
  如图所示,点击左侧菜单栏的"搭建web环境", 后在页面上方的标签栏里找到clash并点击

* ![](/images/clashsetup/2.png)
  
  * 先将红色框内的四个开关打开

  * 将配置文件的内容复制到蓝色框指向位置内

> 记得检查绿色框内的当前clash版本,如没有则更换  
  至于"分流工作模式" 我使用的是大陆白名单 + clash内部分流  
