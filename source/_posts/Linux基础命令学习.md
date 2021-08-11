---
title: Linux基础命令学习
date: 2021-08-11 14:32:05
tags: linux
---

## shell

### 定义

shell是一种**电脑程序**,用于将操作系统的各种服务提供给其他程序或人类使用.

### 名称来源

> It is named a shell because it is the outermost layer around the operating system.

### 命令行shell

命令行界面（CLI）是一个操作系统的外壳，使用字母数字键入键盘上的字符来提供指令和数据到操作系统来进行交互。
如是B(ourne)A(gain)SH(ell)就是Unix Linux的默认shell.

## Linux目录结构

```Bash
    /bin        用于存放二进制可执行文件 
    /boot       存放系统引导文件
    /dev        存放设备文件
    /etc        存放系统配置文件
    /home       存放所有用户文件
    /lib        存放程序运行所需要的共享库文件及内核模块
    /mnt        挂载点目录
    /opt        存放安装的应用程序包文件
    /proc       存放当前内存的映射文件
    /root       超级用户目录
    /sbin       超级用户的二进制可执行文件
    /tmp        存放临时文件
    /usr        存放系统应用程序
    /var        存放运行时需要改变数据的文件
```

> 在"bin"和"sbin"中的文件都称做"外置命令"

## Linux命令基本格式

` <cmd> [options] [arguments] `

>一般来说，后面跟的选项如果单字符选项前使用"-"。单词选项前使用"--"

## 通配符

### 使用格式

* `*`   匹配任何字符/数字
* `?`   匹配任何数字
* `[]`  匹配'[]'内的任何字符
* `[!]`  匹配除了'[!]'内外的的任何字符

### 示例

## 常用文件/目录操作命令

* `.`   代表当前目录
* `..`  代表上一级的目录
* `-`   代表使用`cd`前的目录
* `~`   代表当前用户目录的绝对路径

> 使用`pwd`查看用户的当前命令

* `rmdir [directory]` 删除目录(要求目录为空)
* `touch [file/directory]` 建立文件/修改文件/目录的时间属性
* `ln [参数][源文件或目录][目标文件或目录]`  
    建立链接文件  
    参数:
  * -b 删除，覆盖以前建立的链接
  * -d 允许超级用户制作目录的硬链接
  * -f 强制执行
  * -i 交互模式，文件存在则提示用户是否覆盖
  * -n 把符号链接视为一般目录
  * -s 软链接(符号链接)
  * -v 显示详细的处理过程

> 软链接，以路径的形式存在,可以跨文件系统并可以对目录进行链接
> 不带 '-s' 标记即为硬链接

* `find <path> -[option]`  
    参数:
  * `-name <NAME>` 例如 `find . -name "*.c"`
  * `-type <TYPE>` 例如 `find . -type f` 列举出目录下的所有文件

* `file / stat <file>` 显示文件信息
* `cat` 查看文本文件内容
* `|` 管道命令 将前一个命令输出的内容作为后一个命令的输入  
    如: `ls -la | wc`
* `> / >>` 重定向命令

> `>` 是覆盖模式，`>>` 是追加模式

## 文件压缩/解压缩

### 常用工具

* gzip
* bzip2
* tar

### 对应命令

```Bash
    gzip <file> / gzip -d <file>
    bzip2 <file> / bzip2 -d <file>
    tar -czvf <file> / tar -xzvf <file> 
```
