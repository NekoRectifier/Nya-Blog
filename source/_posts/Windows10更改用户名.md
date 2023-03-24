---
title: Windows10更改用户名
date: 2022-01-08 23:31:09
tags: 
    - Windows
---

## 前言

众所周知,在Windows 10中是无法直接更改你的用户名的。(设置里面根本找不到)
![setttingsofuseraccount](./Windows10%E6%9B%B4%E6%94%B9%E7%94%A8%E6%88%B7%E5%90%8D/setttingsofuseraccount.png)

故有以下保留方法来修改用户名。

## How？

打开`cmd`或`windows terminal`, 输入`netplwiz`直接回车。  
在新出现的窗口里选中你要修改的账户就可以修改其属性了，好耶！

## 除此之外

修改完后记得重启，至少在我的电脑上出现了设置无法打开的bug。

参考：  
[1] [windows - 更改用户账户名称](https://blog.csdn.net/weixin_44198965/article/details/115689689)
