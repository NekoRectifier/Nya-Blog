---
title: 使用John The Ripper破解压缩文件密码
date: 2022-02-03 16:18:28
tags: 
  - crack
---

## 前言

春节已至，正想找几本书来提升一下自己。好不容易找到的pdf却又被`ZipCrypto`加密，只好去网上碰碰运气，结果发现了这个工具，叫做[John The Ripper](https://www.openwall.com/john/)，它是一个非常强大的破解~~压缩文件~~密码的工具。

## 准备工作

- 被加密的压缩文件 （zip、rar均可）  
  本文中假设为 `D:\encrypted.zip`

- John The Ripper 预编译可执行文件，可以通过[这个链接](https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win64.zip)下载 1.9.0版本 （Windows）  

## 获取加密压缩包的哈希值

解压 John The Ripper 压缩包，在 `..\john-1.9.0-jumbo-1-win64\run` 目录下启动使用 `cmd` 或者 `Windows Terminal` 执行以下命令：

```bash
    .\zip2john.exe "D:\encrypted.zip" > "D:\encrypted.zip.hash"
```

> 如果是 `rar` 文件则使用 `rar2john.exe`

执行后会在你指定的目录下生成一个 `encrypted.zip.hash` 文件，有着几倍于源压缩文件的大小。

如果你使用`Windows Terminal`执行上述操作, 则导出的文件可能采用UTF-16编码，需要转换为UTF-8编码才能进行破解。

我这里采用VSC进行编码转换。右击哈希文件使用VSC打开，点击右下角"UTF-16LE"，在弹出来的选项中选择"通过编码保存"，最后选择`UTF-8 utf-8`即可。

![change_encode](change_encode.png)

## 通过哈希值查找密码

在先前的终端中输入以下命令：

```bash
    .\john.exe "D:\encrypted.zip.hash"
```

破解就会开始了。

![crack](crack.png)

如图所示，文件名前面的字符（绿色标记）就是压缩文件密码。至此破解已完成。

## 破解相关

破解所需时间与密码位数关系大致如下：  
**(密码仅由数字和字母组成)**

> E[6位密码] = 0.5 × (62^6 / (2.6 × 10^8)) = 218 s
  E[7位密码] = 0.5 × (62^7 / (2.6 × 10^8)) = 13545 s = 3.76 小时
  E[8位密码] = 0.5 × (62^8 / (2.6 × 10^8)) = 839770 s = 9.71 天
  E[9位密码] = 0.5 × (62^9 / (2.6 × 10^8)) = 21834011 s = 252.71 天
  E[10位密码] = 0.5 × (62^10 / (2.6 × 10^8)) = 1,353,708,655 s = 42.93 年

*(所以太长的就还是不要考虑了*

##### 电子书是...

书是从[板栗](http://blogss.cn/)上整的。是二次收费分发，所以就直接破解掉。

## 参考链接

[1] <https://zhuanlan.zhihu.com/p/129855130>
[2] <https://dfir.science/2014/07/how-to-cracking-zip-and-rar-protected.html>
