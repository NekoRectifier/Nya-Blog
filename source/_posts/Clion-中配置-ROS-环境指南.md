---
title: Clion 中配置 ROS 环境指南
date: 2022-06-22 20:10:44
tags: 
    - Clion
    - ROS
---

# 前言

网上的指南大多是搬运 Clion 官网或 ROS Wiki 的内容，且在解决环境变量的问题时通通采用继承当前终端的环境变量的方法。给不使用终端来启动 Clion 的用户带来很大不便。
本文将在结合上述内容，并提供另外一种设置 Clion 环境变量的方式。

# 步骤

## 1. 创建 ROS 包

具体过程可参考：ROS Wiki 的 [构建ROS软件包](https://wiki.ros.org/cn/ROS/Tutorials/BuildingPackages)

确保你的工作目录为以下（或相似）的结构：
```bash
tree catkin_working_dir
├── CMakeLists.txt
├── build
├── devel
├── src
│   ├── {your_package_name}
│   │   ├── CMakeLists.txt
│   │   ├── src
│   │   ├── ...

```

## 2. 设置 Clion Cmake 相关设置

- 启动 Clion，找到CMake设置（File > Settings <keyboard>Ctrl+Alt+S</keyboard> > Build, Execution, Deployment > CMake）

- 将“Build directory”设为：`<你的工作区目录>/build`
将“CMake Option”设为： `-DCATKIN_DEVEL_PACKAGE_PREFIX=<你的工作区目录>/devel`

## 3. 设置环境变量

### 3.1. 设置环境变量（Clion 内设置）

- 打开终端（保证该终端已 **source** 所需的 `setup.bash` 等）

- 输入 `printenv | grep CMAKE` 并复制 `CMAKE_PREFIX_PATH` 备用

- 用 Clion 打开你的工作区目录，并选择 `<你的工作区目录>/src/CMakeLists.txt` 打开。

- 再次打开步骤 2 中的 CMake 设置界面，并将复制的内容粘贴至 `Environment` 中。
```plain
    CMAKE_PREFIX_PATH=......
```

### 3.2 设置环境变量（终端）

见：[Clion 给的教程](https://www.jetbrains.com/help/clion/ros-setup-tutorial.html#launch-in-sourced)


# 参考链接
【1】https://www.jetbrains.com/help/clion/ros-setup-tutorial.html
【2】https://blog.csdn.net/qq_42731705/article/details/123858765