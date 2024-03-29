---
title: 在2023年试图 root 一台 Redmi K20-Pro
date: 2023-10-10 21:48:38
tags: 
  - Root
  - Android
excerpt: 在 “搞机” 逐渐销声匿迹的当下，还有什么可靠的 Root 方式呢？
---

# 前言

先前终究还是按耐不住入了二手 iPhone 12 mini，在投入到以软件体验为生的苹果的怀抱之后使用体验是确实的上升了。再也不用为了各种系统和内核着急，也不用再去苦苦寻找用来提升使用体验的软件。除此之外苹果无论在生态、动画还是使用体验上都可以算得上是让手机回到了它本质的“工具”属性。这样的日子很好，很舒服——直到今天：  

**我需要一台能够模拟位置的设备来实现签到，代跑之类的工作。**  

我看着手边的 iPhone，只好能把放在抽屉里的 K20 Pro 拿出来，想想其他方法。

# 步骤

## 恢复

凭借着上次刷机的记忆，应该是要把抹除现有系统并恢复到 MIUI 12.5 以作为各个刷机包的基础底包。可以在[这里](https://www.123pan.com/s/Cff7Vv-M0qnH.html)下载刷机包文件，解压 zip，然后执行 `./flash-all.sh` 就可以喝水等着完事了。

## 选择系统

实际上在做出 crDroid OS 的选择之前，我尝试了

- 水龙 13 的官改系统
- CherishOS
- MIUI 国际版 12.5

这些系统的体验感觉对我而言并不是很满意，不过这些刷机包你可以在[这里](https://www.123pan.com/s/Cff7Vv-w0qnH.html)获得。  
在网上又看到了 crDroid OS，安装开机之后的体验确实很不一样。简洁的开机动画，干净的桌面，中意的艺术风格，动画也十分流畅，又同时保留了原生原汁原味的 Android UI 设计。  
所以我想就是它了。

## Root

这个系统很好，但是它是 Android 13。在 Android 13 上，目前主流的 Rec（TWRP & OrangeFox）都不支持 `/data` 分区解密。而且 我的 `rec` 分区貌似还出了问题，fastboot 刷入的 Rec 无法正常启动。只能靠 `fastboot boot rec.img` 临时用一用。

就在我因为 Magisk 需要刷入 zip 包，可我黑苹果系统上的 fastboot 又不能正常走 sideload 而发愁时，[KernalSU](https://kernelsu.org/guide/what-is-kernelsu.html)出现了。

> 官网解释：  
> KernelSU is a root solution for Android GKI devices, it works in kernel mode and grant root permission to userspace application directly in kernel space.

抱着试一试的心态，我下载了 KernalSU 的[管理器](https://www.coolapk.com/apk/me.weishu.kernelsu)。

![kernalsu-manager](kernalsu-manager.png)

不知道出于什么原因，KernalSU 自己就是激活状态。于是顺手安了个 [Zygisk on KernalSU](https://github.com/Dr-TSNG/ZygiskOnKernelSU) 和 Lsposed。（要安装 Lsposed 使用给 magisk 的 zygisk 模式的 zip 包就好，是可以直接使用的）

![lsposed-activated](lsposed-activated.png)

我的系统信息如下：

![system-info](system-version.png)

# 额外

## Fake Location 安装及破解

Root 的问题解决以后，就要开始想办法解决模拟定位的问题了。
模拟位置由 FakeLocation 就能搞定，不过可惜的是，这是一款付费软件。所以还需要 [NFG Multi Crack](https://github.com/rockz5555/NFG-Multi-Crack/releases) 来破解掉它。

> NFG 并不能处理 Fake Location 的最新版本破解，因此需要下载 1.3.1.6 版本。  
> 这是对破解支持的最好的一个版本。 

1. 在 LSP 管理器中激活 NFG 模块，同时作用域中也要包括 “系统框架” 和 “Fake Location”。

2. 打开 NFG 点击 Fake Location 项目右侧的 “关闭” 按钮来激活破解

3. 打开 Fake Location

![](crack.png)

# 参考链接 🔗
【1】<https://kernelsu.com/lsposed-install>  
【2】<https://www.youtube.com/watch?v=XX5XgdlAS8E>  
【3】<https://www.bilibili.com/read/cv22932367>
