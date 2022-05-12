---
title: Meizu E3 解锁/刷机指南
date: 2022-05-12 00:40:58
tags: Android, 刷机
---

## 前言

当我在~~大概~~2018年第一次拿到这手机的时候，感觉还不错。毕竟高通636已经6+64GB的配置在当时看来并不算差。但是由于Flyme系统的封闭，获取root和刷机成了一件难事。鉴于当时没有什么野路子能供我操作，很快我就对它失去了兴趣。然而如今偶然在telegram上看见解锁/刷机的方法，便溯源到xda上的帖子试了下，最后得出了你正在看的这份指南。

- 为什么要写这个指南？
  
  1. 给自己做个记录
  2. ~~原帖子的说明并不是很容易看懂~~

## 资源

 - Material Terminal: https://nekorectifier.lanzouw.com/iaZeH04ohtni

 - TWRP Recovery: https://nekorectifier.lanzouw.com/ipToO04ogd9c

 - LinageOS：https://cowtransfer.com/s/a87df3a2f8a64f 口令：77rulq 

 - LinageOS Boot Image：https://nekorectifier.lanzouw.com/iCuEY04ogh5c

## 具体步骤

### 解锁

根据原作者[99degree@xda](https://forum.xda-developers.com/m/99degree.8186420/)的[教程](https://forum.xda-developers.com/t/meizu-e3-unlock-bootloader-tutorial.4005459/)，解锁方法如下。

1. 获取Flyme系统自带的root权限

2. 安装任意终端app，如Material Terminal, Terminal Emulator, Termux等

3. dump出系统的frp分区
  具体指令如下：  
  
  ```bash
  su
  dd if=/dev/block/platform/soc/c0c4000.sdhci/by-name/frp of=/sdcard/frp.bin
  ```

4. 提出frp.bin到电脑
  运行完指令后，在手机的`/sdcard/`目录下会生成一个frp.bin文件。  
  你可以需要通过[adb](https://developer.android.com/studio/command-line/adb.html)来将其提取到电脑上。（或者用什么其他的方法也可以

5. 修改frp.bin文件
  有两种方法，推荐第一种（因为我确实成功地用它解锁了）
  
  #### (1) 来自博客[叮当窝](https://blog.doreoom.com/644.html)的方法

  访问[frp.xingrz.me](frp.xingrz.me)，按照上面的指令将frp.bin文件上传到服务器，之后再下载回本地。

  #### (2) 来自[原作者](https://www.youtube.com/watch?v=7kKS7a_0CAg&t=2s&ab_channel=99degree)方法的方法

  使用16进制编辑器将`7fff8`和`7fff`处的值设为`1`，然后保存。

  ![asd](orides.png)

  <p align="center">原作者的描述</p>

6. 将修改后的frp文件刷写回去
  代码如下:  
  `dd if=下载的文件的路径 of=/dev/block/platform/soc/c0c4000.sdhci/by-name/frp`

7. 进行解锁操作
  - 将手机关机，并重启至fastboot模式（按音量减和电源键
  - 在电脑上运行以下命令：  
    `fastboot flashing unlock`
    
  > 如果执行命令无效，请再试一次。可能是驱动或者线材等原因导致的。

  - 接着手机会黑屏出现奇怪的白线，你需要用音量键选择到“No”然后按下电源键。
    
  - 随后手机会进入内置的Recovery模式，先按五次音量+再按五次音量-，之后会有清除数据的选项，选择它并重启。

  - 重复先前的过程，再刷一遍frp分区，重启至fastboot模式，并执行以下命令：
    `fastboot flashing unlock_critical`
    
  - 目前解锁操作已完成，如果出现黑屏和白线请按之前的方法再次操作一遍。（我估计你不会遇到）

### 刷入Recovery

  - 将手机关机，并重启至fastboot模式（按音量减和电源键

  - 在电脑上下载twrp镜像文件，并运行以下命令：
    `fastboot flash recovery twrp-meizue3-rec.img`
    待成功后就可以重启至twrp的recovery了。

### 刷入LinageOS

  **提示**：本系统经测试有声音/震动，但是无法打开摄像头。有意者可移步至作者的[发布页面](https://github.com/99degree/android_vendor_meizu_m851q/releases)自行寻找合适的包。

  - 下载LinageOS和boot镜像文件，复制到手机内置存储中，并重启至recovery模式（按音量加和电源键）

  - 在twrp主页面中选择备份，将boot/vendor/modem/efs分区备份至`/sdcard`。随后用电脑提取出来。

  - 在twrp主页面中选择安装，将`system.img`安装到system分区；`vendor.img`安装到vendor分区；`boot.img`安装到boot分区。

  - 先不要重启，回到主界面选择清除。选中data,cache,dalvik分区，点击清除，之后再重启。

  > 系统已经刷写完成，第一次启动可能需要较长时间。如出现启动循环，可长按电源键重启再试。（你可能需要完全关机后再启动）


![meizu](meizue3.png)

<p align="center">最后就可以享受类原生的快乐了</p>
  

