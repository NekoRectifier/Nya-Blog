---
title: Visual Studio Code C/C++ 基础开发环境配置指南
date: 2022-05-17 21:35:48
tags: 
    - VSC
    - C/C++
---

# 前言
说是 VSC 的开发环境配置，其实是 Windows 下 C/C++ 的环境配置指南。

无论是在 Linux 还是 OSX 上，配置 C/C++ 的环境很大程度上都是一行命令能解决的事。而在 Windows 上情况就变得相当复杂了起来。
移植到 Windows 平台的编译器种类繁多：MinGW、MinGW-w64、MSYS/2、Cygwin 等，光是厘清[这些编译器的区别](https://blog.csdn.net/u012408797/article/details/120490201)就足够让人头大了。
但如今 [WinLibs](https://winlibs.com/) 的出现应该能更好的解决配置 C/C++ 环境的问题。

# 编译器解决方案 —— WinLibs

## 简介

官网上是这样描述的：*"In short: it's a free C and C++ compiler for Microsoft Windows."*
实际上也确实如此，不过 WinLibs 不仅仅包含（最新的）GCC，它还涵盖了：LLVM 前端（Clang）、LLDB 调试器与 MinGW-w64 环境。

不可否认，WinLibs 作为一款完备的 C/C++ 开发环境是完全可行的。

## 下载

移步至官网的[下载页面](https://winlibs.com/#download-release)或直接点击这个[链接](https://github.com/brechtsanders/winlibs_mingw/releases/download/12.1.0-14.0.4-10.0.0-ucrt-r2/winlibs-i686-posix-dwarf-gcc-12.1.0-llvm-14.0.4-mingw-w64ucrt-10.0.0-r2.7z)（本文发布时为最新版）

### UCRT 与 MSVCRT 版本的区别

> 传统上，MinGW-w64编译器使用MSVCRT作为运行时库，它在所有版本的Windows中都可用。
自Windows 10开始，Universal C Runtime (UCRT)可作为MSVCRT的替代品。Universal C Runtime也可以安装在早期版本的Windows上（见：Windows中Universal C Runtime的更新）。
除非你的目标是旧版本的Windows，否则UCRT作为运行时库是更好的选择，因为它的编写是为了更好地支持最近的Windows版本，以及提供更好的标准一致性。

也就是说，UCRT 是 “更新的标准”，理应优先采用。

## 安装

1. 将下载的压缩包解压后，得到如下文件
  ![cb](compress_bag.png)

2. 将整个文件夹移动至合适位置
  由于 WinLibs 采用了压缩包来发布，所以不需要进行传统的安装操作。把文件放置到合适位置即可。
  比如我就将其放置到 `D:\Program Files\` 下，完整路径为：`D:\Program Files\mingw64`。

3. 添加路径至 path 变量
  ![ps](path_settings.png)
  添加完整路径到 path 变量下。

4. [OPTIONAL] 测试 path 变量是否正确
  打开 cmd，输入
  
  ```cmd
      gcc --version
      g++ --version
      clang --version
  ```
  
![vt](version_test.png)
  如图所示即为正常。

# Visual Studio Code 设置

1. 安装 CodeRunner 插件
  ![i_cr](install_cr.png)

2. 进行插件配置
  
  - 开启可交互的终端
    按 <kbd>ctrl</kbd> + <kbd>,</kbd> 进入 VSC 设置；
    然后按下图配置将 `Run In Terminal` 选项勾选上；
    ![es](extension_settings.png)

  - 选择 GCC / Clang 编译器
    按 <kbd>ctrl</kbd> + <kbd>,</kbd> 进入 VSC 设置；
    点击右上角按钮，进入 json 编辑界面；
    按如下格式修改 `code-runner.executorMap` 的内容。

    ```json
    "code-runner.executorMap": {
        "javascript": "node",
        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
        "c": "cd $dir && {你想要的编译器名称} $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && {你想要的编译器名称} $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "objective-c": "cd $dir && gcc -framework Cocoa $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        
        ...

    },
    ```
3. 完成配置

  之后在右键菜单/<kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>n</kbd> 都可以直接编译运行 C/C++ 程序并与之交互了。



# 参考链接
【1】https://blog.csdn.net/lzyws739307453/article/details/89823900
【2】https://blog.csdn.net/u012408797/article/details/120490201
【3】https://zhuanlan.zhihu.com/p/401188789
【4】https://blog.csdn.net/cjmqas/article/details/79296865